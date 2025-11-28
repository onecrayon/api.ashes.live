from api.models.card import Card, DiceFlags
from api.services.card import parse_cost_to_weight


def test_dice_to_flags():
    """Card.dice_to_flags() properly converts from dice list to integer flags"""
    # Basic dice are treated the same as no dice
    assert Card.dice_to_flags([DiceFlags.basic.name]) == 0

    # And passing nothing is the same as passing basic
    assert Card.dice_to_flags(None) == 0

    # Single dice return the right number
    assert Card.dice_to_flags([DiceFlags.sympathy.name]) == DiceFlags.sympathy.value

    # Multiple dice return the right number
    assert (
        Card.dice_to_flags([DiceFlags.ceremonial.name, DiceFlags.charm.name])
        == DiceFlags.ceremonial.value + DiceFlags.charm.value
    )


def test_flags_to_dice():
    """Card.flags_to_dice() property converts from integer flag to dice list"""
    # 0 converts to basic
    assert Card.flags_to_dice(0) is None

    # Single dice flag returns the right list
    assert Card.flags_to_dice(DiceFlags.natural.value) == [DiceFlags.natural.name]

    # Multiple dice return the right set
    assert Card.flags_to_dice(
        DiceFlags.illusion.value + DiceFlags.divine.value + DiceFlags.time.value
    ) == [DiceFlags.illusion.name, DiceFlags.divine.name, DiceFlags.time.name]

    # New dice types (artifice and astral) work correctly
    assert Card.flags_to_dice(DiceFlags.artifice.value) == [DiceFlags.artifice.name]
    assert Card.flags_to_dice(DiceFlags.astral.value) == [DiceFlags.astral.name]

    # Multiple dice including new types
    assert Card.flags_to_dice(DiceFlags.artifice.value + DiceFlags.astral.value) == [
        DiceFlags.artifice.name,
        DiceFlags.astral.name,
    ]


def test_dice_weight():
    """Card.dice_weight property is all types of dice in either flag field"""
    card = Card()
    card.dice_flags = DiceFlags.ceremonial.value
    card.alt_dice_flags = DiceFlags.charm.value + DiceFlags.ceremonial.value
    assert card.dice_weight == DiceFlags.ceremonial.value + DiceFlags.charm.value

    # Test with new dice types
    card = Card()
    card.dice_flags = DiceFlags.artifice.value
    card.alt_dice_flags = DiceFlags.astral.value
    assert card.dice_weight == DiceFlags.artifice.value + DiceFlags.astral.value


def test_type_weight():
    """Card.type_weight property must assign proper ordering for cards"""
    card = Card()
    card.card_type = "Phoenixborn"
    assert card.type_weight == 0
    card.card_type = "Conjured Alteration Spell"
    assert card.type_weight == 7


def test_card_weights():
    """Card weights must be calculated properly"""
    # Nonsense is 0
    assert parse_cost_to_weight("1 ceremonial") == 0
    # Nonsense that looks real is 0
    assert parse_cost_to_weight("1 [[Biter]]") == 0
    # Main weight is 5
    assert parse_cost_to_weight("[[main]]") == 5
    # Side weight is 4
    assert parse_cost_to_weight("[[side]]") == 4
    # Discard weight is 3 * cards discarded
    assert parse_cost_to_weight("1 [[discard]]") == 3
    assert parse_cost_to_weight("2 [[discard]]") == 6
    # Basic die is 100
    assert parse_cost_to_weight("1 [[basic]]") == 100
    # Class die is 101
    assert parse_cost_to_weight("1 [[ceremonial:class]]") == 101
    # Power die is 102
    assert parse_cost_to_weight("1 [[ceremonial:power]]") == 102
    # New dice types work correctly
    assert parse_cost_to_weight("1 [[artifice:class]]") == 101
    assert parse_cost_to_weight("2 [[artifice:class]]") == 202
    assert parse_cost_to_weight("1 [[astral:power]]") == 102
    assert parse_cost_to_weight("2 [[astral:power]]") == 204
