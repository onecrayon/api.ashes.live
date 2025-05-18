import re

from api import db
from api.models.card import Card, CardConjuration
from api.models.release import Release
from api.utils.helpers import str_or_int, stubify

from .stream import create_entity

MAGIC_COSTS = (
    "basic",
    "ceremonial",
    "charm",
    "illusion",
    "natural",
    "divine",
    "sympathy",
    "time",
)


def gather_conjurations(card: Card) -> list[Card]:
    """Recursively gather all conjurations that can be created by the given card.

    WARNING: IMPLICIT EXECUTES SQL VIA RELATIONSHIP!
    """
    conjurations = card.conjurations if card.conjurations else []
    for conjuration in conjurations:
        conjurations = conjurations + gather_conjurations(conjuration)
    return conjurations


def gather_root_summons(card: Card) -> list[Card]:
    """Recursively gather the cards that can summon this card (if any).

    Ensures that we find all possible cards that could summon a given conjuration; looks up the
    tree.

    WARNING: IMPLICIT EXECUTES SQL VIA BACKREF!
    """
    if not card.summons:
        return [card]
    root_summons = []
    for summon in card.summons:
        root_summons = root_summons + gather_root_summons(summon)
    return root_summons


class MissingConjurations(Exception):
    pass


def parse_cost_to_weight(cost: str) -> int:
    """Converts a cost string into a weight"""
    match = re.match(r"^\s*(\d*)\s*\[\[([^\]]+)\]\]\s*$", cost)
    if not match:
        return 0
    cost_count = int(match.group(1)) if match.group(1) else None
    cost_parts = match.group(2).split(":")
    cost_type = cost_parts[0].lower()
    cost_subtype = cost_parts[1].lower() if len(cost_parts) > 1 else None
    if cost_type in MAGIC_COSTS and cost_count:
        weight = cost_count * 100
        if cost_subtype == "class":
            weight += cost_count * 1
        elif cost_subtype == "power":
            weight += cost_count * 2
        return weight
    elif cost_type == "discard" and cost_count:
        return cost_count * 3
    elif cost_type == "side":
        return 4
    elif cost_type == "main":
        return 5
    return 0


def parse_costs_to_mapping(costs: list[list[str] | str]) -> dict:
    """Converts a list of costs into an associative mapping between cost and number"""
    magic_cost_re = re.compile(
        r"(\d+)\s+\[\[((?:" + r"|".join(MAGIC_COSTS) + r")(?::\w+)?)\]\]"
    )
    data_object = {}
    for cost in costs:
        # Handle a split cost
        if isinstance(cost, list):
            split_1 = magic_cost_re.match(cost[0])
            split_2 = magic_cost_re.match(cost[1])
            # This line is reached in the tests, but can be missed by coverage due to how the code
            #  execution is optimized: https://github.com/nedbat/coveragepy/issues/198
            if not split_1 or not split_2:  # pragma: no cover
                continue
            magic_cost = max(int(split_1.group(1)), int(split_2.group(1)))
            data_object[f"{split_1.group(2)} / {split_2.group(2)}"] = magic_cost
        else:
            # Normal cost, so just add it to our object
            cost_match = magic_cost_re.match(cost)
            if not cost_match:
                continue
            data_object[cost_match.group(2)] = int(cost_match.group(1))
    return data_object


def dice_name_from_cost(cost: str) -> str:
    """Given a string like `magic:face` returns just `magic`"""
    return cost.split(":")[0]


def compose_card_search_text(
    card: "Card", text: str | None = None, search_keywords: str | None = None
) -> str:
    """Composes our common card "search text" which is normalized text for the card that
    is used by the full text search."""
    # Compose our first line, which is the card name followed by any search keywords
    search_text = f"{card.name}"
    if search_keywords:
        search_text += f" {search_keywords}"
    search_text += "\n"
    # Compose the second line, which is the Phoenixborn for this card, if any
    if card.phoenixborn:
        search_text += f"{card.phoenixborn}\n"
    # Compose the following lines, which are normalized versions of the card text
    if text:
        # Remove apostrophes and formatting characters from search text to ensure words are treated as lexemes
        search_text += re.sub(
            r"\n+", " ", text.replace("[[", "").replace("]]", "").replace("'", "")
        )
    return search_text


def cost_to_weight(cost):
    """Shared helper function for parsing card costs from endpoints into weights and JSON data."""
    cost_list = re.split(r"\s+-\s+", cost) if isinstance(cost, str) else cost
    weight = 0
    json_cost_list = []
    if cost_list:
        for cost_entry in cost_list:
            split_cost = (
                re.split(r"\s+(?:/|or)\s+", cost_entry)
                if isinstance(cost_entry, str)
                else cost_entry
            )
            if len(split_cost) > 1:
                first_weight = parse_cost_to_weight(split_cost[0])
                second_weight = parse_cost_to_weight(split_cost[1])
                weight += max(first_weight, second_weight)
                json_cost_list.append(split_cost)
            else:
                weight += parse_cost_to_weight(split_cost[0])
                json_cost_list.append(split_cost[0])
    return weight, json_cost_list


def create_card(
    session: db.Session,
    name: str,
    card_type: str,
    release: "Release",
    placement: str = None,
    text: str = None,
    cost: list[str] | str | None = None,
    effect_magic_cost: list[str] | str | None = None,
    can_effect_repeat: bool = False,
    dice: list[str] = None,
    alt_dice: list[str] = None,
    phoenixborn: str = None,
    attack: str = None,
    battlefield: str = None,
    life: str = None,
    recover: str = None,
    spellboard: str = None,
    copies: int = None,
) -> "Card":
    """Creates a card, generating the necessary JSON and cost info"""
    card = Card()
    card.name = name
    card.stub = stubify(name)
    card.phoenixborn = phoenixborn
    card.card_type = card_type
    card.placement = placement
    card.release_id = release.id
    card.is_summon_spell = name.startswith("Summon ")
    card.search_text = compose_card_search_text(card, text)
    existing_conjurations = None
    if text:
        # Check for conjurations before we do any more work
        conjuration_stubs = set()
        for match in re.finditer(
            r"\[\[([A-Z][A-Za-z' ]+)\]\](?=[ ](?:(?:conjuration|conjured alteration spell)s?|or))",
            text,
        ):
            conjuration_stubs.add(stubify(match.group(1)))
        existing_conjurations = (
            session.query(Card.id, Card.stub, Card.name)
            .filter(Card.stub.in_(conjuration_stubs), Card.is_legacy.is_(False))
            .all()
        )
        existing_stubs = set(x.stub for x in existing_conjurations)
        missing_conjurations = conjuration_stubs.symmetric_difference(existing_stubs)
        if missing_conjurations:
            raise MissingConjurations(
                f"The following conjurations must be added first: {', '.join([x for x in missing_conjurations])}"
            )

    if copies is not None:
        card.copies = copies
    card.entity_id = create_entity(session)
    weight, json_cost_list = cost_to_weight(cost)
    card.cost_weight = weight
    # Extract our effect costs into a list of strings and lists. We don't actually need the weight, but the parsing
    #  logic is identical otherwise.
    _, effect_cost_list = cost_to_weight(effect_magic_cost)
    # Convert our cost lists into magicCost and effectMagicCost mappings
    json_magic_cost = parse_costs_to_mapping(json_cost_list)
    json_effect_cost = parse_costs_to_mapping(effect_cost_list)
    # And finally, convert our mappings into lists of required dice
    dice_set = set()
    alt_dice_set = set()
    for dice_type in list(json_magic_cost.keys()) + list(json_effect_cost.keys()):
        both_types = dice_type.split(" / ")
        if len(both_types) > 1:
            alt_dice_set.add(dice_name_from_cost(both_types[0]))
            alt_dice_set.add(dice_name_from_cost(both_types[1]))
        else:
            dice_set.add(dice_name_from_cost(both_types[0]))
    if dice is None:
        dice = list(dice_set)
    if alt_dice is None:
        alt_dice = list(alt_dice_set)
    card.dice_flags = Card.dice_to_flags(dice)
    card.alt_dice_flags = Card.dice_to_flags(alt_dice)
    json_data = {
        "name": card.name,
        "stub": card.stub,
        "type": card.card_type,
        "release": {
            "name": release.name,
            "stub": release.stub,
        },
    }
    if existing_conjurations:
        json_data["conjurations"] = [
            {"name": x.name, "stub": x.stub} for x in existing_conjurations
        ]
    if placement:
        json_data["placement"] = placement
    if json_cost_list:
        json_data["cost"] = json_cost_list
    if dice:
        json_data["dice"] = dice
    if alt_dice:
        json_data["altDice"] = alt_dice
    if json_magic_cost:
        json_data["magicCost"] = json_magic_cost
    if json_effect_cost:
        json_data["effectMagicCost"] = json_effect_cost
    if text:
        json_data["text"] = text
    if phoenixborn is not None:
        json_data["phoenixborn"] = phoenixborn
    if attack is not None:
        json_data["attack"] = str_or_int(attack)
    if battlefield is not None:
        json_data["battlefield"] = str_or_int(battlefield)
    if life is not None:
        json_data["life"] = str_or_int(life)
    if recover is not None:
        json_data["recover"] = str_or_int(recover)
    if spellboard is not None:
        json_data["spellboard"] = str_or_int(spellboard)
    if copies is not None:
        json_data["copies"] = copies
    if can_effect_repeat:
        json_data["effectRepeats"] = True
    card.json = json_data
    session.add(card)
    session.commit()
    # Now that we have a card entry, we can populate the conjuration relationship(s)
    if existing_conjurations:
        for conjuration in existing_conjurations:
            session.add(CardConjuration(card_id=card.id, conjuration_id=conjuration.id))
        session.commit()
    return card
