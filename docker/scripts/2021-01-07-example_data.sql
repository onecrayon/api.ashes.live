-- -------------------------------------------------------------
-- TablePlus 3.8.0(336)
--
-- https://tableplus.com/
--
-- Database: asheslive
-- Generation Time: 2020-09-10 09:00:33.5310
-- -------------------------------------------------------------

INSERT INTO "public"."releases" ("id", "name", "is_phg", "is_promo", "designer_name", "designer_url", "is_retiring", "is_legacy", "is_public", "stub") VALUES
('1', 'Core Set', 't', 'f', NULL, NULL, 'f', 't', 't', 'core-set'),
('2', 'The Frostdale Giants', 't', 'f', NULL, NULL, 'f', 't', 't', 'the-frostdale-giants'),
('3', 'The Children of Blackcloud', 't', 'f', NULL, NULL, 'f', 't', 't', 'the-children-of-blackcloud'),
('4', 'The Roaring Rose', 't', 'f', NULL, NULL, 'f', 't', 't', 'the-roaring-rose'),
('5', 'The Duchess of Deception', 't', 'f', NULL, NULL, 'f', 't', 't', 'the-duchess-of-deception'),
('6', 'The Laws of Lions', 't', 'f', NULL, NULL, 'f', 't', 't', 'the-laws-of-lions'),
('7', 'The Song of Soaksend', 't', 'f', NULL, NULL, 'f', 't', 't', 'the-song-of-soaksend'),
('8', 'The Masters of Gravity', 't', 'f', NULL, NULL, 'f', 't', 't', 'the-masters-of-gravity'),
('9', 'The Path of Assassins', 't', 'f', NULL, NULL, 't', 't', 't', 'the-path-of-assassins'),
('10', 'The Goddess of Ishra', 't', 'f', NULL, NULL, 'f', 't', 't', 'the-goddess-of-ishra'),
('11', 'The Boy Among Wolves', 't', 'f', NULL, NULL, 'f', 't', 't', 'the-boy-among-wolves'),
('12', 'The Demons of Darmas', 't', 'f', NULL, NULL, 'f', 't', 't', 'the-demons-of-darmas'),
('13', 'The Spirits of Memoria', 't', 'f', NULL, NULL, 'f', 't', 't', 'the-spirits-of-memoria'),
('14', 'The Ghost Guardian', 't', 'f', NULL, NULL, 'f', 't', 't', 'the-ghost-guardian'),
('15', 'The King of Titans', 't', 'f', NULL, NULL, 'f', 't', 't', 'the-king-of-titans'),
('16', 'The Protector of Argaia', 't', 'f', NULL, NULL, 'f', 't', 't', 'the-protector-of-argaia'),
('17', 'The Grave King', 't', 'f', NULL, NULL, 'f', 't', 't', 'the-grave-king'),
('18', 'Dimona Odinstar (promo)', 't', 't', NULL, NULL, 't', 't', 't', 'dimona-odinstar-promo'),
('19', 'Lulu Firststone (promo)', 't', 't', NULL, NULL, 't', 't', 't', 'lulu-firststone-promo'),
('20', 'Orrick Gilstream (promo)', 't', 't', NULL, NULL, 't', 't', 't', 'orrick-gilstream-promo'),
('21', 'The Treasures of the Ages', 'f', 'f', NULL, NULL, 't', 't', 't', 'the-treasures-of-the-ages'),
('22', 'The Young Ruler', 'f', 'f', NULL, NULL, 't', 't', 't', 'the-young-ruler'),
('23', 'The Scoundrels of the Sea', 'f', 'f', NULL, NULL, 't', 't', 't', 'the-scoundrels-of-the-sea'),
('24', 'The Mad Doctor', 'f', 'f', NULL, NULL, 't', 't', 't', 'the-mad-doctor'),
('25', 'Master Set', 'f', 'f', NULL, NULL, 'f', 'f', 't', 'master-set'),
('26', 'The Frostdale Giants', 'f', 'f', NULL, NULL, 'f', 'f', 't', 'the-frostdale-giants'),
('27', 'The Children of Blackcloud', 'f', 'f', NULL, NULL, 'f', 'f', 't', 'the-children-of-blackcloud'),
('28', 'The Roaring Rose', 'f', 'f', NULL, NULL, 'f', 'f', 't', 'the-roaring-rose'),
('29', 'The Duchess of Deception', 'f', 'f', NULL, NULL, 'f', 'f', 't', 'the-duchess-of-deception'),
('30', 'The Law of Lions', 'f', 'f', NULL, NULL, 'f', 'f', 't', 'the-law-of-lions'),
('31', 'The Song of Soaksend', 'f', 'f', NULL, NULL, 'f', 'f', 't', 'the-song-of-soaksend'),
('32', 'The Masters of Gravity', 'f', 'f', NULL, NULL, 'f', 'f', 't', 'the-masters-of-gravity'),
('33', 'The Boy Among Wolves', 'f', 'f', NULL, NULL, 'f', 'f', 't', 'the-boy-among-wolves'),
('34', 'The Goddess of Ishra', 'f', 'f', NULL, NULL, 'f', 'f', 't', 'the-goddess-of-ishra'),
('35', 'The Demons of Darmas', 'f', 'f', NULL, NULL, 'f', 'f', 't', 'the-demons-of-darmas'),
('36', 'The Spirits of Memoria', 'f', 'f', NULL, NULL, 'f', 'f', 't', 'the-spirits-of-memoria'),
('37', 'The King of Titans', 'f', 'f', NULL, NULL, 'f', 'f', 't', 'the-king-of-titans'),
('38', 'The Ghost Guardian', 'f', 'f', NULL, NULL, 'f', 'f', 't', 'the-ghost-guardian'),
('39', 'The Grave King', 'f', 'f', NULL, NULL, 'f', 'f', 't', 'the-grave-king'),
('40', 'The Protector of Argaia', 'f', 'f', NULL, NULL, 'f', 'f', 't', 'the-protector-of-argaia');

INSERT INTO "public"."card" ("id", "name", "stub", "json", "release_id", "card_type", "cost_weight", "dice_flags", "phoenixborn", "copies", "is_summon_spell", "search_text", "alt_dice_flags", "entity_id", "version", "artist_name", "artist_url", "is_legacy") VALUES
('1', 'Abundance', 'abundance', '{"cost": ["[[main]]", "1 [[illusion:class]]"], "dice": ["illusion"], "name": "Abundance", "stub": "abundance", "text": "[[main]] - [[exhaust]]: All players may draw up to 2 cards. For each card they cannot or do not draw, deal 1 damage to their Phoenixborn.\n\nFocus 1: Reduce the damage your Phoenixborn receives from this spell by 1.\n\nFocus 2: Reduce the damage your Phoenixborn receives from this spell by an additional 1.", "type": "Ready Spell", "weight": 106, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"illusion:class": 1}, "placement": "Spellboard"}', '1', 'Ready Spell', '106', '4', NULL, NULL, 'f', 'Abundance
All players may draw up to 2 cards. For each card they cannot or do not draw, deal 1 damage to their Phoenixborn. Focus 1 Reduce the damage your Phoenixborn receives from this spell by 1. Focus 2 Reduce the damage your Phoenixborn receives from this spell by an additional 1.', '0', '1', '1', NULL, NULL, 't'),
('2', 'Anchornaut', 'anchornaut', '{"cost": ["[[main]]", "1 [[basic]]"], "life": 1, "name": "Anchornaut", "stub": "anchornaut", "text": "Throw 1: During your turn, you may place 1 exhaustion token on this unit to deal 1 damage to a target unit", "type": "Ally", "attack": 0, "weight": 105, "recover": 1, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1}, "placement": "Battlefield"}', '1', 'Ally', '105', '0', NULL, NULL, 'f', 'Anchornaut
Throw 1 During your turn, you may place 1 exhaustion token on this unit to deal 1 damage to a target unit', '0', '2', '1', NULL, NULL, 't'),
('3', 'Aradel Summergaard', 'aradel-summergaard', '{"dice": ["natural"], "life": 16, "name": "Aradel Summergaard", "stub": "aradel-summergaard", "text": "Water Blast: [[side]] - [[exhaust]] - 1 [[natural:class]]: Deal 2 damage to a target unit.", "type": "Phoenixborn", "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "spellboard": 4, "battlefield": 8, "effectMagicCost": {"natural:class": 1}}', '1', 'Phoenixborn', '0', '8', NULL, NULL, 'f', 'Aradel Summergaard
Water Blast Deal 2 damage to a target unit.', '0', '3', '1', NULL, NULL, 't'),
('4', 'Blood Archer', 'blood-archer', '{"cost": ["[[main]]", "1 [[ceremonial:class]]", "1 [[charm:class]]", "2 [[basic]]"], "dice": ["ceremonial", "charm"], "life": 3, "name": "Blood Archer", "stub": "blood-archer", "text": "Blood Oath 2: When you are declaring attackers, you may add 2 attack to this unit for the remainder of this turn. If you do, place 2 wounds on this unit.\n\nBattle Advantage: When this unit is in battle, it inflicts its damage before other units without Battle Advantage inflict their damage.", "type": "Ally", "attack": 3, "weight": 407, "recover": 2, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 2, "charm:class": 1, "ceremonial:class": 1}, "placement": "Battlefield"}', '1', 'Ally', '407', '3', NULL, NULL, 'f', 'Blood Archer
Blood Oath 2 When you are declaring attackers, you may add 2 attack to this unit for the remainder of this turn. If you do, place 2 wounds on this unit. Battle Advantage When this unit is in battle, it inflicts its damage before other units without Battle Advantage inflict their damage.', '0', '4', '1', NULL, NULL, 't'),
('5', 'Blood Puppet', 'blood-puppet', '{"life": 2, "name": "Blood Puppet", "stub": "blood-puppet", "text": "Cursed 1: At the end of each round, place 1 wound token on your Phoenixborn.\n\nSelf Inflict 1: [[side]] - 1 [[basic]]: Deal 1 damage to this unit.", "type": "Conjuration", "attack": 0, "copies": 5, "recover": 0, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield", "effectRepeats": true, "effectMagicCost": {"basic": 1}}', '1', 'Conjuration', '0', '0', NULL, '5', 'f', 'Blood Puppet
Cursed 1 At the end of each round, place 1 wound token on your Phoenixborn. Self Inflict 1 Deal 1 damage to this unit.', '0', '5', '1', NULL, NULL, 't'),
('6', 'Blood Transfer', 'blood-transfer', '{"cost": ["[[main]]"], "dice": ["ceremonial", "charm"], "name": "Blood Transfer", "stub": "blood-transfer", "text": "[[side]] - [[exhaust]] - 1 [[ceremonial:class]] - 1 [[charm:class]]: Deal 2 damage to a target unit you control. If you do, you may remove 2 wound tokens from another unit you control or remove 1 wound token from your Phoenixborn.", "type": "Ready Spell", "weight": 5, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "effectMagicCost": {"charm:class": 1, "ceremonial:class": 1}}', '1', 'Ready Spell', '5', '3', NULL, NULL, 'f', 'Blood Transfer
Deal 2 damage to a target unit you control. If you do, you may remove 2 wound tokens from another unit you control or remove 1 wound token from your Phoenixborn.', '0', '6', '1', NULL, NULL, 't'),
('7', 'Blue Jaguar', 'blue-jaguar', '{"life": 2, "name": "Blue Jaguar", "stub": "blue-jaguar", "text": "Gaze 1: After a unit comes into play on an opponent''s battlefield, you may spend 1 [[basic]] to place 1 exhaustion token on that unit.", "type": "Conjuration", "attack": 2, "copies": 5, "recover": 0, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield", "effectRepeats": true, "effectMagicCost": {"basic": 1}}', '1', 'Conjuration', '0', '0', NULL, '5', 'f', 'Blue Jaguar
Gaze 1 After a unit comes into play on an opponent''s battlefield, you may spend 1 basic to place 1 exhaustion token on that unit.', '0', '7', '1', NULL, NULL, 't'),
('8', 'Bound Soul', 'bound-soul', '{"cost": ["[[main]]", "1 [[ceremonial:class]]"], "dice": ["ceremonial"], "name": "Bound Soul", "stub": "bound-soul", "text": "Search your discard pile for an ally and place it into your hand.", "type": "Action Spell", "weight": 106, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"ceremonial:class": 1}, "placement": "Discard"}', '1', 'Action Spell', '106', '1', NULL, NULL, 'f', 'Bound Soul
Search your discard pile for an ally and place it into your hand.', '0', '8', '1', NULL, NULL, 't'),
('9', 'Bring Forth', 'bring-forth', '{"cost": ["[[main]]", "2 [[ceremonial:class]]"], "dice": ["ceremonial"], "life": "+1", "name": "Bring Forth", "stub": "bring-forth", "text": "* This spell can only be attached to units with the Illusion ability. This unit is no longer considered to have the Illusion ability.\n\n* Respark: 2 [[basic]]", "type": "Alteration Spell", "attack": "+2", "weight": 207, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"ceremonial:class": 2}, "placement": "Unit", "effectMagicCost": {"basic": 2}}', '1', 'Alteration Spell', '207', '1', NULL, NULL, 'f', 'Bring Forth
This spell can only be attached to units with the Illusion ability. This unit is no longer considered to have the Illusion ability. Respark 2', '0', '9', '1', NULL, NULL, 't'),
('10', 'Butterfly Monk', 'butterfly-monk', '{"life": "X", "name": "Butterfly Monk", "stub": "butterfly-monk", "text": "Unit Guard: This unit may guard a unit that is being attacked.\n\n* Last Blessing 1: When this unit is destroyed, remove 1 wound token from a target unit or Phoenixborn.\n\n* X = the number of [[Summon Butterfly Monk]] spells on your spellboard.", "type": "Conjuration", "attack": 1, "copies": 5, "recover": 1, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '1', 'Conjuration', '0', '0', NULL, '5', 'f', 'Butterfly Monk
Unit Guard This unit may guard a unit that is being attacked. Last Blessing 1 When this unit is destroyed, remove 1 wound token from a target unit or Phoenixborn. X = the number of Summon Butterfly Monk spells on your spellboard.', '0', '10', '1', NULL, NULL, 't'),
('11', 'Call Upon The Realms', 'call-upon-the-realms', '{"cost": ["[[main]]"], "name": "Call Upon The Realms", "stub": "call-upon-the-realms", "text": "Change 3 dice in your active pool to a side of your choice.", "type": "Action Spell", "weight": 5, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Discard"}', '1', 'Action Spell', '5', '0', NULL, NULL, 'f', 'Call Upon The Realms
Change 3 dice in your active pool to a side of your choice.', '0', '11', '1', NULL, NULL, 't'),
('12', 'Chant Of Revenge', 'chant-of-revenge', '{"cost": ["[[main]]", "1 [[ceremonial:class]]"], "dice": ["ceremonial"], "name": "Chant Of Revenge", "stub": "chant-of-revenge", "text": "Whenever a unit you control is destroyed, you may place 1 exhaustion token on this spell to deal 1 damage to a target unit or Phoenixborn.", "type": "Ready Spell", "weight": 106, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"ceremonial:class": 1}, "placement": "Spellboard"}', '1', 'Ready Spell', '106', '1', NULL, NULL, 'f', 'Chant Of Revenge
Whenever a unit you control is destroyed, you may place 1 exhaustion token on this spell to deal 1 damage to a target unit or Phoenixborn.', '0', '12', '1', NULL, NULL, 't'),
('13', 'Coal Roarkwin', 'coal-roarkwin', '{"life": 15, "name": "Coal Roarkwin", "stub": "coal-roarkwin", "text": "Slash: [[side]] - 1 [[discard]]: Deal 1 damage to a target unit. If an opponent has no units in play, you may deal 1 damage to their Phoenixborn instead.", "type": "Phoenixborn", "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "spellboard": 5, "battlefield": 6}', '1', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Coal Roarkwin
Slash Deal 1 damage to a target unit. If an opponent has no units in play, you may deal 1 damage to their Phoenixborn instead.', '0', '13', '1', NULL, NULL, 't'),
('14', 'Cut The Strings', 'cut-the-strings', '{"cost": ["[[main]]"], "dice": ["ceremonial"], "name": "Cut The Strings", "stub": "cut-the-strings", "text": "[[main]] - [[exhaust]] - 1 [[ceremonial:class]] - 1 [[basic]]: Deal 2 damage to a unit you control. If you do, you may discard a target alteration spell.", "type": "Ready Spell", "weight": 5, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "effectMagicCost": {"basic": 1, "ceremonial:class": 1}}', '1', 'Ready Spell', '5', '1', NULL, NULL, 'f', 'Cut The Strings
Deal 2 damage to a unit you control. If you do, you may discard a target alteration spell.', '0', '14', '1', NULL, NULL, 't'),
('15', 'Empower', 'empower', '{"cost": ["[[main]]", "2 [[natural:class]]"], "dice": ["natural"], "name": "Empower", "stub": "empower", "text": "After a player has declared attackers, you may spend 1 [[basic]] and place 1 exhaustion token on this spell. If you do, add 1 to a target unit''s attack value for the remainder of this turn.\n\nIn addition, you may draw 1 card. If you do, discard 1 card.\n\nFocus 1: In addition, you may select 1 die in your exhausted pool, re-roll it, and place it into your active pool.", "type": "Ready Spell", "weight": 207, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"natural:class": 2}, "placement": "Spellboard", "diceRecursion": 1, "effectMagicCost": {"basic": 1}}', '1', 'Ready Spell', '207', '8', NULL, NULL, 'f', 'Empower
After a player has declared attackers, you may spend 1  and place 1 exhaustion token on this spell. If you do, add 1 to a target unit''s attack value for the remainder of this turn. In addition, you may draw 1 card. If you do, discard 1 card. Focus 1 In addition, you may select 1 die in your exhausted pool, re-roll it, and place it into your active pool.', '0', '15', '1', NULL, NULL, 't'),
('16', 'Enchanted Violinist', 'enchanted-violinist', '{"cost": ["[[main]]", "1 [[basic]]"], "life": 2, "name": "Enchanted Violinist", "stub": "enchanted-violinist", "text": "Song of Sorrow: After an opponent discards 1 or more cards from their draw pile, you may spend 1 [[basic]] to place 1 wound token on a target unit.", "type": "Ally", "attack": 1, "weight": 105, "recover": 0, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1}, "placement": "Battlefield", "effectRepeats": true, "effectMagicCost": {"basic": 1}}', '1', 'Ally', '105', '0', NULL, NULL, 'f', 'Enchanted Violinist
Song of Sorrow After an opponent discards 1 or more cards from their draw pile, you may spend 1  to place 1 wound token on a target unit.', '0', '16', '1', NULL, NULL, 't'),
('17', 'Expand Energy', 'expand-energy', '{"cost": ["[[main]]", "1 [[ceremonial:power]]"], "dice": ["ceremonial"], "name": "Expand Energy", "stub": "expand-energy", "text": "[[main]] - [[exhaust]]: Select 1 die in your exhausted pool, re-roll it, and place it into your active pool.", "type": "Ready Spell", "weight": 107, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"ceremonial:power": 1}, "placement": "Spellboard", "diceRecursion": 1}', '1', 'Ready Spell', '107', '1', NULL, NULL, 'f', 'Expand Energy
Select 1 die in your exhausted pool, re-roll it, and place it into your active pool.', '0', '17', '1', NULL, NULL, 't'),
('18', 'Fade Away', 'fade-away', '{"cost": ["[[main]]", "1 [[illusion:class]]"], "dice": ["illusion"], "name": "Fade Away", "stub": "fade-away", "text": "Destroy this unit at the end of the round. If the destroyed unit was an ally, remove it from the game.", "type": "Alteration Spell", "weight": 106, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"illusion:class": 1}, "placement": "Unit"}', '1', 'Alteration Spell', '106', '4', NULL, NULL, 'f', 'Fade Away
Destroy this unit at the end of the round. If the destroyed unit was an ally, remove it from the game.', '0', '18', '1', NULL, NULL, 't'),
('19', 'False Demon', 'false-demon', '{"life": 4, "name": "False Demon", "stub": "false-demon", "text": "Unit Guard: This unit may guard a unit being attacked.\n\n* Illusion: If this unit receives damage as a result of a unit''s attack or counter, destroy this unit.", "type": "Conjuration", "attack": 1, "copies": 5, "recover": 0, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '1', 'Conjuration', '0', '0', NULL, '5', 'f', 'False Demon
Unit Guard This unit may guard a unit being attacked. Illusion If this unit receives damage as a result of a unit''s attack or counter, destroy this unit.', '0', '19', '1', NULL, NULL, 't'),
('20', 'Fear', 'fear', '{"cost": ["[[main]]"], "name": "Fear", "stub": "fear", "text": "Choose a target unit under an opponent''s control. If it is a conjuration, return it to its owner''s conjuration pile. Otherwise, return it to its owner''s hand.", "type": "Action Spell", "weight": 5, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Discard", "phoenixborn": "Jessa Na Ni"}', '1', 'Action Spell', '5', '0', 'Jessa Na Ni', NULL, 'f', 'Fear
Choose a target unit under an opponent''s control. If it is a conjuration, return it to its owner''s conjuration pile. Otherwise, return it to its owner''s hand.', '0', '20', '1', NULL, NULL, 't'),
('21', 'Final Cry', 'final-cry', '{"cost": ["1 [[ceremonial:power]]"], "dice": ["ceremonial"], "name": "Final Cry", "stub": "final-cry", "text": "You may play this spell when a unit you control is destroyed. Deal 2 damage to a target unit or Phoenixborn.", "type": "Reaction Spell", "weight": 102, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"ceremonial:power": 1}, "placement": "Discard"}', '1', 'Reaction Spell', '102', '1', NULL, NULL, 'f', 'Final Cry
You may play this spell when a unit you control is destroyed. Deal 2 damage to a target unit or Phoenixborn.', '0', '21', '1', NULL, NULL, 't'),
('22', 'Gilder', 'gilder', '{"life": 2, "name": "Gilder", "stub": "gilder", "text": "Unit Guard: This unit may guard a unit that is being attacked.\n\n* Inheritance 1: When this unit is destroyed you may place 1 status token on a target unit.", "type": "Conjuration", "attack": 1, "copies": 5, "recover": 0, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '1', 'Conjuration', '0', '0', NULL, '5', 'f', 'Gilder
Unit Guard This unit may guard a unit that is being attacked. Inheritance 1 When this unit is destroyed you may place 1 status token on a target unit.', '0', '22', '1', NULL, NULL, 't'),
('23', 'Golden Veil', 'golden-veil', '{"cost": ["1 [[natural:class]]", "1 [[charm:class]]"], "dice": ["natural", "charm"], "name": "Golden Veil", "stub": "golden-veil", "text": "You may play this spell when an opponent uses a spell, ability, or dice power that would target a unit you control. Cancel the effects of that spell, ability, or dice power.", "type": "Reaction Spell", "weight": 202, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"charm:class": 1, "natural:class": 1}, "placement": "Discard"}', '1', 'Reaction Spell', '202', '10', NULL, NULL, 'f', 'Golden Veil
You may play this spell when an opponent uses a spell, ability, or dice power that would target a unit you control. Cancel the effects ot that spell, ability, or dice power.', '0', '23', '1', NULL, NULL, 't'),
('24', 'Hammer Knight', 'hammer-knight', '{"cost": ["[[main]]", "1 [[ceremonial:power]]", "1 [[natural:class]]", "1 [[basic]]"], "dice": ["ceremonial", "natural"], "life": 3, "name": "Hammer Knight", "stub": "hammer-knight", "text": "Aftershock 1: When this unit deals damage by attacking or countering, you may place 1 wound token on a target unit.", "type": "Ally", "attack": 4, "weight": 308, "recover": 1, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "natural:class": 1, "ceremonial:power": 1}, "placement": "Battlefield"}', '1', 'Ally', '308', '9', NULL, NULL, 'f', 'Hammer Knight
Aftershock 1 When this unit deals damage by attacking or countering, you may place 1 wound token on a target unit.', '0', '24', '1', NULL, NULL, 't'),
('25', 'Hidden Power', 'hidden-power', '{"cost": ["[[main]]", "1 [[illusion:class]]"], "dice": ["illusion"], "name": "Hidden Power", "stub": "hidden-power", "text": "Select 2 dice in your exhausted pool and place them into your active pool on a side of your choice.", "type": "Action Spell", "weight": 106, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"illusion:class": 1}, "placement": "Discard", "diceRecursion": 2}', '1', 'Action Spell', '106', '4', NULL, NULL, 'f', 'Hidden Power
Select 2 dice in your exhausted pool and place them into your active pool on a side of your choice.', '0', '25', '1', NULL, NULL, 't'),
('26', 'Hypnotize', 'hypnotize', '{"cost": ["[[main]]"], "dice": ["charm"], "name": "Hypnotize", "stub": "hypnotize", "text": "[[side]] - [[exhaust]] - 2 [[charm:class]]: Choose a target unit you control to gain the following ability for the remainder of the turn.\n\nBypass: This unit cannot be blocked or guarded.", "type": "Ready Spell", "weight": 5, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "effectMagicCost": {"charm:class": 2}}', '1', 'Ready Spell', '5', '2', NULL, NULL, 'f', 'Hypnotize
Choose a target unit you control to gain the following ability for the remainder of the turn. Bypass This unit cannot be blocked or guarded.', '0', '26', '1', NULL, NULL, 't'),
('27', 'Iron Rhino', 'iron-rhino', '{"life": 4, "name": "Iron Rhino", "stub": "iron-rhino", "text": "", "type": "Conjuration", "attack": 5, "copies": 5, "recover": 0, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '1', 'Conjuration', '0', '0', NULL, '5', 'f', 'Iron Rhino
', '0', '27', '1', NULL, NULL, 't'),
('28', 'Iron Worker', 'iron-worker', '{"cost": ["[[main]]", "2 [[basic]]"], "life": 2, "name": "Iron Worker", "stub": "iron-worker", "text": "* Resourceful 1: When this unit comes into play, place 1 status token on this unit. At the beginning of the player turns phase, place 1 status token on this unit.\n\n* Overtime: Anytime during your turn, you may remove any number of status tokens from this unit. For each status token removed, you may take 1 additional side action ([[side]]) this turn.", "type": "Ally", "attack": 2, "weight": 205, "recover": 1, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 2}, "placement": "Battlefield"}', '1', 'Ally', '205', '0', NULL, NULL, 'f', 'Iron Worker
Resourceful 1 When this unit comes into play, place 1 status token on this unit. At the beginning of the player turns phase, place 1 status token on this unit. Overtime Anytime during your turn, you may remove any number of status tokens from this unit. For each status token removed, you may take 1 additional side action () this turn.', '0', '28', '1', NULL, NULL, 't'),
('29', 'Jessa Na Ni', 'jessa-na-ni', '{"life": 18, "name": "Jessa Na Ni", "stub": "jessa-na-ni", "text": "Screams of the Departed: Whenever a unit under an opponent''s control leaves play, you may spend 1 [[basic]] to deal 1 damage to their Phoenixborn.", "type": "Phoenixborn", "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "spellboard": 4, "battlefield": 5, "effectRepeats": true, "effectMagicCost": {"basic": 1}}', '1', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Jessa Na Ni
Screams of the Departed Whenever a unit under an opponent''s control leaves play, you may spend 1  to deal 1 damage to their Phoenixborn.', '0', '29', '1', NULL, NULL, 't'),
('30', 'Leech Warrior', 'leech-warrior', '{"cost": ["[[main]]", "2 [[ceremonial:class]]", "1 [[basic]]"], "dice": ["ceremonial"], "life": 3, "name": "Leech Warrior", "stub": "leech-warrior", "text": "Shadow Drain 1: When this unit receives 1 or more damage, you may select 1 die in a target player''s active pool and place it in that player''s exhausted pool.", "type": "Ally", "attack": 2, "weight": 307, "recover": 3, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "ceremonial:class": 2}, "placement": "Battlefield"}', '1', 'Ally', '307', '1', NULL, NULL, 'f', 'Leech Warrior
Shadow Drain 1 When this unit receives 1 or more damage, you may select 1 die in a target player''s active pool and place it in that player''s exhausted pool.', '0', '30', '1', NULL, NULL, 't'),
('31', 'Living Doll', 'living-doll', '{"cost": ["[[main]]", "1 [[ceremonial:class]]", "1 [[charm:class]]", "1 [[basic]]"], "dice": ["ceremonial", "charm"], "life": 3, "name": "Living Doll", "stub": "living-doll", "text": "Pain Link: Whenever this unit receives damage, you may spend 1 [[basic]] to inflict X amount of damage to a target unit or Phoenixborn.\n\nX = the damage received or this unit''s life value, whichever is less.", "type": "Ally", "attack": 0, "weight": 307, "recover": 1, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "charm:class": 1, "ceremonial:class": 1}, "placement": "Battlefield", "effectRepeats": true, "effectMagicCost": {"basic": 1}}', '1', 'Ally', '307', '3', NULL, NULL, 'f', 'Living Doll
Pain Link Whenever this unit receives damage, you may spend 1  to inflict X amount of damage to a target unit or Phoenixborn. X = the damage received or this unit''s life value, whichever is less.', '0', '31', '1', NULL, NULL, 't'),
('32', 'Maeoni Viper', 'maeoni-viper', '{"life": 22, "name": "Maeoni Viper", "stub": "maeoni-viper", "text": "Strike: After a player has declared attackers, you may spend 1 [[basic]] and place 1 exhaustion token on this card. If you do, add 2 to a target unit''s attack value for the remainder of this turn.", "type": "Phoenixborn", "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "spellboard": 4, "battlefield": 3, "effectMagicCost": {"basic": 1}}', '1', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Maeoni Viper
Strike After a player has declared attackers, you may spend 1  and place 1 exhaustion token on this card. If you do, add 2 to a target unit''s attack value for the remainder of this turn.', '0', '32', '1', NULL, NULL, 't'),
('33', 'Masked Wolf', 'masked-wolf', '{"life": 1, "name": "Masked Wolf", "stub": "masked-wolf", "text": "", "type": "Conjuration", "attack": 2, "copies": 5, "recover": 0, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield", "phoenixborn": "Noah Redmoon"}', '1', 'Conjuration', '0', '0', 'Noah Redmoon', '5', 'f', 'Masked Wolf
', '0', '33', '1', NULL, NULL, 't'),
('34', 'Massive Growth', 'massive-growth', '{"cost": ["[[main]]", "1 [[natural:class]]", "1 [[basic]]"], "dice": ["natural"], "life": "+4", "name": "Massive Growth", "stub": "massive-growth", "text": "* This spell can only be attached to a unit with an attack value of 2 or less.\n\n* Spell Guard: This spell cannot be affected by an opponent''s spell.\n\n* Fleeting: Discard this card at the end of this round.", "type": "Alteration Spell", "attack": "+4", "weight": 206, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "natural:class": 1}, "placement": "Unit"}', '1', 'Alteration Spell', '206', '8', NULL, NULL, 'f', 'Massive Growth
This spell can only be attached to a unit with an attack value of 2 or less. Spell Guard This spell cannot be affected by an opponent''s spell. Fleeting Discard this card at the end of this round.', '0', '34', '1', NULL, NULL, 't'),
('35', 'Mist Spirit', 'mist-spirit', '{"life": 1, "name": "Mist Spirit", "stub": "mist-spirit", "text": "", "type": "Conjuration", "attack": 1, "copies": 10, "recover": 0, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '1', 'Conjuration', '0', '0', NULL, '10', 'f', 'Mist Spirit
', '0', '35', '1', NULL, NULL, 't'),
('36', 'Mist Typhoon', 'mist-typhoon', '{"cost": ["[[main]]", "1 [[illusion:class]]", "1 [[natural:class]]"], "dice": ["illusion", "natural"], "name": "Mist Typhoon", "stub": "mist-typhoon", "text": "Deal 1 damage to all opponent''s units. You may draw 1 card.", "type": "Action Spell", "weight": 207, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"natural:class": 1, "illusion:class": 1}, "placement": "Discard"}', '1', 'Action Spell', '207', '12', NULL, NULL, 'f', 'Mist Typhoon
Deal 1 damage to all opponent''s units. You may draw 1 card.', '0', '36', '1', NULL, NULL, 't'),
('37', 'Molten Gold', 'molten-gold', '{"cost": ["[[main]]", "2 [[natural:power]]"], "dice": ["natural"], "name": "Molten Gold", "stub": "molten-gold", "text": "Place 3 wound tokens on a target unit or Phoenixborn.", "type": "Action Spell", "weight": 209, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"natural:power": 2}, "placement": "Discard"}', '1', 'Action Spell', '209', '8', NULL, NULL, 'f', 'Molten Gold
Place 3 wound tokens on a target unit or Phoenixborn.', '0', '37', '1', NULL, NULL, 't'),
('38', 'Noah Redmoon', 'noah-redmoon', '{"dice": ["ceremonial"], "life": 20, "name": "Noah Redmoon", "stub": "noah-redmoon", "text": "Shadow Target: [[side]] - [[exhaust]] - 1 [[ceremonial:class]]: Place 1 exhaustion token on a target ready spell on an opponent''s spellboard.", "type": "Phoenixborn", "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "spellboard": 3, "battlefield": 6, "effectMagicCost": {"ceremonial:class": 1}}', '1', 'Phoenixborn', '0', '1', NULL, NULL, 'f', 'Noah Redmoon
Shadow Target Place 1 exhaustion token on a target ready spell on an opponent''s spellboard.', '0', '38', '1', NULL, NULL, 't'),
('39', 'One Hundred Blades', 'one-hundred-blades', '{"cost": ["[[main]]", "2 [[basic]]"], "name": "One Hundred Blades", "stub": "one-hundred-blades", "text": "Deal 1 damage to a target Phoenixborn. Deal 1 damage to all opponents'' units. Draw 1 card.", "type": "Action Spell", "weight": 205, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 2}, "placement": "Discard", "phoenixborn": "Coal Roarkwin"}', '1', 'Action Spell', '205', '0', 'Coal Roarkwin', NULL, 'f', 'One Hundred Blades
Deal 1 damage to a target Phoenixborn. Deal 1 damage to all opponents'' units. Draw 1 card.', '0', '39', '1', NULL, NULL, 't'),
('40', 'Open Memories', 'open-memories', '{"cost": ["[[main]]", "1 [[charm:class]]", "1 [[basic]]"], "dice": ["charm"], "name": "Open Memories", "stub": "open-memories", "text": "You may search your draw pile for 1 card and place it into your hand. If you do, shuffle your draw pile.", "type": "Action Spell", "weight": 206, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "charm:class": 1}, "placement": "Discard"}', '1', 'Action Spell', '206', '2', NULL, NULL, 'f', 'Open Memories
You may search your draw pile for 1 card and place it into your hand. If you do, shuffle your draw pile.', '0', '40', '1', NULL, NULL, 't'),
('41', 'Out Of The Mist', 'out-of-the-mist', '{"cost": ["[[side]]", "1 [[illusion:power]]", "1 [[natural:power]]"], "dice": ["illusion", "natural"], "name": "Out Of The Mist", "stub": "out-of-the-mist", "text": "Deal X amount of damage to a target unit. You may draw 1 card.\n\nX = the number of units you have in play.", "type": "Action Spell", "weight": 208, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"natural:power": 1, "illusion:power": 1}, "placement": "Discard"}', '1', 'Action Spell', '208', '12', NULL, NULL, 'f', 'Out Of The Mist
Deal X amount of damage to a target unit. You may draw 1 card. X = the number of units you have in play.', '0', '41', '1', NULL, NULL, 't'),
('42', 'Protect', 'protect', '{"cost": ["[[main]]", "1 [[natural:class]]", "1 [[ceremonial:class]]"], "dice": ["natural", "ceremonial"], "name": "Protect", "stub": "protect", "text": "* When this spell comes into play, place 3 status tokens on it. Discard this card when it no longer has any status tokens on it.\n\nWhen a unit you control would receive damage, you may remove any number of status tokens from this spell. For each status token removed, prevent 1 damage to that unit.", "type": "Ready Spell", "weight": 207, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"natural:class": 1, "ceremonial:class": 1}, "placement": "Spellboard"}', '1', 'Ready Spell', '207', '9', NULL, NULL, 'f', 'Protect
When this spell comes into play, place 3 status tokens on it. Discard this card when it no longer has any status tokens on it. When a unit you control would receive damage, you may remove any number of status tokens from this spell. For each status token removed, prevent 1 damage to that unit.', '0', '42', '1', NULL, NULL, 't'),
('43', 'Purge', 'purge', '{"cost": ["[[main]]"], "dice": ["charm"], "name": "Purge", "stub": "purge", "text": "[[main]] - [[exhaust]] - 1 [[charm:class]]: Choose a target player to discard 1 card off the top of their draw pile.\n\nFocus 1: You may pay 1 [[basic]] to have the target player discard 1 additional card.", "type": "Ready Spell", "weight": 5, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "effectMagicCost": {"basic": 1, "charm:class": 1}}', '1', 'Ready Spell', '5', '2', NULL, NULL, 'f', 'Purge
Choose a target player to discard 1 card off the top of their draw pile. Focus 1 You may pay 1  to have the target player discard 1 additional card.', '0', '43', '1', NULL, NULL, 't'),
('44', 'Redirect', 'redirect', '{"cost": ["1 [[charm:class]]"], "dice": ["charm"], "name": "Redirect", "stub": "redirect", "text": "You may play this spell when your Phoenixborn would be dealt damage and you have at least one unit in play. Do not deal that damage to your Phoenixborn. Instead deal that damage to a target unit you control.", "type": "Reaction Spell", "weight": 101, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"charm:class": 1}, "placement": "Discard"}', '1', 'Reaction Spell', '101', '2', NULL, NULL, 'f', 'Redirect
You may play this spell when your Phoenixborn would be dealt damage and you have at least one unit in play. Do not deal that damage to your Phoenixborn. Instead deal that damage to a target unit you control.', '0', '44', '1', NULL, NULL, 't'),
('45', 'Reflections In The Water', 'reflections-in-the-water', '{"cost": ["[[main]]", "1 [[illusion:class]]"], "dice": ["illusion"], "name": "Reflections In The Water", "stub": "reflections-in-the-water", "text": "As long as this spell is attached to this unit it is considered to have no abilities other than inexhaustible abilities.\n\n* Respark: 1 [[basic]]", "type": "Alteration Spell", "weight": 106, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"illusion:class": 1}, "placement": "Unit", "effectMagicCost": {"basic": 1}}', '1', 'Alteration Spell', '106', '4', NULL, NULL, 'f', 'Reflections In The Water
As long as this spell is attached to this unit it is considered to have no abilities other than inexhaustible abilities. Respark 1', '0', '45', '1', NULL, NULL, 't'),
('46', 'Refresh', 'refresh', '{"cost": ["[[main]]", "1 [[charm:class]]", "1 [[basic]]"], "dice": ["charm"], "name": "Refresh", "stub": "refresh", "text": "Remove all exhaustion tokens from a target unit.", "type": "Action Spell", "weight": 206, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "charm:class": 1}, "placement": "Discard"}', '1', 'Action Spell', '206', '2', NULL, NULL, 'f', 'Refresh
Remove all exhaustion tokens from a target unit.', '0', '46', '1', NULL, NULL, 't'),
('47', 'Root Armor', 'root-armor', '{"cost": ["[[side]]", "1 [[natural:class]]"], "dice": ["natural"], "life": "+2", "name": "Root Armor", "stub": "root-armor", "text": "* Respark: 1 [[basic]]", "type": "Alteration Spell", "weight": 105, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"natural:class": 1}, "placement": "Unit", "effectMagicCost": {"basic": 1}}', '1', 'Alteration Spell', '105', '8', NULL, NULL, 'f', 'Root Armor
Respark 1', '0', '47', '1', NULL, NULL, 't'),
('48', 'Rose Fire Dancer', 'rose-fire-dancer', '{"cost": ["[[main]]", "1 [[illusion:class]]", "1 [[basic]]"], "dice": ["illusion"], "life": 1, "name": "Rose Fire Dancer", "stub": "rose-fire-dancer", "text": "Distract: [[side]] - [[exhaust]]: Place 1 exhaustion token on a target unit.", "type": "Ally", "attack": 3, "weight": 206, "recover": 0, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "illusion:class": 1}, "placement": "Battlefield"}', '1', 'Ally', '206', '4', NULL, NULL, 'f', 'Rose Fire Dancer
Distract Place 1 exhaustion token on a target unit.', '0', '48', '1', NULL, NULL, 't'),
('49', 'Saria Guideman', 'saria-guideman', '{"dice": ["charm"], "life": 20, "name": "Saria Guideman", "stub": "saria-guideman", "text": "Heart''s Pull: [[side]] - [[exhaust]] - 1 [[charm:class]]: You may draw 1 card. If you do, you may choose a target player to discard 1 card off the top of their draw pile.", "type": "Phoenixborn", "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "spellboard": 4, "battlefield": 5, "effectMagicCost": {"charm:class": 1}}', '1', 'Phoenixborn', '0', '2', NULL, NULL, 'f', 'Saria Guideman
Heart''s Pull You may draw 1 card. If you do, you may choose a target player to discard 1 card off the top of their draw pile.', '0', '49', '1', NULL, NULL, 't'),
('50', 'Seal', 'seal', '{"cost": ["[[main]]", "1 [[illusion:class]]", "1 [[charm:class]]"], "dice": ["illusion", "charm"], "name": "Seal", "stub": "seal", "text": "Choose a ready spell on a target player''s spellboard. Place 1 exhaustion token on the chosen spell and on each other copy of the chosen spell on that player''s spellboard.", "type": "Action Spell", "weight": 207, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"charm:class": 1, "illusion:class": 1}, "placement": "Discard"}', '1', 'Action Spell', '207', '6', NULL, NULL, 'f', 'Seal
Choose a ready spell on a target player''s spellboard. Place 1 exhaustion token on the chosen spell and on each other copy of the chosen spell on that player''s spellboard.', '0', '50', '1', NULL, NULL, 't'),
('51', 'Seaside Raven', 'seaside-raven', '{"life": 2, "name": "Seaside Raven", "stub": "seaside-raven", "text": "Battle Advantage: When this unit is in battle, it inflicts its damage before other units without Battle Advantage inflict their damage.\n\n* Magic Guard: This unit cannot be affected by an opponent''s spell.", "type": "Conjuration", "attack": 3, "copies": 2, "recover": 0, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield", "phoenixborn": "Saria Guideman"}', '1', 'Conjuration', '0', '0', 'Saria Guideman', '2', 'f', 'Seaside Raven
Battle Advantage When this unit is in battle, it inflicts its damage before other units without Battle Advantage inflict their damage. Magic Guard This unit cannot be affected by an opponent''s spell.', '0', '51', '1', NULL, NULL, 't'),
('52', 'Shadow Counter', 'shadow-counter', '{"cost": ["1 [[illusion:class]]", "1 [[basic]]"], "dice": ["illusion"], "name": "Shadow Counter", "stub": "shadow-counter", "text": "You may play this spell after your Phoenixborn receives damage from an attack. Deal 6 damage to a target unit your opponent controls.", "type": "Reaction Spell", "weight": 201, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "illusion:class": 1}, "placement": "Discard"}', '1', 'Reaction Spell', '201', '4', NULL, NULL, 'f', 'Shadow Counter
You may play this spell after your Phoenixborn receives damage from an attack. Deal 6 damage to a target unit your opponent controls.', '0', '52', '1', NULL, NULL, 't'),
('53', 'Shifting Mist', 'shifting-mist', '{"cost": ["[[main]]", "1 [[illusion:class]]"], "dice": ["illusion"], "name": "Shifting Mist", "stub": "shifting-mist", "text": "[[side]] - [[exhaust]]: Change 2 dice in your active pool to a side of your choice.", "type": "Ready Spell", "weight": 106, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"illusion:class": 1}, "placement": "Spellboard"}', '1', 'Ready Spell', '106', '4', NULL, NULL, 'f', 'Shifting Mist
Change 2 dice in your active pool to a side of your choice.', '0', '53', '1', NULL, NULL, 't'),
('54', 'Silver Snake', 'silver-snake', '{"life": 4, "name": "Silver Snake", "stub": "silver-snake", "text": "* Consume: Whenever an opponent''s unit is destroyed as a result of a spell, attack, counter, ability, or dice power you control, place 1 status token on this unit. If the destroyed unit was an ally, remove it from the game.\n\n* X = the number of status tokens on this unit.", "type": "Conjuration", "attack": "X", "copies": 3, "recover": 3, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield", "phoenixborn": "Maeoni Viper"}', '1', 'Conjuration', '0', '0', 'Maeoni Viper', '3', 'f', 'Silver Snake
Consume Whenever an opponent''s unit is destroyed as a result of a spell, attack, counter, ability, or dice power you control, place 1 status token on this unit. If the destroyed unit was an ally, remove it from the game. X = the number of status tokens on this unit.', '0', '54', '1', NULL, NULL, 't'),
('55', 'Sleeping Widow', 'sleeping-widow', '{"life": 1, "name": "Sleeping Widow", "stub": "sleeping-widow", "text": "", "type": "Conjuration", "attack": 2, "copies": 6, "recover": 0, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '1', 'Conjuration', '0', '0', NULL, '6', 'f', 'Sleeping Widow
', '0', '55', '1', NULL, NULL, 't'),
('56', 'Sleight Of Hand', 'sleight-of-hand', '{"cost": ["[[main]]", "1 [[illusion:power]]", "1 [[basic]]"], "dice": ["illusion"], "name": "Sleight Of Hand", "stub": "sleight-of-hand", "text": "Draw 3 cards.", "type": "Action Spell", "weight": 207, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "illusion:power": 1}, "placement": "Discard"}', '1', 'Action Spell', '207', '4', NULL, NULL, 'f', 'Sleight Of Hand
Draw 3 cards.', '0', '56', '1', NULL, NULL, 't'),
('57', 'Small Sacrifice', 'small-sacrifice', '{"cost": ["[[main]]"], "dice": ["ceremonial"], "name": "Small Sacrifice", "stub": "small-sacrifice", "text": "[[main]] - [[exhaust]] - 1 [[ceremonial:class]]: Deal 1 damage to a target unit on your battlefield. If you do, you may deal 1 damage to a target unit on an opponent''s battlefield.\n\nFocus 1: If both targeted units are unexhausted, you may place 1 exhaustion token on both units instead of damage.", "type": "Ready Spell", "weight": 5, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "effectMagicCost": {"ceremonial:class": 1}}', '1', 'Ready Spell', '5', '1', NULL, NULL, 'f', 'Small Sacrifice
Deal 1 damage to a target unit on your battlefield. If you do, you may deal 1 damage to a target unit on an opponent''s battlefield. Focus 1 If both targeted units are unexhausted, you may place 1 exhaustion token on both units instead of damage.', '0', '57', '1', NULL, NULL, 't'),
('58', 'Spiked Armor', 'spiked-armor', '{"cost": ["[[main]]", "1 [[natural:class]]", "1 [[basic]]"], "dice": ["natural"], "life": "+2", "name": "Spiked Armor", "stub": "spiked-armor", "text": "* This unit now has the following ability:\n\n* Spiked Skin 2: When this unit is dealt damage by one or more attacking or countering units, deal 2 damage to each unit that is attacking or countering this unit.", "type": "Alteration Spell", "weight": 206, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "natural:class": 1}, "placement": "Unit"}', '1', 'Alteration Spell', '206', '8', NULL, NULL, 'f', 'Spiked Armor
This unit now has the following ability: Spiked Skin 2 When this unit is dealt damage by one or more attacking or countering units, deal 2 damage to each unit that is attacking or countering this unit.', '0', '58', '1', NULL, NULL, 't'),
('59', 'Steady Gaze', 'steady-gaze', '{"cost": ["[[main]]", "2 [[illusion:class]]"], "dice": ["illusion"], "name": "Steady Gaze", "stub": "steady-gaze", "text": "Place 2 exhaustion tokens on a target unit.", "type": "Action Spell", "weight": 207, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"illusion:class": 2}, "placement": "Discard"}', '1', 'Action Spell', '207', '4', NULL, NULL, 'f', 'Steady Gaze
Place 2 exhaustion tokens on a target unit.', '0', '59', '1', NULL, NULL, 't'),
('60', 'Stormwind Sniper', 'stormwind-sniper', '{"cost": ["[[main]]", "1 [[illusion:class]]", "1 [[ceremonial:class]]", "1 [[basic]]"], "dice": ["illusion", "ceremonial"], "life": 1, "name": "Stormwind Sniper", "stub": "stormwind-sniper", "text": "Ambush 2: When this unit comes into play, you may inflict 2 damage on a target unit or Phoenixborn.", "type": "Ally", "attack": 2, "weight": 307, "recover": 1, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "illusion:class": 1, "ceremonial:class": 1}, "placement": "Battlefield"}', '1', 'Ally', '307', '5', NULL, NULL, 'f', 'Stormwind Sniper
Ambush 2 When this unit comes into play, you may inflict 2 damage on a target unit or Phoenixborn.', '0', '60', '1', NULL, NULL, 't'),
('61', 'Strange Copy', 'strange-copy', '{"cost": ["[[main]]", "2 [[illusion:class]]"], "dice": ["illusion"], "name": "Strange Copy", "stub": "strange-copy", "text": "* When placing this spell onto your battlefield, choose a unit an opponent has in play. Place status tokens on this spell equal to the chosen unit''s attack value. This spell is considered to be an ally that has an attack and life value equal to the number of status tokens on it, and a recover value of 0. Alterations cannot be placed on this spell.\n\n* Fleeting: Discard this card at the end of this round.", "type": "Action Spell", "weight": 207, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"illusion:class": 2}, "placement": "Discard"}', '1', 'Action Spell', '207', '4', NULL, NULL, 'f', 'Strange Copy
When placing this spell onto your battlefield, choose a unit an opponent has in play. Place status tokens on this spell equal to the chosen unit''s attack value. This spell is considered to be an ally that has an attack and life value equal to the number of status tokens on it, and a recover value of 0. Alterations cannot be placed on this spell. Fleeting Discard this card at the end of this round.', '0', '61', '1', NULL, NULL, 't'),
('62', 'Strengthen', 'strengthen', '{"cost": ["[[main]]", "1 [[natural:class]]", "1 [[ceremonial:class]]"], "dice": ["natural", "ceremonial"], "name": "Strengthen", "stub": "strengthen", "text": "[[side]] - [[exhaust]]: Add 2 to a target unit''s attack value for the remainder of the turn.\n\nFocus 2: Add 1 more to that unit''s attack value for the remainder of the turn.", "type": "Ready Spell", "weight": 207, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"natural:class": 1, "ceremonial:class": 1}, "placement": "Spellboard"}', '1', 'Ready Spell', '207', '9', NULL, NULL, 'f', 'Strengthen
Add 2 to a target unit''s attack value for the remainder of the turn. Focus 2 Add 1 more to that unit''s attack value for the remainder of the turn.', '0', '62', '1', NULL, NULL, 't'),
('63', 'Summon Blood Puppet', 'summon-blood-puppet', '{"cost": ["[[main]]"], "dice": ["ceremonial"], "name": "Summon Blood Puppet", "stub": "summon-blood-puppet", "text": "[[main]] - [[exhaust]] - 1 [[ceremonial:class]]: Place a [[Blood Puppet]] conjuration onto a target player''s battlefield.", "type": "Ready Spell", "weight": 5, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "conjurations": [{"name": "Blood Puppet", "stub": "blood-puppet"}], "effectMagicCost": {"ceremonial:class": 1}}', '1', 'Ready Spell', '5', '1', NULL, NULL, 't', 'Summon Blood Puppet
Place a Blood Puppet conjuration onto a target player''s battlefield.', '0', '63', '1', NULL, NULL, 't'),
('64', 'Summon Blue Jaguar', 'summon-blue-jaguar', '{"cost": ["[[main]]"], "name": "Summon Blue Jaguar", "stub": "summon-blue-jaguar", "text": "[[main]] - [[exhaust]] - 2 [[basic]]: Place a [[Blue Jaguar]] conjuration onto your battlefield.", "type": "Ready Spell", "weight": 5, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "phoenixborn": "Aradel Summergaard", "conjurations": [{"name": "Blue Jaguar", "stub": "blue-jaguar"}], "effectMagicCost": {"basic": 2}}', '1', 'Ready Spell', '5', '0', 'Aradel Summergaard', NULL, 't', 'Summon Blue Jaguar
Place a Blue Jaguar conjuration onto your battlefield.', '0', '64', '1', NULL, NULL, 't'),
('65', 'Summon Butterfly Monk', 'summon-butterfly-monk', '{"cost": ["[[main]]"], "dice": ["natural"], "name": "Summon Butterfly Monk", "stub": "summon-butterfly-monk", "text": "[[main]] - [[exhaust]] - 1 [[natural:power]]: Place a [[Butterfly Monk]] conjuration onto your battlefield.", "type": "Ready Spell", "weight": 5, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "conjurations": [{"name": "Butterfly Monk", "stub": "butterfly-monk"}], "effectMagicCost": {"natural:power": 1}}', '1', 'Ready Spell', '5', '8', NULL, NULL, 't', 'Summon Butterfly Monk
Place a Butterfly Monk conjuration onto your battlefield.', '0', '65', '1', NULL, NULL, 't'),
('66', 'Summon False Demon', 'summon-false-demon', '{"cost": ["[[main]]"], "dice": ["illusion"], "name": "Summon False Demon", "stub": "summon-false-demon", "text": "[[main]] - [[exhaust]] - 1 [[illusion:class]] - 1 [[basic]]: Place a [[False Demon]] conjuration onto your battlefield.", "type": "Ready Spell", "weight": 5, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "conjurations": [{"name": "False Demon", "stub": "false-demon"}], "effectMagicCost": {"basic": 1, "illusion:class": 1}}', '1', 'Ready Spell', '5', '4', NULL, NULL, 't', 'Summon False Demon
Place a False Demon conjuration onto your battlefield.', '0', '66', '1', NULL, NULL, 't'),
('67', 'Summon Gilder', 'summon-gilder', '{"cost": ["[[main]]", "1 [[charm:class]]"], "dice": ["charm", "natural"], "name": "Summon Gilder", "stub": "summon-gilder", "text": "[[main]] - [[exhaust]] - 1 [[natural:class]]: Place a [[Gilder]] conjuration onto your battlefield. You may deal 1 damage to a target unit.", "type": "Ready Spell", "weight": 106, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"charm:class": 1}, "placement": "Spellboard", "conjurations": [{"name": "Gilder", "stub": "gilder"}], "effectMagicCost": {"natural:class": 1}}', '1', 'Ready Spell', '106', '10', NULL, NULL, 't', 'Summon Gilder
Place a Gilder conjuration onto your battlefield. You may deal 1 damage to a target unit.', '0', '67', '1', NULL, NULL, 't'),
('68', 'Summon Iron Rhino', 'summon-iron-rhino', '{"cost": ["[[main]]", "1 [[natural:class]]"], "dice": ["natural"], "name": "Summon Iron Rhino", "stub": "summon-iron-rhino", "text": "[[main]] - [[exhaust]] - 6 [[basic]]: Place an [[Iron Rhino]] conjuration onto your battlefield.\n\nFocus 1: Reduce the activate cost of this spell by 1 [[basic]].\n\nFocus 2: Reduce the activation cost of this spell by an additional 1 [[basic]].", "type": "Ready Spell", "weight": 106, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"natural:class": 1}, "placement": "Spellboard", "conjurations": [{"name": "Iron Rhino", "stub": "iron-rhino"}], "effectMagicCost": {"basic": 6}}', '1', 'Ready Spell', '106', '8', NULL, NULL, 't', 'Summon Iron Rhino
Place an Iron Rhino conjuration onto your battlefield. Focus 1 Reduce the activate cost of this spell by 1 . Focus 2 Reduce the activation cost of this spell by an additional 1 .', '0', '68', '1', NULL, NULL, 't'),
('69', 'Summon Masked Wolf', 'summon-masked-wolf', '{"cost": ["[[main]]"], "dice": ["illusion"], "name": "Summon Masked Wolf", "stub": "summon-masked-wolf", "text": "[[side]] - [[exhaust]] - 1 [[illusion:class]] - 1 [[basic]]: Place a [[Masked Wolf]] conjuration onto your battlefield.\n\nFocus 1: You may change the activation cost of this ability to [[side]] - [[exhaust]] - 1 [[illusion:power]].", "type": "Ready Spell", "weight": 5, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "phoenixborn": "Noah Redmoon", "conjurations": [{"name": "Masked Wolf", "stub": "masked-wolf"}], "effectMagicCost": {"basic": 1, "illusion:class": 1}}', '1', 'Ready Spell', '5', '4', 'Noah Redmoon', NULL, 't', 'Summon Masked Wolf
Place a Masked Wolf conjuration onto your battlefield. Focus 1 You may change the activation cost of this ability to  -  - 1 .', '0', '69', '1', NULL, NULL, 't'),
('70', 'Summon Mist Spirit', 'summon-mist-spirit', '{"cost": ["[[main]]"], "dice": ["illusion"], "name": "Summon Mist Spirit", "stub": "summon-mist-spirit", "text": "[[main]] - [[exhaust]] - 1 [[illusion:class]]: Place a [[Mist Spirit]] conjuration onto your battlefield. You may spend an additional 1 [[basic]] when activating this spell to place an additional [[Mist Spirit]] conjuration onto your battlefield.", "type": "Ready Spell", "weight": 5, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "conjurations": [{"name": "Mist Spirit", "stub": "mist-spirit"}], "effectMagicCost": {"basic": 1, "illusion:class": 1}}', '1', 'Ready Spell', '5', '4', NULL, NULL, 't', 'Summon Mist Spirit
Place a Mist Spirit conjuration onto your battlefield. You may spend an additional 1  when activating this spell to place an additional Mist Spirit conjuration onto your battlefield.', '0', '70', '1', NULL, NULL, 't'),
('71', 'Summon Seaside Raven', 'summon-seaside-raven', '{"cost": ["[[main]]"], "name": "Summon Seaside Raven", "stub": "summon-seaside-raven", "text": "[[main]] - [[exhaust]] - 3 [[basic]]: Place a [[Seaside Raven]] conjuration onto your battlefield.", "type": "Ready Spell", "weight": 5, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "phoenixborn": "Saria Guideman", "conjurations": [{"name": "Seaside Raven", "stub": "seaside-raven"}], "effectMagicCost": {"basic": 3}}', '1', 'Ready Spell', '5', '0', 'Saria Guideman', NULL, 't', 'Summon Seaside Raven
Place a Seaside Raven conjuration onto your battlefield.', '0', '71', '1', NULL, NULL, 't'),
('72', 'Summon Silver Snake', 'summon-silver-snake', '{"cost": ["[[main]]"], "dice": ["charm", "natural"], "name": "Summon Silver Snake", "stub": "summon-silver-snake", "text": "[[main]] - [[exhaust]] - 1 [[charm:power]] - 1 [[natural:power]]: Place a [[Silver Snake]] conjuration onto your battlefield.\n\nFocus 1: Place 1 status token on that Silver Snake.\n\nFocus 2: Place 1 additional status token on that Silver Snake.\n\n* Spell Guard: This spell cannot be affected by an opponent''s spell.", "type": "Ready Spell", "weight": 5, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "phoenixborn": "Maeoni Viper", "conjurations": [{"name": "Silver Snake", "stub": "silver-snake"}], "effectMagicCost": {"charm:power": 1, "natural:power": 1}}', '1', 'Ready Spell', '5', '10', 'Maeoni Viper', NULL, 't', 'Summon Silver Snake
Place a Silver Snake conjuration onto your battlefield. Focus 1 Place 1 status token on that Silver Snake. Focus 2 Place 1 additional status token on that Silver Snake. Spell Guard This spell cannot be affected by an opponent''s spell.', '0', '72', '1', NULL, NULL, 't'),
('73', 'Summon Sleeping Widows', 'summon-sleeping-widows', '{"cost": ["2 [[ceremonial:class]]"], "dice": ["ceremonial"], "name": "Summon Sleeping Widows", "stub": "summon-sleeping-widows", "text": "You may play this spell when a unit you control is destroyed. Place up to 2 [[Sleeping Widow]] conjurations onto your battlefield.", "type": "Reaction Spell", "weight": 202, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"ceremonial:class": 2}, "placement": "Discard", "conjurations": [{"name": "Sleeping Widow", "stub": "sleeping-widow"}]}', '1', 'Reaction Spell', '202', '1', NULL, NULL, 't', 'Summon Sleeping Widows
You may play this spell when a unit you control is destroyed. Place up to 2 Sleeping Widow conjurations onto your battlefield.', '0', '73', '1', NULL, NULL, 't'),
('74', 'Summon Three-Eyed Owl', 'summon-three-eyed-owl', '{"cost": ["[[main]]"], "dice": ["charm"], "name": "Summon Three-Eyed Owl", "stub": "summon-three-eyed-owl", "text": "[[main]] - [[exhaust]] - 1 [[charm:class]]: Place a [[Three-Eyed Owl]] conjuration onto your battlefield.", "type": "Ready Spell", "weight": 5, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "conjurations": [{"name": "Three-Eyed Owl", "stub": "three-eyed-owl"}], "effectMagicCost": {"charm:class": 1}}', '1', 'Ready Spell', '5', '2', NULL, NULL, 't', 'Summon Three-Eyed Owl
Place a Three-Eyed Owl conjuration onto your battlefield.', '0', '74', '1', NULL, NULL, 't'),
('75', 'Sympathy Pain', 'sympathy-pain', '{"cost": ["2 [[charm:class]]"], "dice": ["charm"], "name": "Sympathy Pain", "stub": "sympathy-pain", "text": "You may play this spell after your Phoenixborn has received damage. Deal 3 damage to a target unit or Phoenixborn.", "type": "Reaction Spell", "weight": 202, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"charm:class": 2}, "placement": "Discard"}', '1', 'Reaction Spell', '202', '2', NULL, NULL, 'f', 'Sympathy Pain
You may play this spell after your Phoenixborn has received damage. Deal 3 damage to a target unit or Phoenixborn.', '0', '75', '1', NULL, NULL, 't'),
('76', 'Three-Eyed Owl', 'three-eyed-owl', '{"life": 2, "name": "Three-Eyed Owl", "stub": "three-eyed-owl", "text": "Memory Drain 1: [[main]] - [[exhaust]]: Choose a target player to discard 1 card of their choice from their hand.", "type": "Conjuration", "attack": 1, "copies": 5, "recover": 0, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '1', 'Conjuration', '0', '0', NULL, '5', 'f', 'Three-Eyed Owl
Memory Drain 1 Choose a target player to discard 1 card of their choice from their hand.', '0', '76', '1', NULL, NULL, 't'),
('77', 'Transfer', 'transfer', '{"cost": ["[[main]]", "1 [[charm:class]]", "1 [[basic]]"], "dice": ["charm"], "name": "Transfer", "stub": "transfer", "text": "Move 1 token from a target player''s non-Phoenixborn card onto another non-Phoenixborn card that player controls.", "type": "Action Spell", "weight": 206, "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "charm:class": 1}, "placement": "Discard"}', '1', 'Action Spell', '206', '2', NULL, NULL, 'f', 'Transfer
Move 1 token from a target player''s non-Phoenixborn card onto another non-Phoenixborn card that player controls.', '0', '77', '1', NULL, NULL, 't'),
('78', 'Undying Heart', 'undying-heart', '{"cost": ["[[main]]", "1 [[charm:class]]", "1 [[basic]]"], "dice": ["charm"], "life": "+2", "name": "Undying Heart", "stub": "undying-heart", "text": "* Respark: 2 [[basic]]", "type": "Alteration Spell", "weight": 206, "recover": "+2", "release": {"name": "Core Set", "stub": "core-set", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "charm:class": 1}, "placement": "Unit", "effectMagicCost": {"basic": 2}}', '1', 'Alteration Spell', '206', '2', NULL, NULL, 'f', 'Undying Heart
Respark 2', '0', '78', '1', NULL, NULL, 't'),
('79', 'Crystal Shield', 'crystal-shield', '{"cost": ["[[main]]", "1 [[natural:class]]", "1 [[basic]]"], "dice": ["natural"], "life": "+2", "name": "Crystal Shield", "stub": "crystal-shield", "text": "This unit now has the following ability:\n\nUnit Guard: This unit may guard a unit that is being attacked.", "type": "Alteration Spell", "weight": 206, "release": {"name": "The Frostdale Giants", "stub": "the-frostdale-giants", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "natural:class": 1}, "placement": "Unit"}', '2', 'Alteration Spell', '206', '8', NULL, NULL, 'f', 'Crystal Shield
This unit now has the following ability: Unit Guard This unit may guard a unit that is being attacked.', '0', '79', '1', NULL, NULL, 't'),
('80', 'Deep Freeze', 'deep-freeze', '{"cost": ["[[main]]", "1 [[natural:class]]"], "dice": ["natural"], "name": "Deep Freeze", "stub": "deep-freeze", "text": "* When attaching this spell, place 3 status tokens on this spell. Discard this spell when it no longer has any status tokens on it. As long as this spell is attached to this unit, this unit is considered to be exhausted.\n\n* This unit now has the following ability:\n\n* Thaw: [[side]]: Remove 1 status token from a Deep Freeze alteration spell attached to this unit.", "type": "Alteration Spell", "weight": 106, "release": {"name": "The Frostdale Giants", "stub": "the-frostdale-giants", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"natural:class": 1}, "placement": "Unit"}', '2', 'Alteration Spell', '106', '8', NULL, NULL, 'f', 'Deep Freeze
When attaching this spell, place 3 status tokens on this spell. Discard this spell when it no longer has any status tokens on it. As long as this spell is attached to this unit, this unit is considered to be exhausted. This unit now has the following ability: Thaw Remove 1 status token from a Deep Freeze alteration spell attached to this unit.', '0', '80', '1', NULL, NULL, 't'),
('81', 'Freezing Blast', 'freezing-blast', '{"cost": ["[[main]]", "2 [[natural:class]]"], "dice": ["natural"], "name": "Freezing Blast", "stub": "freezing-blast", "text": "Deal 2 damage to a target unit. Remove 2 status tokens from that unit.", "type": "Action Spell", "weight": 207, "release": {"name": "The Frostdale Giants", "stub": "the-frostdale-giants", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"natural:class": 2}, "placement": "Discard"}', '2', 'Action Spell', '207', '8', NULL, NULL, 'f', 'Freezing Blast
Deal 2 damage to a target unit. Remove 2 status tokens from that unit.', '0', '81', '1', NULL, NULL, 't'),
('82', 'Frostback Bear', 'frostback-bear', '{"life": 3, "name": "Frostback Bear", "stub": "frostback-bear", "text": "Freeze 1: When this unit deals damage to another unit, you may spend 1 [[basic]] to place 1 exhaustion token on that unit.\n\nSpite 1: When this unit deals damage to a Phoenixborn by attacking, you may deal 1 additional damage to that Phoenixborn.", "type": "Conjuration", "attack": 2, "copies": 4, "recover": 0, "release": {"name": "The Frostdale Giants", "stub": "the-frostdale-giants", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield", "effectMagicCost": {"basic": 1}}', '2', 'Conjuration', '0', '0', NULL, '4', 'f', 'Frostback Bear
Freeze 1 When this unit deals damage to another unit, you may spend 1 basic to place 1 exhaustion token on that unit. Spite 1 When this unit deals damage to a Phoenixborn by attacking, you may deal 1 additional damage to that Phoenixborn.', '0', '82', '1', NULL, NULL, 't'),
('83', 'Frost Bite', 'frost-bite', '{"cost": ["[[main]]"], "name": "Frost Bite", "stub": "frost-bite", "text": "[[main]] - [[exhaust]] - 1 [[natural:class]]: Deal 1 damage to a target unit or Phoenixborn.\n\nFocus 1: You may change the activation cost of this ability to [[main]] - [[exhaust]] - 1 [[basic]].", "type": "Ready Spell", "weight": 5, "altDice": ["natural"], "release": {"name": "The Frostdale Giants", "stub": "the-frostdale-giants", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "effectMagicCost": {"natural:class": 1}}', '2', 'Ready Spell', '5', '0', NULL, NULL, 'f', 'Frost Bite
Deal 1 damage to a target unit or Phoenixborn. Focus 1 You may change the activation cost of this ability to  -  - 1 .', '8', '83', '1', NULL, NULL, 't'),
('84', 'Frost Fang', 'frost-fang', '{"cost": ["[[main]]", "1 [[natural:power]]"], "dice": ["natural"], "life": 1, "name": "Frost Fang", "stub": "frost-fang", "text": "* Rapid Healing 1: When this unit would receive damage, you may spend any number of [[basic]]. For each 1 [[basic]] spent, prevent 1 damage.\n\nBattle Advantage: When this unit is in battle, it deals its damage before other units without Battle Advantage deal their damage.", "type": "Ally", "attack": 1, "weight": 107, "recover": 1, "release": {"name": "The Frostdale Giants", "stub": "the-frostdale-giants", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"natural:power": 1}, "placement": "Battlefield", "effectRepeats": true, "effectMagicCost": {"basic": 1}}', '2', 'Ally', '107', '8', NULL, NULL, 'f', 'Frost Fang
Rapid Healing 1 When this unit would receive damage, you may spend any number of . For each 1  spent, prevent 1 damage. Battle Advantage When this unit is in battle, it deals its damage before other units without Battle Advantage deal their damage.', '0', '84', '1', NULL, NULL, 't'),
('85', 'Frozen Crown', 'frozen-crown', '{"cost": ["[[main]]", "1 [[natural:class]]", "2 [[basic]]"], "dice": ["natural"], "name": "Frozen Crown", "stub": "frozen-crown", "text": "", "type": "Alteration Spell", "attack": "+3", "weight": 306, "release": {"name": "The Frostdale Giants", "stub": "the-frostdale-giants", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 2, "natural:class": 1}, "placement": "Unit"}', '2', 'Alteration Spell', '306', '8', NULL, NULL, 'f', 'Frozen Crown
', '0', '85', '1', NULL, NULL, 't'),
('86', 'Ice Buff', 'ice-buff', '{"life": "+1", "name": "Ice Buff", "stub": "ice-buff", "text": "", "type": "Conjured Alteration Spell", "copies": 5, "release": {"name": "The Frostdale Giants", "stub": "the-frostdale-giants", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Unit", "phoenixborn": "Rin Northfell"}', '2', 'Conjured Alteration Spell', '0', '0', 'Rin Northfell', '5', 'f', 'Ice Buff
', '0', '86', '1', NULL, NULL, 't'),
('87', 'Ice Golem', 'ice-golem', '{"life": 2, "name": "Ice Golem", "stub": "ice-golem", "text": "* Skin Morph 2: Add 2 to this unit''s life value if it has 1 or more alteration spells attached to it.", "type": "Conjuration", "attack": 3, "copies": 3, "recover": 0, "release": {"name": "The Frostdale Giants", "stub": "the-frostdale-giants", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '2', 'Conjuration', '0', '0', NULL, '3', 'f', 'Ice Golem
Skin Morph 2 Add 2 to this unit''s life value if it has 1 or more alteration spells attached to it.', '0', '87', '1', NULL, NULL, 't'),
('88', 'Ice Trap', 'ice-trap', '{"cost": ["1 [[natural:class]]"], "dice": ["natural"], "name": "Ice Trap", "stub": "ice-trap", "text": "You may play this spell after a unit with a life value of 2 or less comes into play. Destroy that target unit.", "type": "Reaction Spell", "weight": 101, "release": {"name": "The Frostdale Giants", "stub": "the-frostdale-giants", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"natural:class": 1}, "placement": "Discard"}', '2', 'Reaction Spell', '101', '8', NULL, NULL, 'f', 'Ice Trap
You may play this spell after a unit with a life value of 2 or less comes into play. Destroy that target unit.', '0', '88', '1', NULL, NULL, 't'),
('89', 'Rin Northfell', 'rin-northfell', '{"life": 17, "name": "Rin Northfell", "stub": "rin-northfell", "text": "Ice Buff: [[side]] - [[exhaust]]: Attach an [[Ice Buff]] conjured alteration spell to a target unit you control.", "type": "Phoenixborn", "release": {"name": "The Frostdale Giants", "stub": "the-frostdale-giants", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "spellboard": 4, "battlefield": 6, "conjurations": [{"name": "Ice Buff", "stub": "ice-buff"}]}', '2', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Rin Northfell
Ice Buff Attach an Ice Buff conjured alteration spell to a target unit you control.', '0', '89', '1', NULL, NULL, 't'),
('90', 'Rin''s Fury', 'rins-fury', '{"cost": ["[[main]]", "3 [[basic]]"], "name": "Rin''s Fury", "stub": "rins-fury", "text": "You may select up to 5 dice in your exhausted pool, re-roll them, and place them into your active pool. You may spend any number of [[natural:power]] just rolled to deal that much damage to a target unit or Phoenixborn.", "type": "Action Spell", "weight": 305, "altDice": ["natural"], "release": {"name": "The Frostdale Giants", "stub": "the-frostdale-giants", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 3}, "placement": "Discard", "phoenixborn": "Rin Northfell", "diceRecursion": 5}', '2', 'Action Spell', '305', '0', 'Rin Northfell', NULL, 'f', 'Rin''s Fury
You may select up to 5 dice in your exhausted pool, re-roll them, and place them into your active pool. You may spend any number of  just rolled to deal that much damage to a target unit or Phoenixborn.', '8', '90', '1', NULL, NULL, 't'),
('91', 'Summon Frostback Bear', 'summon-frostback-bear', '{"cost": ["[[main]]", "1 [[natural:power]]"], "dice": ["natural"], "name": "Summon Frostback Bear", "stub": "summon-frostback-bear", "text": "[[main]] - [[exhaust]] - 1 [[natural:class]] - 1 [[basic]]: Place a [[Frostback Bear]] conjuration onto your battlefield.", "type": "Ready Spell", "weight": 107, "release": {"name": "The Frostdale Giants", "stub": "the-frostdale-giants", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"natural:power": 1}, "placement": "Spellboard", "conjurations": [{"name": "Frostback Bear", "stub": "frostback-bear"}], "effectMagicCost": {"basic": 1, "natural:class": 1}}', '2', 'Ready Spell', '107', '8', NULL, NULL, 't', 'Summon Frostback Bear
Place a Frostback Bear conjuration onto your battlefield.', '0', '91', '1', NULL, NULL, 't'),
('92', 'Summon Ice Golem', 'summon-ice-golem', '{"cost": ["[[main]]"], "dice": ["natural"], "name": "Summon Ice Golem", "stub": "summon-ice-golem", "text": "[[main]] - [[exhaust]] - 2 [[natural:class]] - 1 [[basic]]: Place an [[Ice Golem]] conjuration onto your battlefield.\n\nFocus 2: You may remove 1 wound token from all Ice Golems you control.", "type": "Ready Spell", "weight": 5, "release": {"name": "The Frostdale Giants", "stub": "the-frostdale-giants", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "conjurations": [{"name": "Ice Golem", "stub": "ice-golem"}], "effectMagicCost": {"basic": 1, "natural:class": 2}}', '2', 'Ready Spell', '5', '8', NULL, NULL, 't', 'Summon Ice Golem
Place an Ice Golem conjuration onto your battlefield. Focus 2 You may remove 1 wound token from all Ice Golems you control.', '0', '92', '1', NULL, NULL, 't'),
('93', 'Blackcloud Ninja', 'blackcloud-ninja', '{"cost": ["[[main]]", "1 [[ceremonial:class]]", "2 [[basic]]"], "dice": ["ceremonial"], "life": 2, "name": "Blackcloud Ninja", "stub": "blackcloud-ninja", "text": "Seal Strike 1: When this unit comes into play, you may spend 1 [[basic]] to place 1 exhaustion token on a target ready spell.\n\nShadow Strike 2: [[main]] - [[exhaust]]: Deal 2 damage to a target unit.", "type": "Ally", "attack": 3, "weight": 306, "recover": 2, "release": {"name": "The Children of Blackcloud", "stub": "the-children-of-blackcloud", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 2, "ceremonial:class": 1}, "placement": "Battlefield", "phoenixborn": "Brennen Blackcloud", "effectMagicCost": {"basic": 1}}', '3', 'Ally', '306', '1', 'Brennen Blackcloud', NULL, 'f', 'Blackcloud Ninja
Seal Strike 1 When this unit comes into play, you may spend 1  to place 1 exhaustion token on a target ready spell. Shadow Strike 2 Deal 2 damage to a target unit.', '0', '93', '1', NULL, NULL, 't'),
('94', 'Blood Chains', 'blood-chains', '{"cost": ["[[main]]", "1 [[ceremonial:class]]"], "dice": ["ceremonial"], "name": "Blood Chains", "stub": "blood-chains", "text": "Choose a unit you control and destroy it. If you do, place X exhaustion tokens on a target unit.\n\nX = the chosen unit''s life value minus the number of wound tokens on the chosen unit.", "type": "Action Spell", "weight": 106, "release": {"name": "The Children of Blackcloud", "stub": "the-children-of-blackcloud", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"ceremonial:class": 1}, "placement": "Discard"}', '3', 'Action Spell', '106', '1', NULL, NULL, 'f', 'Blood Chains
Choose a unit you control and destroy it. If you do, place X exhaustion tokens on a target unit. X = the chosen unit''s life value minus the number of wound tokens on the chosen unit.', '0', '94', '2', NULL, NULL, 't'),
('95', 'Brennen Blackcloud', 'brennen-blackcloud', '{"life": 20, "name": "Brennen Blackcloud", "stub": "brennen-blackcloud", "text": "Spirit Burn: [[side]] - [[exhaust]] - 1 [[basic]]: Destroy a unit you control. If you do, you may deal 2 damage to a target unit or Phoenixborn.", "type": "Phoenixborn", "release": {"name": "The Children of Blackcloud", "stub": "the-children-of-blackcloud", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "spellboard": 3, "battlefield": 5, "effectMagicCost": {"basic": 1}}', '3', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Brennen Blackcloud
Spirit Burn Destroy a unit you control. If you do, you may deal 2 damage to a target unit or Phoenixborn.', '0', '95', '1', NULL, NULL, 't'),
('96', 'Chant Of Protection', 'chant-of-protection', '{"cost": ["[[main]]", "1 [[basic]]", "1 [[discard]]"], "name": "Chant Of Protection", "stub": "chant-of-protection", "text": "* When this spell comes into play, place 3 status tokens on it. Discard this spell when it no longer has any status tokens on it.\n\nWhen your Phoenixborn would receive damage, you may remove any number of status tokens from this spell. For each status token removed, prevent 1 damage to your Phoenixborn.", "type": "Ready Spell", "weight": 108, "release": {"name": "The Children of Blackcloud", "stub": "the-children-of-blackcloud", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1}, "placement": "Spellboard"}', '3', 'Ready Spell', '108', '0', NULL, NULL, 'f', 'Chant Of Protection
When this spell comes into play, place 3 status tokens on it. Discard this spell when it no longer has any status tokens on it. When your Phoenixborn would receive damage, you may remove any number of status tokens from this spell. For each status token removed, prevent 1 damage to your Phoenixborn.', '0', '96', '1', NULL, NULL, 't'),
('97', 'Chant Of The Dead', 'chant-of-the-dead', '{"cost": ["[[main]]", "1 [[ceremonial:class]]"], "dice": ["ceremonial"], "name": "Chant Of The Dead", "stub": "chant-of-the-dead", "text": "* When an ally you control is destroyed, you may place 1 status token on this spell.\n\nDuring your turn, if this spell has 3 or more status tokens on it, you may discard this spell to select 3 dice in your exhausted pool and place them into your active pool on a side of your choice.", "type": "Ready Spell", "weight": 106, "release": {"name": "The Children of Blackcloud", "stub": "the-children-of-blackcloud", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"ceremonial:class": 1}, "placement": "Spellboard"}', '3', 'Ready Spell', '106', '1', NULL, NULL, 'f', 'Chant Of The Dead
When an ally you control is destroyed, you may place 1 status token on this spell. During your turn, if this spell has 3 or more status tokens on it, you may discard this spell to select 3 dice in your exhausted pool and place them into your active pool on a side of your choice.', '0', '97', '1', NULL, NULL, 't'),
('98', 'Choke', 'choke', '{"cost": ["1 [[ceremonial:class]]"], "dice": ["ceremonial"], "name": "Choke", "stub": "choke", "text": "You may play this spell when an opponent would use a unit or Phoenixborn ability that is not inexhaustible. Cancel the effects of that ability for the remainder of this turn.", "type": "Reaction Spell", "weight": 101, "release": {"name": "The Children of Blackcloud", "stub": "the-children-of-blackcloud", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"ceremonial:class": 1}, "placement": "Discard"}', '3', 'Reaction Spell', '101', '1', NULL, NULL, 'f', 'Choke
You may play this spell when an opponent would use a unit or Phoenixborn ability that is not inexhaustible. Cancel the effects of that ability for the remainder of this turn.', '0', '98', '1', NULL, NULL, 't'),
('99', 'Crimson Bomber', 'crimson-bomber', '{"cost": ["[[main]]", "2 [[ceremonial:class]]"], "dice": ["ceremonial"], "life": 2, "name": "Crimson Bomber", "stub": "crimson-bomber", "text": "Detonate 3: [[side]]: Destroy this unit to place 1 wound token on up to 3 target units.", "type": "Ally", "attack": 3, "weight": 206, "recover": 0, "release": {"name": "The Children of Blackcloud", "stub": "the-children-of-blackcloud", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"ceremonial:class": 2}, "placement": "Battlefield"}', '3', 'Ally', '206', '1', NULL, NULL, 'f', 'Crimson Bomber
Detonate 3 Destroy this unit to place 1 wound token on up to 3 target units.', '0', '99', '1', NULL, NULL, 't'),
('100', 'Dread Wraith', 'dread-wraith', '{"life": 6, "name": "Dread Wraith", "stub": "dread-wraith", "text": "* Rage 1: Add 1 to this unit''s attack value for each wound token on this unit.", "type": "Conjuration", "attack": 1, "copies": 2, "recover": 0, "release": {"name": "The Children of Blackcloud", "stub": "the-children-of-blackcloud", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '3', 'Conjuration', '0', '0', NULL, '2', 'f', 'Dread Wraith
Rage 1 Add 1 to this unit''s attack value for each wound token on this unit.', '0', '100', '1', NULL, NULL, 't'),
('101', 'Fire Archer', 'fire-archer', '{"cost": ["[[main]]", "1 [[ceremonial:class]]"], "dice": ["ceremonial"], "life": 1, "name": "Fire Archer", "stub": "fire-archer", "text": "Ambush 1: When this unit comes into play, you may deal 1 damage to a target unit or Phoenixborn.", "type": "Ally", "attack": 1, "weight": 106, "recover": 0, "release": {"name": "The Children of Blackcloud", "stub": "the-children-of-blackcloud", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"ceremonial:class": 1}, "placement": "Battlefield"}', '3', 'Ally', '106', '1', NULL, NULL, 'f', 'Fire Archer
Ambush 1 When this unit comes into play, you may deal 1 damage to a target unit or Phoenixborn.', '0', '101', '1', NULL, NULL, 't'),
('102', 'Poison', 'poison', '{"cost": ["[[main]]", "1 [[ceremonial:class]]"], "dice": ["ceremonial"], "name": "Poison", "stub": "poison", "text": "* After you take a main action other than pass, deal 1 damage to this unit.", "type": "Alteration Spell", "weight": 106, "release": {"name": "The Children of Blackcloud", "stub": "the-children-of-blackcloud", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"ceremonial:class": 1}, "placement": "Unit"}', '3', 'Alteration Spell', '106', '1', NULL, NULL, 'f', 'Poison
After you take a main action other than pass, deal 1 damage to this unit.', '0', '102', '1', NULL, NULL, 't'),
('103', 'Regress', 'regress', '{"cost": ["[[main]]", "1 [[ceremonial:class]]", "1 [[basic]]"], "dice": ["ceremonial"], "name": "Regress", "stub": "regress", "text": "When attaching this spell, discard all other alteration spells attached to this unit.", "type": "Alteration Spell", "attack": "-5", "weight": 206, "release": {"name": "The Children of Blackcloud", "stub": "the-children-of-blackcloud", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "ceremonial:class": 1}, "placement": "Unit"}', '3', 'Alteration Spell', '206', '1', NULL, NULL, 'f', 'Regress
When attaching this spell, discard all other alteration spells attached to this unit.', '0', '103', '1', NULL, NULL, 't'),
('104', 'Summon Dread Wraith', 'summon-dread-wraith', '{"cost": ["[[main]]"], "dice": ["ceremonial"], "name": "Summon Dread Wraith", "stub": "summon-dread-wraith", "text": "[[main]] - [[exhaust]] - 3 [[ceremonial:class]]: Place a [[Dread Wraith]] conjuration on to your battlefield.\n\nFocus 2: You may remove 1 exhaustion token from a Dread Wraith you control.", "type": "Ready Spell", "weight": 5, "release": {"name": "The Children of Blackcloud", "stub": "the-children-of-blackcloud", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "conjurations": [{"name": "Dread Wraith", "stub": "dread-wraith"}], "effectMagicCost": {"ceremonial:class": 3}}', '3', 'Ready Spell', '5', '1', NULL, NULL, 't', 'Summon Dread Wraith
Place a Dread Wraith conjuration on to your battlefield. Focus 2 You may remove 1 exhaustion token from a Dread Wraith you control.', '0', '104', '1', NULL, NULL, 't'),
('105', 'Amplify', 'amplify', '{"cost": ["[[main]]", "1 [[charm:class]]"], "dice": ["charm"], "life": "+X", "name": "Amplify", "stub": "amplify", "text": "* X = the number of charm dice on this unit.\n\n* Respark: 1 [[basic]]", "type": "Alteration Spell", "attack": "+X", "weight": 106, "recover": "+X", "release": {"name": "The Roaring Rose", "stub": "the-roaring-rose", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"charm:class": 1}, "placement": "Unit", "effectMagicCost": {"basic": 1}}', '4', 'Alteration Spell', '106', '2', NULL, NULL, 'f', 'Amplify
X = the number of charm dice on this unit. Respark 1', '0', '105', '1', NULL, NULL, 't'),
('106', 'Anguish', 'anguish', '{"cost": ["[[main]]", "2 [[basic]]"], "name": "Anguish", "stub": "anguish", "text": "Choose a target Phoenixborn. Its controlling player may discard 1 card at random from their hand. If they do not or cannot, place 2 wound tokens on that Phoenixborn. Then choose a target Phoenixborn. Its controlling player may move 2 dice of your choice from their active pool to their exhausted pool. If they do not or cannot, place 2 wound tokens on that Phoenixborn.", "type": "Action Spell", "weight": 205, "release": {"name": "The Roaring Rose", "stub": "the-roaring-rose", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 2}, "placement": "Discard", "phoenixborn": "Leo Sunshadow"}', '4', 'Action Spell', '205', '0', 'Leo Sunshadow', NULL, 'f', 'Anguish
Choose a target Phoenixborn. Its controlling player may discard 1 card at random from their hand. If they do not or cannot, place 2 wound tokens on that Phoenixborn. Then choose a target Phoenixborn. Its controlling player may move 2 dice of your choice from their active pool to their exhausted pool. If they do not or cannot, place 2 wound tokens on that Phoenixborn.', '0', '106', '1', NULL, NULL, 't'),
('107', 'Beast Tamer', 'beast-tamer', '{"cost": ["[[main]]", "1 [[charm:power]]", "1 [[charm:class]]", "1 [[basic]]"], "dice": ["charm"], "life": 3, "name": "Beast Tamer", "stub": "beast-tamer", "text": "Diminish 1: After an opponent has declared attackers, you may spend 1 [[basic]] to reduce the attack value of each attacking unit by 1 for the remainder of this turn.", "type": "Ally", "attack": 3, "weight": 308, "recover": 2, "release": {"name": "The Roaring Rose", "stub": "the-roaring-rose", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "charm:class": 1, "charm:power": 1}, "placement": "Battlefield", "effectRepeats": true, "effectMagicCost": {"basic": 1}}', '4', 'Ally', '308', '2', NULL, NULL, 'f', 'Beast Tamer
Diminish 1 After an opponent has declared attackers, you may spend 1  to reduce the attack value of each attacking unit by 1 for the remainder of this turn.', '0', '107', '1', NULL, NULL, 't'),
('108', 'Change Psyche', 'change-psyche', '{"cost": ["[[main]]", "1 [[charm:class]]", "1 [[basic]]"], "dice": ["charm"], "name": "Change Psyche", "stub": "change-psyche", "text": "Remove 1 exhaustion token from a target unit or place 1 exhaustion token on a target unit.", "type": "Action Spell", "weight": 206, "release": {"name": "The Roaring Rose", "stub": "the-roaring-rose", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "charm:class": 1}, "placement": "Discard"}', '4', 'Action Spell', '206', '2', NULL, NULL, 'f', 'Change Psyche
Remove 1 exhaustion token from a target unit or place 1 exhaustion token on a target unit.', '0', '108', '1', NULL, NULL, 't'),
('109', 'Dispel', 'dispel', '{"cost": ["[[main]]", "1 [[basic]]"], "name": "Dispel", "stub": "dispel", "text": "Remove 2 status tokens from a target card or choose a target alteration spell. If that alteration spell is a conjured alteration spell, return it to its owner''s conjuration pile. Otherwise, shuffle it into its owner''s draw pile.", "type": "Action Spell", "weight": 105, "release": {"name": "The Roaring Rose", "stub": "the-roaring-rose", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1}, "placement": "Discard"}', '4', 'Action Spell', '105', '0', NULL, NULL, 'f', 'Dispel
Remove 2 status tokens from a target card or choose a target alteration spell. If that alteration spell is a conjured alteration spell, return it to its owner''s conjuration pile. Otherwise, shuffle it into its owner''s draw pile.', '0', '109', '1', NULL, NULL, 't'),
('110', 'Glow Finch', 'glow-finch', '{"life": 2, "name": "Glow Finch", "stub": "glow-finch", "text": "Unit Guard: This unit may guard a unit that is being attacked.\n\nDecoy: When a unit you control would become the target of a spell, ability or dice power, and this unit could have been chosen as that target, you may place 1 exhaustion token on this unit to change the chosen target to be this unit instead.\n\n* Last Request 1: When this unit is destroyed, discard 1 card off the top of a target player''s draw pile.\n\n* Magic Rejuvenation: [[side]]: Remove an alteration spell attached to this unit from the game. If you do, remove all exhaustion tokens from this unit.", "type": "Conjuration", "attack": 0, "copies": 1, "recover": 1, "release": {"name": "The Roaring Rose", "stub": "the-roaring-rose", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield", "phoenixborn": "Leo Sunshadow"}', '4', 'Conjuration', '0', '0', 'Leo Sunshadow', '1', 'f', 'Glow Finch
Unit Guard This unit may guard a unit that is being attacked. Decoy When a unit you control would become the target of a spell, ability or dice power, and this unit could have been chosen as that target, you may place 1 exhaustion token on this unit to change the chosen target to be this unit instead. Last Request 1 When this unit is destroyed, discard 1 card off the top of a target player''s draw pile. Magic Rejuvenation Remove an alteration spell attached to this unit from the game. If you do, remove all exhaustion tokens from this unit.', '0', '110', '1', NULL, NULL, 't'),
('111', 'Leo Sunshadow', 'leo-sunshadow', '{"life": 19, "name": "Leo Sunshadow", "stub": "leo-sunshadow", "text": "Summon Glow Finch: [[side]] - [[exhaust]] - 1 [[basic]]: Place a [[Glow Finch]] conjuration onto your battlefield.", "type": "Phoenixborn", "release": {"name": "The Roaring Rose", "stub": "the-roaring-rose", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "spellboard": 3, "battlefield": 6, "conjurations": [{"name": "Glow Finch", "stub": "glow-finch"}], "effectMagicCost": {"basic": 1}}', '4', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Leo Sunshadow
Summon Glow Finch Place a Glow Finch conjuration onto your battlefield.', '0', '111', '1', NULL, NULL, 't'),
('112', 'Memory Theft', 'memory-theft', '{"cost": ["[[main]]"], "dice": ["charm"], "name": "Memory Theft", "stub": "memory-theft", "text": "[[main]] - [[exhaust]] - 1 [[charm:class]]: Look at a target player''s hand. That player may discard 1 card of your choice from that hand. If they do not or cannot, place 1 wound token on their Phoenixborn.", "type": "Ready Spell", "weight": 5, "release": {"name": "The Roaring Rose", "stub": "the-roaring-rose", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "effectMagicCost": {"charm:class": 1}}', '4', 'Ready Spell', '5', '2', NULL, NULL, 'f', 'Memory Theft
Look at a target player''s hand. That player may discard 1 card of your choice from that hand. If they do not or cannot, place 1 wound token on their Phoenixborn.', '0', '112', '1', NULL, NULL, 't'),
('113', 'Mind Probe', 'mind-probe', '{"cost": ["[[main]]", "1 [[charm:class]]"], "dice": ["charm"], "name": "Mind Probe", "stub": "mind-probe", "text": "Choose a target opponent to reveal the top 5 cards of their draw pile. Choose 1 of those revealed cards and remove it from the game. Return the rest of the revealed cards to the top of that opponent''s draw pile in the order of your choice.", "type": "Action Spell", "weight": 106, "release": {"name": "The Roaring Rose", "stub": "the-roaring-rose", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"charm:class": 1}, "placement": "Discard"}', '4', 'Action Spell', '106', '2', NULL, NULL, 'f', 'Mind Probe
Choose a target opponent to reveal the top 5 cards of their draw pile. Choose 1 of those revealed cards and remove it from the game. Return the rest of the revealed cards to the top of that opponent''s draw pile in the order of your choice.', '0', '113', '1', NULL, NULL, 't'),
('114', 'Nightshade Swallow', 'nightshade-swallow', '{"life": 2, "name": "Nightshade Swallow", "stub": "nightshade-swallow", "text": "Deathstrike: When this unit deals 1 or more damage to a unit it is attacking or countering, destroy that unit.", "type": "Conjuration", "attack": 1, "copies": 5, "recover": 1, "release": {"name": "The Roaring Rose", "stub": "the-roaring-rose", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '4', 'Conjuration', '0', '0', NULL, '5', 'f', 'Nightshade Swallow
Deathstrike When this unit deals 1 or more damage to a unit it is attacking or countering, destroy that unit.', '0', '114', '1', NULL, NULL, 't'),
('115', 'Orchid Dove', 'orchid-dove', '{"life": 1, "name": "Orchid Dove", "stub": "orchid-dove", "text": "* Peaceful Melody: Your opponents cannot take an Attack a Phoenixborn main action or Attack a Unit main action. During their turn an opponent may spend 1 [[basic]]. If they do, all units are no longer considered to have the Peaceful Melody ability for the remainder of that turn.", "type": "Conjuration", "attack": 1, "copies": 5, "recover": 0, "release": {"name": "The Roaring Rose", "stub": "the-roaring-rose", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield", "effectRepeats": true, "effectMagicCost": {"basic": 1}}', '4', 'Conjuration', '0', '0', NULL, '5', 'f', 'Orchid Dove
Peaceful Melody Your opponents cannot take an Attack a Phoenixborn main action or Attack a Unit main action. During their turn an opponent may spend 1 . If they do, all units are no longer considered to have the Peaceful Melody ability for the remainder of that turn.', '0', '115', '1', NULL, NULL, 't'),
('116', 'Remorse', 'remorse', '{"cost": ["1 [[charm:class]]", "1 [[basic]]"], "dice": ["charm"], "name": "Remorse", "stub": "remorse", "text": "You may play this spell after an opponent takes an Attack a Phoenixborn main action or Attack a Unit main action. Deal 2 damage to a target Phoenixborn. The player that controls that Phoenixborn must discard 2 cards off the top of their draw pile. If they cannot, deal 1 additional damage to their Phoenixborn.", "type": "Reaction Spell", "weight": 201, "release": {"name": "The Roaring Rose", "stub": "the-roaring-rose", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "charm:class": 1}, "placement": "Discard"}', '4', 'Reaction Spell', '201', '2', NULL, NULL, 'f', 'Remorse
You may play this spell after an opponent takes an Attack a Phoenixborn main action or Attack a Unit main action. Deal 2 damage to a target Phoenixborn. The player that controls that Phoenixborn must discard 2 cards off the top of their draw pile. If they cannot, deal 1 additional damage to their Phoenixborn.', '0', '116', '1', NULL, NULL, 't'),
('117', 'Summon Nightshade Swallow', 'summon-nightshade-swallow', '{"cost": ["[[main]]"], "dice": ["charm"], "name": "Summon Nightshade Swallow", "stub": "summon-nightshade-swallow", "text": "[[main]] - [[exhaust]] - 2 [[charm:class]]: Place a [[Nightshade Swallow]] conjuration onto your battlefield.\n\nFocus 1: You may choose a target player to discard 1 card off the top of their draw pile if you have fewer dice in your active pool than an opponent.", "type": "Ready Spell", "weight": 5, "release": {"name": "The Roaring Rose", "stub": "the-roaring-rose", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "conjurations": [{"name": "Nightshade Swallow", "stub": "nightshade-swallow"}], "effectMagicCost": {"charm:class": 2}}', '4', 'Ready Spell', '5', '2', NULL, NULL, 't', 'Summon Nightshade Swallow
Place a Nightshade Swallow conjuration onto your battlefield. Focus 1 You may choose a target player to discard 1 card off the top of their draw pile if you have fewer dice in your active pool than an opponent.', '0', '117', '1', NULL, NULL, 't'),
('118', 'Summon Orchid Dove', 'summon-orchid-dove', '{"cost": ["[[main]]"], "name": "Summon Orchid Dove", "stub": "summon-orchid-dove", "text": "[[main]] - [[exhaust]] - 1 [[charm:class]]: Place an [[Orchid Dove]] conjuration onto your battlefield.\n\nFocus 1: You may change the activation cost of this spell to [[main]] - [[exhaust]] - 1 [[basic]].\n\nFocus 2: You may deal 1 damage to a target player''s Phoenxiborn if they do not have any cards in their draw pile.", "type": "Ready Spell", "weight": 5, "altDice": ["charm"], "release": {"name": "The Roaring Rose", "stub": "the-roaring-rose", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "conjurations": [{"name": "Orchid Dove", "stub": "orchid-dove"}], "effectMagicCost": {"charm:class": 1}}', '4', 'Ready Spell', '5', '0', NULL, NULL, 't', 'Summon Orchid Dove
Place an Orchid Dove conjuration onto your battlefield. Focus 1 You may change the activation cost of this spell to  -  - 1 . Focus 2 You may deal 1 damage to a target player''s Phoenxiborn if they do not have any cards in their draw pile.', '2', '118', '1', NULL, NULL, 't'),
('119', 'Body Inversion', 'body-inversion', '{"cost": ["[[main]]", "2 [[illusion:class]]"], "dice": ["illusion"], "name": "Body Inversion", "stub": "body-inversion", "text": "This spell cannot be attached to a unit that already has a spell with the word \"Inversion\" in its title attached to it.\n\nWhen attaching this spell to a unit that has the Illusion ability, the player that played this spell may select 2 Illusion dice in their exhausted pool and place them into their active pool on the side of their choice.\n\n* Switch this unit''s printed attack and life values.", "type": "Alteration Spell", "weight": 207, "release": {"name": "The Duchess of Deception", "stub": "the-duchess-of-deception", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"illusion:class": 2}, "placement": "Unit", "diceRecursion": 2}', '5', 'Alteration Spell', '207', '4', NULL, NULL, 'f', 'Body Inversion
This spell cannot be attached to a unit that already has a spell with the word "Inversion" in its title attached to it. When attaching this spell to a unit that has the Illusion ability, the player that played this spell may select 2 Illusion dice in their exhausted pool and place them into their active pool on the side of their choice. Switch this unit''s printed attack and life values.', '0', '119', '1', NULL, NULL, 't'),
('120', 'Figures In The Fog', 'figures-in-the-fog', '{"cost": ["2 [[illusion:class]]", "1 [[basic]]"], "dice": ["illusion"], "name": "Figures In The Fog", "stub": "figures-in-the-fog", "text": "You may play this spell when an opponent chooses to counter with a unit they control. Prevent all damage the attacking unit or units would receive from the the countering unit in this battle.", "type": "Reaction Spell", "weight": 302, "release": {"name": "The Duchess of Deception", "stub": "the-duchess-of-deception", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "illusion:class": 2}, "placement": "Discard"}', '5', 'Reaction Spell', '302', '4', NULL, NULL, 'f', 'Figures In The Fog
You may play this spell when an opponent chooses to counter with a unit they control. Prevent all damage the attacking unit or units would receive from the the countering unit in this battle.', '0', '120', '1', NULL, NULL, 't'),
('121', 'Flash Archer', 'flash-archer', '{"cost": ["[[main]]", "2 [[illusion:class]]", "2 [[basic]]"], "dice": ["illusion"], "life": 2, "name": "Flash Archer", "stub": "flash-archer", "text": "Doublt Shot 1: [[side]] - [[exhaust]]: Deal 1 damage to a target unit. Then you may deal 1 damage to a target unit.", "type": "Ally", "attack": 4, "weight": 407, "recover": 2, "release": {"name": "The Duchess of Deception", "stub": "the-duchess-of-deception", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 2, "illusion:class": 2}, "placement": "Battlefield"}', '5', 'Ally', '407', '4', NULL, NULL, 'f', 'Flash Archer
Doublt Shot 1 Deal 1 damage to a target unit. Then you may deal 1 damage to a target unit.', '0', '121', '1', NULL, NULL, 't'),
('122', 'Illusionary Cycle', 'illusionary-cycle', '{"cost": ["[[main]]"], "name": "Illusionary Cycle", "stub": "illusionary-cycle", "text": "Select 1 Illusion die in your exhausted pool and place it into your active pool on a side of your choice. Shuffle this card into your draw pile.", "type": "Action Spell", "weight": 5, "release": {"name": "The Duchess of Deception", "stub": "the-duchess-of-deception", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Discard", "phoenixborn": "Victoria Glassfire", "diceRecursion": 1}', '5', 'Action Spell', '5', '0', 'Victoria Glassfire', NULL, 'f', 'Illusionary Cycle
Select 1 Illusion die in your exhausted pool and place it into your active pool on a side of your choice. Shuffle this card into your draw pile.', '0', '122', '1', NULL, NULL, 't'),
('123', 'Particle Shield', 'particle-shield', '{"cost": ["1 [[basic]]"], "name": "Particle Shield", "stub": "particle-shield", "text": "You may play this spell when a unit you control would receive 1 or more damage. This spell may be played even if you have already played reaction spells this turn. Prevent 1 damage to that unit. Shuffle this card into your draw pile.", "type": "Reaction Spell", "weight": 100, "release": {"name": "The Duchess of Deception", "stub": "the-duchess-of-deception", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1}, "placement": "Discard"}', '5', 'Reaction Spell', '100', '0', NULL, NULL, 'f', 'Particle Shield
You may play this spell when a unit you control would receive 1 or more damage. This spell may be played even if you have already played reaction spells this turn. Prevent 1 damage to that unit. Shuffle this card into your draw pile.', '0', '123', '1', NULL, NULL, 't'),
('124', 'Secret Door', 'secret-door', '{"cost": ["[[main]]", "1 [[illusion:class]]", "1 [[basic]]"], "dice": ["illusion"], "name": "Secret Door", "stub": "secret-door", "text": "After a reaction spell is played and its effects have been resolved, you may place 1 exhaustion token on this spell to draw 1 card, or discard this card to take the reaction spell just played from its owner''s discard pile and place it in its owner''s hand.", "type": "Ready Spell", "weight": 206, "release": {"name": "The Duchess of Deception", "stub": "the-duchess-of-deception", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "illusion:class": 1}, "placement": "Spellboard"}', '5', 'Ready Spell', '206', '4', NULL, NULL, 'f', 'Secret Door
After a reaction spell is played and its effects have been resolved, you may place 1 exhaustion token on this spell to draw 1 card, or discard this card to take the reaction spell just played from its owner''s discard pile and place it in its owner''s hand.', '0', '124', '1', NULL, NULL, 't'),
('125', 'Shadow Hound', 'shadow-hound', '{"life": 5, "name": "Shadow Hound", "stub": "shadow-hound", "text": "* Illusion: If this unit receives damage as a result of a unit''s attack or counter, destroy this unit.", "type": "Conjuration", "attack": 3, "copies": 3, "recover": 0, "release": {"name": "The Duchess of Deception", "stub": "the-duchess-of-deception", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '5', 'Conjuration', '0', '0', NULL, '3', 'f', 'Shadow Hound
Illusion If this unit receives damage as a result of a unit''s attack or counter, destroy this unit.', '0', '125', '1', NULL, NULL, 't'),
('126', 'Shadow Spirit', 'shadow-spirit', '{"life": "X", "name": "Shadow Spirit", "stub": "shadow-spirit", "text": "* Illusion: If this unit receives damage as a result of a unit''s attack or counter, destroy this unit.\n\n* X = the number of [[Summon Shadow Spirit]] spells on your spellboard.", "type": "Conjuration", "attack": 2, "copies": 4, "recover": 0, "release": {"name": "The Duchess of Deception", "stub": "the-duchess-of-deception", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '5', 'Conjuration', '0', '0', NULL, '4', 'f', 'Shadow Spirit
Illusion If this unit receives damage as a result of a unit''s attack or counter, destroy this unit. X = the number of Summon Shadow Spirit spells on your spellboard.', '0', '126', '1', NULL, NULL, 't'),
('127', 'Summon Shadow Hound', 'summon-shadow-hound', '{"cost": ["[[main]]"], "dice": ["illusion"], "name": "Summon Shadow Hound", "stub": "summon-shadow-hound", "text": "[[main]] - [[exhaust]] - 3 [[illusion:class]]: Place a [[Shadow Hound]] conjuration onto your battlefield.\n\nFocus 1: You may deal 1 damage to a target unit.\n\nFocus 2: Then you may deal 1 damage to a target unit.", "type": "Ready Spell", "weight": 5, "release": {"name": "The Duchess of Deception", "stub": "the-duchess-of-deception", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "conjurations": [{"name": "Shadow Hound", "stub": "shadow-hound"}], "effectMagicCost": {"illusion:class": 3}}', '5', 'Ready Spell', '5', '4', NULL, NULL, 't', 'Summon Shadow Hound
Place a Shadow Hound conjuration onto your battlefield. Focus 1 You may deal 1 damage to a target unit. Focus 2 Then you may deal 1 damage to a target unit.', '0', '127', '1', NULL, NULL, 't'),
('128', 'Summon Shadow Spirit', 'summon-shadow-spirit', '{"cost": ["[[main]]"], "dice": ["illusion"], "name": "Summon Shadow Spirit", "stub": "summon-shadow-spirit", "text": "[[main]] - [[exhaust]] - 1 [[illusion:power]]: Place a [[Shadow Spirit]] conjuration onto your battlefield.", "type": "Ready Spell", "weight": 5, "release": {"name": "The Duchess of Deception", "stub": "the-duchess-of-deception", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "conjurations": [{"name": "Shadow Spirit", "stub": "shadow-spirit"}], "effectMagicCost": {"illusion:power": 1}}', '5', 'Ready Spell', '5', '4', NULL, NULL, 't', 'Summon Shadow Spirit
Place a Shadow Spirit conjuration onto your battlefield.', '0', '128', '1', NULL, NULL, 't'),
('129', 'To Shadows', 'to-shadows', '{"cost": ["[[main]]"], "dice": ["illusion"], "name": "To Shadows", "stub": "to-shadows", "text": "[[side]] - [[exhaust]] - 1 [[illusion:class]]: Choose a target unit to gain the following ability for the remainder of this turn:\n\n* Illusion: If this unit receives damage as a result of a unit''s attack or counter, destroy this unit.", "type": "Ready Spell", "weight": 5, "release": {"name": "The Duchess of Deception", "stub": "the-duchess-of-deception", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "effectMagicCost": {"illusion:class": 1}}', '5', 'Ready Spell', '5', '4', NULL, NULL, 'f', 'To Shadows
Choose a target unit to gain the following ability for the remainder of this turn: Illusion If this unit receives damage as a result of a unit''s attack or counter, destroy this unit.', '0', '129', '1', NULL, NULL, 't'),
('130', 'Vanish', 'vanish', '{"cost": ["2 [[illusion:class]]"], "dice": ["illusion"], "name": "Vanish", "stub": "vanish", "text": "You may play this spell when an opponent would use a spell, ability, or dice power that targets you, your draw pile, your discard pile, or your Phoenixborn. Cancel the effects of that spell, ability, or dice power.", "type": "Reaction Spell", "weight": 202, "release": {"name": "The Duchess of Deception", "stub": "the-duchess-of-deception", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"illusion:class": 2}, "placement": "Discard"}', '5', 'Reaction Spell', '202', '4', NULL, NULL, 'f', 'Vanish
You may play this spell when an opponent would use a spell, ability, or dice power that targets you, your draw pile, your discard pile, or your Phoenixborn. Cancel the effects of that spell, ability, or dice power.', '0', '130', '1', NULL, NULL, 't'),
('131', 'Victoria Glassfire', 'victoria-glassfire', '{"dice": ["illusion"], "life": 18, "name": "Victoria Glassfire", "stub": "victoria-glassfire", "text": "Shadow Spring: [[side]] - [[exhaust]] - 1 [[illusion:power]]: Select 2 dice in your exhausted pool and place them into your active pool on a side of your choice.", "type": "Phoenixborn", "release": {"name": "The Duchess of Deception", "stub": "the-duchess-of-deception", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "spellboard": 4, "battlefield": 5, "diceRecursion": 2, "effectMagicCost": {"illusion:power": 1}}', '5', 'Phoenixborn', '0', '4', NULL, NULL, 'f', 'Victoria Glassfire
Shadow Spring Select 2 dice in your exhausted pool and place them into your active pool on a side of your choice.', '0', '131', '1', NULL, NULL, 't'),
('132', 'Emperor Lion', 'emperor-lion', '{"life": 3, "name": "Emperor Lion", "stub": "emperor-lion", "text": "Spite 1: When this unit deals damage to a Phoenixborn by attacking, you may deal 1 additional damage to that Phoenixborn.\n\n* Healing Aura 1: The recover value of all other units you control is increased by 1.", "type": "Conjuration", "attack": 3, "copies": 3, "recover": 0, "release": {"name": "The Laws of Lions", "stub": "the-laws-of-lions", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '6', 'Conjuration', '0', '0', NULL, '3', 'f', 'Emperor Lion
Spite 1 When this unit deals damage to a Phoenixborn by attacking, you may deal 1 additional damage to that Phoenixborn. Healing Aura 1 The recover value of all other units you control is increased by 1.', '0', '132', '1', NULL, NULL, 't'),
('133', 'Heal', 'heal', '{"cost": ["[[side]]", "1 [[divine:class]]"], "dice": ["divine"], "name": "Heal", "stub": "heal", "text": "Remove all wound tokens from a target unit or 2 wound tokens from a target Phoenixborn.", "type": "Action Spell", "weight": 105, "release": {"name": "The Laws of Lions", "stub": "the-laws-of-lions", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"divine:class": 1}, "placement": "Discard"}', '6', 'Action Spell', '105', '16', NULL, NULL, 'f', 'Heal
Remove all wound tokens from a target unit or 2 wound tokens from a target Phoenixborn.', '0', '133', '1', NULL, NULL, 't'),
('134', 'Holy Knight', 'holy-knight', '{"cost": ["[[main]]", "1 [[divine:power]]", "2 [[divine:class]]", "1 [[basic]]"], "dice": ["divine"], "life": 3, "name": "Holy Knight", "stub": "holy-knight", "text": "Impenetrable: This unit cannot be affected by spells, abilities, or dice powers used by an opponent.", "type": "Ally", "attack": 5, "weight": 409, "recover": 2, "release": {"name": "The Laws of Lions", "stub": "the-laws-of-lions", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "divine:class": 2, "divine:power": 1}, "placement": "Battlefield"}', '6', 'Ally', '409', '16', NULL, NULL, 'f', 'Holy Knight
Impenetrable This unit cannot be affected by spells, abilities, or dice powers used by an opponent.', '0', '134', '1', NULL, NULL, 't'),
('135', 'Law Of Assurance', 'law-of-assurance', '{"cost": ["[[main]]", "1 [[divine:class]]", "1 [[basic]]"], "dice": ["divine"], "name": "Law Of Assurance", "stub": "law-of-assurance", "text": "When this spell comes into play, you may select 2 dice in your exhausted pool and place them into your active pool on a side of your choice.\n\nPlayers'' active dice pools cannot be affected by spells, abilities, or dice powers used by their opponents.\n\n* Bound: This card cannot be discarded from your spellboard when you Meditate.\n\n* Fleeting: Discard this card at the end of this round.", "type": "Ready Spell", "weight": 206, "release": {"name": "The Laws of Lions", "stub": "the-laws-of-lions", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "divine:class": 1}, "placement": "Spellboard", "diceRecursion": 2}', '6', 'Ready Spell', '206', '16', NULL, NULL, 'f', 'Law Of Assurance
When this spell comes into play, you may select 2 dice in your exhausted pool and place them into your active pool on a side of your choice. Players'' active dice pools cannot be affected by spells, abilities, or dice powers used by their opponents. Bound This card cannot be discarded from your spellboard when you Meditate. Fleeting Discard this card at the end of this round.', '0', '135', '1', NULL, NULL, 't'),
('136', 'Law Of Sight', 'law-of-sight', '{"cost": ["[[side]]", "1 [[divine:class]]", "1 [[basic]]"], "dice": ["divine"], "name": "Law Of Sight", "stub": "law-of-sight", "text": "When this spell comes into play, you may draw up to 2 cards.\n\nNo player may play reaction spells.\n\n* Bound: This card cannot be discarded from your spellboard when you Meditate.\n\n* Fleeting: Discard this card at the end of this round.", "type": "Ready Spell", "weight": 205, "release": {"name": "The Laws of Lions", "stub": "the-laws-of-lions", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "divine:class": 1}, "placement": "Spellboard"}', '6', 'Ready Spell', '205', '16', NULL, NULL, 'f', 'Law Of Sight
When this spell comes into play, you may draw up to 2 cards. No player may play reaction spells. Bound This card cannot be discarded from your spellboard when you Meditate. Fleeting Discard this card at the end of this round.', '0', '136', '1', NULL, NULL, 't'),
('137', 'Meteor', 'meteor', '{"cost": ["[[main]]", "2 [[divine:power]]"], "dice": ["divine"], "name": "Meteor", "stub": "meteor", "text": "Deal 2 damage to all units.\n\nFor each unit, place 1 exhaustion token on that unit unless its controlling player spends 1 [[basic]].", "type": "Action Spell", "weight": 209, "release": {"name": "The Laws of Lions", "stub": "the-laws-of-lions", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"divine:power": 2}, "placement": "Discard", "effectRepeats": true, "effectMagicCost": {"basic": 1}}', '6', 'Action Spell', '209', '16', NULL, NULL, 'f', 'Meteor
Deal 2 damage to all units. For each unit, place 1 exhaustion token on that unit unless its controlling player spends 1 .', '0', '137', '1', NULL, NULL, 't'),
('138', 'Odette Diamondcrest', 'odette-diamondcrest', '{"life": 17, "name": "Odette Diamondcrest", "stub": "odette-diamondcrest", "text": "Retribution: After this Phoenixborn receives damage while guarding, place 2 wound tokens on a target attacking unit.", "type": "Phoenixborn", "release": {"name": "The Laws of Lions", "stub": "the-laws-of-lions", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "spellboard": 4, "battlefield": 5}', '6', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Odette Diamondcrest
Retribution After this Phoenixborn receives damage while guarding, place 2 wound tokens on a target attacking unit.', '0', '138', '1', NULL, NULL, 't'),
('139', 'Power Through', 'power-through', '{"cost": ["[[side]]", "1 [[divine:class]]", "1 [[basic]]"], "dice": ["divine"], "name": "Power Through", "stub": "power-through", "text": "This unit now has the following ability:\n\nOverkill 2: When this unit destroys a unit an opponent controls by attacking, deal 2 damage to that opponent''s Phoenixborn.\n\n* Respark: 1 [[discard]]", "type": "Alteration Spell", "attack": "+1", "weight": 205, "release": {"name": "The Laws of Lions", "stub": "the-laws-of-lions", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "divine:class": 1}, "placement": "Unit"}', '6', 'Alteration Spell', '205', '16', NULL, NULL, 'f', 'Power Through
This unit now has the following ability: Overkill 2 When this unit destroys a unit an opponent controls by attacking, deal 2 damage to that opponent''s Phoenixborn. Respark 1', '0', '139', '1', NULL, NULL, 't'),
('140', 'Shield Mage', 'shield-mage', '{"cost": ["[[main]]", "1 [[divine:power]]"], "dice": ["divine"], "life": 2, "name": "Shield Mage", "stub": "shield-mage", "text": "Exert: [[side]]: Place 1 exhaustion token on this unit.\n\n* Protective Aura 1: While this unit has 1 or more exhaustion tokens on it, the life value of all other units you control is increased by 1.", "type": "Ally", "attack": 0, "weight": 107, "recover": 2, "release": {"name": "The Laws of Lions", "stub": "the-laws-of-lions", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"divine:power": 1}, "placement": "Battlefield"}', '6', 'Ally', '107', '16', NULL, NULL, 'f', 'Shield Mage
Exert Place 1 exhaustion token on this unit. Protective Aura 1 While this unit has 1 or more exhaustion tokens on it, the life value of all other units you control is increased by 1.', '0', '140', '1', NULL, NULL, 't'),
('141', 'Summon Emperor Lion', 'summon-emperor-lion', '{"cost": ["[[main]]"], "dice": ["divine"], "name": "Summon Emperor Lion", "stub": "summon-emperor-lion", "text": "[[main]] - [[exhaust]] - 2 [[divine:class]] - 1 [[basic]]: Place an [[Emperor Lion]] conjuration onto your battlefield.", "type": "Ready Spell", "weight": 5, "release": {"name": "The Laws of Lions", "stub": "the-laws-of-lions", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "conjurations": [{"name": "Emperor Lion", "stub": "emperor-lion"}], "effectMagicCost": {"basic": 1, "divine:class": 2}}', '6', 'Ready Spell', '5', '16', NULL, NULL, 't', 'Summon Emperor Lion
Place an Emperor Lion conjuration onto your battlefield.', '0', '141', '1', NULL, NULL, 't'),
('142', 'Summon Winged Lioness', 'summon-winged-lioness', '{"cost": ["[[main]]"], "dice": ["divine"], "name": "Summon Winged Lioness", "stub": "summon-winged-lioness", "text": "[[main]] - [[exhaust]] - 1 [[divine:class]] - 1 [[basic]]: Place a [[Winged Lioness]] conjuration onto your battlefield.", "type": "Ready Spell", "weight": 5, "release": {"name": "The Laws of Lions", "stub": "the-laws-of-lions", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "conjurations": [{"name": "Winged Lioness", "stub": "winged-lioness"}], "effectMagicCost": {"basic": 1, "divine:class": 1}}', '6', 'Ready Spell', '5', '16', NULL, NULL, 't', 'Summon Winged Lioness
Place a Winged Lioness conjuration onto your battlefield.', '0', '142', '1', NULL, NULL, 't'),
('143', 'Sword Of Virtue', 'sword-of-virtue', '{"cost": ["[[main]]", "2 [[basic]]"], "name": "Sword Of Virtue", "stub": "sword-of-virtue", "text": "Destroy a target unit or remove all wound tokens from a target unit.", "type": "Action Spell", "weight": 205, "release": {"name": "The Laws of Lions", "stub": "the-laws-of-lions", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 2}, "placement": "Discard", "phoenixborn": "Odette Diamondcrest"}', '6', 'Action Spell', '205', '0', 'Odette Diamondcrest', NULL, 'f', 'Sword Of Virtue
Destroy a target unit or remove all wound tokens from a target unit.', '0', '143', '1', NULL, NULL, 't'),
('144', 'Winged Lioness', 'winged-lioness', '{"life": 2, "name": "Winged Lioness", "stub": "winged-lioness", "text": "Stalk: This unit cannot be guarded against.", "type": "Conjuration", "attack": 2, "copies": 4, "recover": 1, "release": {"name": "The Laws of Lions", "stub": "the-laws-of-lions", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '6', 'Conjuration', '0', '0', NULL, '4', 'f', 'Winged Lioness
Stalk This unit cannot be guarded against.', '0', '144', '1', NULL, NULL, 't'),
('145', 'Crescendo', 'crescendo', '{"cost": ["1 [[sympathy:class]]", "1 [[discard]]"], "dice": ["sympathy"], "name": "Crescendo", "stub": "crescendo", "text": "You may play this spell after you have declared attackers. Deal 1 damage to a target unit you control to deal 3 damage to a target unit.", "type": "Reaction Spell", "weight": 104, "release": {"name": "The Song of Soaksend", "stub": "the-song-of-soaksend", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"sympathy:class": 1}, "placement": "Discard"}', '7', 'Reaction Spell', '104', '32', NULL, NULL, 'f', 'Crescendo
You may play this spell after you have declared attackers. Deal 1 damage to a target unit you control to deal 3 damage to a target unit.', '0', '145', '1', NULL, NULL, 't'),
('146', 'Encore', 'encore', '{"cost": ["[[main]]"], "name": "Encore", "stub": "encore", "text": "Search your discard pile for a card other than Encore and place it on the top or bottom of your draw pile. Draw 1 card.", "type": "Action Spell", "weight": 5, "release": {"name": "The Song of Soaksend", "stub": "the-song-of-soaksend", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Discard", "phoenixborn": "Namine Hymntide"}', '7', 'Action Spell', '5', '0', 'Namine Hymntide', NULL, 'f', 'Encore
Search your discard pile for a card other than Encore and place it on the top or bottom of your draw pile. Draw 1 card.', '0', '146', '1', NULL, NULL, 't'),
('147', 'Flute Mage', 'flute-mage', '{"cost": ["[[main]]", "1 [[sympathy:class]]", "1 [[basic]]"], "dice": ["sympathy"], "life": 2, "name": "Flute Mage", "stub": "flute-mage", "text": "Enliven: [[side]] - [[exhaust]]: Remove 1 exhaustion token from a target unit.", "type": "Ally", "attack": 1, "weight": 206, "recover": 1, "release": {"name": "The Song of Soaksend", "stub": "the-song-of-soaksend", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "sympathy:class": 1}, "placement": "Battlefield"}', '7', 'Ally', '206', '32', NULL, NULL, 'f', 'Flute Mage
Enliven Remove 1 exhaustion token from a target unit.', '0', '147', '1', NULL, NULL, 't'),
('148', 'Guilt Link', 'guilt-link', '{"cost": ["[[main]]", "1 [[sympathy:class]]"], "dice": ["sympathy"], "name": "Guilt Link", "stub": "guilt-link", "text": "When your Phoenixborn receives 1 or more damage, you may place 1 exhaustion token on this spell to place 1 wound token on a target unit or Phoenixborn. The player that controls the targeted unit or Phoenixborn may discard 1 ready spell they control or 1 unit they control to prevent that wound from being placed.", "type": "Ready Spell", "weight": 106, "release": {"name": "The Song of Soaksend", "stub": "the-song-of-soaksend", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"sympathy:class": 1}, "placement": "Spellboard"}', '7', 'Ready Spell', '106', '32', NULL, NULL, 'f', 'Guilt Link
When your Phoenixborn receives 1 or more damage, you may place 1 exhaustion token on this spell to place 1 wound token on a target unit or Phoenixborn. The player that controls the targeted unit or Phoenixborn may discard 1 ready spell they control or 1 unit they control to prevent that wound from being placed.', '0', '148', '1', NULL, NULL, 't'),
('149', 'Magic Syphon', 'magic-syphon', '{"cost": ["[[main]]", "1 [[sympathy:class]]"], "dice": ["sympathy"], "name": "Magic Syphon", "stub": "magic-syphon", "text": "[[side]] - [[exhaust]]: Change 1 die in your active pool to a side of your choice. Change 1 die in a target player''s active pool to a side of your choice.", "type": "Ready Spell", "weight": 106, "release": {"name": "The Song of Soaksend", "stub": "the-song-of-soaksend", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"sympathy:class": 1}, "placement": "Spellboard"}', '7', 'Ready Spell', '106', '32', NULL, NULL, 'f', 'Magic Syphon
Change 1 die in your active pool to a side of your choice. Change 1 die in a target player''s active pool to a side of your choice.', '0', '149', '1', NULL, NULL, 't'),
('150', 'Namine Hymntide', 'namine-hymntide', '{"dice": ["sympathy"], "life": 17, "name": "Namine Hymntide", "stub": "namine-hymntide", "text": "Calming Melody: [[side]] - [[exhaust]] - 1 [[sympathy:class]]: Draw 1 card. You may place 1 exhaustion token on this card and 1 exhaustion token on a target Phoenixborn.", "type": "Phoenixborn", "release": {"name": "The Song of Soaksend", "stub": "the-song-of-soaksend", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "spellboard": 4, "battlefield": 6, "effectMagicCost": {"sympathy:class": 1}}', '7', 'Phoenixborn', '0', '32', NULL, NULL, 'f', 'Namine Hymntide
Calming Melody Draw 1 card. You may place 1 exhaustion token on this card and 1 exhaustion token on a target Phoenixborn.', '0', '150', '1', NULL, NULL, 't'),
('151', 'River Skald', 'river-skald', '{"cost": ["[[main]]", "1 [[sympathy:power]]", "1 [[sympathy:class]]", "1 [[basic]]"], "dice": ["sympathy"], "life": 3, "name": "River Skald", "stub": "river-skald", "text": "Harsh Melody: When you draw 1 or more cards during your turn, you may place 1 exhaustion token on this unit to place a number of wound tokens equal to this unit''s attack value on a target unit.", "type": "Ally", "attack": 3, "weight": 308, "recover": 2, "release": {"name": "The Song of Soaksend", "stub": "the-song-of-soaksend", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "sympathy:class": 1, "sympathy:power": 1}, "placement": "Battlefield"}', '7', 'Ally', '308', '32', NULL, NULL, 'f', 'River Skald
Harsh Melody When you draw 1 or more cards during your turn, you may place 1 exhaustion token on this unit to place a number of wound tokens equal to this unit''s attack value on a target unit.', '0', '151', '1', NULL, NULL, 't'),
('152', 'Salamander Monk', 'salamander-monk', '{"life": 1, "name": "Salamander Monk", "stub": "salamander-monk", "text": "* Spirit Form: When this unit is destroyed, place a [[Salamander Monk Spirit]] conjuration onto your battlefield.", "type": "Conjuration", "attack": 1, "copies": 2, "recover": 0, "release": {"name": "The Song of Soaksend", "stub": "the-song-of-soaksend", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield", "conjurations": [{"name": "Salamander Monk Spirit", "stub": "salamander-monk-spirit"}]}', '7', 'Conjuration', '0', '0', NULL, '2', 'f', 'Salamander Monk
Spirit Form When this unit is destroyed, place a Salamander Monk Spirit conjuration onto your battlefield.', '0', '152', '1', NULL, NULL, 't'),
('153', 'Salamander Monk Spirit', 'salamander-monk-spirit', '{"life": 1, "name": "Salamander Monk Spirit", "stub": "salamander-monk-spirit", "text": "* Temporary: This unit cannot block or be chosen at the target of an attack.", "type": "Conjuration", "attack": 1, "copies": 3, "recover": 0, "release": {"name": "The Song of Soaksend", "stub": "the-song-of-soaksend", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '7', 'Conjuration', '0', '0', NULL, '3', 'f', 'Salamander Monk Spirit
Temporary This unit cannot block or be chosen at the target of an attack.', '0', '153', '1', NULL, NULL, 't'),
('154', 'Shatter Pulse', 'shatter-pulse', '{"cost": ["2 [[sympathy:class]]", "1 [[basic]]"], "dice": ["sympathy"], "name": "Shatter Pulse", "stub": "shatter-pulse", "text": "You may play this spell after a unit you control is destroyed. Destroy a target unit. You may change 2 dice in a target player''s active pool to a side of your choice.", "type": "Reaction Spell", "weight": 302, "release": {"name": "The Song of Soaksend", "stub": "the-song-of-soaksend", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "sympathy:class": 2}, "placement": "Discard"}', '7', 'Reaction Spell', '302', '32', NULL, NULL, 'f', 'Shatter Pulse
You may play this spell after a unit you control is destroyed. Destroy a target unit. You may change 2 dice in a target player''s active pool to a side of your choice.', '0', '154', '1', NULL, NULL, 't'),
('155', 'Squall Stallion', 'squall-stallion', '{"life": 3, "name": "Squall Stallion", "stub": "squall-stallion", "text": "Opportunist 2: When you draw 1 or more cards during a player''s turn, add 2 to this unit''s attack value for the remainder of that turn.", "type": "Conjuration", "attack": 1, "copies": 5, "recover": 0, "release": {"name": "The Song of Soaksend", "stub": "the-song-of-soaksend", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '7', 'Conjuration', '0', '0', NULL, '5', 'f', 'Squall Stallion
Opportunist 2 When you draw 1 or more cards during a player''s turn, add 2 to this unit''s attack value for the remainder of that turn.', '0', '155', '1', NULL, NULL, 't'),
('156', 'String Mage', 'string-mage', '{"cost": ["[[main]]", "1 [[sympathy:power]]", "1 [[sympathy:class]]"], "dice": ["sympathy"], "life": 3, "name": "String Mage", "stub": "string-mage", "text": "Exchange Link 1: [[side]]: Move 1 wound or status token from a target unit onto this unit, or move 1 wound or status token from this unit onto a target unit.", "type": "Ally", "attack": 1, "weight": 208, "recover": 2, "release": {"name": "The Song of Soaksend", "stub": "the-song-of-soaksend", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"sympathy:class": 1, "sympathy:power": 1}, "placement": "Battlefield"}', '7', 'Ally', '208', '32', NULL, NULL, 'f', 'String Mage
Exchange Link 1 Move 1 wound or status token from a target unit onto this unit, or move 1 wound or status token from this unit onto a target unit.', '0', '156', '1', NULL, NULL, 't'),
('157', 'Summon Salamander Monk', 'summon-salamander-monk', '{"cost": ["[[main]]"], "dice": ["sympathy"], "name": "Summon Salamander Monk", "stub": "summon-salamander-monk", "text": "[[main]] - [[exhaust]] - 1 [[sympathy:class]]: Place a [[Salamander Monk]] conjuration onto your battlefield.", "type": "Ready Spell", "weight": 5, "release": {"name": "The Song of Soaksend", "stub": "the-song-of-soaksend", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "conjurations": [{"name": "Salamander Monk", "stub": "salamander-monk"}], "effectMagicCost": {"sympathy:class": 1}}', '7', 'Ready Spell', '5', '32', NULL, NULL, 't', 'Summon Salamander Monk
Place a Salamander Monk conjuration onto your battlefield.', '0', '157', '1', NULL, NULL, 't'),
('158', 'Summon Squall Stallion', 'summon-squall-stallion', '{"cost": ["[[main]]", "1 [[sympathy:power]]"], "dice": ["sympathy"], "name": "Summon Squall Stallion", "stub": "summon-squall-stallion", "text": "[[main]] - [[exhaust]] - 1 [[sympathy:class]] - 1 [[basic]]: Draw 1 card. Place a [[Squall Stallion]] conjuration onto your battlefield.", "type": "Ready Spell", "weight": 107, "release": {"name": "The Song of Soaksend", "stub": "the-song-of-soaksend", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"sympathy:power": 1}, "placement": "Battlefield", "conjurations": [{"name": "Squall Stallion", "stub": "squall-stallion"}], "effectMagicCost": {"basic": 1, "sympathy:class": 1}}', '7', 'Ready Spell', '107', '32', NULL, NULL, 't', 'Summon Squall Stallion
Draw 1 card. Place a Squall Stallion conjuration onto your battlefield.', '0', '158', '1', NULL, NULL, 't'),
('159', 'Dimona Odinstar', 'dimona-odinstar', '{"life": 17, "name": "Dimona Odinstar", "stub": "dimona-odinstar", "text": "Order: [[side]] - [[exhaust]] - 2 [[basic]]: Remove 1 exhaustion token from a target unit on your battlefield.", "type": "Phoenixborn", "release": {"name": "Dimona Odinstar (promo)", "stub": "dimona-odinstar-(promo)", "is_phg": true, "is_promo": true, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "spellboard": 5, "battlefield": 5, "effectMagicCost": {"basic": 2}}', '18', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Dimona Odinstar
Order Remove 1 exhaustion token from a target unit on your battlefield.', '0', '159', '1', NULL, NULL, 't'),
('160', 'Rayward Knight', 'rayward-knight', '{"cost": ["[[main]]", "3 [[basic]]"], "life": 3, "name": "Rayward Knight", "stub": "rayward-knight", "text": "* Endurance: Remove all exhaustion tokens from this unit at the end of each round.", "type": "Ally", "attack": 3, "weight": 305, "recover": 3, "release": {"name": "Dimona Odinstar (promo)", "stub": "dimona-odinstar-(promo)", "is_phg": true, "is_promo": true, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"basic": 3}, "placement": "Battlefield", "phoenixborn": "Dimona Odinstar"}', '18', 'Ally', '305', '0', 'Dimona Odinstar', NULL, 'f', 'Rayward Knight
Endurance Remove all exhaustion tokens from this unit at the end of each round.', '0', '160', '1', NULL, NULL, 't'),
('161', 'Lulu Firststone', 'lulu-firststone', '{"life": 21, "name": "Lulu Firststone", "stub": "lulu-firststone", "text": "Bolster: [[side]] - [[exhaust]] - 1 [[basic]]: Add 1 to the attack value of all units you currently control for the remainder of this turn.", "type": "Phoenixborn", "release": {"name": "Lulu Firststone (promo)", "stub": "lulu-firststone-(promo)", "is_phg": true, "is_promo": true, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "spellboard": 4, "battlefield": 4, "effectMagicCost": {"basic": 1}}', '19', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Lulu Firststone
Bolster Add 1 to the attack value of all units you currently control for the remainder of this turn.', '0', '161', '1', NULL, NULL, 't'),
('162', 'Phoenix Barrage', 'phoenix-barrage', '{"cost": ["[[main]]", "3 [[basic]]"], "name": "Phoenix Barrage", "stub": "phoenix-barrage", "text": "Deal 4 damage to a target unit. Deal 2 damage to a target Phoenixborn.", "type": "Action Spell", "weight": 305, "release": {"name": "Lulu Firststone (promo)", "stub": "lulu-firststone-(promo)", "is_phg": true, "is_promo": true, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"basic": 3}, "placement": "Discard", "phoenixborn": "Lulu Firststone"}', '19', 'Action Spell', '305', '0', 'Lulu Firststone', NULL, 'f', 'Phoenix Barrage
Deal 4 damage to a target unit. Deal 2 damage to a target Phoenixborn.', '0', '162', '1', NULL, NULL, 't'),
('163', 'Gobi Sunshield', 'gobi-sunshield', '{"cost": ["[[main]]", "4 [[basic]]"], "life": 5, "name": "Gobi Sunshield", "stub": "gobi-sunshield", "text": "Alert: Do not place an exhaustion token on this unit as a result of its countering.", "type": "Ally", "attack": 2, "weight": 405, "recover": 3, "release": {"name": "Orrick Gilstream (promo)", "stub": "orrick-gilstream-(promo)", "is_phg": true, "is_promo": true, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"basic": 4}, "placement": "Battlefield", "phoenixborn": "Orrick Gilstream"}', '20', 'Ally', '405', '0', 'Orrick Gilstream', NULL, 'f', 'Gobi Sunshield
Alert Do not place an exhaustion token on this unit as a result of its countering.', '0', '163', '1', NULL, NULL, 't'),
('164', 'Orrick Gilstream', 'orrick-gilstream', '{"life": 19, "name": "Orrick Gilstream", "stub": "orrick-gilstream", "text": "Bounty: [[side]] - [[exhaust]] - 2 [[basic]]: Select up to 4 dice in your exhausted pool. They must all be different types. Re-roll them, and place them into your active pool.", "type": "Phoenixborn", "release": {"name": "Orrick Gilstream (promo)", "stub": "orrick-gilstream-(promo)", "is_phg": true, "is_promo": true, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "spellboard": 4, "battlefield": 5, "diceRecursion": 4, "effectMagicCost": {"basic": 2}}', '20', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Orrick Gilstream
Bounty Select up to 4 dice in your exhausted pool. They must all be different types. Re-roll them, and place them into your active pool.', '0', '164', '1', NULL, NULL, 't'),
('165', 'Changing Winds', 'changing-winds', '{"cost": ["[[main]]", "1 [[sympathy:class]]", "1 [[basic]]"], "dice": ["sympathy"], "name": "Changing Winds", "stub": "changing-winds", "text": "When this spell comes into play, you may draw 2 cards. If you do, choose 2 cards in your hand and place each one on the top or bottom of your draw pile.\n\n[[side]] - [[exhaust]]: Draw 1 card. Change 1 die in your active pool to a side of your choice.", "type": "Ready Spell", "weight": 206, "release": {"name": "The Masters of Gravity", "stub": "the-masters-of-gravity", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "sympathy:class": 1}, "placement": "Spellboard"}', '8', 'Ready Spell', '206', '32', NULL, NULL, 'f', 'Changing Winds
When this spell comes into play, you may draw 2 cards. If you do, choose 2 cards in your hand and place each one on the top or bottom of your draw pile. Draw 1 card. Change 1 die in your active pool to a side of your choice.', '0', '165', '1', NULL, NULL, 't'),
('166', 'Chaos Gravity', 'chaos-gravity', '{"cost": ["[[main]]", ["1 [[divine:class]]", "1 [[sympathy:class]]"], "1 [[basic]]"], "name": "Chaos Gravity", "stub": "chaos-gravity", "text": "Place 1 exhaustion token on a target unit. Move 1 exhaustion token from a target unit to another unit controlled by the same player. Remove 1 exhaustion token from a target unit.", "type": "Action Spell", "weight": 206, "altDice": ["divine", "sympathy"], "release": {"name": "The Masters of Gravity", "stub": "the-masters-of-gravity", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "divine:class / sympathy:class": 1}, "placement": "Discard", "phoenixborn": "Echo Greystorm"}', '8', 'Action Spell', '206', '0', 'Echo Greystorm', NULL, 'f', 'Chaos Gravity
Place 1 exhaustion token on a target unit. Move 1 exhaustion token from a target unit to another unit controlled by the same player. Remove 1 exhaustion token from a target unit.', '48', '166', '1', NULL, NULL, 't'),
('167', 'Echo Greystorm', 'echo-greystorm', '{"life": 17, "name": "Echo Greystorm", "stub": "echo-greystorm", "text": "Increase Gravity: When 1 or more exhaustion tokens are placed on a target unit, you may spend 1 [[basic]] and place 1 exhaustion token on this card to place 1 exhaustion token on that target unit.", "type": "Phoenixborn", "release": {"name": "The Masters of Gravity", "stub": "the-masters-of-gravity", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "spellboard": 4, "battlefield": 6, "effectMagicCost": {"basic": 1}}', '8', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Echo Greystorm
Increase Gravity When 1 or more exhaustion tokens are placed on a target unit, you may spend 1  and place 1 exhaustion token on this card to place 1 exhaustion token on that target unit.', '0', '167', '1', NULL, NULL, 't'),
('168', 'Enhanced Strength', 'enhanced-strength', '{"life": "+1", "name": "Enhanced Strength", "stub": "enhanced-strength", "text": "* This unit now has the following ability:\n\n* Endurance: Remove all exhaustion tokens from this unit at the end of each round.", "type": "Conjured Alteration Spell", "attack": "+1", "copies": 3, "release": {"name": "The Masters of Gravity", "stub": "the-masters-of-gravity", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Unit"}', '8', 'Conjured Alteration Spell', '0', '0', NULL, '3', 'f', 'Enhanced Strength
This unit now has the following ability: Endurance Remove all exhaustion tokens from this unit at the end of each round.', '0', '168', '1', NULL, NULL, 't'),
('169', 'Enlightenment', 'enlightenment', '{"cost": ["[[main]]", "1 [[divine:class]]", "1 [[basic]]"], "dice": ["divine"], "name": "Enlightenment", "stub": "enlightenment", "text": "Remove 1 exhaustion token from a target card.", "type": "Action Spell", "weight": 206, "release": {"name": "The Masters of Gravity", "stub": "the-masters-of-gravity", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "divine:class": 1}, "placement": "Discard"}', '8', 'Action Spell', '206', '16', NULL, NULL, 'f', 'Enlightenment
Remove 1 exhaustion token from a target card.', '0', '169', '1', NULL, NULL, 't'),
('170', 'Gravity Training', 'gravity-training', '{"cost": ["[[main]]"], "name": "Gravity Training", "stub": "gravity-training", "text": "After 1 or more exhaustion tokens are placed on a unit you control, you may spend 1 [[divine:class]] or 1 [[sympathy:class]] and place 1 exhaustion token on this spell to attach an [[Enhanced Strength]] conjured alteration spell to that unit.", "type": "Ready Spell", "weight": 5, "altDice": ["divine", "sympathy"], "release": {"name": "The Masters of Gravity", "stub": "the-masters-of-gravity", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "conjurations": [{"name": "Enhanced Strength", "stub": "enhanced-strength"}], "effectMagicCost": {"divine:class / sympathy:class": 1}}', '8', 'Ready Spell', '5', '0', NULL, NULL, 'f', 'Gravity Training
After 1 or more exhaustion tokens are placed on a unit you control, you may spend 1  or 1  and place 1 exhaustion token on this spell to attach an Enhanced Strength conjured alteration spell to that unit.', '48', '170', '1', NULL, NULL, 't'),
('171', 'Holy Relics', 'holy-relics', '{"cost": ["[[main]]", "2 [[divine:class]]"], "dice": ["divine"], "life": "+2", "name": "Holy Relics", "stub": "holy-relics", "text": "", "type": "Alteration Spell", "attack": "+2", "weight": 207, "release": {"name": "The Masters of Gravity", "stub": "the-masters-of-gravity", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"divine:class": 2}, "placement": "Unit"}', '8', 'Alteration Spell', '207', '16', NULL, NULL, 'f', 'Holy Relics
', '0', '171', '1', NULL, NULL, 't'),
('172', 'Law Of Fear', 'law-of-fear', '{"cost": ["[[side]]", "1 [[divine:class]]"], "dice": ["divine"], "name": "Law Of Fear", "stub": "law-of-fear", "text": "When this spell comes into play, choose up to 3 target units. Those units add 1 to their attack value for the remainder of this turn.\n\nPlayers must spend 1 [[basic]] or place 2 wound tokens on their Phoenixborn to declare blockers or declare a guard.\n\n* Bound: This card cannot be discarded from your spellboard when you Meditate.\n\n* Fleeting: Discard this card at the end of this round.", "type": "Ready Spell", "weight": 105, "release": {"name": "The Masters of Gravity", "stub": "the-masters-of-gravity", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"divine:class": 1}, "placement": "Spellboard", "effectMagicCost": {"basic": 1}}', '8', 'Ready Spell', '105', '16', NULL, NULL, 'f', 'Law Of Fear
When this spell comes into play, choose up to 3 target units. Those units add 1 to their attack value for the remainder of this turn. Players must spend 1  or place 2 wound tokens on their Phoenixborn to declare blockers or declare a guard. Bound This card cannot be discarded from your spellboard when you Meditate. Fleeting Discard this card at the end of this round.', '0', '172', '1', NULL, NULL, 't'),
('173', 'Light Swordsman', 'light-swordsman', '{"cost": [["[[main]]", "[[side]]"], "1 [[sympathy:class]]", "1 [[divine:class]]"], "dice": ["sympathy", "divine"], "life": 2, "name": "Light Swordsman", "stub": "light-swordsman", "text": "Battle Advantage: When this unit is in battle, it deals its damage before other units without Battle Advantage deal their damage.\n\nOpportunist 1: When you draw 1 or more cards during a player''s turn, add 1 to this unit''s attack value for the remainder of that turn.", "type": "Ally", "attack": 1, "weight": 206, "recover": 2, "release": {"name": "The Masters of Gravity", "stub": "the-masters-of-gravity", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"divine:class": 1, "sympathy:class": 1}, "placement": "Battlefield"}', '8', 'Ally', '206', '48', NULL, NULL, 'f', 'Light Swordsman
Battle Advantage When this unit is in battle, it deals its damage before other units without Battle Advantage deal their damage. Opportunist 1 When you draw 1 or more cards during a player''s turn, add 1 to this unit''s attack value for the remainder of that turn.', '0', '173', '1', NULL, NULL, 't'),
('174', 'Mirror Spirit', 'mirror-spirit', '{"life": 2, "name": "Mirror Spirit", "stub": "mirror-spirit", "text": "Reflect Sorrow: When this unit comes into play, place 1 status token on this unit for each exhaustion token on units a target player controls.\n\n* X = the number of status tokens on this unit.", "type": "Conjuration", "attack": "X", "copies": 3, "recover": 0, "release": {"name": "The Masters of Gravity", "stub": "the-masters-of-gravity", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '8', 'Conjuration', '0', '0', NULL, '3', 'f', 'Mirror Spirit
Reflect Sorrow When this unit comes into play, place 1 status token on this unit for each exhaustion token on units a target player controls. X = the number of status tokens on this unit.', '0', '174', '1', NULL, NULL, 't'),
('175', 'Polarity Mage', 'polarity-mage', '{"cost": ["[[main]]", ["1 [[divine:class]]", "1 [[sympathy:class]]"]], "life": 2, "name": "Polarity Mage", "stub": "polarity-mage", "text": "Take: [[side]] - 1 [[basic]]: Remove 1 alteration spell from a target unit you control and place that alteration spell face down under this unit.\n\n* Give: When a unit comes into play onto your battlefield, you may choose 1 face down alteration spell under this unit and attach it face up to that unit.\n\n* X = the number of face down cards under this unit.", "type": "Ally", "attack": "X", "weight": 106, "altDice": ["divine", "sympathy"], "recover": "X", "release": {"name": "The Masters of Gravity", "stub": "the-masters-of-gravity", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"divine:class / sympathy:class": 1}, "placement": "Battlefield", "effectRepeats": true, "effectMagicCost": {"basic": 1}}', '8', 'Ally', '106', '0', NULL, NULL, 'f', 'Polarity Mage
Take Remove 1 alteration spell from a target unit you control and place that alteration spell face down under this unit. Give When a unit comes into play onto your battlefield, you may choose 1 face down alteration spell under this unit and attach it face up to that unit. X = the number of face down cards under this unit.', '48', '175', '1', NULL, NULL, 't'),
('176', 'Sonic Swordsman', 'sonic-swordsman', '{"cost": ["[[main]]", "1 [[divine:power]]", "1 [[sympathy:class]]", "1 [[basic]]"], "dice": ["divine", "sympathy"], "life": 3, "name": "Sonic Swordsman", "stub": "sonic-swordsman", "text": "Aftershock 2: When this unit deals damage by attacking or countering, you may place 2 wound tokens on a target unit.\n\n* Rhythmic Healing 1: When you draw 1 or more cards, you may remove 1 wound token from this unit.", "type": "Ally", "attack": 2, "weight": 308, "recover": 1, "release": {"name": "The Masters of Gravity", "stub": "the-masters-of-gravity", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "divine:power": 1, "sympathy:class": 1}, "placement": "Battlefield"}', '8', 'Ally', '308', '48', NULL, NULL, 'f', 'Sonic Swordsman
Aftershock 2 When this unit deals damage by attacking or countering, you may place 2 wound tokens on a target unit. Rhythmic Healing 1 When you draw 1 or more cards, you may remove 1 wound token from this unit.', '0', '176', '1', NULL, NULL, 't'),
('177', 'Summon Mirror Spirit', 'summon-mirror-spirit', '{"cost": ["[[main]]"], "dice": ["sympathy"], "name": "Summon Mirror Spirit", "stub": "summon-mirror-spirit", "text": "[[main]] - [[exhaust]] - 1 [[sympathy:class]] - 1 [[basic]]: Place a [[Mirror Spirit]] conjuration onto your battlefield.\n\nFocus 1: You may remove all status tokens from a Mirror Spirit you control. If you remove at least 1 status token, place 1 exhaustion token on a target unit.", "type": "Ready Spell", "weight": 5, "release": {"name": "The Masters of Gravity", "stub": "the-masters-of-gravity", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "conjurations": [{"name": "Mirror Spirit", "stub": "mirror-spirit"}], "effectMagicCost": {"basic": 1, "sympathy:class": 1}}', '8', 'Ready Spell', '5', '32', NULL, NULL, 't', 'Summon Mirror Spirit
Place a Mirror Spirit conjuration onto your battlefield. Focus 1 You may remove all status tokens from a Mirror Spirit you control. If you remove at least 1 status token, place 1 exhaustion token on a target unit.', '0', '177', '1', NULL, NULL, 't'),
('178', 'Battle Mage', 'battle-mage', '{"cost": ["[[main]]", "3 [[basic]]"], "life": 3, "name": "Battle Mage", "stub": "battle-mage", "text": "Magic Potential 1: When this unit deals damage by attacking or countering, select 1 die in your exhausted pool and place it into your active pool on its basic side.", "type": "Ally", "attack": 2, "weight": 305, "recover": 1, "release": {"name": "The Path of Assassins", "stub": "the-path-of-assassins", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"basic": 3}, "placement": "Battlefield", "diceRecursion": 1}', '9', 'Ally', '305', '0', NULL, NULL, 'f', 'Battle Mage
Magic Potential 1 When this unit deals damage by attacking or countering, select 1 die in your exhausted pool and place it into your active pool on its basic side.', '0', '178', '1', NULL, NULL, 't'),
('179', 'Double Edge', 'double-edge', '{"cost": ["[[side]]"], "name": "Double Edge", "stub": "double-edge", "text": "Draw 2 cards. You may discard up to 2 cards from your hand. For each card you discard, place 1 wound token on a target unit or a target Phoenixborn.", "type": "Action Spell", "weight": 4, "release": {"name": "The Path of Assassins", "stub": "the-path-of-assassins", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "placement": "Discard", "phoenixborn": "Jericho Kill"}', '9', 'Action Spell', '4', '0', 'Jericho Kill', NULL, 'f', 'Double Edge
Draw 2 cards. You may discard up to 2 cards from your hand. For each card you discard, place 1 wound token on a target unit or a target Phoenixborn.', '0', '179', '1', NULL, NULL, 't'),
('180', 'Elephant Rider', 'elephant-rider', '{"cost": ["[[main]]", "7 [[basic]]"], "life": 6, "name": "Elephant Rider", "stub": "elephant-rider", "text": "Overkill 2: When this unit destroys a unit an opponent controls by attacking, deal 2 damage to that opponent''s Phoenixborn.\n\n* Unbreakable 2: If this unit has 2 or fewer wound tokens on it, it cannot be affected by spells, abilities, or dice powers that would place exhaustion tokens on it, destroy it, or return it to its owner''s hand.", "type": "Ally", "attack": 6, "weight": 705, "recover": 3, "release": {"name": "The Path of Assassins", "stub": "the-path-of-assassins", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"basic": 7}, "placement": "Battlefield"}', '9', 'Ally', '705', '0', NULL, NULL, 'f', 'Elephant Rider
Overkill 2 When this unit destroys a unit an opponent controls by attacking, deal 2 damage to that opponent''s Phoenixborn. Unbreakable 2 If this unit has 2 or fewer wound tokens on it, it cannot be affected by spells, abilities, or dice powers that would place exhaustion tokens on it, destroy it, or return it to its owner''s hand.', '0', '180', '1', NULL, NULL, 't'),
('181', 'Hand Tricks', 'hand-tricks', '{"cost": ["[[side]]", "1 [[basic]]"], "name": "Hand Tricks", "stub": "hand-tricks", "text": "Select 1 die in your exhausted pool and place it into your active pool on its basic side. Draw 1 card.\n\n~ Return 1: When your turn begins, if this card is in your discard pile, you may spend 1 [[basic]] and discard 1 card off the top of your draw pile to place this card into your hand.", "type": "Action Spell", "weight": 104, "release": {"name": "The Path of Assassins", "stub": "the-path-of-assassins", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"basic": 1}, "placement": "Discard", "diceRecursion": 1, "effectRepeats": true, "effectMagicCost": {"basic": 1}}', '9', 'Action Spell', '104', '0', NULL, NULL, 'f', 'Hand Tricks
Select 1 die in your exhausted pool and place it into your active pool on its basic side. Draw 1 card. Return 1 When your turn begins, if this card is in your discard pile, you may spend 1  and discard 1 card off the top of your draw pile to place this card into your hand.', '0', '181', '1', NULL, NULL, 't'),
('182', 'Jericho Kill', 'jericho-kill', '{"life": 15, "name": "Jericho Kill", "stub": "jericho-kill", "text": "Build Magic: At the beginning of each prepare phase you may place 1 card from your hand face down under this card.\n\nRe-Tool Magic: [[side]]: Discard 1 face down card from under this card to deal 1 damage to a target unit or remove 1 wound token from this card.", "type": "Phoenixborn", "release": {"name": "The Path of Assassins", "stub": "the-path-of-assassins", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "spellboard": 4, "battlefield": 9}', '9', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Jericho Kill
Build Magic At the beginning of each prepare phase you may place 1 card from your hand face down under this card. Re-Tool Magic: : Discard 1 face down card from under this card to deal 1 damage to a target unit or remove 1 wound token from this card.', '0', '182', '1', NULL, NULL, 't'),
('183', 'Lucky Rabbit', 'lucky-rabbit', '{"life": 2, "name": "Lucky Rabbit", "stub": "lucky-rabbit", "text": "Luck Stream: When placing 3 or more dice in your exhausted pool, re-roll them. If you roll 1 or more power symbols, you may return 1 of those dice to your active pool on its basic side. Luck Stream cannot be used to return more than 1 die each turn.", "type": "Conjuration", "attack": 1, "copies": 4, "recover": 0, "release": {"name": "The Path of Assassins", "stub": "the-path-of-assassins", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "placement": "Battlefield", "diceRecursion": 1}', '9', 'Conjuration', '0', '0', NULL, '4', 'f', 'Lucky Rabbit
Luck Stream When placing 3 or more dice in your exhausted pool, re-roll them. If you roll 1 or more power symbols, you may return 1 of those dice to your active pool on its basic side. Luck Stream cannot be used to return more than 1 die each turn.', '0', '183', '1', NULL, NULL, 't'),
('184', 'Magic Purity', 'magic-purity', '{"cost": ["[[main]]"], "name": "Magic Purity", "stub": "magic-purity", "text": "After you pay a cost that includes 3 or more basic symbols, you may place 1 exhaustion token on this spell to select 1 die in your exhausted pool and place it into your active pool on its basic side.", "type": "Ready Spell", "weight": 5, "release": {"name": "The Path of Assassins", "stub": "the-path-of-assassins", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "placement": "Spellboard", "diceRecursion": 1}', '9', 'Ready Spell', '5', '0', NULL, NULL, 'f', 'Magic Purity
After you pay a cost that includes 3 or more basic symbols, you may place 1 exhaustion token on this spell to select 1 die in your exhausted pool and place it into your active pool on its basic side.', '0', '184', '1', NULL, NULL, 't'),
('185', 'Prepare', 'prepare', '{"cost": ["[[main]]"], "name": "Prepare", "stub": "prepare", "text": "[[main]] - [[exhaust]]: Place 1 card from your hand or from the top of your draw pile face down under your Phoenixborn, or choose a face down card under your Phoenixborn and place it into your hand.\n\nFocus 1: You may change the activation cost of this spell to [[side]] - [[exhaust]].", "type": "Ready Spell", "weight": 5, "release": {"name": "The Path of Assassins", "stub": "the-path-of-assassins", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "placement": "Spellboard"}', '9', 'Ready Spell', '5', '0', NULL, NULL, 'f', 'Prepare
Place 1 card from your hand or from the top of your draw pile face down under your Phoenixborn, or choose a face down card under your Phoenixborn and place it into your hand. Focus 1 You may change the activation cost of this spell to  - .', '0', '185', '1', NULL, NULL, 't'),
('186', 'Spear Master', 'spear-master', '{"cost": ["[[main]]", "3 [[basic]]", "1 [[discard]]"], "life": 3, "name": "Spear Master", "stub": "spear-master", "text": "Battle Advantage: When this unit is in battle, it deals its damage before other units without Battle Advantage deal their damage.", "type": "Ally", "attack": 3, "weight": 308, "recover": 2, "release": {"name": "The Path of Assassins", "stub": "the-path-of-assassins", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"basic": 3}, "placement": "Battlefield"}', '9', 'Ally', '308', '0', NULL, NULL, 'f', 'Spear Master
Battle Advantage When this unit is in battle, it deals its damage before other units without Battle Advantage deal their damage.', '0', '186', '1', NULL, NULL, 't'),
('187', 'Squire', 'squire', '{"cost": ["[[main]]", "1 [[basic]]"], "life": 1, "name": "Squire", "stub": "squire", "text": "Assist 1: When this unit comes into play, you may change 1 die in your active pool that is on its power side to its basic side. If you do, draw 1 card.", "type": "Ally", "attack": 1, "weight": 105, "recover": 1, "release": {"name": "The Path of Assassins", "stub": "the-path-of-assassins", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"basic": 1}, "placement": "Battlefield"}', '9', 'Ally', '105', '0', NULL, NULL, 'f', 'Squire
Assist 1 When this unit comes into play, you may change 1 die in your active pool that is on its power side to its basic side. If you do, draw 1 card.', '0', '187', '1', NULL, NULL, 't'),
('188', 'Summon Lucky Rabbit', 'summon-lucky-rabbit', '{"cost": ["[[main]]"], "name": "Summon Lucky Rabbit", "stub": "summon-lucky-rabbit", "text": "[[main]] - [[exhaust]] - 2 [[basic]]: Place a [[Lucky Rabbit]] conjuration onto your battlefield.\n\nFocus 1: You may select 1 die in your exhausted pool and place it into your active pool on its basic side.", "type": "Ready Spell", "weight": 5, "release": {"name": "The Path of Assassins", "stub": "the-path-of-assassins", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "placement": "Spellboard", "conjurations": [{"name": "Lucky Rabbit", "stub": "lucky-rabbit"}], "diceRecursion": 1, "effectMagicCost": {"basic": 2}}', '9', 'Ready Spell', '5', '0', NULL, NULL, 't', 'Summon Lucky Rabbit
Place a Lucky Rabbit conjuration onto your battlefield. Focus 1 You may select 1 die in your exhausted pool and place it into your active pool on its basic side.', '0', '188', '1', NULL, NULL, 't'),
('189', 'Summon Turtle Guard', 'summon-turtle-guard', '{"cost": ["[[main]]"], "name": "Summon Turtle Guard", "stub": "summon-turtle-guard", "text": "[[main]] - [[exhaust]] - 3 [[basic]]: Place a [[Turtle Guard]] conjuration onto your battlefield.", "type": "Ready Spell", "weight": 5, "release": {"name": "The Path of Assassins", "stub": "the-path-of-assassins", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "placement": "Spellboard", "conjurations": [{"name": "Turtle Guard", "stub": "turtle-guard"}], "effectMagicCost": {"basic": 3}}', '9', 'Ready Spell', '5', '0', NULL, NULL, 't', 'Summon Turtle Guard
Place a Turtle Guard conjuration onto your battlefield.', '0', '189', '1', NULL, NULL, 't'),
('190', 'Turtle Guard', 'turtle-guard', '{"life": 5, "name": "Turtle Guard", "stub": "turtle-guard", "text": "Unit Guard: This unit may guard a unit that is being attacked.\n\nCumbersome: After this unit receives damage in battle, place 1 exhaustion token on it.", "type": "Conjuration", "attack": 1, "copies": 4, "recover": 2, "release": {"name": "The Path of Assassins", "stub": "the-path-of-assassins", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "placement": "Battlefield"}', '9', 'Conjuration', '0', '0', NULL, '4', 'f', 'Turtle Guard
Unit Guard This unit may guard a unit that is being attacked. Cumbersome After this unit receives damage in battle, place 1 exhaustion token on it.', '0', '190', '1', NULL, NULL, 't'),
('191', 'Astrea', 'astrea', '{"life": 18, "name": "Astrea", "stub": "astrea", "text": "Beguile: When a player would declare attackers, you may place 1 exhaustion token on this card to place 1 exhaustion token on an unexhausted unit you control. If you do, place 1 exhaustion token on a target unit.", "type": "Phoenixborn", "release": {"name": "The Goddess of Ishra", "stub": "the-goddess-of-ishra", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "spellboard": 4, "battlefield": 5}', '10', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Astrea
Beguile When a player would declare attackers, you may place 1 exhaustion token on this card to place 1 exhaustion token on an unexhausted unit you control. If you do, place 1 exhaustion token on a target unit.', '0', '191', '1', NULL, NULL, 't'),
('192', 'Call To Action', 'call-to-action', '{"cost": ["1 [[charm:power]]"], "dice": ["charm"], "name": "Call To Action", "stub": "call-to-action", "text": "You may play this spell after an opponent declares attackers. Remove 1 exhaustion token from a target unit you control.", "type": "Reaction Spell", "weight": 102, "release": {"name": "The Goddess of Ishra", "stub": "the-goddess-of-ishra", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"charm:power": 1}, "placement": "Discard"}', '10', 'Reaction Spell', '102', '2', NULL, NULL, 'f', 'Call To Action
You may play this spell after an opponent declares attackers. Remove 1 exhaustion token from a target unit you control.', '0', '192', '1', NULL, NULL, 't'),
('193', 'Devotion', 'devotion', '{"cost": ["[[side]]", "1 [[divine:class]]", "1 [[basic]]"], "dice": ["divine"], "life": "+2", "name": "Devotion", "stub": "devotion", "text": "When 1 or more exhaustion tokens are placed on this unit by the effect of a spell, ability, or dice power, you may move 1 of those exhaustion tokens onto this spell.\n\n* Respark: 1 [[basic]]", "type": "Alteration Spell", "weight": 205, "recover": "+1", "release": {"name": "The Goddess of Ishra", "stub": "the-goddess-of-ishra", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "divine:class": 1}, "placement": "Unit", "effectMagicCost": {"basic": 1}}', '10', 'Alteration Spell', '205', '16', NULL, NULL, 'f', 'Devotion
When 1 or more exhaustion tokens are placed on this unit by the effect of a spell, ability, or dice power, you may move 1 of those exhaustion tokens onto this spell. Respark 1', '0', '193', '1', NULL, NULL, 't'),
('194', 'Imperial Ninja', 'imperial-ninja', '{"cost": ["[[main]]", "1 [[charm:power]]", "1 [[charm:class]]"], "dice": ["charm"], "life": 2, "name": "Imperial Ninja", "stub": "imperial-ninja", "text": "Interrogate: When this unit deals damage to a Phoenixborn by attacking, name a card. The opponent that controls that Phoenixborn reveals their hand. That opponent must discard all copies of the named card from their hand.", "type": "Ally", "attack": 3, "weight": 208, "recover": 1, "release": {"name": "The Goddess of Ishra", "stub": "the-goddess-of-ishra", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"charm:class": 1, "charm:power": 1}, "placement": "Battlefield"}', '10', 'Ally', '208', '2', NULL, NULL, 'f', 'Imperial Ninja
Interrogate When this unit deals damage to a Phoenixborn by attacking, name a card. The opponent that controls that Phoenixborn reveals their hand. That opponent must discard all copies of the named card from their hand.', '0', '194', '1', NULL, NULL, 't'),
('195', 'Infatuated', 'infatuated', '{"name": "Infatuated", "stub": "infatuated", "text": "When an opponent is attacking with a unit with the Infatuate ability, this unit may only block a unit with the Infatuate ability.", "type": "Conjured Alteration Spell", "copies": 2, "release": {"name": "The Goddess of Ishra", "stub": "the-goddess-of-ishra", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Unit"}', '10', 'Conjured Alteration Spell', '0', '0', NULL, '2', 'f', 'Infatuated
When an opponent is attacking with a unit with the Infatuate ability, this unit may only block a unit with the Infatuate ability.', '0', '195', '1', NULL, NULL, 't'),
('196', 'Kneel', 'kneel', '{"cost": ["[[main]]", "1 [[divine:class]]", "1 [[charm:class]]"], "dice": ["divine", "charm"], "name": "Kneel", "stub": "kneel", "text": "Place 1 exhaustion token on each unexhausted unit.", "type": "Action Spell", "weight": 207, "release": {"name": "The Goddess of Ishra", "stub": "the-goddess-of-ishra", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"charm:class": 1, "divine:class": 1}, "placement": "Discard"}', '10', 'Action Spell', '207', '18', NULL, NULL, 'f', 'Kneel
Place 1 exhaustion token on each unexhausted unit.', '0', '196', '1', NULL, NULL, 't'),
('197', 'Light Bringer', 'light-bringer', '{"life": 2, "name": "Light Bringer", "stub": "light-bringer", "text": "Infatuate: When this unit comes into play, you may spend 1 [[basic]] to attach an [[Infatuated]] conjured alteration spell to a target unit.", "type": "Conjuration", "attack": 1, "copies": 5, "recover": 0, "release": {"name": "The Goddess of Ishra", "stub": "the-goddess-of-ishra", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield", "conjurations": [{"name": "Infatuated", "stub": "infatuated"}], "effectMagicCost": {"basic": 1}}', '10', 'Conjuration', '0', '0', NULL, '5', 'f', 'Light Bringer
Infatuate When this unit comes into play, you may spend 1  to attach an Infatuated conjured alteration spell to a target unit.', '0', '197', '1', NULL, NULL, 't'),
('198', 'Mark Of The Goddess', 'mark-of-the-goddess', '{"cost": ["[[main]]", "2 [[basic]]"], "name": "Mark Of The Goddess", "stub": "mark-of-the-goddess", "text": "This spell can only be attached if the player that played it has an open battlefield slot.\n\nWhen attaching this spell, the player that played it places this unit onto their battlefield.\n\n* When this spell leaves play, place this unit back onto its owner''s battlefield or discard this unit if there is no open slot on that battlefield.\n\n* Fleeting: Discard this card at the end of the round.", "type": "Alteration Spell", "weight": 205, "release": {"name": "The Goddess of Ishra", "stub": "the-goddess-of-ishra", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 2}, "placement": "Unit", "phoenixborn": "Astrea"}', '10', 'Alteration Spell', '205', '0', 'Astrea', NULL, 'f', 'Mark Of The Goddess
This spell can only be attached if the player that played it has an open battlefield slot. When attaching this spell, the player that played it places this unit onto their battlefield. When this spell leaves play, place this unit back onto its owner''s battlefield or discard this unit if there is no open slot on that battlefield. Fleeting Discard this card at the end of the round.', '0', '198', '1', NULL, NULL, 't'),
('199', 'Royal Charm', 'royal-charm', '{"cost": ["[[main]]", "1 [[basic]]"], "name": "Royal Charm", "stub": "royal-charm", "text": "After you spend a charm or divine power symbol, you may place 1 exhaustion token on this spell to place that die with that symbol onto a target unit you control. That die is considered to have been placed by its dice power ability.", "type": "Ready Spell", "weight": 105, "altDice": ["charm", "divine"], "release": {"name": "The Goddess of Ishra", "stub": "the-goddess-of-ishra", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1}, "placement": "Spellboard"}', '10', 'Ready Spell', '105', '0', NULL, NULL, 'f', 'Royal Charm
After you spend a charm or divine power symbol, you may place 1 exhaustion token on this spell to place that die with that symbol onto a target unit you control. That die is considered to have been placed by its dice power ability.', '18', '199', '1', NULL, NULL, 't'),
('200', 'Steadfast Guardian', 'steadfast-guardian', '{"life": 2, "name": "Steadfast Guardian", "stub": "steadfast-guardian", "text": "Lift Burdens: When this unit comes into play, you may spend 1 [[basic]] to remove all exhaustion tokens from a target unit and place them onto this unit.", "type": "Conjuration", "attack": 2, "copies": 3, "recover": 0, "release": {"name": "The Goddess of Ishra", "stub": "the-goddess-of-ishra", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield", "effectMagicCost": {"basic": 1}}', '10', 'Conjuration', '0', '0', NULL, '3', 'f', 'Steadfast Guardian
Lift Burdens When this unit comes into play, you may spend 1  to remove all exhaustion tokens from a target unit and place them onto this unit.', '0', '200', '1', NULL, NULL, 't'),
('201', 'Summon Light Bringer', 'summon-light-bringer', '{"cost": ["[[main]]"], "dice": ["divine"], "name": "Summon Light Bringer", "stub": "summon-light-bringer", "text": "[[main]] - [[exhaust]] - 1 [[divine:class]]: Place a [[Light Bringer]] conjuration onto your battlefield.", "type": "Ready Spell", "weight": 5, "release": {"name": "The Goddess of Ishra", "stub": "the-goddess-of-ishra", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "conjurations": [{"name": "Light Bringer", "stub": "light-bringer"}], "effectMagicCost": {"divine:class": 1}}', '10', 'Ready Spell', '5', '16', NULL, NULL, 't', 'Summon Light Bringer
Place a Light Bringer conjuration onto your battlefield.', '0', '201', '1', NULL, NULL, 't'),
('202', 'Summon Steadfast Guardian', 'summon-steadfast-guardian', '{"cost": ["[[main]]"], "dice": ["divine", "charm"], "name": "Summon Steadfast Guardian", "stub": "summon-steadfast-guardian", "text": "After 1 or more exhaustion tokens are placed on a unit you control by the effect of a spell or ability, you may spend 1 [[divine:class]] and 1 [[charm:class]] and place 1 exhaustion token on this spell to place a [[Steadfast Guardian]] conjuration onto your battlefield.\n\nFocus 1: You may search a target discard pile for 1 card and remove it from the game.", "type": "Ready Spell", "weight": 5, "release": {"name": "The Goddess of Ishra", "stub": "the-goddess-of-ishra", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "conjurations": [{"name": "Steadfast Guardian", "stub": "steadfast-guardian"}], "effectMagicCost": {"charm:class": 1, "divine:class": 1}}', '10', 'Ready Spell', '5', '18', NULL, NULL, 't', 'Summon Steadfast Guardian
After 1 or more exhaustion tokens are placed on a unit you control by the effect of a spell or ability, you may spend 1  and 1  and place 1 exhaustion token on this spell to place a Steadfast Guardian conjuration onto your battlefield. Focus 1 You may search a target discard pile for 1 card and remove it from the game.', '0', '202', '1', NULL, NULL, 't'),
('203', 'Summon Weeping Spirit', 'summon-weeping-spirit', '{"cost": ["[[main]]"], "dice": ["charm"], "name": "Summon Weeping Spirit", "stub": "summon-weeping-spirit", "text": "[[main]] - [[exhaust]] - 1 [[charm:class]]: Place a [[Weeping Spirit]] conjuration onto a target player''s battlefield.\n\nFocus 1: You may search a target discard pile for 1 card and remove it from the game.", "type": "Ready Spell", "weight": 5, "release": {"name": "The Goddess of Ishra", "stub": "the-goddess-of-ishra", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "conjurations": [{"name": "Weeping Spirit", "stub": "weeping-spirit"}], "effectMagicCost": {"charm:class": 1}}', '10', 'Ready Spell', '5', '2', NULL, NULL, 't', 'Summon Weeping Spirit
Place a Weeping Spirit conjuration onto a target player''s battlefield. Focus 1 You may search a target discard pile for 1 card and remove it from the game.', '0', '203', '1', NULL, NULL, 't'),
('204', 'Sun Sister', 'sun-sister', '{"cost": ["[[main]]", "1 [[divine:class]]", "1 [[basic]]"], "dice": ["divine"], "life": 2, "name": "Sun Sister", "stub": "sun-sister", "text": "Resurrect: When this unit would leave play, you may search your discard pile for an ally with a title other than this unit''s title and place it into your hand.", "type": "Ally", "attack": 2, "weight": 206, "recover": 2, "release": {"name": "The Goddess of Ishra", "stub": "the-goddess-of-ishra", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "divine:class": 1}, "placement": "Battlefield"}', '10', 'Ally', '206', '16', NULL, NULL, 'f', 'Sun Sister
Resurrect When this unit would leave play, you may search your discard pile for an ally with a title other than this unit''s title and place it into your hand.', '0', '204', '2', NULL, NULL, 't'),
('205', 'Weeping Spirit', 'weeping-spirit', '{"life": 2, "name": "Weeping Spirit", "stub": "weeping-spirit", "text": "Fearful: This unit cannot block.\n\nQuell: [[side]] - [[discard]]: Destroy this unit.", "type": "Conjuration", "attack": 0, "copies": 4, "recover": 0, "release": {"name": "The Goddess of Ishra", "stub": "the-goddess-of-ishra", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '10', 'Conjuration', '0', '0', NULL, '4', 'f', 'Weeping Spirit
Fearful This unit cannot block. Quell Destroy this unit.', '0', '205', '1', NULL, NULL, 't'),
('206', 'Biter', 'biter', '{"life": 2, "name": "Biter", "stub": "biter", "text": "Unit Guard: This unit may guard a unit that is being attacked.\n\nRooted: This unit cannot attack.", "type": "Conjuration", "attack": 3, "copies": 4, "recover": 0, "release": {"name": "The Boy Among Wolves", "stub": "the-boy-among-wolves", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '11', 'Conjuration', '0', '0', NULL, '4', 'f', 'Biter
Unit Guard This unit may guard a unit that is being attacked. Rooted This unit cannot attack.', '0', '206', '1', NULL, NULL, 't'),
('207', 'Brilliant Thorn', 'brilliant-thorn', '{"life": 2, "name": "Brilliant Thorn", "stub": "brilliant-thorn", "text": "* Inheritance 1: When this unit is destroyed, you may place 1 status token on a target unit.\n\n* Fade: Destroy this unit at the end of this round.", "type": "Conjuration", "attack": 3, "copies": 6, "recover": 0, "release": {"name": "The Boy Among Wolves", "stub": "the-boy-among-wolves", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '11', 'Conjuration', '0', '0', NULL, '6', 'f', 'Brilliant Thorn
Inheritance 1 When this unit is destroyed, you may place 1 status token on a target unit. Fade Destroy this unit at the end of this round.', '0', '207', '1', NULL, NULL, 't'),
('208', 'Explosive Growth', 'explosive-growth', '{"cost": ["[[side]]", "1 [[sympathy:class]]", "1 [[natural:class]]"], "dice": ["sympathy", "natural"], "name": "Explosive Growth", "stub": "explosive-growth", "text": "When attaching this spell, place 2 status tokens on this unit. Discard all other copies of Explosive Growth attached to this unit.\n\nX = the number of status tokens on this unit.", "type": "Alteration Spell", "attack": "+X", "weight": 206, "release": {"name": "The Boy Among Wolves", "stub": "the-boy-among-wolves", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"natural:class": 1, "sympathy:class": 1}, "placement": "Unit"}', '11', 'Alteration Spell', '206', '40', NULL, NULL, 'f', 'Explosive Growth
When attaching this spell, place 2 status tokens on this unit. Discard all other copies of Explosive Growth attached to this unit. X = the number of status tokens on this unit.', '0', '208', '1', NULL, NULL, 't'),
('209', 'Hunt Master', 'hunt-master', '{"cost": ["[[main]]", "1 [[natural:power]]", "1 [[sympathy:class]]", "1 [[basic]]"], "dice": ["natural", "sympathy"], "life": 3, "name": "Hunt Master", "stub": "hunt-master", "text": "Call the Hunt: When this unit would be declared as an attacker, you may place a [[Panther Spirit]] conjuration onto your battlefield. That Panther Spirit may be declared as an attacker.", "type": "Ally", "attack": 2, "weight": 308, "recover": 1, "release": {"name": "The Boy Among Wolves", "stub": "the-boy-among-wolves", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "natural:power": 1, "sympathy:class": 1}, "placement": "Battlefield", "conjurations": [{"name": "Panther Spirit", "stub": "panther-spirit"}]}', '11', 'Ally', '308', '40', NULL, NULL, 'f', 'Hunt Master
Call the Hunt When this unit would be declared as an attacker, you may place a Panther Spirit conjuration onto your battlefield. That Panther Spirit may be declared as an attacker.', '0', '209', '1', NULL, NULL, 't'),
('210', 'Indiglow Creeper', 'indiglow-creeper', '{"life": 1, "name": "Indiglow Creeper", "stub": "indiglow-creeper", "text": "* Germinate: When this unit is destroyed, place a [[Luminous Seedling]] conjuration onto your battlefield.\n\n* Fade: Destroy this unit at the end of this round.", "type": "Conjuration", "attack": 2, "copies": 3, "recover": 0, "release": {"name": "The Boy Among Wolves", "stub": "the-boy-among-wolves", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield", "conjurations": [{"name": "Luminous Seedling", "stub": "luminous-seedling"}]}', '11', 'Conjuration', '0', '0', NULL, '3', 'f', 'Indiglow Creeper
Germinate When this unit is destroyed, place a Luminous Seedling conjuration onto your battlefield. Fade Destroy this unit at the end of this round.', '0', '210', '1', NULL, NULL, 't'),
('211', 'Join The Hunt', 'join-the-hunt', '{"cost": ["[[main]]", "1 [[sympathy:class]]"], "dice": ["sympathy"], "name": "Join The Hunt", "stub": "join-the-hunt", "text": "After you declare attackers, you may place 1 exhaustion token on this spell to place 1 exhaustion token on an unexhausted unit you control that is not attacking. If you do, add 2 to the attack value of a unit you control for the remainder of the turn.", "type": "Ready Spell", "weight": 106, "release": {"name": "The Boy Among Wolves", "stub": "the-boy-among-wolves", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"sympathy:class": 1}, "placement": "Spellboard"}', '11', 'Ready Spell', '106', '32', NULL, NULL, 'f', 'Join The Hunt
After you declare attackers, you may place 1 exhaustion token on this spell to place 1 exhaustion token on an unexhausted unit you control that is not attacking. If you do, add 2 to the attack value of a unit you control for the remainder of the turn.', '0', '211', '1', NULL, NULL, 't'),
('212', 'Jungle Warrior', 'jungle-warrior', '{"cost": ["[[main]]", "1 [[sympathy:class]]", "1 [[basic]]"], "dice": ["sympathy"], "life": 2, "name": "Jungle Warrior", "stub": "jungle-warrior", "text": "* Last Orders 1: When this unit is destroyed, you may spend 1 [[basic]] to remove 1 exhaustion token from a target unit.\n\n* Inheritance 1: When this unit is destroyed, you may place 1 status token on a target unit.", "type": "Ally", "attack": 2, "weight": 206, "recover": 1, "release": {"name": "The Boy Among Wolves", "stub": "the-boy-among-wolves", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "sympathy:class": 1}, "placement": "Battlefield", "effectMagicCost": {"basic": 1}}', '11', 'Ally', '206', '32', NULL, NULL, 'f', 'Jungle Warrior
Last Orders 1 When this unit is destroyed, you may spend 1  to remove 1 exhaustion token from a target unit. Inheritance 1 When this unit is destroyed, you may place 1 status token on a target unit.', '0', '212', '1', NULL, NULL, 't'),
('213', 'Lick Wounds', 'lick-wounds', '{"cost": [["[[main]]", "[[side]]"], "2 [[basic]]"], "name": "Lick Wounds", "stub": "lick-wounds", "text": "Remove 2 wound tokens and 1 exhaustion token from a target unit or Phoenixborn.", "type": "Action Spell", "weight": 204, "release": {"name": "The Boy Among Wolves", "stub": "the-boy-among-wolves", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 2}, "placement": "Discard", "phoenixborn": "Koji Wolfcub"}', '11', 'Action Spell', '204', '0', 'Koji Wolfcub', NULL, 'f', 'Lick Wounds
Remove 2 wound tokens and 1 exhaustion token from a target unit or Phoenixborn.', '0', '213', '1', NULL, NULL, 't'),
('214', 'Koji Wolfcub', 'koji-wolfcub', '{"life": 16, "name": "Koji Wolfcub", "stub": "koji-wolfcub", "text": "Accelerate Growth: [[side]] - [[exhaust]]: Place 1 status token on a target card.", "type": "Phoenixborn", "release": {"name": "The Boy Among Wolves", "stub": "the-boy-among-wolves", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "spellboard": 3, "battlefield": 10}', '11', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Koji Wolfcub
Accelerate Growth Place 1 status token on a target card.', '0', '214', '1', NULL, NULL, 't'),
('215', 'Luminous Seedling', 'luminous-seedling', '{"life": 2, "name": "Luminous Seedling", "stub": "luminous-seedling", "text": "Blossom: [[main]]: Remove 2 status tokens from this unit and destroy this unit. If you do, place up to 2 [[Brilliant Thorn]] conjurations onto your battlefield.\n\n* Growth: Add 1 to this unit''s life value for each status token on this unit.", "type": "Conjuration", "attack": 0, "copies": 3, "recover": 0, "release": {"name": "The Boy Among Wolves", "stub": "the-boy-among-wolves", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield", "conjurations": [{"name": "Brilliant Thorn", "stub": "brilliant-thorn"}]}', '11', 'Conjuration', '0', '0', NULL, '3', 'f', 'Luminous Seedling
Blossom Remove 2 status tokens from this unit and destroy this unit. If you do, place up to 2 Brilliant Thorn conjurations onto your battlefield. Growth Add 1 to this unit''s life value for each status token on this unit.', '0', '215', '1', NULL, NULL, 't'),
('216', 'Mark Of The Red Flower', 'mark-of-the-red-flower', '{"cost": [["[[main]]", "[[side]]"]], "name": "Mark Of The Red Flower", "stub": "mark-of-the-red-flower", "text": "Growing Flames: [[side]] - 1 [[natural:class]] / 1 [[sympathy:class]]: Place 1 status token on the attached unit.\n\nThis unit now has the following ability:\n\nFire Mastery: [[exhaust]]: Remove 2 status tokens from this unit. If you do, deal 3 damage to a target unit. You may only activate this ability during your turn.", "type": "Alteration Spell", "weight": 4, "altDice": ["natural", "sympathy"], "release": {"name": "The Boy Among Wolves", "stub": "the-boy-among-wolves", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Unit", "effectRepeats": true, "effectMagicCost": {"natural:class / sympathy:class": 1}}', '11', 'Alteration Spell', '4', '0', NULL, NULL, 'f', 'Mark Of The Red Flower
Growing Flames  - 1  / 1 : Place 1 status token on the attached unit. This unit now has the following ability: Fire Mastery Remove 2 status tokens from this unit. If you do, deal 3 damage to a target unit. You may only activate this ability during your turn.', '40', '216', '1', NULL, NULL, 't'),
('217', 'Panther Spirit', 'panther-spirit', '{"life": 1, "name": "Panther Spirit", "stub": "panther-spirit", "text": "* Fleeting: Discard this card at the end of this round.", "type": "Conjuration", "attack": 1, "copies": 3, "recover": 0, "release": {"name": "The Boy Among Wolves", "stub": "the-boy-among-wolves", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '11', 'Conjuration', '0', '0', NULL, '3', 'f', 'Panther Spirit
Fleeting Discard this card at the end of this round.', '0', '217', '1', NULL, NULL, 't'),
('218', 'Sleeping Bear', 'sleeping-bear', '{"cost": ["[[main]]", "2 [[natural:class]]"], "dice": ["natural"], "life": 4, "name": "Sleeping Bear", "stub": "sleeping-bear", "text": "Slumbering 1: When this unit comes into play, place 1 exhaustion token on it.", "type": "Ally", "attack": 4, "weight": 207, "recover": 2, "release": {"name": "The Boy Among Wolves", "stub": "the-boy-among-wolves", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"natural:class": 2}, "placement": "Battlefield"}', '11', 'Ally', '207', '8', NULL, NULL, 'f', 'Sleeping Bear
Slumbering 1 When this unit comes into play, place 1 exhaustion token on it.', '0', '218', '1', NULL, NULL, 't'),
('219', 'Summon Biter', 'summon-biter', '{"cost": ["[[main]]"], "dice": ["natural"], "name": "Summon Biter", "stub": "summon-biter", "text": "[[main]] - [[exhaust]] - 1 [[natural:class]] - 1 [[basic]]: Place a [[Biter]] conjuration onto your battlefield.", "type": "Ready Spell", "weight": 5, "release": {"name": "The Boy Among Wolves", "stub": "the-boy-among-wolves", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "conjurations": [{"name": "Biter", "stub": "biter"}], "effectMagicCost": {"basic": 1, "natural:class": 1}}', '11', 'Ready Spell', '5', '8', NULL, NULL, 't', 'Summon Biter
Place a Biter conjuration onto your battlefield.', '0', '219', '1', NULL, NULL, 't'),
('220', 'Summon Indiglow Creeper', 'summon-indiglow-creeper', '{"cost": ["[[main]]"], "dice": ["natural", "sympathy"], "name": "Summon Indiglow Creeper", "stub": "summon-indiglow-creeper", "text": "[[main]] - [[exhaust]] - 1 [[natural:class]] - 1 [[sympathy:class]]: Place an [[Indiglow Creeper]] conjuration onto your battlefield.\n\nFocus 1: You may place 1 status token on a target unit you control.\n\nFocus 2: You may place a [[Luminous Seedling]] conjuration onto your battlefield.", "type": "Ready Spell", "weight": 5, "release": {"name": "The Boy Among Wolves", "stub": "the-boy-among-wolves", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "conjurations": [{"name": "Indiglow Creeper", "stub": "indiglow-creeper"}, {"name": "Luminous Seedling", "stub": "luminous-seedling"}], "effectMagicCost": {"natural:class": 1, "sympathy:class": 1}}', '11', 'Ready Spell', '5', '40', NULL, NULL, 't', 'Summon Indiglow Creeper
Place an Indiglow Creeper conjuration onto your battlefield. Focus 1 You may place 1 status token on a target unit you control. Focus 2 You may place a Luminous Seedling conjuration onto your battlefield.', '0', '220', '1', NULL, NULL, 't'),
('221', 'Temple Elder', 'temple-elder', '{"cost": ["[[main]]", "2 [[basic]]"], "life": 2, "name": "Temple Elder", "stub": "temple-elder", "text": "* Resourceful 1: When this unit comes into play, place 1 status token on this unit. At the beginning of the player turns phase, place 1 status token on this unit.\n\nWisdom 1: [[side]] - 1 [[sympathy: class]]: Remove 1 status token from this unit. If you do, draw 1 card.", "type": "Ally", "attack": 2, "weight": 205, "recover": 1, "release": {"name": "The Boy Among Wolves", "stub": "the-boy-among-wolves", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 2}, "placement": "Battlefield", "effectRepeats": true, "effectMagicCost": {"sympathy:class": 1}}', '11', 'Ally', '205', '0', NULL, NULL, 'f', 'Temple Elder
Resourceful 1 When this unit comes into play, place 1 status token on this unit. At the beginning of the player turns phase, place 1 status token on this unit. Wisdom 1  - 1 : Remove 1 status token from this unit. If you do, draw 1 card.', '0', '221', '1', NULL, NULL, 't'),
('222', 'Adrenaline Rush', 'adrenaline-rush', '{"cost": ["1 [[ceremonial:class]]"], "dice": ["ceremonial"], "name": "Adrenaline Rush", "stub": "adrenaline-rush", "text": "You may play this spell when you would declare attackers. Deal 2 damage to a target unit you control and remove 1 exhaustion token from that unit. That unit may be declared as an attacker.", "type": "Reaction Spell", "weight": 101, "release": {"name": "The Demons of Darmas", "stub": "the-demons-of-darmas", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"ceremonial:class": 1}, "placement": "Discard"}', '12', 'Reaction Spell', '101', '1', NULL, NULL, 'f', 'Adrenaline Rush
You may play this spell when you would declare attackers. Deal 2 damage to a target unit you control and remove 1 exhaustion token from that unit. That unit may be declared as an attacker.', '0', '2087', '1', NULL, NULL, 't'),
('223', 'Beast Mage', 'beast-mage', '{"cost": ["[[main]]", "2 [[sympathy:class]]", "1 [[basic]]"], "dice": ["sympathy"], "life": 2, "name": "Beast Mage", "stub": "beast-mage", "text": "Terrifying 1: This unit cannot be blocked or guarded against by units with an attack value of 1 or less.\n\n* Transform 2: While you do not have the first player token, the attack value, life value, and recover value of this unit are increased by 2.", "type": "Ally", "attack": 2, "weight": 307, "recover": 0, "release": {"name": "The Demons of Darmas", "stub": "the-demons-of-darmas", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "sympathy:class": 2}, "placement": "Battlefield"}', '12', 'Ally', '307', '32', NULL, NULL, 'f', 'Beast Mage
Terrifying 1 This unit cannot be blocked or guarded against by units with an attack value of 1 or less. Transform 2 While you do not have the first player token, the attack value, life value, and recover value of this unit are increased by 2.', '0', '2088', '1', NULL, NULL, 't'),
('224', 'Beast Warrior', 'beast-warrior', '{"cost": ["[[main]]", "[[side]]", "1 [[sympathy:class]]"], "dice": ["sympathy"], "life": 1, "name": "Beast Warrior", "stub": "beast-warrior", "text": "Group Tactics 1: After you declare 3 or more attackers, you may add 1 to this unit''s attack value for the remainder of this turn.\n\n* Transform 1: While you do not have the first player token, the attack value, life value, and recover value of this unit are increased by 1.", "type": "Ally", "attack": 1, "weight": 110, "recover": 0, "release": {"name": "The Demons of Darmas", "stub": "the-demons-of-darmas", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"sympathy:class": 1}, "placement": "Battlefield"}', '12', 'Ally', '110', '32', NULL, NULL, 'f', 'Beast Warrior
Group Tactics 1 After you declare 3 or more attackers, you may add 1 to this unit''s attack value for the remainder of this turn. Transform 1 While you do not have the first player token, the attack value, life value, and recover value of this unit are increased by 1.', '0', '2089', '1', NULL, NULL, 't'),
('225', 'Dark Reaping', 'dark-reaping', '{"cost": ["[[main]]", "2 [[ceremonial:class]]"], "dice": ["ceremonial"], "name": "Dark Reaping", "stub": "dark-reaping", "text": "Destroy a target unit you control. If you do, select 4 dice in your exhausted pool, re-roll them, and place them into your active pool.", "type": "Action Spell", "weight": 207, "release": {"name": "The Demons of Darmas", "stub": "the-demons-of-darmas", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"ceremonial:class": 2}, "placement": "Discard", "diceRecursion": 4}', '12', 'Action Spell', '207', '1', NULL, NULL, 'f', 'Dark Reaping
Destroy a target unit you control. If you do, select 4 dice in your exhausted pool, re-roll them, and place them into your active pool.', '0', '2090', '1', NULL, NULL, 't'),
('226', 'Dark Transformation', 'dark-transformation', '{"life": "+1", "name": "Dark Transformation", "stub": "dark-transformation", "text": "After attaching this spell, you may select 1 die in your exhausted pool, re-roll it, and place it into your active pool.\n\n* Spell Guard: This spell cannot be affected by an opponent''s spell.", "type": "Conjured Alteration Spell", "copies": 3, "release": {"name": "The Demons of Darmas", "stub": "the-demons-of-darmas", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Phoenixborn", "spellboard": "+1", "battlefield": "+1", "phoenixborn": "Harold Westraven"}', '12', 'Conjured Alteration Spell', '0', '0', 'Harold Westraven', '3', 'f', 'Dark Transformation
After attaching this spell, you may select 1 die in your exhausted pool, re-roll it, and place it into your active pool. Spell Guard This spell cannot be affected by an opponent''s spell.', '0', '2091', '1', NULL, NULL, 't'),
('227', 'Drain Vitality', 'drain-vitality', '{"cost": [["[[main]]", "[[side]]"], "1 [[basic]]"], "name": "Drain Vitality", "stub": "drain-vitality", "text": "[[main]] - [[exhaust]] - 1 [[ceremonial:class]]: Deal 1 damage to a target unit. If you do, remove 1 wound token from a target unit.\n\n[[side]] - [[exhaust]] - 1 [[sympathy:class]]: Remove 1 status token from a target unit. If you do, place 1 status token on a target unit.", "type": "Ready Spell", "weight": 104, "altDice": ["ceremonial", "sympathy"], "release": {"name": "The Demons of Darmas", "stub": "the-demons-of-darmas", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1}, "placement": "Spellboard", "effectMagicCost": {"sympathy:class": 1, "ceremonial:class": 1}}', '12', 'Ready Spell', '104', '0', NULL, NULL, 'f', 'Drain Vitality
Deal 1 damage to a target unit. If you do, remove 1 wound token from a target unit. Remove 1 status token from a target unit. If you do, place 1 status token on a target unit.', '33', '2092', '1', NULL, NULL, 't'),
('228', 'Harold Westraven', 'harold-westraven', '{"life": 21, "name": "Harold Westraven", "stub": "harold-westraven", "text": "Mark Prey: [[side]] - [[exhaust]] - 1 [[basic]]: Attach a [[Hunter''s Mark]] conjured alteration spell to a target unit.", "type": "Phoenixborn", "release": {"name": "The Demons of Darmas", "stub": "the-demons-of-darmas", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "spellboard": 2, "battlefield": 5, "conjurations": [{"name": "Hunter''s Mark", "stub": "hunters-mark"}], "effectMagicCost": {"basic": 1}}', '12', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Harold Westraven
Mark Prey Attach a Hunter''s Mark conjured alteration spell to a target unit.', '0', '2093', '1', NULL, NULL, 't'),
('229', 'Harvest Soul', 'harvest-soul', '{"cost": [], "name": "Harvest Soul", "stub": "harvest-soul", "text": "You may play this spell when a unit is destroyed as a result of a spell, attack, counter, ability, or dice power you control. Remove that unit from the game. Draw 1 card and attach a [[Dark Transformation]] conjured alteration spell to your Phoenixborn.", "type": "Reaction Spell", "weight": 0, "release": {"name": "The Demons of Darmas", "stub": "the-demons-of-darmas", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Discard", "phoenixborn": "Harold Westraven", "conjurations": [{"name": "Dark Transformation", "stub": "dark-transformation"}], "diceRecursion": 1}', '12', 'Reaction Spell', '0', '0', 'Harold Westraven', NULL, 'f', 'Harvest Soul
You may play this spell when a unit is destroyed as a result of a spell, attack, counter, ability, or dice power you control. Remove that unit from the game. Draw 1 card and attach a Dark Transformation conjured alteration spell to your Phoenixborn.', '0', '2094', '1', NULL, NULL, 't'),
('230', 'Hunter''s Mark', 'hunters-mark', '{"cost": [], "name": "Hunter''s Mark", "stub": "hunters-mark", "text": "When this unit receives damage, place twice the normal number of wound tokens on it.\n\nWhile this unit is the target of an attack, no guard may be declared.", "type": "Conjured Alteration Spell", "copies": 1, "weight": 0, "release": {"name": "The Demons of Darmas", "stub": "the-demons-of-darmas", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Unit", "phoenixborn": "Harold Westraven"}', '12', 'Conjured Alteration Spell', '0', '0', 'Harold Westraven', '1', 'f', 'Hunter''s Mark
When this unit receives damage, place twice the normal number of wound tokens on it. While this unit is the target of an attack, no guard may be declared.', '0', '2095', '1', NULL, NULL, 't'),
('231', 'Master Vampire', 'master-vampire', '{"cost": ["[[main]]", ["1 [[ceremonial:power]]", "1 [[sympathy:power]]"], "1 [[ceremonial:class]]", "1 [[sympathy:class]]"], "dice": ["ceremonial", "sympathy"], "life": 4, "name": "Master Vampire", "stub": "master-vampire", "text": "Blood Drain 1: When a unit is destroyed as a result of this unit''s attack, place 1 status token on this unit.\n\nMesmerize: When this unit becomes blocked or guarded against by a unit, you may remove 1 status token from this unit. If you do, that unit cannot counter for the remainder of this turn.", "type": "Ally", "attack": 3, "weight": 309, "altDice": ["ceremonial", "sympathy"], "recover": 1, "release": {"name": "The Demons of Darmas", "stub": "the-demons-of-darmas", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"sympathy:class": 1, "ceremonial:class": 1, "ceremonial:power / sympathy:power": 1}, "placement": "Battlefield"}', '12', 'Ally', '309', '33', NULL, NULL, 'f', 'Master Vampire
Blood Drain 1 When a unit is destroyed as a result of this unit''s attack, place 1 status token on this unit. Mesmerize When this unit becomes blocked or guarded against by a unit, you may remove 1 status token from this unit. If you do, that unit cannot counter for the remainder of this turn.', '33', '2096', '1', NULL, NULL, 't'),
('232', 'Psychic Vampire', 'psychic-vampire', '{"cost": ["[[main]]", "1 [[ceremonial:power]]"], "dice": ["ceremonial"], "life": 1, "name": "Psychic Vampire", "stub": "psychic-vampire", "text": "Lobotomize 1: When this unit is destroyed as a result of a spell, attack, counter, ability, or dice power an opponent controls, that opponent must discard 1 card of their choice from their hand.", "type": "Ally", "attack": 2, "weight": 107, "recover": 0, "release": {"name": "The Demons of Darmas", "stub": "the-demons-of-darmas", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"ceremonial:power": 1}, "placement": "Battlefield"}', '12', 'Ally', '107', '1', NULL, NULL, 'f', 'Psychic Vampire
Lobotomize 1 When this unit is destroyed as a result of a spell, attack, counter, ability, or dice power an opponent controls, that opponent must discard 1 card of their choice from their hand.', '0', '2097', '1', NULL, NULL, 't'),
('233', 'Summon Vampire Bat Swarm', 'summon-vampire-bat-swarm', '{"cost": ["[[main]]"], "dice": ["ceremonial", "sympathy"], "name": "Summon Vampire Bat Swarm", "stub": "summon-vampire-bat-swarm", "text": "[[main]] - [[exhaust]] - 1 [[ceremonial:class]] - 1 [[sympathy:class]]: Place a [[Vampire Bat Swarm]] conjuration onto your battlefield.", "type": "Ready Spell", "weight": 5, "release": {"name": "The Demons of Darmas", "stub": "the-demons-of-darmas", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "conjurations": [{"name": "Vampire Bat Swarm", "stub": "vampire-bat-swarm"}], "effectMagicCost": {"sympathy:class": 1, "ceremonial:class": 1}}', '12', 'Ready Spell', '5', '33', NULL, NULL, 't', 'Summon Vampire Bat Swarm
Place a Vampire Bat Swarm conjuration onto your battlefield.', '0', '2098', '1', NULL, NULL, 't'),
('234', 'Transmute Magic', 'transmute-magic', '{"cost": ["[[side]]", "1 [[sympathy:class]]", "X [[basic]]"], "dice": ["sympathy"], "name": "Transmute Magic", "stub": "transmute-magic", "text": "Select X dice in your exhausted pool and place them into your active pool on a side of your choice. Change 2 dice in a target player''s active pool to a side of your choice.", "type": "Action Spell", "weight": 105, "release": {"name": "The Demons of Darmas", "stub": "the-demons-of-darmas", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"sympathy:class": 1}, "placement": "Discard"}', '12', 'Action Spell', '105', '32', NULL, NULL, 'f', 'Transmute Magic
Select X dice in your exhausted pool and place them into your active pool on a side of your choice. Change 2 dice in a target player''s active pool to a side of your choice.', '0', '2099', '1', NULL, NULL, 't'),
('235', 'Vampire Bat Swarm', 'vampire-bat-swarm', '{"life": 3, "name": "Vampire Bat Swarm", "stub": "vampire-bat-swarm", "text": "Swarm 2: When this unit would deal damage to a Phoenixborn by attacking, you may instead deal 1 damage to up to 2 target units.\n\n* Relentless: When this unit would receive damage, reduce that damage to 1.\n\n* Fleeting: Discard this card at the end of this round.", "type": "Conjuration", "attack": 2, "copies": 3, "recover": 0, "release": {"name": "The Demons of Darmas", "stub": "the-demons-of-darmas", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '12', 'Conjuration', '0', '0', NULL, '3', 'f', 'Vampire Bat Swarm
Swarm 2 When this unit would deal damage to a Phoenixborn by attacking, you may instead deal 1 damage to up to 2 target units. Relentless When this unit would receive damage, reduce that damage to 1. Fleeting Discard this card at the end of this round.', '0', '2100', '1', NULL, NULL, 't'),
('236', 'Admonisher', 'admonisher', '{"life": 2, "name": "Admonisher", "stub": "admonisher", "text": "Rebuke 1: At the end of each round, deal 1 damage to a target Phoenixborn.", "type": "Conjuration", "attack": 0, "copies": 3, "recover": 0, "release": {"name": "The Spirits of Memoria", "stub": "the-spirits-of-memoria", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '13', 'Conjuration', '0', '0', NULL, '3', 'f', 'Admonisher
Rebuke 1 At the end of each round, deal 1 damage to a target Phoenixborn.', '0', '2101', '1', NULL, NULL, 't'),
('237', 'Angelic Rescue', 'angelic-rescue', '{"cost": ["1 [[illusion:power]]"], "dice": ["illusion"], "name": "Angelic Rescue", "stub": "angelic-rescue", "text": "You may play this spell when an opponent would use a spell, ability, or dice power that targets a unit you control. Cancel the effects of that spell, ability, or dice power. You may spend 1 [[divine:class]] to attach an [[Angel''s Embrace]] conjured alteration spell to that unit.", "type": "Reaction Spell", "weight": 102, "altDice": ["divine"], "release": {"name": "The Spirits of Memoria", "stub": "the-spirits-of-memoria", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"illusion:power": 1}, "placement": "Discard", "conjurations": [{"name": "Angel''s Embrace", "stub": "angels-embrace"}], "effectMagicCost": {"divine:class": 1}}', '13', 'Reaction Spell', '102', '4', NULL, NULL, 'f', 'Angelic Rescue
You may play this spell when an opponent would use a spell, ability, or dice power that targets a unit you control. Cancel the effects of that spell, ability, or dice power. You may spend 1 divine:class to attach an Angel''s Embrace conjured alteration spell to that unit.', '16', '2102', '1', NULL, NULL, 't'),
('238', 'Angel''s Embrace', 'angels-embrace', '{"name": "Angel''s Embrace", "stub": "angels-embrace", "text": "* Fleeting: Discard this card at the end of this round.\n\n* This unit now has the following abilities:\n\n* Magic Guard: This unit cannot be affected by an opponent''s spell.\n\n* Word of Recall: [[side]]: If this unit is an ally, place it into its owner''s hand.", "type": "Conjured Alteration Spell", "copies": 3, "release": {"name": "The Spirits of Memoria", "stub": "the-spirits-of-memoria", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Unit"}', '13', 'Conjured Alteration Spell', '0', '0', NULL, '3', 'f', 'Angel''s Embrace
Fleeting Discard this card at the end of this round. This unit now has the following abilities: Magic Guard This unit cannot be affected by an opponent''s spell. Word of Recall If this unit is an ally, place it into its owner''s hand.', '0', '2103', '1', NULL, NULL, 't'),
('239', 'Celestial Knight', 'celestial-knight', '{"cost": ["[[main]]", "1 [[divine:power]]", "2 [[divine:class]]"], "dice": ["divine"], "life": 3, "name": "Celestial Knight", "stub": "celestial-knight", "text": "* Spiked Skin 2: When this unit is dealt damage by one or more attacking or countering units, deal 2 damage to each unit that is attacking or countering this unit.\n\n* Armored 1: When this unit would receive damage, prevent 1 damage.", "type": "Ally", "attack": 3, "weight": 309, "recover": 2, "release": {"name": "The Spirits of Memoria", "stub": "the-spirits-of-memoria", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"divine:class": 2, "divine:power": 1}, "placement": "Battlefield"}', '13', 'Ally', '309', '16', NULL, NULL, 'f', 'Celestial Knight
Spiked Skin 2 When this unit is dealt damage by one or more attacking or countering units, deal 2 damage to each unit that is attacking or countering this unit. Armored 1 When this unit would receive damage, prevent 1 damage.', '0', '2104', '1', NULL, NULL, 't'),
('240', 'Chained Creations', 'chained-creations', '{"cost": ["[[main]]", "[[side]]", "1 [[illusion:class]]", "1 [[divine:class]]"], "dice": ["illusion", "divine"], "name": "Chained Creations", "stub": "chained-creations", "text": "When an ally is placed into your hand from your discard pile or from your battlefield, you may discard this card. If you do, remove a target conjuration from the game.\n\n* Respark: 1 [[basic]] or 1 [[discard]]", "type": "Ready Spell", "weight": 211, "release": {"name": "The Spirits of Memoria", "stub": "the-spirits-of-memoria", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"divine:class": 1, "illusion:class": 1}, "placement": "Spellboard", "effectMagicCost": {"basic": 1}}', '13', 'Ready Spell', '211', '20', NULL, NULL, 'f', 'Chained Creations
When an ally is placed into your hand from your discard pile or from your battlefield, you may discard this card. If you do, remove a target conjuration from the game. Respark 1 basic or 1 discard', '0', '2105', '1', NULL, NULL, 't'),
('241', 'Gates Thrown Open', 'gates-thrown-open', '{"cost": ["[[main]]", "2 [[illusion:class]]"], "dice": ["illusion"], "name": "Gates Thrown Open", "stub": "gates-thrown-open", "text": "When this spell comes into play, select 4 dice in your exhausted pool and place them onto this spell on a side of your choice.\n\nYou may exhaust dice on this spell as if they were in your active pool when paying the costs of cards in your hand.\n\n* Bound: This card cannot be discarded from your spellboard when you Meditate.", "type": "Ready Spell", "weight": 207, "release": {"name": "The Spirits of Memoria", "stub": "the-spirits-of-memoria", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"illusion:class": 2}, "placement": "Spellboard", "diceRecursion": 4}', '13', 'Ready Spell', '207', '4', NULL, NULL, 'f', 'Gates Thrown Open
When this spell comes into play, select 4 dice in your exhausted pool and place them onto this spell on a side of your choice. You may exhaust dice on this spell as if they were in your active pool when paying the costs of cards in your hand. Bound This card cannot be discarded from your spellboard when you Meditate.', '0', '2106', '1', NULL, NULL, 't'),
('242', 'Law Of Banishment', 'law-of-banishment', '{"cost": ["[[main]]", "1 [[divine:class]]"], "dice": ["divine"], "name": "Law Of Banishment", "stub": "law-of-banishment", "text": "When this spell comes into play, choose a player. That player must place 1 exhaustion token on an unexhausted ready spell they control.\n\nWhen a conjuration leaves play, that conjuration''s controlling player may discard an unexhausted ready spell they control. If they do not or cannot, remove that conjuration from the game.\n\n* Bound: This card cannot be discarded from your spellboard when you Meditate.\n\n* Fleeting: Discard this card at the end of this round.", "type": "Ready Spell", "weight": 106, "release": {"name": "The Spirits of Memoria", "stub": "the-spirits-of-memoria", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"divine:class": 1}, "placement": "Spellboard"}', '13', 'Ready Spell', '106', '16', NULL, NULL, 'f', 'Law Of Banishment
When this spell comes into play, choose a player. That player must place 1 exhaustion token on an unexhausted ready spell they control. When a conjuration leaves play, that conjuration''s controlling player may discard an unexhausted ready spell they control. If they do not or cannot, remove that conjuration from the game. Bound This card cannot be discarded from your spellboard when you Meditate. Fleeting Discard this card at the end of this round.', '0', '2107', '1', NULL, NULL, 't'),
('243', 'Sembali Grimtongue', 'sembali-grimtongue', '{"life": 19, "name": "Sembali Grimtongue", "stub": "sembali-grimtongue", "text": "Ban Manifestation: When a unit you control leaves play, you may discard 1 card from your hand and place 1 exhaustion token on this card to choose a target conjuration an opponent owns. That opponent must remove that conjuration from the game or remove all copies of that conjuration in their conjuration pile from the game.", "type": "Phoenixborn", "release": {"name": "The Spirits of Memoria", "stub": "the-spirits-of-memoria", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "spellboard": 3, "battlefield": 5}', '13', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Sembali Grimtongue
Ban Manifestation When a unit you control leaves play, you may discard 1 card from your hand and place 1 exhaustion token on this card to choose a target conjuration an opponent owns. That opponent must remove that conjuration from the game or remove all copies of that conjuration in their conjuration pile from the game.', '0', '2108', '1', NULL, NULL, 't'),
('244', 'Shadow Guard', 'shadow-guard', '{"cost": ["[[main]]", "2 [[illusion:class]]"], "dice": ["illusion"], "life": 1, "name": "Shadow Guard", "stub": "shadow-guard", "text": "~ Hidden: After an opponent has declared attackers, you may play this unit from your hand without paying its main action cost.\n\nUnit Guard: This unit may guard a unit that is being attacked.", "type": "Ally", "attack": 3, "weight": 207, "recover": 1, "release": {"name": "The Spirits of Memoria", "stub": "the-spirits-of-memoria", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"illusion:class": 2}, "placement": "Battlefield"}', '13', 'Ally', '207', '4', NULL, NULL, 'f', 'Shadow Guard
Hidden After an opponent has declared attackers, you may play this unit from your hand without paying its main action cost. Unit Guard This unit may guard a unit that is being attacked.', '0', '2109', '1', NULL, NULL, 't'),
('245', 'Shepherd Of Lost Souls', 'shepherd-of-lost-souls', '{"cost": ["[[main]]", "[[side]]", "1 [[divine:class]]"], "dice": ["divine"], "life": 1, "name": "Shepherd Of Lost Souls", "stub": "shepherd-of-lost-souls", "text": "Spirit Guide: When this unit comes into play, you may search your discard pile for an ally with a title other than this unit''s title and place it into your hand.", "type": "Ally", "attack": 1, "weight": 110, "recover": 0, "release": {"name": "The Spirits of Memoria", "stub": "the-spirits-of-memoria", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"divine:class": 1}, "placement": "Battlefield"}', '13', 'Ally', '110', '16', NULL, NULL, 'f', 'Shepherd Of Lost Souls
Spirit Guide When this unit comes into play, you may search your discard pile for an ally with a title other than this unit''s title and place it into your hand.', '0', '2110', '1', NULL, NULL, 't'),
('246', 'Spectral Assassin', 'spectral-assassin', '{"life": 1, "name": "Spectral Assassin", "stub": "spectral-assassin", "text": "Spy 1: After this unit deals damage to an opponent''s Phoenixborn by attacking, you may draw 1 card.", "type": "Conjuration", "attack": 2, "copies": 3, "recover": 0, "release": {"name": "The Spirits of Memoria", "stub": "the-spirits-of-memoria", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '13', 'Conjuration', '0', '0', NULL, '3', 'f', 'Spectral Assassin
Spy 1 After this unit deals damage to an opponent''s Phoenixborn by attacking, you may draw 1 card.', '0', '2111', '1', NULL, NULL, 't'),
('247', 'Summon Admonisher', 'summon-admonisher', '{"cost": ["[[main]]"], "dice": ["divine"], "name": "Summon Admonisher", "stub": "summon-admonisher", "text": "[[main]] - [[exhaust]] - 1 [[divine:class]]: Place an [[Admonisher]] conjuration onto your battlefield.\n\nFocus 1: If you cannot, deal 1 damage to a target Phoenixborn.", "type": "Ready Spell", "weight": 5, "release": {"name": "The Spirits of Memoria", "stub": "the-spirits-of-memoria", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "conjurations": [{"name": "Admonisher", "stub": "admonisher"}], "effectMagicCost": {"divine:class": 1}}', '13', 'Ready Spell', '5', '16', NULL, NULL, 't', 'Summon Admonisher
Place an Admonisher conjuration onto your battlefield. Focus 1 If you cannot, deal 1 damage to a target Phoenixborn.', '0', '2112', '1', NULL, NULL, 't'),
('248', 'Summon Spectral Assassin', 'summon-spectral-assassin', '{"cost": ["[[side]]", "1 [[illusion:class]]", "1 [[basic]]"], "dice": ["illusion"], "name": "Summon Spectral Assassin", "stub": "summon-spectral-assassin", "text": "Choose a target ally you control and place it into its owner''s hand. If you do, place a [[Spectral Assassin]] conjuration onto your battlefield. You may draw 1 card.", "type": "Action Spell", "weight": 205, "release": {"name": "The Spirits of Memoria", "stub": "the-spirits-of-memoria", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "illusion:class": 1}, "placement": "Discard", "conjurations": [{"name": "Spectral Assassin", "stub": "spectral-assassin"}]}', '13', 'Action Spell', '205', '4', NULL, NULL, 't', 'Summon Spectral Assassin
Choose a target ally you control and place it into its owner''s hand. If you do, place a Spectral Assassin conjuration onto your battlefield. You may draw 1 card.', '0', '2113', '1', NULL, NULL, 't'),
('249', 'Veil Of Reversal', 'veil-of-reversal', '{"cost": ["2 [[basic]]"], "name": "Veil Of Reversal", "stub": "veil-of-reversal", "text": "You may play this spell when an opponent would use a spell, ability, or dice power that targets you, your draw pile, your discard pile, or your Phoenixborn. Cancel the effects of that spell, ability, or dice power. You may choose a target ally you control and place it into its owner''s hand. If you do, remove a target conjuration from the game.", "type": "Reaction Spell", "weight": 200, "release": {"name": "The Spirits of Memoria", "stub": "the-spirits-of-memoria", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 2}, "placement": "Discard", "phoenixborn": "Sembali Grimtongue"}', '13', 'Reaction Spell', '200', '0', 'Sembali Grimtongue', NULL, 'f', 'Veil Of Reversal
You may play this spell when an opponent would use a spell, ability, or dice power that targets you, your draw pile, your discard pile, or your Phoenixborn. Cancel the effects of that spell, ability, or dice power. You may choose a target ally you control and place it into its owner''s hand. If you do, remove a target conjuration from the game.', '0', '2114', '1', NULL, NULL, 't'),
('250', 'Ancestor Spirit', 'ancestor-spirit', '{"life": 1, "name": "Ancestor Spirit", "stub": "ancestor-spirit", "text": "Distract: [[side]] - [[exhaust]]: Place 1 exhaustion token on a target unit.\n\n* Ephemeral: After this unit becomes exhausted, remove it from the game.", "type": "Conjuration", "attack": 0, "copies": 5, "recover": 0, "release": {"name": "The Ghost Guardian", "stub": "the-ghost-guardian", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '14', 'Conjuration', '0', '0', NULL, '5', 'f', 'Ancestor Spirit
Distract Place 1 exhaustion token on a target unit. Ephemeral After this unit becomes exhausted, remove it from the game.', '0', '3499', '1', NULL, NULL, 't'),
('251', 'Ancestral Army', 'ancestral-army', '{"cost": ["[[main]]", "3 [[basic]]"], "life": 3, "name": "Ancestral Army", "stub": "ancestral-army", "text": "* Dauntless: If this unit receives damage in battle, remove 1 exhaustion token from this unit at the end of that battle.\n\n* Inviolable: This unit cannot be targeted by a spell or have alteration spells attached to it.", "type": "Ally", "attack": 3, "weight": 305, "recover": 0, "release": {"name": "The Ghost Guardian", "stub": "the-ghost-guardian", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 3}, "placement": "Battlefield", "phoenixborn": "Rimea Careworn"}', '14', 'Ally', '305', '0', 'Rimea Careworn', NULL, 'f', 'Ancestral Army
Dauntless If this unit receives damage in battle, remove 1 exhaustion token from this unit at the end of that battle. Inviolable This unit cannot be targeted by a spell or have alteration spells attached to it.', '0', '3500', '1', NULL, NULL, 't'),
('252', 'Augury', 'augury', '{"cost": ["[[main]]", "1 [[sympathy:class]]"], "dice": ["sympathy"], "name": "Augury", "stub": "augury", "text": "* When this spell comes into play, place 3 status tokens on it. Discard this card when it no longer has any status tokens on it.\n\n[[side]] - [[exhaust]] - 1 [[basic]]: Search your draw pile for 1 card with a magic play cost of X, reveal it, and place it into your hand. Shuffle your draw pile. Remove 1 status token from this spell.\n\n* X = the number of status tokens on this spell.\n\n* Bound: This card cannot be discarded from your spellboard when you Meditate.", "type": "Ready Spell", "weight": 106, "release": {"name": "The Ghost Guardian", "stub": "the-ghost-guardian", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"sympathy:class": 1}, "placement": "Spellboard", "effectMagicCost": {"basic": 1}}', '14', 'Ready Spell', '106', '32', NULL, NULL, 'f', 'Augury
When this spell comes into play, place 3 status tokens on it. Discard this card when it no longer has any status tokens on it. Search your draw pile for 1 card with a magic play cost of X, reveal it, and place it into your hand. Shuffle your draw pile. Remove 1 status token from this spell. X = the number of status tokens on this spell. Bound This card cannot be discarded from your spellboard when you Meditate.', '0', '3501', '1', NULL, NULL, 't'),
('253', 'Battle Seer', 'battle-seer', '{"cost": ["[[main]]", "1 [[illusion:power]]", "1 [[sympathy:class]]", "1 [[basic]]"], "dice": ["illusion", "sympathy"], "life": 3, "name": "Battle Seer", "stub": "battle-seer", "text": "Battle Trance: When this unit is declared as an attacker or leaves play, you may draw 1 card.", "type": "Ally", "attack": 3, "weight": 308, "recover": 1, "release": {"name": "The Ghost Guardian", "stub": "the-ghost-guardian", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "illusion:power": 1, "sympathy:class": 1}, "placement": "Battlefield"}', '14', 'Ally', '308', '36', NULL, NULL, 'f', 'Battle Seer
Battle Trance When this unit is declared as an attacker or leaves play, you may draw 1 card.', '0', '3502', '1', NULL, NULL, 't'),
('254', 'Dark Presence', 'dark-presence', '{"cost": ["[[main]]", "1 [[sympathy:class]]"], "dice": ["sympathy"], "name": "Dark Presence", "stub": "dark-presence", "text": "* All units you control now have the following ability:\n\n* Fog of War: When this unit deals damage to an opponent''s Phoenixborn, that opponent places the top card of their draw pile on the bottom of their draw pile. Then, that opponent discards the top card of their draw pile.\n\nFocus 1: [[main]] or [[side]] - 1 [[basic]] - [[exhaust]]: Place 1 exhaustion token on an unexhausted unit you control. That unit deals 1 damage to a Phoenixborn.\n\nFocus 2: You may remove 1 token from that unit.", "type": "Ready Spell", "weight": 106, "release": {"name": "The Ghost Guardian", "stub": "the-ghost-guardian", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"sympathy:class": 1}, "placement": "Spellboard", "effectMagicCost": {"basic": 1}}', '14', 'Ready Spell', '106', '32', NULL, NULL, 'f', 'Dark Presence
All units you control now have the following ability: Fog of War When this unit deals damage to an opponent''s Phoenixborn, that opponent places the top card of their draw pile on the bottom of their draw pile. Then, that opponent discards the top card of their draw pile. Focus 1 Place 1 exhaustion token on an unexhausted unit you control. That unit deals 1 damage to a Phoenixborn. Focus 2 You may remove 1 token from that unit.', '0', '3503', '1', NULL, NULL, 't'),
('255', 'Hex Bane', 'hex-bane', '{"cost": ["[[main]]", "1 [[sympathy:class]]"], "dice": ["sympathy"], "name": "Hex Bane", "stub": "hex-bane", "text": "After an opponent uses an ability or dice power to place a die into your exhausted pool, you may place 1 exhaustion token on this spell to select 1 die in that opponent''s active pool and place it in that opponent''s exhausted pool. After an opponent uses an ability or dice power to deal damage to a unit or Phoenixborn you control, you may place 1 exhaustion token on this spell to deal 1 damage to that opponent''s Phoenixborn.", "type": "Ready Spell", "weight": 106, "release": {"name": "The Ghost Guardian", "stub": "the-ghost-guardian", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"sympathy:class": 1}, "placement": "Spellboard"}', '14', 'Ready Spell', '106', '32', NULL, NULL, 'f', 'Hex Bane
After an opponent uses an ability or dice power to place a die into your exhausted pool, you may place 1 exhaustion token on this spell to select 1 die in that opponent''s active pool and place it in that opponent''s exhausted pool. After an opponent uses an ability or dice power to deal damage to a unit or Phoenixborn you control, you may place 1 exhaustion token on this spell to deal 1 damage to that opponent''s Phoenixborn.', '0', '3504', '1', NULL, NULL, 't'),
('256', 'Hollow', 'hollow', '{"cost": ["[[main]]", ["1 [[sympathy:class]]", "1 [[illusion:class]]"]], "life": 1, "name": "Hollow", "stub": "hollow", "text": "Possession: When this unit leaves play as a result of a spell, ability, or dice power you control, you may spend 1 [[sympathy:power]] to remove all exhaustion tokens from a target unit you control.\n\n~ Poltergeist: After a player has declared attackers, you may spend 1 [[illusion:power]] to remove this card from the game. If you do, reduce the attack value of a target unit by 2 for the remainder of this turn.", "type": "Ally", "attack": 2, "weight": 106, "altDice": ["sympathy", "illusion"], "recover": 0, "release": {"name": "The Ghost Guardian", "stub": "the-ghost-guardian", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"sympathy:class / illusion:class": 1}, "placement": "Battlefield", "effectMagicCost": {"illusion:power": 1, "sympathy:power": 1}}', '14', 'Ally', '106', '0', NULL, NULL, 'f', 'Hollow
Possession When this unit leaves play as a result of a spell, ability, or dice power you control, you may spend 1 sympathy:power to remove all exhaustion tokens from a target unit you control. Poltergeist After a player has declared attackers, you may spend 1 illusion:power to remove this card from the game. If you do, reduce the attack value of a target unit by 2 for the remainder of this turn.', '36', '3505', '1', NULL, NULL, 't'),
('257', 'Nightmare Mount', 'nightmare-mount', '{"life": 3, "name": "Nightmare Mount", "stub": "nightmare-mount", "text": "Terrifying 2: This unit cannot be blocked or guarded against by units with an attack value of 2 or less.\n\n* Unsummon: [[main]]: Discard this unit.\n\n* Dismount Rider: After this unit leaves play, choose a face down ally that was under this unit and dismount that ally.", "type": "Conjuration", "attack": 4, "copies": 2, "recover": 0, "release": {"name": "The Ghost Guardian", "stub": "the-ghost-guardian", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '14', 'Conjuration', '0', '0', NULL, '2', 'f', 'Nightmare Mount
Terrifying 2 This unit cannot be blocked or guarded against by units with an attack value of 2 or less. Unsummon Discard this unit. Dismount Rider After this unit leaves play, choose a face down ally that was under this unit and dismount that ally.', '0', '3506', '1', NULL, NULL, 't'),
('258', 'Pale Steed Mount', 'pale-steed-mount', '{"life": 4, "name": "Pale Steed Mount", "stub": "pale-steed-mount", "text": "Unit Guard: This unit may guard a unit that is being attacked.\n\n* Unsummon: [[main]]: Discard this unit.\n\n* Dismount Rider: After this unit leaves play, choose a face down ally that was under this unit and dismount that ally.", "type": "Conjuration", "attack": 2, "copies": 2, "recover": 0, "release": {"name": "The Ghost Guardian", "stub": "the-ghost-guardian", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '14', 'Conjuration', '0', '0', NULL, '2', 'f', 'Pale Steed Mount
Unit Guard This unit may guard a unit that is being attacked. Unsummon Discard this unit. Dismount Rider After this unit leaves play, choose a face down ally that was under this unit and dismount that ally.', '0', '3507', '1', NULL, NULL, 't'),
('259', 'Resonance', 'resonance', '{"cost": ["[[side]]", "2 [[sympathy:class]]", "1 [[basic]]"], "dice": ["sympathy"], "name": "Resonance", "stub": "resonance", "text": "When this spell comes into play, select 2 dice in your exhausted pool and place them into your active pool on a side of your choice.\n\nWhen you play this spell, place it face up under a ready spell on your spellboard. While this card is on your spellboard, all other cards in its spellboard slot are focused one additional time.", "type": "Ready Spell", "weight": 306, "release": {"name": "The Ghost Guardian", "stub": "the-ghost-guardian", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "sympathy:class": 2}, "placement": "Spellboard", "diceRecursion": 2}', '14', 'Ready Spell', '306', '32', NULL, NULL, 'f', 'Resonance
When this spell comes into play, select 2 dice in your exhausted pool and place them into your active pool on a side of your choice. When you play this spell, place it face up under a ready spell on your spellboard. While this card is on your spellboard, all other cards in its spellboard slot are focused one additional time.', '0', '3508', '1', NULL, NULL, 't'),
('260', 'Rimea Careworn', 'rimea-careworn', '{"life": 20, "name": "Rimea Careworn", "stub": "rimea-careworn", "text": "Visions: [[side]]: Look at the top 3 cards of a target draw pile. You may spend 1 [[basic]] and place 1 exhaustion token on this card to place 1 of those cards on the bottom of that draw pile. Place the remaining looked at cards on the top of that draw pile in the order of your choice.", "type": "Phoenixborn", "release": {"name": "The Ghost Guardian", "stub": "the-ghost-guardian", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "spellboard": 5, "battlefield": 4, "effectMagicCost": {"basic": 1}}', '14', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Rimea Careworn
Visions Look at the top 3 cards of a target draw pile. You may spend 1 basic and place 1 exhaustion token on this card to place 1 of those cards on the bottom of that draw pile. Place the remaining looked at cards on the top of that draw pile in the order of your choice.', '0', '3509', '1', NULL, NULL, 't'),
('261', 'Shared Sorrow', 'shared-sorrow', '{"cost": ["[[main]]", "1 [[sympathy:class]]", "1 [[basic]]"], "dice": ["sympathy"], "name": "Shared Sorrow", "stub": "shared-sorrow", "text": "Discard 1 card from your hand with a magic play cost of 1 or more. Search your discard pile for another card with a magic play cost of X and place it into your hand. Deal X damage to a target unit.\n\nX = the magic play cost of the discarded card.", "type": "Action Spell", "weight": 206, "release": {"name": "The Ghost Guardian", "stub": "the-ghost-guardian", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "sympathy:class": 1}, "placement": "Discard"}', '14', 'Action Spell', '206', '32', NULL, NULL, 'f', 'Shared Sorrow
Discard 1 card from your hand with a magic play cost of 1 or more. Search your discard pile for another card with a magic play cost of X and place it into your hand. Deal X damage to a target unit. X = the magic play cost of the discarded card.', '0', '3510', '1', NULL, NULL, 't'),
('262', 'Spectral Charger Mount', 'spectral-charger-mount', '{"life": 2, "name": "Spectral Charger Mount", "stub": "spectral-charger-mount", "text": "Battle Advantage: When this unit is in battle, it deals its damage before other units without Battle Advantage deal their damage.\n\n* Unsummon: [[main]]: Discard this unit.\n\n* Dismount Rider: After this unit leaves play, choose a face down ally that was under this unit and dismount that ally.", "type": "Conjuration", "attack": 3, "copies": 2, "recover": 0, "release": {"name": "The Ghost Guardian", "stub": "the-ghost-guardian", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '14', 'Conjuration', '0', '0', NULL, '2', 'f', 'Spectral Charger Mount
Battle Advantage When this unit is in battle, it deals its damage before other units without Battle Advantage deal their damage. Unsummon Discard this unit. Dismount Rider After this unit leaves play, choose a face down ally that was under this unit and dismount that ally.', '0', '3511', '1', NULL, NULL, 't'),
('263', 'Summon Ancestor Spirit', 'summon-ancestor-spirit', '{"cost": ["[[main]]", "1 [[illusion:class]]", "1 [[basic]]"], "dice": ["illusion"], "name": "Summon Ancestor Spirit", "stub": "summon-ancestor-spirit", "text": "[[main]] - [[exhaust]]: Discard 1 card from your hand or move 1 die from your active pool to your exhausted pool. If you do, draw 1 card or place an [[Ancestor Spirit]] conjuration onto your battlefield.", "type": "Ready Spell", "weight": 206, "release": {"name": "The Ghost Guardian", "stub": "the-ghost-guardian", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "illusion:class": 1}, "placement": "Spellboard", "conjurations": [{"name": "Ancestor Spirit", "stub": "ancestor-spirit"}]}', '14', 'Ready Spell', '206', '4', NULL, NULL, 't', 'Summon Ancestor Spirit
Discard 1 card from your hand or move 1 die from your active pool to your exhausted pool. If you do, draw 1 card or place an Ancestor Spirit conjuration onto your battlefield.', '0', '3512', '1', NULL, NULL, 't'),
('264', 'Summon Ghostly Mount', 'summon-ghostly-mount', '{"cost": ["[[main]]", "1 [[basic]]"], "dice": ["illusion", "sympathy"], "name": "Summon Ghostly Mount", "stub": "summon-ghostly-mount", "text": "[[main]] or [[side]] - [[exhaust]] - 1 [[illusion:class]] - 1 [[sympathy:class]]: Remove an unexhausted ally you control from play. If you do, place a [[Pale Steed Mount]] or [[Spectral Charger Mount]] conjuration onto your battlefield and place that ally face down under that unit.\n\nFocus 2: You may place a [[Nightmare Mount]] conjuration instead.", "type": "Ready Spell", "weight": 105, "release": {"name": "The Ghost Guardian", "stub": "the-ghost-guardian", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1}, "placement": "Spellboard", "conjurations": [{"name": "Pale Steed Mount", "stub": "pale-steed-mount"}, {"name": "Spectral Charger Mount", "stub": "spectral-charger-mount"}, {"name": "Nightmare Mount", "stub": "nightmare-mount"}], "effectMagicCost": {"illusion:class": 1, "sympathy:class": 1}}', '14', 'Ready Spell', '105', '36', NULL, NULL, 't', 'Summon Ghostly Mount
Remove an unexhausted ally you control from play. If you do, place a Pale Steed Mount or Spectral Charger Mount conjuration onto your battlefield and place that ally face down under that unit. Focus 2 You may place a Nightmare Mount conjuration instead.', '0', '3513', '1', NULL, NULL, 't'),
('265', 'Archasaurus Mount', 'archasaurus-mount', '{"life": 5, "name": "Archasaurus Mount", "stub": "archasaurus-mount", "text": "Gigantic 2: This unit cannot be blocked or guarded against by units with a life value of 2 or less.\n\n* Unsummon: [[main]]: Discard this unit.\n\n* Dismount Rider: After this unit leaves play, choose a face down ally that was under this unit and dismount that ally.", "type": "Conjuration", "attack": 4, "copies": 1, "recover": 0, "release": {"name": "The King of Titans", "stub": "the-king-of-titans", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '15', 'Conjuration', '0', '0', NULL, '1', 'f', 'Archasaurus Mount
Gigantic 2 This unit cannot be blocked or guarded against by units with a life value of 2 or less. Unsummon Discard this unit. Dismount Rider After this unit leaves play, choose a face down ally that was under this unit and dismount that ally.', '0', '3514', '1', NULL, NULL, 't'),
('266', 'Cerasaurus Mount', 'cerasaurus-mount', '{"life": 3, "name": "Cerasaurus Mount", "stub": "cerasaurus-mount", "text": "Overkill 1: When this unit destroys a unit an opponent controls by attacking, deal 1 damage to that opponent''s Phoenixborn.\n\n* Unsummon: [[main]]: Discard this unit.\n\n* Dismount Rider: After this unit leaves play, choose a face down ally that was under this unit and dismount that ally.", "type": "Conjuration", "attack": 3, "copies": 3, "recover": 0, "release": {"name": "The King of Titans", "stub": "the-king-of-titans", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '15', 'Conjuration', '0', '0', NULL, '3', 'f', 'Cerasaurus Mount
Overkill 1 When this unit destroys a unit an opponent controls by attacking, deal 1 damage to that opponent''s Phoenixborn. Unsummon Discard this unit. Dismount Rider After this unit leaves play, choose a face down ally that was under this unit and dismount that ally.', '0', '3515', '1', NULL, NULL, 't'),
('267', 'Earthquake', 'earthquake', '{"cost": ["[[main]]", "2 [[basic]]"], "name": "Earthquake", "stub": "earthquake", "text": "Deal 4 damage to a target unit and 1 damage to each other unit.", "type": "Action Spell", "weight": 205, "release": {"name": "The King of Titans", "stub": "the-king-of-titans", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 2}, "placement": "Discard", "phoenixborn": "Xander Heartsblood"}', '15', 'Action Spell', '205', '0', 'Xander Heartsblood', NULL, 'f', 'Earthquake
Deal 4 damage to a target unit and 1 damage to each other unit.', '0', '3516', '1', NULL, NULL, 't'),
('268', 'Law Of Domination', 'law-of-domination', '{"cost": ["[[main]]", "1 [[divine:class]]"], "dice": ["divine"], "name": "Law Of Domination", "stub": "law-of-domination", "text": "When this spell comes into play, choose an opponent to choose a unit they control. Then, choose a unit you control. Those units deal damage to each other equal to their attack value.\n\nThis damage, and damage from attacking or countering, cannot be prevented.\n\n* Bound: This card cannot be discarded from your spellboard when you Meditate.\n\n* Fleeting: Discard this card at the end of this round.", "type": "Ready Spell", "weight": 106, "release": {"name": "The King of Titans", "stub": "the-king-of-titans", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"divine:class": 1}, "placement": "Spellboard"}', '15', 'Ready Spell', '106', '16', NULL, NULL, 'f', 'Law Of Domination
When this spell comes into play, choose an opponent to choose a unit they control. Then, choose a unit you control. Those units deal damage to each other equal to their attack value. This damage, and damage from attacking or countering, cannot be prevented. Bound This card cannot be discarded from your spellboard when you Meditate. Fleeting Discard this card at the end of this round.', '0', '3517', '1', NULL, NULL, 't'),
('269', 'Mass Heal', 'mass-heal', '{"cost": ["[[side]]"], "name": "Mass Heal", "stub": "mass-heal", "text": "Remove 1 wound token from all units. If you have a divine die on its class or power side in your active pool, you may instead remove 1 wound token from your Phoenixborn and all units you control.", "type": "Action Spell", "weight": 4, "release": {"name": "The King of Titans", "stub": "the-king-of-titans", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Discard"}', '15', 'Action Spell', '4', '0', NULL, NULL, 'f', 'Mass Heal
Remove 1 wound token from all units. If you have a divine die on its class or power side in your active pool, you may instead remove 1 wound token from your Phoenixborn and all units you control.', '0', '3518', '1', NULL, NULL, 't'),
('270', 'Nature''s Wrath', 'natures-wrath', '{"cost": ["[[main]]", "1 [[natural:class]]"], "dice": ["natural"], "name": "Nature''s Wrath", "stub": "natures-wrath", "text": "Deal 1 damage to all units.", "type": "Action Spell", "weight": 106, "release": {"name": "The King of Titans", "stub": "the-king-of-titans", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"natural:class": 1}, "placement": "Discard"}', '15', 'Action Spell', '106', '8', NULL, NULL, 'f', 'Nature''s Wrath
Deal 1 damage to all units.', '0', '3519', '1', NULL, NULL, 't'),
('271', 'Pain Shaman', 'pain-shaman', '{"cost": ["[[main]]", "1 [[divine:power]]", "1 [[natural:class]]", "1 [[basic]]"], "dice": ["divine", "natural"], "life": 3, "name": "Pain Shaman", "stub": "pain-shaman", "text": "Exchange Pain 1: After this unit receives damage, you may deal 1 damage to a target unit or remove 1 wound token from a target unit.", "type": "Ally", "attack": 2, "weight": 308, "recover": 3, "release": {"name": "The King of Titans", "stub": "the-king-of-titans", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "divine:power": 1, "natural:class": 1}, "placement": "Battlefield"}', '15', 'Ally', '308', '24', NULL, NULL, 'f', 'Pain Shaman
Exchange Pain 1 After this unit receives damage, you may deal 1 damage to a target unit or remove 1 wound token from a target unit.', '0', '3520', '1', NULL, NULL, 't'),
('272', 'Raptor Hatchling', 'raptor-hatchling', '{"life": 1, "name": "Raptor Hatchling", "stub": "raptor-hatchling", "text": "Group Tactics 2: After you declare 3 or more attackers, you may add 2 to this unit''s attack value for the remainder of this turn.", "type": "Conjuration", "attack": 0, "copies": 3, "recover": 0, "release": {"name": "The King of Titans", "stub": "the-king-of-titans", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '15', 'Conjuration', '0', '0', NULL, '3', 'f', 'Raptor Hatchling
Group Tactics 2 After you declare 3 or more attackers, you may add 2 to this unit''s attack value for the remainder of this turn.', '0', '3521', '1', NULL, NULL, 't'),
('273', 'Raptor Herder', 'raptor-herder', '{"cost": ["[[main]]", ["1 [[natural:class]]", "1 [[sympathy:class]]"]], "life": 1, "name": "Raptor Herder", "stub": "raptor-herder", "text": "Call Raptor Hatchling: When this unit comes into play, place a [[Raptor Hatchling]] conjuration onto your battlefield.", "type": "Ally", "attack": 1, "weight": 106, "altDice": ["natural", "sympathy"], "recover": 1, "release": {"name": "The King of Titans", "stub": "the-king-of-titans", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"natural:class / sympathy:class": 1}, "placement": "Battlefield", "conjurations": [{"name": "Raptor Hatchling", "stub": "raptor-hatchling"}]}', '15', 'Ally', '106', '0', NULL, NULL, 'f', 'Raptor Herder
Call Raptor Hatchling When this unit comes into play, place a Raptor Hatchling conjuration onto your battlefield.', '40', '3522', '1', NULL, NULL, 't'),
('274', 'Sacred Ground', 'sacred-ground', '{"cost": ["[[main]]", "1 [[divine:power]]"], "dice": ["divine"], "name": "Sacred Ground", "stub": "sacred-ground", "text": "When an opponent would use a spell that affects all units or each unexhausted unit, you may discard this spell. If you do, cancel the effects of that spell.\n\nAfter a player has declared attackers, you may place 1 exhaustion token on this spell to have all units gain the following ability for the remainder of this turn:\n\n* Armored 1: When this unit would receive damage, prevent 1 damage.", "type": "Ready Spell", "weight": 107, "release": {"name": "The King of Titans", "stub": "the-king-of-titans", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"divine:power": 1}, "placement": "Spellboard"}', '15', 'Ready Spell', '107', '16', NULL, NULL, 'f', 'Sacred Ground
When an opponent would use a spell that affects all units or each unexhausted unit, you may discard this spell. If you do, cancel the effects of that spell. After a player has declared attackers, you may place 1 exhaustion token on this spell to have all units gain the following ability for the remainder of this turn: Armored 1 When this unit would receive damage, prevent 1 damage.', '0', '3523', '1', NULL, NULL, 't'),
('275', 'Shining Hydra', 'shining-hydra', '{"life": 3, "name": "Shining Hydra", "stub": "shining-hydra", "text": "Regenerate Heads: After 1 or more wound tokens are placed on this unit as a result of damage, if this unit is not destroyed, attach a [[Shining Hydra Head]] conjured alteration spell to this unit.", "type": "Conjuration", "attack": 3, "copies": 3, "recover": 0, "release": {"name": "The King of Titans", "stub": "the-king-of-titans", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield", "conjurations": [{"name": "Shining Hydra Head", "stub": "shining-hydra-head"}]}', '15', 'Conjuration', '0', '0', NULL, '3', 'f', 'Shining Hydra
Regenerate Heads After 1 or more wound tokens are placed on this unit as a result of damage, if this unit is not destroyed, attach a Shining Hydra Head conjured alteration spell to this unit.', '0', '3524', '1', NULL, NULL, 't'),
('276', 'Shining Hydra Head', 'shining-hydra-head', '{"life": "+1", "name": "Shining Hydra Head", "stub": "shining-hydra-head", "text": "This unit now has the following ability:\n\nTerrifying 1: This unit cannot be blocked or guarded against by units with an attack value of 1 or less.\n\n* Fleeting: Discard this card at the end of this round.", "type": "Conjured Alteration Spell", "attack": "+1", "copies": 7, "recover": "+1", "release": {"name": "The King of Titans", "stub": "the-king-of-titans", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Unit"}', '15', 'Conjured Alteration Spell', '0', '0', NULL, '7', 'f', 'Shining Hydra Head
This unit now has the following ability: Terrifying 1 This unit cannot be blocked or guarded against by units with an attack value of 1 or less. Fleeting Discard this card at the end of this round.', '0', '3525', '1', NULL, NULL, 't'),
('277', 'Summon Archasaurus Mount', 'summon-archasaurus-mount', '{"cost": ["[[main]]", "[[side]]", "1 [[divine:class]]", "1 [[natural:class]]", "1 [[basic]]"], "dice": ["divine", "natural"], "name": "Summon Archasaurus Mount", "stub": "summon-archasaurus-mount", "text": "Remove an unexhausted ally you control from play. If you do, place an [[Archasaurus Mount]] conjuration onto your battlefield and place that ally face down under that unit.", "type": "Action Spell", "weight": 311, "release": {"name": "The King of Titans", "stub": "the-king-of-titans", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "divine:class": 1, "natural:class": 1}, "placement": "Discard", "conjurations": [{"name": "Archasaurus Mount", "stub": "archasaurus-mount"}]}', '15', 'Action Spell', '311', '24', NULL, NULL, 't', 'Summon Archasaurus Mount
Remove an unexhausted ally you control from play. If you do, place an Archasaurus Mount conjuration onto your battlefield and place that ally face down under that unit.', '0', '3526', '1', NULL, NULL, 't'),
('278', 'Summon Cerasaurus Mount', 'summon-cerasaurus-mount', '{"cost": ["[[main]]", "1 [[basic]]"], "dice": ["natural", "divine"], "name": "Summon Cerasaurus Mount", "stub": "summon-cerasaurus-mount", "text": "[[side]] - [[exhaust]] - 1 [[natural:class]] - 1 [[divine:class]]: Remove an unexhausted ally you control from play. If you do, place a [[Cerasaurus Mount]] conjuration onto your battlefield and place that ally face down under that unit.", "type": "Ready Spell", "weight": 105, "release": {"name": "The King of Titans", "stub": "the-king-of-titans", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1}, "placement": "Spellboard", "conjurations": [{"name": "Cerasaurus Mount", "stub": "cerasaurus-mount"}], "effectMagicCost": {"divine:class": 1, "natural:class": 1}}', '15', 'Ready Spell', '105', '24', NULL, NULL, 't', 'Summon Cerasaurus Mount
Remove an unexhausted ally you control from play. If you do, place a Cerasaurus Mount conjuration onto your battlefield and place that ally face down under that unit.', '0', '3527', '1', NULL, NULL, 't'),
('279', 'Summon Shining Hydra', 'summon-shining-hydra', '{"cost": ["[[main]]", "1 [[divine:class]]", "1 [[natural:class]]", "1 [[basic]]"], "dice": ["divine", "natural"], "name": "Summon Shining Hydra", "stub": "summon-shining-hydra", "text": "Place a [[Shining Hydra]] conjuration onto your battlefield.", "type": "Action Spell", "weight": 307, "release": {"name": "The King of Titans", "stub": "the-king-of-titans", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "divine:class": 1, "natural:class": 1}, "placement": "Discard", "conjurations": [{"name": "Shining Hydra", "stub": "shining-hydra"}]}', '15', 'Action Spell', '307', '24', NULL, NULL, 't', 'Summon Shining Hydra
Place a Shining Hydra conjuration onto your battlefield.', '0', '3528', '1', NULL, NULL, 't'),
('280', 'Xander Heartsblood', 'xander-heartsblood', '{"dice": ["divine"], "life": 20, "name": "Xander Heartsblood", "stub": "xander-heartsblood", "text": "Reincarnate: [[side]] - [[exhaust]] - 1 [[divine:class]]: Search your discard pile for an ally and place it into your hand.", "type": "Phoenixborn", "release": {"name": "The King of Titans", "stub": "the-king-of-titans", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "spellboard": 3, "battlefield": 6, "effectMagicCost": {"divine:class": 1}}', '15', 'Phoenixborn', '0', '16', NULL, NULL, 'f', 'Xander Heartsblood
Reincarnate Search your discard pile for an ally and place it into your hand.', '0', '3529', '1', NULL, NULL, 't'),
('281', 'Cognitive Dissonance', 'cognitive-dissonance', '{"cost": ["1 [[charm:class]]"], "dice": ["charm"], "name": "Cognitive Dissonance", "stub": "cognitive-dissonance", "text": "You may play this spell after an opponent draws 1 or more cards or places 1 or more cards into their hand. That opponent discards 3 cards off the top of their draw pile. Then, remove up to 3 spells in each player''s discard pile from the game.", "type": "Reaction Spell", "weight": 101, "release": {"name": "The Protector of Argaia", "stub": "the-protector-of-argaia", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"charm:class": 1}, "placement": "Discard"}', '16', 'Reaction Spell', '101', '2', NULL, NULL, 'f', 'Cognitive Dissonance
You may play this spell after an opponent draws 1 or more cards or places 1 or more cards into their hand. That opponent discards 3 cards off the top of their draw pile. Then, remove up to 3 spells in each player''s discard pile from the game.', '0', '4694', '1', NULL, NULL, 't'),
('282', 'Confusion Spores', 'confusion-spores', '{"cost": ["[[main]]", "1 [[charm:class]]"], "dice": ["charm"], "name": "Confusion Spores", "stub": "confusion-spores", "text": "[[side]] - [[exhaust]]: Target unit cannot block or guard for the remainder of this turn.\n\nFocus 1: You may spend an additional 1 [[sympathy:class]] to take 1 additional side action ([[side]]) this turn.", "type": "Ready Spell", "weight": 106, "altDice": ["sympathy"], "release": {"name": "The Protector of Argaia", "stub": "the-protector-of-argaia", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"charm:class": 1}, "placement": "Spellboard", "effectMagicCost": {"sympathy:class": 1}}', '16', 'Ready Spell', '106', '2', NULL, NULL, 'f', 'Confusion Spores
Target unit cannot block or guard for the remainder of this turn. Focus 1 You may spend an additional 1 sympathy:class to take 1 additional side action (side) this turn.', '32', '4695', '1', NULL, NULL, 't');
INSERT INTO "public"."card" ("id", "name", "stub", "json", "release_id", "card_type", "cost_weight", "dice_flags", "phoenixborn", "copies", "is_summon_spell", "search_text", "alt_dice_flags", "entity_id", "version", "artist_name", "artist_url", "is_legacy") VALUES
('283', 'Essence Druid', 'essence-druid', '{"cost": ["[[main]]", "2 [[sympathy:class]]", "1 [[basic]]"], "dice": ["sympathy"], "life": 4, "name": "Essence Druid", "stub": "essence-druid", "text": "Spell Recall: When this unit comes into play, search your discard pile for a ready spell and place it into your hand.\n\nCalm the Beast: While this unit is in battle, reduce the attack value of all units in battle with this unit that you do not control by 4.", "type": "Ally", "attack": 1, "weight": 307, "recover": 1, "release": {"name": "The Protector of Argaia", "stub": "the-protector-of-argaia", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "sympathy:class": 2}, "placement": "Battlefield"}', '16', 'Ally', '307', '32', NULL, NULL, 'f', 'Essence Druid
Spell Recall When this unit comes into play, search your discard pile for a ready spell and place it into your hand. Calm the Beast While this unit is in battle, reduce the attack value of all units in battle with this unit that you do not control by 4.', '0', '4696', '1', NULL, NULL, 't'),
('284', 'Exhortation', 'exhortation', '{"cost": ["[[side]]", "1 [[charm:class]]", "1 [[sympathy:class]]"], "dice": ["charm", "sympathy"], "name": "Exhortation", "stub": "exhortation", "text": "Choose 2 units you control. For each unit, add the other unit''s current attack value to its attack value for the remainder of this turn.", "type": "Action Spell", "weight": 206, "release": {"name": "The Protector of Argaia", "stub": "the-protector-of-argaia", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"charm:class": 1, "sympathy:class": 1}, "placement": "Discard"}', '16', 'Action Spell', '206', '34', NULL, NULL, 'f', 'Exhortation
Choose 2 units you control. For each unit, add the other unit''s current attack value to its attack value for the remainder of this turn.', '0', '4697', '1', NULL, NULL, 't'),
('285', 'Fiona Mercywind', 'fiona-mercywind', '{"life": 15, "name": "Fiona Mercywind", "stub": "fiona-mercywind", "text": "Ingenuity: [[side]] - [[exhaust]] - 1 [[discard]]: Draw 1 card or remove 1 exhaustion token from a ready spell you control.", "type": "Phoenixborn", "release": {"name": "The Protector of Argaia", "stub": "the-protector-of-argaia", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "spellboard": 5, "battlefield": 6}', '16', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Fiona Mercywind
Ingenuity Draw 1 card or remove 1 exhaustion token from a ready spell you control.', '0', '4698', '1', NULL, NULL, 't'),
('286', 'Majestic Titan', 'majestic-titan', '{"life": 6, "name": "Majestic Titan", "stub": "majestic-titan", "text": "Gigantic 2: This unit cannot be blocked or guarded against by units with a life value of 2 or less.\n\nBefuddling Blow: When this unit deals damage to a unit, you may force that unit to deal damage equal to its attack value to a target unit of your choice other than itself.", "type": "Conjuration", "attack": 2, "copies": 1, "recover": 3, "release": {"name": "The Protector of Argaia", "stub": "the-protector-of-argaia", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '16', 'Conjuration', '0', '0', NULL, '1', 'f', 'Majestic Titan
Gigantic 2 This unit cannot be blocked or guarded against by units with a life value of 2 or less. Befuddling Blow When this unit deals damage to a unit, you may force that unit to deal damage equal to its attack value to a target unit of your choice other than itself.', '0', '4699', '1', NULL, NULL, 't'),
('287', 'Mind Fog Owl', 'mind-fog-owl', '{"life": 2, "name": "Mind Fog Owl", "stub": "mind-fog-owl", "text": "Unseen: This unit cannot be blocked unless all attacking units without the Unseen ability have been blocked.", "type": "Conjuration", "attack": 2, "copies": 2, "recover": 0, "release": {"name": "The Protector of Argaia", "stub": "the-protector-of-argaia", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '16', 'Conjuration', '0', '0', NULL, '2', 'f', 'Mind Fog Owl
Unseen This unit cannot be blocked unless all attacking units without the Unseen ability have been blocked.', '0', '4700', '1', NULL, NULL, 't'),
('288', 'Mind Maze', 'mind-maze', '{"cost": ["[[main]]", "1 [[basic]]"], "name": "Mind Maze", "stub": "mind-maze", "text": "This unit cannot attack, block, or guard.\n\nWhen this spell would leave play, discard this unit unless its controlling player spends 1 [[basic]].\n\n* Fleeting: Discard this card at the end of this round.", "type": "Alteration Spell", "weight": 105, "release": {"name": "The Protector of Argaia", "stub": "the-protector-of-argaia", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1}, "placement": "Unit", "phoenixborn": "Fiona Mercywind", "effectMagicCost": {"basic": 1}}', '16', 'Alteration Spell', '105', '0', 'Fiona Mercywind', NULL, 'f', 'Mind Maze
This unit cannot attack, block, or guard. When this spell would leave play, discard this unit unless its controlling player spends 1 basic. Fleeting Discard this card at the end of this round.', '0', '4701', '1', NULL, NULL, 't'),
('289', 'New Ideas', 'new-ideas', '{"cost": [["[[main]]", "[[side]]"], "1 [[sympathy:class]]"], "dice": ["sympathy"], "name": "New Ideas", "stub": "new-ideas", "text": "Draw 2 cards.\n\n~ If you did not Meditate this turn, after this card is discarded unplayed form your hand, you may draw 1 card.", "type": "Action Spell", "weight": 105, "release": {"name": "The Protector of Argaia", "stub": "the-protector-of-argaia", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"sympathy:class": 1}, "placement": "Discard"}', '16', 'Action Spell', '105', '32', NULL, NULL, 'f', 'New Ideas
Draw 2 cards. If you did not Meditate this turn, after this card is discarded unplayed form your hand, you may draw 1 card.', '0', '4702', '1', NULL, NULL, 't'),
('290', 'Nightsong Cricket', 'nightsong-cricket', '{"life": 1, "name": "Nightsong Cricket", "stub": "nightsong-cricket", "text": "Polyphony: When this unit is destroyed, change 1 die in a target player''s active pool to a side of your choice.\n\nRenewed Harmony: When this unit is destroyed, you and a target opponent each choose a card in the other''s discard pile. Place the chosen cards into their owner''s hand.", "type": "Conjuration", "attack": 2, "copies": 4, "recover": 0, "release": {"name": "The Protector of Argaia", "stub": "the-protector-of-argaia", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '16', 'Conjuration', '0', '0', NULL, '4', 'f', 'Nightsong Cricket
Polyphony When this unit is destroyed, change 1 die in a target player''s active pool to a side of your choice. Renewed Harmony When this unit is destroyed, you and a target opponent each choose a card in the other''s discard pile. Place the chosen cards into their owner''s hand.', '0', '4703', '1', NULL, NULL, 't'),
('291', 'Seeds Of Aggression', 'seeds-of-aggression', '{"cost": ["[[main]]", ["1 [[charm:power]]", "1 [[sympathy:power]]"]], "name": "Seeds Of Aggression", "stub": "seeds-of-aggression", "text": "Choose a target unit you control and a target unit an opponent controls. Those units deal damage to each other equal to their attack value.", "type": "Action Spell", "weight": 107, "altDice": ["charm", "sympathy"], "release": {"name": "The Protector of Argaia", "stub": "the-protector-of-argaia", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"charm:power / sympathy:power": 1}, "placement": "Discard"}', '16', 'Action Spell', '107', '0', NULL, NULL, 'f', 'Seeds Of Aggression
Choose a target unit you control and a target unit an opponent controls. Those units deal damage to each other equal to their attack value.', '34', '4704', '1', NULL, NULL, 't'),
('292', 'Summon Majestic Titan', 'summon-majestic-titan', '{"cost": ["[[main]]"], "dice": ["charm"], "name": "Summon Majestic Titan", "stub": "summon-majestic-titan", "text": "When a spell, ability, or dice power would target a [[Majestic Titan]] you control, you may discard this card to cancel the effects of that spell, ability, or dice power.\n\n[[main]] - [[exhaust]] - 1 [[charm:power]] - 1 [[charm:class]] or 1 [[sympathy:class]] - 2 [[basic]]: Place a [[Majestic Titan]] conjuration onto your battlefield.\n\nFocus 1: Opponents cannot attach an alteration spell to a [[Majestic Titan]] you control.", "type": "Ready Spell", "weight": 5, "altDice": ["charm", "sympathy"], "release": {"name": "The Protector of Argaia", "stub": "the-protector-of-argaia", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "conjurations": [{"name": "Majestic Titan", "stub": "majestic-titan"}], "effectMagicCost": {"basic": 2, "charm:class": 1, "charm:power": 1}}', '16', 'Ready Spell', '5', '2', NULL, NULL, 't', 'Summon Majestic Titan
When a spell, ability, or dice power would target a Majestic Titan you control, you may discard this card to cancel the effects of that spell, ability, or dice power. Place a Majestic Titan conjuration onto your battlefield. Focus 1 Opponents cannot attach an alteration spell to a Majestic Titan you control.', '34', '4705', '1', NULL, NULL, 't'),
('293', 'Summon Mind Fog Owl', 'summon-mind-fog-owl', '{"cost": ["[[main]]"], "dice": ["charm"], "name": "Summon Mind Fog Owl", "stub": "summon-mind-fog-owl", "text": "~ During a player''s turn, when you would draw 1 or more cards, you may draw 1 fewer card. If you do, place this card onto your spellboard.\n\n[[main]] - [[exhaust]] - 1 [[charm:class]] - 1 [[basic]]: Place a [[Mind Fog Owl]] conjuration onto your battlefield.\n\nFocus 1: You may change the activation cost of this spell to [[main]] - [[exhaust]] - 1 [[charm:power]] - 1 [[discard]].\n\nFocus 2: If you cannot place a Mind Fog Owl, choose a target opponent to discard 1 card of their choice from their hand.", "type": "Ready Spell", "weight": 5, "release": {"name": "The Protector of Argaia", "stub": "the-protector-of-argaia", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "conjurations": [{"name": "Mind Fog Owl", "stub": "mind-fog-owl"}], "effectMagicCost": {"basic": 1, "charm:class": 1}}', '16', 'Ready Spell', '5', '2', NULL, NULL, 't', 'Summon Mind Fog Owl
During a player''s turn, when you would draw 1 or more cards, you may draw 1 fewer card. If you do, place this card onto your spellboard. Place a Mind Fog Owl conjuration onto your battlefield. Focus 1 You may change the activation cost of this spell to main - exhaust - 1 charm:power - 1 discard. Focus 2 If you cannot place a Mind Fog Owl, choose a target opponent to discard 1 card of their choice from their hand.', '0', '4706', '1', NULL, NULL, 't'),
('294', 'Summon Nightsong Cricket', 'summon-nightsong-cricket', '{"cost": ["[[main]]"], "dice": ["sympathy"], "name": "Summon Nightsong Cricket", "stub": "summon-nightsong-cricket", "text": "~ If you did not Meditate this turn, after this card is discarded from your hand, you may spend 1 [[basic]] to place it onto your spellboard.\n\n[[main]] - [[exhaust]] - 1 [[sympathy:class]] - 1 [[basic]]: Place a [[Nightsong Cricket]] conjuration onto your battlefield.\n\nFocus 1: You may, as an additional cost, discard 1 card from your hand to place 1 exhaustion token on an unexhausted copy of this spell that you control. If you do, place an additional [[Nightsong Cricket]] conjuration onto your battlefield.", "type": "Ready Spell", "weight": 5, "release": {"name": "The Protector of Argaia", "stub": "the-protector-of-argaia", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Spellboard", "conjurations": [{"name": "Nightsong Cricket", "stub": "nightsong-cricket"}], "effectMagicCost": {"basic": 1, "sympathy:class": 1}}', '16', 'Ready Spell', '5', '32', NULL, NULL, 't', 'Summon Nightsong Cricket
If you did not Meditate this turn, after this card is discarded from your hand, you may spend 1 basic to place it onto your spellboard. Place a Nightsong Cricket conjuration onto your battlefield. Focus 1 You may, as an additional cost, discard 1 card from your hand to place 1 exhaustion token on an unexhausted copy of this spell that you control. If you do, place an additional Nightsong Cricket conjuration onto your battlefield.', '0', '4707', '1', NULL, NULL, 't'),
('295', 'Chant Of Sacrifice', 'chant-of-sacrifice', '{"cost": ["[[main]]", "1 [[ceremonial:class]]", "1 [[divine:class]]"], "dice": ["ceremonial", "divine"], "name": "Chant Of Sacrifice", "stub": "chant-of-sacrifice", "text": "After a player has declared blockers, you may place 1 exhaustion token on this spell to destroy a unit you control. If you do, for the remainder of this turn, a target unit you control adds 2 to its attack value or gains one of the following abilities:\n\nBattle Advantage: When this unit is in battle, it deals its damage before other units without Battle Advantage deal their damage.\n\nArmored 2: When this unit would receive damage, prevent 2 damage.", "type": "Ready Spell", "weight": 207, "release": {"name": "The Grave King", "stub": "the-grave-king", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"divine:class": 1, "ceremonial:class": 1}, "placement": "Spellboard"}', '17', 'Ready Spell', '207', '17', NULL, NULL, 'f', 'Chant Of Sacrifice
After a player has declared blockers, you may place 1 exhaustion token on this spell to destroy a unit you control. If you do, for the remainder of this turn, a target unit you control adds 2 to its attack value or gains one of the following abilities: Battle Advantage When this unit is in battle, it deals its damage before other units without Battle Advantage deal their damage. Armored 2 When this unit would receive damage, prevent 2 damage.', '0', '4708', '1', NULL, NULL, 't'),
('296', 'Fallen', 'fallen', '{"life": 1, "name": "Fallen", "stub": "fallen", "text": "Infectious: Damage dealt by this unit by attacking or countering cannot be prevented.", "type": "Conjuration", "attack": 1, "copies": 7, "recover": 1, "release": {"name": "The Grave King", "stub": "the-grave-king", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Battlefield"}', '17', 'Conjuration', '0', '0', NULL, '7', 'f', 'Fallen
Infectious Damage dealt by this unit by attacking or countering cannot be prevented.', '0', '4709', '1', NULL, NULL, 't'),
('297', 'Grave Knight', 'grave-knight', '{"cost": ["[[main]]", "1 [[ceremonial:power]]", "1 [[divine:class]]", "1 [[basic]]"], "dice": ["ceremonial", "divine"], "life": 3, "name": "Grave Knight", "stub": "grave-knight", "text": "Battle Advantage: When this unit is in battle, it deals its damage before other units without Battle Advantage deal their damage.\n\nSmite 1: After this unit destroys a unit by attacking or countering, you may remove 1 wound token from your Phoenixborn.", "type": "Ally", "attack": 3, "weight": 308, "recover": 2, "release": {"name": "The Grave King", "stub": "the-grave-king", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"basic": 1, "divine:class": 1, "ceremonial:power": 1}, "placement": "Battlefield"}', '17', 'Ally', '308', '17', NULL, NULL, 'f', 'Grave Knight
Battle Advantage When this unit is in battle, it deals its damage before other units without Battle Advantage deal their damage. Smite 1 After this unit destroys a unit by attacking or countering, you may remove 1 wound token from your Phoenixborn.', '0', '4710', '1', NULL, NULL, 't'),
('298', 'Immortal Commander', 'immortal-commander', '{"cost": ["[[main]]", "2 [[divine:class]]"], "dice": ["divine"], "life": 2, "name": "Immortal Commander", "stub": "immortal-commander", "text": "Exert: [[side]]: Place 1 exhaustion token on this unit.\n\n* Command 1: While this unit has 1 or more exhaustion tokens on it, the attack value of all other units you control is increased by 1.\n\n~ Soul Fire 2: When this card would leave your discard pile, you may spend 1 [[divine:power]] to deal 2 damage to a target unit.", "type": "Ally", "attack": 2, "weight": 207, "recover": 1, "release": {"name": "The Grave King", "stub": "the-grave-king", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"divine:class": 2}, "placement": "Battlefield", "effectMagicCost": {"divine:power": 1}}', '17', 'Ally', '207', '16', NULL, NULL, 'f', 'Immortal Commander
Exert Place 1 exhaustion token on this unit. Command 1 While this unit has 1 or more exhaustion tokens on it, the attack value of all other units you control is increased by 1. Soul Fire 2 When this card would leave your discard pile, you may spend 1 divine:power to deal 2 damage to a target unit.', '0', '4711', '1', NULL, NULL, 't'),
('299', 'James Endersight', 'james-endersight', '{"life": 19, "name": "James Endersight", "stub": "james-endersight", "text": "Convene With Souls: [[side]] - [[exhaust]]: Search your draw pile for an ally, reveal it, and place it into your hand. Place a number of wound tokens equal to that ally''s life value on this card. Shuffle your draw pile.", "type": "Phoenixborn", "release": {"name": "The Grave King", "stub": "the-grave-king", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "spellboard": 3, "battlefield": 7}', '17', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'James Endersight
Convene With Souls Search your draw pile for an ally, reveal it, and place it into your hand. Place a number of wound tokens equal to that ally''s life value on this card. Shuffle your draw pile.', '0', '4712', '1', NULL, NULL, 't'),
('300', 'Law Of Repentance', 'law-of-repentance', '{"cost": ["[[side]]", "1 [[divine:class]]"], "dice": ["divine"], "name": "Law Of Repentance", "stub": "law-of-repentance", "text": "When this spell comes into play, if you control an ally, remove 2 wound tokens from your Phoenixborn.\n\nWhen a player would place 1 or more dice into their active pool from their exhausted pool, deal 1 damage to that player''s Phoenixborn.\n\n* Bound: This card cannot be discarded from your spellboard when you Meditate.\n\n* Fleeting: Discard this card at the end of the round.", "type": "Ready Spell", "weight": 105, "release": {"name": "The Grave King", "stub": "the-grave-king", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"divine:class": 1}, "placement": "Spellboard"}', '17', 'Ready Spell', '105', '16', NULL, NULL, 'f', 'Law Of Repentance
When this spell comes into play, if you control an ally, remove 2 wound tokens from your Phoenixborn. When a player would place 1 or more dice into their active pool from their exhausted pool, deal 1 damage to that player''s Phoenixborn. Bound This card cannot be discarded from your spellboard when you Meditate. Fleeting Discard this card at the end of the round.', '0', '4713', '1', NULL, NULL, 't'),
('301', 'Rally The Troops', 'rally-the-troops', '{"cost": ["[[side]]", "1 [[divine:class]]"], "dice": ["divine"], "name": "Rally The Troops", "stub": "rally-the-troops", "text": "Choose X allies you control with 1 or more exhaustion tokens on them and place them into their owner''s hand. Remove X wound tokens from your Phoenixborn.", "type": "Action Spell", "weight": 105, "release": {"name": "The Grave King", "stub": "the-grave-king", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"divine:class": 1}, "placement": "Discard"}', '17', 'Action Spell', '105', '16', NULL, NULL, 'f', 'Rally The Troops
Choose X allies you control with 1 or more exhaustion tokens on them and place them into their owner''s hand. Remove X wound tokens from your Phoenixborn.', '0', '4714', '1', NULL, NULL, 't'),
('302', 'Reaping Angel', 'reaping-angel', '{"cost": ["[[main]]", "1 [[ceremonial:class]]", "1 [[divine:class]]"], "dice": ["ceremonial", "divine"], "life": 2, "name": "Reaping Angel", "stub": "reaping-angel", "text": "Offer: When this unit comes into play, you may search your draw pile for an ally and place it into your discard pile. If you do, remove a number of wound tokens from equal to that ally''s recover value from your Phoenixborn. Shuffle your draw pile.\n\nSustain 1: When a unit you control would receive damage, you may place 1 wound token on this unit. If you do, prevent 1 damage to that unit.", "type": "Ally", "attack": 1, "weight": 207, "recover": 3, "release": {"name": "The Grave King", "stub": "the-grave-king", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"divine:class": 1, "ceremonial:class": 1}, "placement": "Battlefield"}', '17', 'Ally', '207', '17', NULL, NULL, 'f', 'Reaping Angel
Offer When this unit comes into play, you may search your draw pile for an ally and place it into your discard pile. If you do, remove a number of wound tokens from equal to that ally''s recover value from your Phoenixborn. Shuffle your draw pile. Sustain 1 When a unit you control would receive damage, you may place 1 wound token on this unit. If you do, prevent 1 damage to that unit.', '0', '4715', '1', NULL, NULL, 't'),
('303', 'Reclaim Soul', 'reclaim-soul', '{"cost": ["[[main]]", "2 [[ceremonial:class]]"], "dice": ["ceremonial"], "name": "Reclaim Soul", "stub": "reclaim-soul", "text": "Choose a target unit. That unit deals damage equal to its attack value to itself. The owner of that unit selects a number of of dice in their exhausted pool up to that unit''s recover value, re-rolls them, and places them into their active pool.", "type": "Action Spell", "weight": 207, "release": {"name": "The Grave King", "stub": "the-grave-king", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"ceremonial:class": 2}, "placement": "Discard"}', '17', 'Action Spell', '207', '1', NULL, NULL, 'f', 'Reclaim Soul
Choose a target unit. That unit deals damage equal to its attack value to itself. The owner of that unit selects a number of of dice in their exhausted pool up to that unit''s recover value, re-rolls them, and places them into their active pool.', '0', '4716', '1', NULL, NULL, 't'),
('304', 'Rising Horde', 'rising-horde', '{"cost": ["[[main]]", "2 [[ceremonial:class]]"], "dice": ["ceremonial"], "life": 1, "name": "Rising Horde", "stub": "rising-horde", "text": "* Raise Fallen: When this unit is destroyed, place 2 [[Fallen]] conjurations onto your battlefield.", "type": "Ally", "attack": 1, "weight": 207, "recover": 1, "release": {"name": "The Grave King", "stub": "the-grave-king", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"ceremonial:class": 2}, "placement": "Battlefield", "conjurations": [{"name": "Fallen", "stub": "fallen"}]}', '17', 'Ally', '207', '1', NULL, NULL, 'f', 'Rising Horde
Raise Fallen When this unit is destroyed, place 2 Fallen conjurations onto your battlefield.', '0', '4717', '1', NULL, NULL, 't'),
('305', 'Summon Fallen', 'summon-fallen', '{"cost": ["[[main]]", "1 [[ceremonial:class]]"], "dice": ["ceremonial"], "name": "Summon Fallen", "stub": "summon-fallen", "text": "[[main]] - 1 [[basic]]: Discard an ally from your hand or remove an ally in your discard pile from the game. If you do, place a [[Fallen]] conjuration onto your battlefield. You may repeat this effect one additional time.\n\nFocus 1: When a [[Fallen]] conjuration you control would receive damage, you may place 1 exhaustion token on this spell. If you do, prevent that damage.", "type": "Ready Spell", "weight": 106, "release": {"name": "The Grave King", "stub": "the-grave-king", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "magicCost": {"ceremonial:class": 1}, "placement": "Spellboard", "conjurations": [{"name": "Fallen", "stub": "fallen"}], "effectRepeats": true, "effectMagicCost": {"basic": 1}}', '17', 'Ready Spell', '106', '1', NULL, NULL, 't', 'Summon Fallen
Discard an ally from your hand or remove an ally in your discard pile from the game. If you do, place a Fallen conjuration onto your battlefield. You may repeat this effect one additional time. Focus 1 When a Fallen conjuration you control would receive damage, you may place 1 exhaustion token on this spell. If you do, prevent that damage.', '0', '4718', '1', NULL, NULL, 't'),
('306', 'Vengeance', 'vengeance', '{"cost": ["X [[basic]]"], "name": "Vengeance", "stub": "vengeance", "text": "You may play this spell after you declare an Attack a Phoenixborn main action. Destroy X units you control. If you do, X target units you currently control gain the following abilities for the remainder of this turn:\n\nOverkill X: When this unit destroys a unit an opponent controls by attacking, deal X damage to that opponent''s Phoenixborn.\n\nSpite X: When this unit deals damage to a Phoenixborn by attacking, you may deal X additional damage to that Phoenixborn.", "type": "Reaction Spell", "weight": 0, "release": {"name": "The Grave King", "stub": "the-grave-king", "is_phg": true, "is_promo": false, "is_legacy": true, "is_retiring": false}, "is_legacy": true, "placement": "Discard", "phoenixborn": "James Endersight"}', '17', 'Reaction Spell', '0', '0', 'James Endersight', NULL, 'f', 'Vengeance
You may play this spell after you declare an Attack a Phoenixborn main action. Destroy X units you control. If you do, X target units you currently control gain the following abilities for the remainder of this turn: Overkill X When this unit destroys a unit an opponent controls by attacking, deal X damage to that opponent''s Phoenixborn. Spite X When this unit deals damage to a Phoenixborn by attacking, you may deal X additional damage to that Phoenixborn.', '0', '4719', '1', NULL, NULL, 't'),
('307', 'Bloodstained Dagger', 'bloodstained-dagger', '{"cost": ["[[main]]", "1 [[time:class]]"], "dice": ["time"], "name": "Bloodstained Dagger", "stub": "bloodstained-dagger", "text": "~ Conceal 1: When a player declares blockers, you may remove 1 card in your discard pile from the game to play this spell from your discard pile without paying its main action cost.\n\nThis unit now has the following ability:\n\nThrow 1: During your turn, you may place 1 exhaustion token on this unit to deal 1 damage to a target unit.", "type": "Alteration Spell", "attack": "+1", "weight": 106, "release": {"name": "The Treasures of the Ages", "stub": "the-treasures-of-the-ages", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"time:class": 1}, "placement": "Unit"}', '21', 'Alteration Spell', '106', '64', NULL, NULL, 'f', 'Bloodstained Dagger
Conceal 1 When a player declares blockers, you may remove 1 card in your discard pile from the game to play this spell from your discard pile without paying its main action cost. This unit now has the following ability: Throw 1 During your turn, you may place 1 exhaustion token on this unit to deal 1 damage to a target unit.', '0', '7932', '1', NULL, NULL, 't'),
('308', 'Chimera Smasher', 'chimera-smasher', '{"cost": [["1 [[time:class]]", "[[main]]"], "[[side]]", "1 [[time:power]]"], "dice": ["time"], "name": "Chimera Smasher", "stub": "chimera-smasher", "text": "This unit now has the following abilities:\n\nAftershock 1: When this unit deals damage by attacking or countering, you may place 1 wound token on a target unit.\n\nBattle Impairment: When this unit is in battle, it deals its damage after other units without Battle Impairment deal their damage. If this unit also has Battle Advantage, it loses that ability and this one.", "type": "Alteration Spell", "attack": "+2", "weight": 111, "release": {"name": "The Treasures of the Ages", "stub": "the-treasures-of-the-ages", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"time:power": 1}, "placement": "Unit"}', '21', 'Alteration Spell', '111', '64', NULL, NULL, 'f', 'Chimera Smasher
This unit now has the following abilities: Aftershock 1 When this unit deals damage by attacking or countering, you may place 1 wound token on a target unit. Battle Impairment When this unit is in battle, it deals its damage after other units without Battle Impairment deal their damage. If this unit also has Battle Advantage, it loses that ability and this one.', '0', '7933', '1', NULL, NULL, 't'),
('309', 'Deteriorating Armor', 'deteriorating-armor', '{"cost": ["[[main]]", "[[side]]", "1 [[time:class]]"], "dice": ["time"], "life": "+X", "name": "Deteriorating Armor", "stub": "deteriorating-armor", "text": "* Countdown 2: This card comes into play with 2 status tokens. At the end of the round, remove 1 status token from this card. If you cannot, dsicard this card instead.\n\n* X = Number of status tokens on this card.\n\nThis unit now has the following ability:\n\n* Armored 1: When this unit would receive damage, prevent 1 damage.", "type": "Alteration Spell", "weight": 110, "release": {"name": "The Treasures of the Ages", "stub": "the-treasures-of-the-ages", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"time:class": 1}, "placement": "Unit"}', '21', 'Alteration Spell', '110', '64', NULL, NULL, 'f', 'Deteriorating Armor
Countdown 2 This card comes into play with 2 status tokens. At the end of the round, remove 1 status token from this card. If you cannot, dsicard this card instead. X = Number of status tokens on this card. This unit now has the following ability: Armored 1 When this unit would receive damage, prevent 1 damage.', '0', '7934', '1', NULL, NULL, 't'),
('310', 'Hastened Response', 'hastened-response', '{"cost": ["[[main]]", "1 [[time:class]]"], "dice": ["time"], "name": "Hastened Response", "stub": "hastened-response", "text": "After an opponent declares attackers, you may place 1 exhaustion token on this card to choose a unit you control. That unit gains the following ability for the remainder of this turn:\n\nUnit Guard: This unit may guard a unit that is being attacked.", "type": "Ready Spell", "weight": 106, "release": {"name": "The Treasures of the Ages", "stub": "the-treasures-of-the-ages", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"time:class": 1}, "placement": "Spellboard"}', '21', 'Ready Spell', '106', '64', NULL, NULL, 'f', 'Hastened Response
After an opponent declares attackers, you may place 1 exhaustion token on this card to choose a unit you control. That unit gains the following ability for the remainder of this turn: Unit Guard This unit may guard a unit that is being attacked.', '0', '7935', '1', NULL, NULL, 't'),
('311', 'Missing Page', 'missing-page', '{"cost": ["1 [[time:class]]"], "dice": ["time"], "name": "Missing Page", "stub": "missing-page", "text": "You may play this spell when a conjuration is destroyed.\n\nPlace 1 exhaustion token on a target ready spell with a printed effect that can place a unit of the same name onto a battlefield.", "type": "Reaction Spell", "weight": 101, "release": {"name": "The Treasures of the Ages", "stub": "the-treasures-of-the-ages", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"time:class": 1}, "placement": "Discard"}', '21', 'Reaction Spell', '101', '64', NULL, NULL, 'f', 'Missing Page
You may play this spell when a conjuration is destroyed. Place 1 exhaustion token on a target ready spell with a printed effect that can place a unit of the same name onto a battlefield.', '0', '7936', '1', NULL, NULL, 't'),
('312', 'Paradox Clone', 'paradox-clone', '{"cost": ["1 [[time:power]]"], "dice": ["time"], "name": "Paradox Clone", "stub": "paradox-clone", "text": "You may play this spell when a conjuration with no abilities enters the battlefield under your control.\n\nPlace an additional conjuration of the same name from your conjuration pile onto the battlefield and attach a [[Broken Timeline]] conjured alteration spell to that unit.", "type": "Reaction Spell", "weight": 102, "release": {"name": "The Treasures of the Ages", "stub": "the-treasures-of-the-ages", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"time:power": 1}, "placement": "Discard", "conjurations": [{"name": "Broken Timeline", "stub": "broken-timeline"}]}', '21', 'Reaction Spell', '102', '64', NULL, NULL, 'f', 'Paradox Clone
You may play this spell when a conjuration with no abilities enters the battlefield under your control. Place an additional conjuration of the same name from your conjuration pile onto the battlefield and attach a Broken Timeline conjured alteration spell to that unit.', '0', '7937', '1', NULL, NULL, 't'),
('313', 'Relic Broker', 'relic-broker', '{"cost": ["[[main]]", "1 [[time:power]]", "1 [[time:class]]", "1 [[basic]]"], "dice": ["time"], "life": 1, "name": "Relic Broker", "stub": "relic-broker", "text": "Tools Across Time: When this unit comes into play, search your draw pile and discard pile for up to 1 alteration spell from each pile and attach them to this unit. All alterations attached this way must have a Magic Play Cost of 3 or less, and be named differently. Shuffle your draw pile afterward.", "type": "Ally", "attack": 0, "weight": 308, "recover": 0, "release": {"name": "The Treasures of the Ages", "stub": "the-treasures-of-the-ages", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"basic": 1, "time:class": 1, "time:power": 1}, "placement": "Battlefield"}', '21', 'Ally', '308', '64', NULL, NULL, 'f', 'Relic Broker
Tools Across Time When this unit comes into play, search your draw pile and discard pile for up to 1 alteration spell from each pile and attach them to this unit. All alterations attached this way must have a Magic Play Cost of 3 or less, and be named differently. Shuffle your draw pile afterward.', '0', '7938', '1', NULL, NULL, 't'),
('314', 'Summon Flying Monkey', 'summon-flying-monkey', '{"cost": ["[[main]]"], "dice": ["time"], "name": "Summon Flying Monkey", "stub": "summon-flying-monkey", "text": "[[main]] - [[exhaust]] - 1 [[time:class]] - 1 [[basic]]: Place a [[Flying Monkey]] conjuration onto your battlefield. Choose a target alteration spell or unit with 1 or more alteration spells attached to it. You may add or remove 1 status token to/from that target.\n\nFocus 1: You may move an alteration spell attached to a unit you control onto that [[Flying Monkey]].", "type": "Ready Spell", "weight": 5, "release": {"name": "The Treasures of the Ages", "stub": "the-treasures-of-the-ages", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "placement": "Spellboard", "conjurations": [{"name": "Flying Monkey", "stub": "flying-monkey"}], "effectMagicCost": {"basic": 1, "time:class": 1}}', '21', 'Ready Spell', '5', '64', NULL, NULL, 't', 'Summon Flying Monkey
Place a Flying Monkey conjuration onto your battlefield. Choose a target alteration spell or unit with 1 or more alteration spells attached to it. You may add or remove 1 status token to/from that target. Focus 1 You may move an alteration spell attached to a unit you control onto that Flying Monkey.', '0', '7939', '1', NULL, NULL, 't'),
('315', 'Summon Loyal Hound', 'summon-loyal-hound', '{"cost": ["[[main]]"], "name": "Summon Loyal Hound", "stub": "summon-loyal-hound", "text": "[[main]] - [[exhaust]] - 3 [[basic]]: Place a [[Loyal Hound]] conjuration onto your battlefield.", "type": "Ready Spell", "weight": 5, "release": {"name": "The Treasures of the Ages", "stub": "the-treasures-of-the-ages", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "placement": "Spellboard", "conjurations": [{"name": "Loyal Hound", "stub": "loyal-hound"}], "effectMagicCost": {"basic": 3}}', '21', 'Ready Spell', '5', '0', NULL, NULL, 't', 'Summon Loyal Hound
Place a Loyal Hound conjuration onto your battlefield.', '0', '7940', '1', NULL, NULL, 't'),
('316', 'Trusted Boomerang', 'trusted-boomerang', '{"cost": [["1 [[time:class]]", "[[main]]"], "[[side]]"], "name": "Trusted Boomerang", "stub": "trusted-boomerang", "text": "Deal 1 damage to a target unit an opponent controls. Continue repeating this effect until it doesn''t result in the destruction of a unit. Then, if any units received damage from this effect, draw 1 card.\n\n~ Callback: When your turn begins, if this card is in your discard pile and your Phoenixborn is unexhausted, you may spend 1 [[basic]] and place 1 exhaustion token on your Phoenixborn to return this card from your discard pile to your hand.", "type": "Action Spell", "weight": 9, "altDice": ["time"], "release": {"name": "The Treasures of the Ages", "stub": "the-treasures-of-the-ages", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "placement": "Discard", "phoenixborn": "Jill Traversack", "effectMagicCost": {"basic": 1}}', '21', 'Action Spell', '9', '0', 'Jill Traversack', NULL, 'f', 'Trusted Boomerang
Deal 1 damage to a target unit an opponent controls. Continue repeating this effect until it doesn''t result in the destruction of a unit. Then, if any units received damage from this effect, draw 1 card. Callback When your turn begins, if this card is in your discard pile and your Phoenixborn is unexhausted, you may spend 1 basic and place 1 exhaustion token on your Phoenixborn to return this card from your discard pile to your hand.', '64', '7941', '1', NULL, NULL, 't'),
('317', 'Broken Timeline', 'broken-timeline', '{"name": "Broken Timeline", "stub": "broken-timeline", "text": "* This spell cannot be moved or leave play unless the attached unit leaves play.\n\nThis unit gains the following ability:\n\n* Temporary Existence: When this unit would leave play for any reason, remove it from the game instead.", "type": "Conjured Alteration Spell", "copies": 3, "release": {"name": "The Treasures of the Ages", "stub": "the-treasures-of-the-ages", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "placement": "Unit"}', '21', 'Conjured Alteration Spell', '0', '0', NULL, '3', 'f', 'Broken Timeline
This spell cannot be moved or leave play unless the attached unit leaves play. This unit gains the following ability: Temporary Existence When this unit would leave play for any reason, remove it from the game instead.', '0', '7942', '1', NULL, NULL, 't'),
('318', 'Loyal Hound', 'loyal-hound', '{"life": 4, "name": "Loyal Hound", "stub": "loyal-hound", "text": "Fetch: When this unit deals damage to an opponent''s Phoenixborn, remove up to 1 target card in that player''s discard pile from the game. If you do, you may shuffle a card from your discard pile into your draw pile.\n\n* Rage 2: Add 2 to this unit''s attack value for each wound token on this unit.", "type": "Conjuration", "attack": 0, "copies": 3, "recover": 0, "release": {"name": "The Treasures of the Ages", "stub": "the-treasures-of-the-ages", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "placement": "Battlefield"}', '21', 'Conjuration', '0', '0', NULL, '3', 'f', 'Loyal Hound
Fetch When this unit deals damage to an opponent''s Phoenixborn, remove up to 1 target card in that player''s discard pile from the game. If you do, you may shuffle a card from your discard pile into your draw pile. Rage 2 Add 2 to this unit''s attack value for each wound token on this unit.', '0', '7943', '1', NULL, NULL, 't'),
('319', 'Flying Monkey', 'flying-monkey', '{"life": 1, "name": "Flying Monkey", "stub": "flying-monkey", "text": "", "type": "Conjuration", "attack": 3, "copies": 4, "recover": 0, "release": {"name": "The Treasures of the Ages", "stub": "the-treasures-of-the-ages", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "placement": "Battlefield"}', '21', 'Conjuration', '0', '0', NULL, '4', 'f', 'Flying Monkey
', '0', '7944', '1', NULL, NULL, 't'),
('320', 'Jill Traversack', 'jill-traversack', '{"life": 17, "name": "Jill Traversack", "stub": "jill-traversack", "text": "Treasures of the Ages: When an alteration that doesn''t share a name with any other card you control enters play attached to a unit or Phoenixborn you control, you may reroll a die in your exhausted pool and place it in your active pool. This ability can only trigger once per turn.", "type": "Phoenixborn", "release": {"name": "The Treasures of the Ages", "stub": "the-treasures-of-the-ages", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "spellboard": 4, "battlefield": 5, "diceRecursion": 1}', '21', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Jill Traversack
Treasures of the Ages When an alteration that doesn''t share a name with any other card you control enters play attached to a unit or Phoenixborn you control, you may reroll a die in your exhausted pool and place it in your active pool. This ability can only trigger once per turn.', '0', '7945', '1', NULL, NULL, 't'),
('321', 'Flicker', 'flicker', '{"cost": ["[[side]]", "1 [[time:class]]"], "dice": ["time"], "name": "Flicker", "stub": "flicker", "text": "Disenchant: [[side]] - 1 [[discard]]: Discard this card.\n\nRespark: 1 [[charm:class]]", "type": "Alteration Spell", "weight": 105, "altDice": ["charm"], "release": {"name": "The Young Ruler", "stub": "the-young-ruler", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"time:class": 1}, "placement": "Unit", "effectMagicCost": {"charm:class": 1}}', '22', 'Alteration Spell', '105', '64', NULL, NULL, 'f', 'Flicker
Disenchant Discard this card. Respark 1 charm:class', '2', '7946', '1', NULL, NULL, 't'),
('322', 'Future Visions', 'future-visions', '{"cost": ["[[main]]", "1 [[time:class]]"], "dice": ["time"], "name": "Future Visions", "stub": "future-visions", "text": "* After the prepare phase, each player draws 1 card.\n\n[[main]] or [[side]] - [[exhaust]]: Look at the top card of each player''s draw pile. Then, choose one of the following effects:\n\n- Each player draws 1 card.\n\n- Discard 1 card off the top of each player''s draw pile.\n\nFocus 2: Each opponent with no cards in their draw pile must discard 1 card of their choice from their hand.", "type": "Ready Spell", "weight": 106, "release": {"name": "The Young Ruler", "stub": "the-young-ruler", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"time:class": 1}, "placement": "Spellboard"}', '22', 'Ready Spell', '106', '64', NULL, NULL, 'f', 'Future Visions
After the prepare phase, each player draws 1 card. Look at the top card of each player''s draw pile. Then, choose one of the following effects: - Each player draws 1 card. - Discard 1 card off the top of each player''s draw pile. Focus 2 Each opponent with no cards in their draw pile must discard 1 card of their choice from their hand.', '0', '7947', '1', NULL, NULL, 't'),
('323', 'Law Of Courtesy', 'law-of-courtesy', '{"cost": ["[[main]]", ["1 [[divine:class]]", "1 [[charm:class]]"]], "name": "Law Of Courtesy", "stub": "law-of-courtesy", "text": "When this spell comes into play, you may remove 1 exhaustion token from a target unit with an attack value of 2 or less.\n\nPlayers must spend 1 [[basic]] to take an Attack a Phoenixborn main action or Attack a Unit main action.\n\n* Bound: This card cannot be discarded from your spellboard when you Meditate.\n\n* Fleeting: Discard this card at the end of the round.", "type": "Ready Spell", "weight": 106, "altDice": ["divine", "charm"], "release": {"name": "The Young Ruler", "stub": "the-young-ruler", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"divine:class / charm:class": 1}, "placement": "Spellboard", "effectRepeats": true, "effectMagicCost": {"basic": 1}}', '22', 'Ready Spell', '106', '0', NULL, NULL, 'f', 'Law Of Courtesy
When this spell comes into play, you may remove 1 exhaustion token from a target unit with an attack value of 2 or less. Players must spend 1 basic to take an Attack a Phoenixborn main action or Attack a Unit main action. Bound This card cannot be discarded from your spellboard when you Meditate. Fleeting Discard this card at the end of the round.', '18', '7948', '1', NULL, NULL, 't'),
('324', 'Royal Vizier', 'royal-vizier', '{"cost": ["[[main]]", ["1 [[time:power]]", "1 [[charm:power]]"], "1 [[charm:class]]"], "dice": ["charm"], "life": 3, "name": "Royal Vizier", "stub": "royal-vizier", "text": "Ambush 1: When this unit comes into play, you may deal 1 damage to a target unit or Phoenixborn.\n\n* Diplomacy: When this unit deals damage to an opponent''s Phoenixborn, you may choose not to place wound tokens on that Phoenixborn. If you do, look at the top 2 cards of that player''s draw pile. Remove 1 of those cards from the game, and place the other card on either the top or bottom of its owner''s draw pile.", "type": "Ally", "attack": 1, "weight": 208, "altDice": ["time"], "recover": 1, "release": {"name": "The Young Ruler", "stub": "the-young-ruler", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"charm:class": 1, "time:power / charm:power": 1}, "placement": "Battlefield"}', '22', 'Ally', '208', '2', NULL, NULL, 'f', 'Royal Vizier
Ambush 1 When this unit comes into play, you may deal 1 damage to a target unit or Phoenixborn. Diplomacy When this unit deals damage to an opponent''s Phoenixborn, you may choose not to place wound tokens on that Phoenixborn. If you do, look at the top 2 cards of that player''s draw pile. Remove 1 of those cards from the game, and place the other card on either the top or bottom of its owner''s draw pile.', '64', '7949', '1', NULL, NULL, 't'),
('325', 'Summon Clockwork Frog', 'summon-clockwork-frog', '{"cost": ["[[main]]"], "dice": ["time"], "name": "Summon Clockwork Frog", "stub": "summon-clockwork-frog", "text": "[[main]] - [[exhaust]] - 1 [[time:class]]: Place a [[Clockwork Frog]] conjuration onto your battlefield.", "type": "Ready Spell", "weight": 5, "release": {"name": "The Young Ruler", "stub": "the-young-ruler", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "placement": "Spellboard", "conjurations": [{"name": "Clockwork Frog", "stub": "clockwork-frog"}], "effectMagicCost": {"time:class": 1}}', '22', 'Ready Spell', '5', '64', NULL, NULL, 't', 'Summon Clockwork Frog
Place a Clockwork Frog conjuration onto your battlefield.', '0', '7950', '1', NULL, NULL, 't'),
('326', 'Summon Exotic Gorilla', 'summon-exotic-gorilla', '{"cost": ["[[main]]", "1 [[time:power]]"], "dice": ["time"], "name": "Summon Exotic Gorilla", "stub": "summon-exotic-gorilla", "text": "[[main]] - [[exhaust]] - 1 [[time:class]] - 1 [[basic]]: Place an [[Exotic Gorilla]] conjuration onto your battlefield.\n\nFocus 1: You may discard an unexhausted ready spell you control. If you do, draw 1 card, then discard 1 card off the top of a target player''s draw pile.", "type": "Ready Spell", "weight": 107, "release": {"name": "The Young Ruler", "stub": "the-young-ruler", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"time:power": 1}, "placement": "Spellboard", "conjurations": [{"name": "Exotic Gorilla", "stub": "exotic-gorilla"}], "effectMagicCost": {"basic": 1, "time:class": 1}}', '22', 'Ready Spell', '107', '64', NULL, NULL, 't', 'Summon Exotic Gorilla
Place an Exotic Gorilla conjuration onto your battlefield. Focus 1 You may discard an unexhausted ready spell you control. If you do, draw 1 card, then discard 1 card off the top of a target player''s draw pile.', '0', '7951', '1', NULL, NULL, 't'),
('327', 'Sycophant', 'sycophant', '{"cost": ["[[main]]", "1 [[charm:class]]", "1 [[basic]]"], "dice": ["charm"], "life": 2, "name": "Sycophant", "stub": "sycophant", "text": "* Last Blessing 2: When this unit is destroyed, remove 2 wound tokens from a target unit or Phoenixborn.\n\n* Last Request 1: When this unit is destroyed, discard 1 card off the top of a target player''s draw pile.\n\n~ Exile: When this unit is placed in its owner''s discard pile, remove it from the game.", "type": "Ally", "attack": 1, "weight": 206, "recover": 0, "release": {"name": "The Young Ruler", "stub": "the-young-ruler", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"basic": 1, "charm:class": 1}, "placement": "Battlefield"}', '22', 'Ally', '206', '2', NULL, NULL, 'f', 'Sycophant
Last Blessing 2 When this unit is destroyed, remove 2 wound tokens from a target unit or Phoenixborn. Last Request 1 When this unit is destroyed, discard 1 card off the top of a target player''s draw pile. Exile When this unit is placed in its owner''s discard pile, remove it from the game.', '0', '7952', '1', NULL, NULL, 't'),
('328', 'Time Stop', 'time-stop', '{"cost": ["[[side]]", "1 [[time:class]]"], "dice": ["time"], "name": "Time Stop", "stub": "time-stop", "text": "Choose a target unit you own. That unit gains the following abilies for the rest of the turn:\n\nBypass: This unit cannot be blocked or guarded.\n\n* Reality Fracture: At the end of the turn, remove this unit from the game.", "type": "Action Spell", "weight": 105, "release": {"name": "The Young Ruler", "stub": "the-young-ruler", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"time:class": 1}, "placement": "Discard"}', '22', 'Action Spell', '105', '64', NULL, NULL, 'f', 'Time Stop
Choose a target unit you own. That unit gains the following abilies for the rest of the turn: Bypass This unit cannot be blocked or guarded. Reality Fracture At the end of the turn, remove this unit from the game.', '0', '7953', '1', NULL, NULL, 't'),
('329', 'Unwavering Loyalty', 'unwavering-loyalty', '{"cost": ["[[side]]", "1 [[charm:class]]"], "dice": ["charm"], "name": "Unwavering Loyalty", "stub": "unwavering-loyalty", "text": "* When this spell is removed from play, discard the attached unit.\n\n* This unit does not count towards your battlefield limit and gains the following ability:\n\nDecoy: When a unit you control would become the target of a spell, ability, or dice power, and this unit could have been chosen as that target, you may place 1 exhaustion token on this unit to change the chosen target to be this unit instead.", "type": "Alteration Spell", "weight": 105, "release": {"name": "The Young Ruler", "stub": "the-young-ruler", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"charm:class": 1}, "placement": "Unit"}', '22', 'Alteration Spell', '105', '2', NULL, NULL, 'f', 'Unwavering Loyalty
When this spell is removed from play, discard the attached unit. This unit does not count towards your battlefield limit and gains the following ability: Decoy When a unit you control would become the target of a spell, ability, or dice power, and this unit could have been chosen as that target, you may place 1 exhaustion token on this unit to change the chosen target to be this unit instead.', '0', '7954', '1', NULL, NULL, 't'),
('330', 'Forever In The Moment', 'forever-in-the-moment', '{"cost": ["[[main]]", "1 [[basic]]"], "name": "Forever In The Moment", "stub": "forever-in-the-moment", "text": "Take 2 additional main actions ([[main]]) this turn. You cannot take an Attack a Phoenixborn or Attack a Unit main action this turn.", "type": "Action Spell", "weight": 105, "release": {"name": "The Young Ruler", "stub": "the-young-ruler", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"basic": 1}, "placement": "Discard", "phoenixborn": "Tolliver I"}', '22', 'Action Spell', '105', '0', 'Tolliver I', NULL, 'f', 'Forever In The Moment
Take 2 additional main actions (main) this turn. You cannot take an Attack a Phoenixborn or Attack a Unit main action this turn.', '0', '7955', '1', NULL, NULL, 't'),
('331', 'Clockwork Frog', 'clockwork-frog', '{"life": 1, "name": "Clockwork Frog", "stub": "clockwork-frog", "text": "Spiked Skin 2: When this unit is dealt damage by one or more attacking or countering units, deal 2 damage to each unit that is attacking or countering this unit.\n\nArmored 1: When this unit would receive damage, prevent 1 damage.", "type": "Conjuration", "attack": 0, "copies": 3, "recover": 0, "release": {"name": "The Young Ruler", "stub": "the-young-ruler", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "placement": "Battlefield"}', '22', 'Conjuration', '0', '0', NULL, '3', 'f', 'Clockwork Frog
Spiked Skin 2 When this unit is dealt damage by one or more attacking or countering units, deal 2 damage to each unit that is attacking or countering this unit. Armored 1 When this unit would receive damage, prevent 1 damage.', '0', '7956', '1', NULL, NULL, 't'),
('332', 'Exotic Gorilla', 'exotic-gorilla', '{"life": 4, "name": "Exotic Gorilla", "stub": "exotic-gorilla", "text": "Gigantic 2: This unit cannot be blocked or guarded against by units with a life value of 2 or less.\n\n* Massive 1: This unit occupies 1 additional slot on your battlefield. (This unit cannot be placed or moved onto your battlefield unless you have 1 additional slot.)", "type": "Conjuration", "attack": 3, "copies": 2, "recover": 0, "release": {"name": "The Young Ruler", "stub": "the-young-ruler", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "placement": "Battlefield"}', '22', 'Conjuration', '0', '0', NULL, '2', 'f', 'Exotic Gorilla
Gigantic 2 This unit cannot be blocked or guarded against by units with a life value of 2 or less. Massive 1 This unit occupies 1 additional slot on your battlefield. (This unit cannot be placed or moved onto your battlefield unless you have 1 additional slot.)', '0', '7957', '1', NULL, NULL, 't'),
('333', 'Tolliver I', 'tolliver-i', '{"life": 18, "name": "Tolliver I", "stub": "tolliver-i", "text": "Renewal: [[side]] - [[exhaust]]: You may take 1 additional main action ([[main]]) this turn, but only to take a pass action.", "type": "Phoenixborn", "release": {"name": "The Young Ruler", "stub": "the-young-ruler", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "spellboard": 3, "battlefield": 8}', '22', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Tolliver I
Renewal You may take 1 additional main action (main) this turn, but only to take a pass action.', '0', '7958', '1', NULL, NULL, 't'),
('334', 'Bone Sea Privateer', 'bone-sea-privateer', '{"cost": ["[[main]]", "1 [[natural:class]]", "1 [[basic]]"], "dice": ["natural"], "life": 2, "name": "Bone Sea Privateer", "stub": "bone-sea-privateer", "text": "Fathom Trawl: When this unit comes into play, you may return an alteration spell from your discard to your hand.\n\n* Inheritance 1: When this unit is destroyed, you may place 1 status token on a target unit.", "type": "Ally", "attack": 1, "weight": 206, "recover": 0, "release": {"name": "The Scoundrels of the Sea", "stub": "the-scoundrels-of-the-sea", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"basic": 1, "natural:class": 1}, "placement": "Battlefield"}', '23', 'Ally', '206', '8', NULL, NULL, 'f', 'Bone Sea Privateer
Fathom Trawl When this unit comes into play, you may return an alteration spell from your discard to your hand. Inheritance 1 When this unit is destroyed, you may place 1 status token on a target unit.', '0', '8194', '1', NULL, NULL, 't'),
('335', 'Flash Back', 'flash-back', '{"cost": ["[[main]]", "1 [[time:class]]"], "dice": ["time"], "name": "Flash Back", "stub": "flash-back", "text": "Remove up to 3 wound tokens and 1 exhaustion token from among Phoenixborn your opponents control. Then remove an equivalent number of tokens (by type) from your Phoenixborn.", "type": "Action Spell", "weight": 106, "release": {"name": "The Scoundrels of the Sea", "stub": "the-scoundrels-of-the-sea", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"time:class": 1}, "placement": "Discard"}', '23', 'Action Spell', '106', '64', NULL, NULL, 'f', 'Flash Back
Remove up to 3 wound tokens and 1 exhaustion token from among Phoenixborn your opponents control. Then remove an equivalent number of tokens (by type) from your Phoenixborn.', '0', '8195', '1', NULL, NULL, 't'),
('336', 'Loot The Future', 'loot-the-future', '{"cost": ["[[main]]", ["1 [[time:class]]", "[[side]]"]], "name": "Loot The Future", "stub": "loot-the-future", "text": "As an additional cost to cast this spell, remove up to four status tokens from among units you control.\n\nRemove 1 + X wound tokens from among units you control, where X is the number of of status tokens you removed to cast this spell.", "type": "Action Spell", "weight": 9, "altDice": ["time"], "release": {"name": "The Scoundrels of the Sea", "stub": "the-scoundrels-of-the-sea", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "placement": "Discard"}', '23', 'Action Spell', '9', '0', NULL, NULL, 'f', 'Loot The Future
As an additional cost to cast this spell, remove up to four status tokens from among units you control. Remove 1 + X wound tokens from among units you control, where X is the number of of status tokens you removed to cast this spell.', '64', '8196', '1', NULL, NULL, 't'),
('337', 'Pearl Conch Venom', 'pearl-conch-venom', '{"cost": ["[[main]]", "1 [[natural:power]]"], "dice": ["natural"], "name": "Pearl Conch Venom", "stub": "pearl-conch-venom", "text": "This unit now has the following abilities:\n\nBattle Advantage: When this unit is in battle, it deals its damage before other units without Battle Advantage deal their damage.\n\nDeathstrike: When this unit deals 1 or more damage to a unit it is attacking or countering, destroy that unit.", "type": "Alteration Spell", "weight": 107, "release": {"name": "The Scoundrels of the Sea", "stub": "the-scoundrels-of-the-sea", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"natural:power": 1}, "placement": "Unit"}', '23', 'Alteration Spell', '107', '8', NULL, NULL, 'f', 'Pearl Conch Venom
This unit now has the following abilities: Battle Advantage When this unit is in battle, it deals its damage before other units without Battle Advantage deal their damage. Deathstrike When this unit deals 1 or more damage to a unit it is attacking or countering, destroy that unit.', '0', '8197', '1', NULL, NULL, 't'),
('338', 'Shipside Assassin', 'shipside-assassin', '{"cost": ["[[main]]", "1 [[time:power]]", "1 [[natural:class]]", "1 [[basic]]"], "dice": ["time", "natural"], "life": 3, "name": "Shipside Assassin", "stub": "shipside-assassin", "text": "* Biding Time: While this unit has 1 or more exhaustion tokens on it, it cannot be affected by opponents'' spells, abilities, or dice powers, and cannot be chosen as the target of an attack action.", "type": "Ally", "attack": 4, "weight": 308, "recover": 1, "release": {"name": "The Scoundrels of the Sea", "stub": "the-scoundrels-of-the-sea", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"basic": 1, "time:power": 1, "natural:class": 1}, "placement": "Battlefield"}', '23', 'Ally', '308', '72', NULL, NULL, 'f', 'Shipside Assassin
Biding Time While this unit has 1 or more exhaustion tokens on it, it cannot be affected by opponents'' spells, abilities, or dice powers, and cannot be chosen as the target of an attack action.', '0', '8198', '1', NULL, NULL, 't'),
('339', 'Shriveling', 'shriveling', '{"cost": ["[[main]]", "1 [[time:class]]"], "dice": ["time"], "name": "Shriveling", "stub": "shriveling", "text": "When one or more exhaustion tokens are removed from this Phoenixborn, place 1 wound token on this Phoenixborn.\n\n* At the end of the round, move 1 die from your active pool to your exhausted pool.", "type": "Alteration Spell", "weight": 106, "release": {"name": "The Scoundrels of the Sea", "stub": "the-scoundrels-of-the-sea", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"time:class": 1}, "placement": "Phoenixborn"}', '23', 'Alteration Spell', '106', '64', NULL, NULL, 'f', 'Shriveling
When one or more exhaustion tokens are removed from this Phoenixborn, place 1 wound token on this Phoenixborn. At the end of the round, move 1 die from your active pool to your exhausted pool.', '0', '8199', '1', NULL, NULL, 't'),
('340', 'Summon Deepwater Hammerhead', 'summon-deepwater-hammerhead', '{"cost": ["[[main]]", "3 [[time:class]]", "2 [[basic]]"], "dice": ["time"], "name": "Summon Deepwater Hammerhead", "stub": "summon-deepwater-hammerhead", "text": "[[main]] - [[exhaust]]: Place a [[Deepwater Hammerhead]] conjuration onto the battlefield.", "type": "Ready Spell", "weight": 508, "release": {"name": "The Scoundrels of the Sea", "stub": "the-scoundrels-of-the-sea", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"basic": 2, "time:class": 3}, "placement": "Spellboard", "conjurations": [{"name": "Deepwater Hammerhead", "stub": "deepwater-hammerhead"}]}', '23', 'Ready Spell', '508', '64', NULL, NULL, 't', 'Summon Deepwater Hammerhead
Place a Deepwater Hammerhead conjuration onto the battlefield.', '0', '8200', '1', NULL, NULL, 't'),
('341', 'Summon Riptide Siren', 'summon-riptide-siren', '{"cost": ["[[main]]", "1 [[time:class]]"], "dice": ["time"], "name": "Summon Riptide Siren", "stub": "summon-riptide-siren", "text": "[[main]] - [[exhaust]]: Discard the top 2 cards of your draw pile. If you do, place a [[Riptide Siren]] conjuration onto your battlefield.\n\nFocus 1: Discard 1 fewer card from the top of your draw pile.\n\nFocus 2: You may place 1 status token on a Riptide Siren you control.", "type": "Ready Spell", "weight": 106, "release": {"name": "The Scoundrels of the Sea", "stub": "the-scoundrels-of-the-sea", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"time:class": 1}, "placement": "Spellboard", "conjurations": [{"name": "Riptide Siren", "stub": "riptide-siren"}]}', '23', 'Ready Spell', '106', '64', NULL, NULL, 't', 'Summon Riptide Siren
Discard the top 2 cards of your draw pile. If you do, place a Riptide Siren conjuration onto your battlefield. Focus 1 Discard 1 fewer card from the top of your draw pile. Focus 2 You may place 1 status token on a Riptide Siren you control.', '0', '8201', '1', NULL, NULL, 't'),
('342', 'Whirlpool', 'whirlpool', '{"cost": ["[[main]]"], "dice": ["natural"], "name": "Whirlpool", "stub": "whirlpool", "text": "When a unit would deal damage by attacking or countering, you may spend 1 [[natural:class]] and place 1 exhaustion token on this card to reduce a target unit''s attack value by 1 until the end of the turn.\n\nFocus 1: You may reduce that unit''s attack value by an additional 1.\n\nFocus 2: Then, you may reduce that unit''s attack value by an additional 1.", "type": "Ready Spell", "weight": 5, "release": {"name": "The Scoundrels of the Sea", "stub": "the-scoundrels-of-the-sea", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "placement": "Spellboard", "effectMagicCost": {"natural:class": 1}}', '23', 'Ready Spell', '5', '8', NULL, NULL, 'f', 'Whirlpool
When a unit would deal damage by attacking or countering, you may spend 1 natural:class and place 1 exhaustion token on this card to reduce a target unit''s attack value by 1 until the end of the turn. Focus 1 You may reduce that unit''s attack value by an additional 1. Focus 2 Then, you may reduce that unit''s attack value by an additional 1.', '0', '8202', '1', NULL, NULL, 't'),
('343', 'The Perfect Storm', 'the-perfect-storm', '{"cost": ["[[main]]", "2 [[basic]]"], "name": "The Perfect Storm", "stub": "the-perfect-storm", "text": "Deal 2 damage to each unit without any status tokens on them.", "type": "Action Spell", "weight": 205, "release": {"name": "The Scoundrels of the Sea", "stub": "the-scoundrels-of-the-sea", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"basic": 2}, "placement": "Discard", "phoenixborn": "Devlin Longbow"}', '23', 'Action Spell', '205', '0', 'Devlin Longbow', NULL, 'f', 'The Perfect Storm
Deal 2 damage to each unit without any status tokens on them.', '0', '8203', '1', NULL, NULL, 't'),
('344', 'Devlin Longbow', 'devlin-longbow', '{"life": 19, "name": "Devlin Longbow", "stub": "devlin-longbow", "text": "Trial by Fire: [[side]] - [[exhaust]] - 1 [[basic]]: Choose a target unexhausted unit you control and a target unexhausted unit an opponent controls. Those units deal damage to each other equal to their attack value. If only one of those units remains in play afterward, place 1 status token on it.", "type": "Phoenixborn", "release": {"name": "The Scoundrels of the Sea", "stub": "the-scoundrels-of-the-sea", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "spellboard": 3, "battlefield": 6, "effectMagicCost": {"basic": 1}}', '23', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Devlin Longbow
Trial by Fire Choose a target unexhausted unit you control and a target unexhausted unit an opponent controls. Those units deal damage to each other equal to their attack value. If only one of those units remains in play afterward, place 1 status token on it.', '0', '8204', '1', NULL, NULL, 't'),
('345', 'Deepwater Hammerhead', 'deepwater-hammerhead', '{"life": 4, "name": "Deepwater Hammerhead", "stub": "deepwater-hammerhead", "text": "* Consume: Whenever an opponent''s unit is destroyed as a result of a spell, attack, counter, ability, or dice power you control, place 1 status token on this unit. If the destroyed unit was an ally, remove it from the game.\n\n* Blood in the Water: Whenever a conjuration would leave play, you may remove 3 status tokens from this card. If you do, until the end of the turn whenever a conjuration would be removed from the game, discard it instead.", "type": "Conjuration", "attack": 3, "copies": 2, "recover": 1, "release": {"name": "The Scoundrels of the Sea", "stub": "the-scoundrels-of-the-sea", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "placement": "Battlefield"}', '23', 'Conjuration', '0', '0', NULL, '2', 'f', 'Deepwater Hammerhead
Consume Whenever an opponent''s unit is destroyed as a result of a spell, attack, counter, ability, or dice power you control, place 1 status token on this unit. If the destroyed unit was an ally, remove it from the game. Blood in the Water Whenever a conjuration would leave play, you may remove 3 status tokens from this card. If you do, until the end of the turn whenever a conjuration would be removed from the game, discard it instead.', '0', '8205', '1', NULL, NULL, 't'),
('346', 'Riptide Siren', 'riptide-siren', '{"life": 2, "name": "Riptide Siren", "stub": "riptide-siren", "text": "Entrancing Melody: [[main]]: Remove 1 status token from this unit. If you do, choose a card in a target discard pile. Either shuffle that card into its owner''s draw pile, or remove it from the game.", "type": "Conjuration", "attack": 2, "copies": 4, "recover": 0, "release": {"name": "The Scoundrels of the Sea", "stub": "the-scoundrels-of-the-sea", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "placement": "Battlefield"}', '23', 'Conjuration', '0', '0', NULL, '4', 'f', 'Riptide Siren
Entrancing Melody Remove 1 status token from this unit. If you do, choose a card in a target discard pile. Either shuffle that card into its owner''s draw pile, or remove it from the game.', '0', '8206', '1', NULL, NULL, 't'),
('347', 'Alchemist', 'alchemist', '{"cost": ["[[main]]", "1 [[time:power]] : 1 [[basic]]"], "dice": ["time"], "life": 3, "name": "Alchemist", "stub": "alchemist", "text": "Create Elixir: [[side]]: Place a die from your active pool onto this card on a class side.\n\n* Consume Elixir: You may exhaust dice on this card as if they were in your active pool when paying costs of cards in your hand or the activation costs of ready spells.", "type": "Ally", "attack": 1, "weight": 5, "recover": 1, "release": {"name": "The Mad Doctor", "stub": "the-mad-doctor", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"time:power": 1}, "placement": "Battlefield"}', '24', 'Ally', '5', '64', NULL, NULL, 'f', 'Alchemist
Create Elixir Place a die from your active pool onto this card on a class side. Consume Elixir You may exhaust dice on this card as if they were in your active pool when paying costs of cards in your hand or the activation costs of ready spells.', '0', '8207', '1', NULL, NULL, 't'),
('348', 'Cheat Death', 'cheat-death', '{"cost": ["1 [[time:class]]"], "dice": ["time"], "name": "Cheat Death", "stub": "cheat-death", "text": "You may play this spell when a unit would be destroyed or removed from the game.\n\nPrevent that destruction or removal. If the unit is an ally you control, place it in your hand. Otherwise, discard that unit and draw 1 card.", "type": "Reaction Spell", "weight": 101, "release": {"name": "The Mad Doctor", "stub": "the-mad-doctor", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"time:class": 1}, "placement": "Discard"}', '24', 'Reaction Spell', '101', '64', NULL, NULL, 'f', 'Cheat Death
You may play this spell when a unit would be destroyed or removed from the game. Prevent that destruction or removal. If the unit is an ally you control, place it in your hand. Otherwise, discard that unit and draw 1 card.', '0', '8208', '1', NULL, NULL, 't'),
('349', 'Dark Procurement', 'dark-procurement', '{"cost": ["[[main]]", "1 [[ceremonial:class]]"], "dice": ["ceremonial"], "name": "Dark Procurement", "stub": "dark-procurement", "text": "When this spell comes into play, re-roll up to 1 die in your exhausted pool and place it into your active pool.\n\nWhen an ally would be placed in a player''s discard pile from the battlefield, you may place 1 exhaustion token on this spell. If you do, place that ally under your Phoenixborn face down instead of placing it in its owner''s discard pile.", "type": "Ready Spell", "weight": 106, "release": {"name": "The Mad Doctor", "stub": "the-mad-doctor", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"ceremonial:class": 1}, "placement": "Spellboard", "diceRecursion": 1}', '24', 'Ready Spell', '106', '1', NULL, NULL, 'f', 'Dark Procurement
When this spell comes into play, re-roll up to 1 die in your exhausted pool and place it into your active pool. When an ally would be placed in a player''s discard pile from the battlefield, you may place 1 exhaustion token on this spell. If you do, place that ally under your Phoenixborn face down instead of placing it in its owner''s discard pile.', '0', '8209', '1', NULL, NULL, 't'),
('350', 'Nihilist', 'nihilist', '{"cost": ["[[main]]", "1 [[time:class]]"], "dice": ["time"], "life": 2, "name": "Nihilist", "stub": "nihilist", "text": "One with Nothing: [[main]] - [[exhaust]]: Place 1 wound token on a target unit and 1 wound token on a target Phoenixborn. Then, destroy this unit.\n\n~ Entombed: This unit cannot be placed in your hand from a discard pile through abilities or dice powers.", "type": "Ally", "attack": 0, "weight": 106, "recover": 0, "release": {"name": "The Mad Doctor", "stub": "the-mad-doctor", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"time:class": 1}, "placement": "Battlefield"}', '24', 'Ally', '106', '64', NULL, NULL, 'f', 'Nihilist
One with Nothing Place 1 wound token on a target unit and 1 wound token on a target Phoenixborn. Then, destroy this unit. Entombed This unit cannot be placed in your hand from a discard pile through abilities or dice powers.', '0', '8210', '1', NULL, NULL, 't'),
('351', 'Plague Doctor', 'plague-doctor', '{"cost": ["[[main]]", "1 [[ceremonial:power]]", "1 [[time:class]]", "1 [[basic]]"], "dice": ["ceremonial", "time"], "life": 4, "name": "Plague Doctor", "stub": "plague-doctor", "text": "Deathstrike: When this unit deals 1 or more damage to a unit it is attacking or countering, destroy that unit.\n\nAlert: Do not place an exhaustion token on this unit as a result of it countering.", "type": "Ally", "attack": 1, "weight": 308, "recover": 2, "release": {"name": "The Mad Doctor", "stub": "the-mad-doctor", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"basic": 1, "time:class": 1, "ceremonial:power": 1}, "placement": "Battlefield"}', '24', 'Ally', '308', '65', NULL, NULL, 'f', 'Plague Doctor
Deathstrike When this unit deals 1 or more damage to a unit it is attacking or countering, destroy that unit. Alert Do not place an exhaustion token on this unit as a result of it countering.', '0', '8211', '1', NULL, NULL, 't'),
('352', 'Reaper''s Rescue', 'reapers-rescue', '{"cost": ["1 [[ceremonial:class]]"], "dice": ["ceremonial"], "name": "Reaper''s Rescue", "stub": "reapers-rescue", "text": "You may play this spell when an opponent''s spell, ability, or dice power targets a unit you control or would become attached to it. If you do, draw 1 card, then select 1 die in your exhausted pool, re-roll it, and place it in your active pool.\n\nDestroy the targeted unit and cancel all remaining effects of that spell, ability, or dice power.", "type": "Reaction Spell", "weight": 101, "release": {"name": "The Mad Doctor", "stub": "the-mad-doctor", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"ceremonial:class": 1}, "placement": "Discard", "diceRecursion": 1}', '24', 'Reaction Spell', '101', '1', NULL, NULL, 'f', 'Reaper''s Rescue
You may play this spell when an opponent''s spell, ability, or dice power targets a unit you control or would become attached to it. If you do, draw 1 card, then select 1 die in your exhausted pool, re-roll it, and place it in your active pool. Destroy the targeted unit and cancel all remaining effects of that spell, ability, or dice power.', '0', '8212', '1', NULL, NULL, 't'),
('353', 'Soul Augur', 'soul-augur', '{"cost": ["[[main]]", "1 [[ceremonial:class]]", "1 [[time:class]]"], "dice": ["ceremonial", "time"], "life": 2, "name": "Soul Augur", "stub": "soul-augur", "text": "Fateful Arrival: When this unit leaves play, search your draw pile for an ally card with a name other than Soul Augur, reveal it, and place it in your hand. Shuffle your draw pile.", "type": "Ally", "attack": 2, "weight": 207, "recover": 0, "release": {"name": "The Mad Doctor", "stub": "the-mad-doctor", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"time:class": 1, "ceremonial:class": 1}, "placement": "Battlefield"}', '24', 'Ally', '207', '65', NULL, NULL, 'f', 'Soul Augur
Fateful Arrival When this unit leaves play, search your draw pile for an ally card with a name other than Soul Augur, reveal it, and place it in your hand. Shuffle your draw pile.', '0', '8213', '1', NULL, NULL, 't'),
('354', 'Summon Necromantic Abomination', 'summon-necromantic-abomination', '{"cost": ["[[main]]"], "dice": ["ceremonial", "time"], "name": "Summon Necromantic Abomination", "stub": "summon-necromantic-abomination", "text": "[[main]] - [[exhaust]] - 1 [[ceremonial:class]] - 1 [[time:class]]: Reveal any number of ally cards from your hand and face down under your Phoenixborn. Place a [[Necromantic Abomination]] conjuration onto the battlefield, and place all revealed ally cards face down underneath that unit.\n\nFocus 1: You may place 1 additional ally from your discard pile face down underneath that [[Necromantic Abomination]].\n\nFocus 2: Move any number of face down ally cards from under a [[Necromantic Abomination]] you control to another [[Necromantic Abomination]] you control.", "type": "Ready Spell", "weight": 5, "release": {"name": "The Mad Doctor", "stub": "the-mad-doctor", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "placement": "Spellboard", "conjurations": [{"name": "Necromantic Abomination", "stub": "necromantic-abomination"}], "effectMagicCost": {"time:class": 1, "ceremonial:class": 1}}', '24', 'Ready Spell', '5', '65', NULL, NULL, 't', 'Summon Necromantic Abomination
Reveal any number of ally cards from your hand and face down under your Phoenixborn. Place a Necromantic Abomination conjuration onto the battlefield, and place all revealed ally cards face down underneath that unit. Focus 1 You may place 1 additional ally from your discard pile face down underneath that Necromantic Abomination. Focus 2 Move any number of face down ally cards from under a Necromantic Abomination you control to another Necromantic Abomination you control.', '0', '8214', '1', NULL, NULL, 't'),
('355', 'Summon Reaper Mount', 'summon-reaper-mount', '{"cost": ["[[main]]", "1 [[basic]]"], "dice": ["ceremonial", "time"], "name": "Summon Reaper Mount", "stub": "summon-reaper-mount", "text": "[[side]] - [[exhaust]] - 1 [[ceremonial:class]] - 1 [[time:class]]: Remove an unexhausted ally you control from play. If you do, place a [[Reaper Mount]] conjuration onto your battlefield and place that ally face down under that unit.", "type": "Ready Spell", "weight": 105, "release": {"name": "The Mad Doctor", "stub": "the-mad-doctor", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "magicCost": {"basic": 1}, "placement": "Spellboard", "conjurations": [{"name": "Reaper Mount", "stub": "reaper-mount"}], "effectMagicCost": {"time:class": 1, "ceremonial:class": 1}}', '24', 'Ready Spell', '105', '65', NULL, NULL, 't', 'Summon Reaper Mount
Remove an unexhausted ally you control from play. If you do, place a Reaper Mount conjuration onto your battlefield and place that ally face down under that unit.', '0', '8215', '1', NULL, NULL, 't'),
('356', 'Extend Animation', 'extend-animation', '{"cost": ["[[main]]"], "dice": ["ceremonial"], "name": "Extend Animation", "stub": "extend-animation", "text": "When a unit with no inexhaustible abilities would be destroyed, you may spend 1 [[ceremonial:class]], 1 [[basic]], and place 1 exhaustion token on this card. If you do, remove all tokens, attached cards, and dice from that unit. Then, instead of destroying it, place it on your battlefield with an [[Unnatural]] conjured alteration spell attached to it.\n\nFocus 2: You may choose not to attach an [[Unnatural]] conjured alteration spell to that unit.", "type": "Ready Spell", "weight": 5, "release": {"name": "The Mad Doctor", "stub": "the-mad-doctor", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "placement": "Spellboard", "phoenixborn": "Plutarch Eastgate", "conjurations": [{"name": "Unnatural", "stub": "unnatural"}], "effectMagicCost": {"basic": 1, "ceremonial:class": 1}}', '24', 'Ready Spell', '5', '1', 'Plutarch Eastgate', NULL, 'f', 'Extend Animation
When a unit with no inexhaustible abilities would be destroyed, you may spend 1 ceremonial:class, 1 basic, and place 1 exhaustion token on this card. If you do, remove all tokens, attached cards, and dice from that unit. Then, instead of destroying it, place it on your battlefield with an Unnatural conjured alteration spell attached to it. Focus 2 You may choose not to attach an Unnatural conjured alteration spell to that unit.', '0', '8216', '1', NULL, NULL, 't'),
('357', 'Imbued Vigor', 'imbued-vigor', '{"name": "Imbued Vigor", "stub": "imbued-vigor", "text": "* Discard this alteration at the beginning of your turn.\n\nThis unit now has the following ability:\n\n* Dauntless: If this unit recevies damage in battle, remove 1 exhaustion token from this unit at the end of that battle.", "type": "Conjured Alteration Spell", "attack": "+1", "copies": 1, "release": {"name": "The Mad Doctor", "stub": "the-mad-doctor", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "placement": "Unit", "phoenixborn": "Plutarch Eastgate"}', '24', 'Conjured Alteration Spell', '0', '0', 'Plutarch Eastgate', '1', 'f', 'Imbued Vigor
Discard this alteration at the beginning of your turn. This unit now has the following ability: Dauntless If this unit recevies damage in battle, remove 1 exhaustion token from this unit at the end of that battle.', '0', '8217', '1', NULL, NULL, 't'),
('358', 'Unnatural', 'unnatural', '{"name": "Unnatural", "stub": "unnatural", "text": "* This unit is considered to have no abilities.\n\n* If this alteration would become unattached from this unit, discard this card and destroy the attached unit instead.", "type": "Conjured Alteration Spell", "copies": 5, "recover": "-3", "release": {"name": "The Mad Doctor", "stub": "the-mad-doctor", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "placement": "Unit", "phoenixborn": "Plutarch Eastgate"}', '24', 'Conjured Alteration Spell', '0', '0', 'Plutarch Eastgate', '5', 'f', 'Unnatural
This unit is considered to have no abilities. If this alteration would become unattached from this unit, discard this card and destroy the attached unit instead.', '0', '8218', '1', NULL, NULL, 't'),
('359', 'Necromantic Abomination', 'necromantic-abomination', '{"life": 1, "name": "Necromantic Abomination", "stub": "necromantic-abomination", "text": "Terrifying 1: This unit cannot be blocked or guarded against by units with an attack value of 1 or less.\n\n* Extra Limbs: For each face down card under this unit, add 1 to this unit''s attack and life values.\n\n* Slough: When this unit would receive damage, you may discard a face down card underneath this unit to prevent that damage.", "type": "Conjuration", "attack": 1, "copies": 2, "recover": 0, "release": {"name": "The Mad Doctor", "stub": "the-mad-doctor", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "placement": "Battlefield"}', '24', 'Conjuration', '0', '0', NULL, '2', 'f', 'Necromantic Abomination
Terrifying 1 This unit cannot be blocked or guarded against by units with an attack value of 1 or less. Extra Limbs For each face down card under this unit, add 1 to this unit''s attack and life values. Slough When this unit would receive damage, you may discard a face down card underneath this unit to prevent that damage.', '0', '8219', '1', NULL, NULL, 't'),
('360', 'Plutarch Eastgate', 'plutarch-eastgate', '{"life": 19, "name": "Plutarch Eastgate", "stub": "plutarch-eastgate", "text": "Gather Specimens: At the end of the prepare phase, you may place 1 ally from any discard pile face down under this card.\n\nExtract Essence: [[side]]: Discard 1 face down card from this card. If that card is an ally, attach an [[Imbued Vigor]] conjured alteration spell to a target unit.", "type": "Phoenixborn", "release": {"name": "The Mad Doctor", "stub": "the-mad-doctor", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "spellboard": 4, "battlefield": 5, "conjurations": [{"name": "Imbued Vigor", "stub": "imbued-vigor"}]}', '24', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Plutarch Eastgate
Gather Specimens At the end of the prepare phase, you may place 1 ally from any discard pile face down under this card. Extract Essence Discard 1 face down card from this card. If that card is an ally, attach an Imbued Vigor conjured alteration spell to a target unit.', '0', '8220', '1', NULL, NULL, 't'),
('361', 'Reaper Mount', 'reaper-mount', '{"life": 3, "name": "Reaper Mount", "stub": "reaper-mount", "text": "Stalk: This unit cannot be guarded against.\n\n* Unsummon: [[main]]: Discard this unit.\n\n* Dismount Rider: After this unit leaves play, choose a face down ally that was under this unit and dismount that ally.", "type": "Conjuration", "attack": 3, "copies": 2, "recover": 0, "release": {"name": "The Mad Doctor", "stub": "the-mad-doctor", "is_phg": false, "is_promo": false, "is_legacy": true, "is_retiring": true}, "is_legacy": true, "placement": "Battlefield"}', '24', 'Conjuration', '0', '0', NULL, '2', 'f', 'Reaper Mount
Stalk This unit cannot be guarded against. Unsummon Discard this unit. Dismount Rider After this unit leaves play, choose a face down ally that was under this unit and dismount that ally.', '0', '8221', '1', NULL, NULL, 't'),
('362', 'Jessa Na Ni', 'jessa-na-ni', '{"life": 19, "name": "Jessa Na Ni", "stub": "jessa-na-ni", "text": "Screams of the Departed: Once per turn, after a unit is destroyed, you may spend 1 [[basic]] to deal 1 damage to a target Phoenixborn.", "type": "Phoenixborn", "release": {"name": "Master Set", "stub": "master-set"}, "spellboard": 4, "battlefield": 4, "effectRepeats": true}', '25', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Jessa Na Ni
Screams of the Departed: Once per turn, after a unit is destroyed, you may spend 1 basic to deal 1 damage to a target Phoenixborn.', '0', '9947', '1', NULL, NULL, 'f'),
('363', 'Fear', 'fear', '{"cost": ["[[main]]", "1 [[basic]]"], "dice": ["basic"], "name": "Fear", "stub": "fear", "text": "Destroy a unit you control. If you do, remove wound tokens from your Phoenixborn equal to the destroyed unit''s recover value and then discard a target unit an opponent controls.", "type": "Action Spell", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"basic": 1}, "placement": "Discard", "phoenixborn": "Jessa Na Ni"}', '25', 'Action Spell', '105', '0', 'Jessa Na Ni', NULL, 'f', 'Fear
Destroy a unit you control. If you do, remove wound tokens from your Phoenixborn equal to the destroyed unit''s recover value and then discard a target unit an opponent controls.', '0', '9948', '1', NULL, NULL, 'f'),
('364', 'Blood Puppet', 'blood-puppet', '{"life": 2, "name": "Blood Puppet", "stub": "blood-puppet", "text": "Cursed 1: At the end of each round, place 1 wound token on your Phoenixborn.\n\nSelf Inflict 1: [[side]] - 1 [[basic]]: Deal 1 damage to this unit.", "type": "Conjuration", "attack": 0, "copies": 5, "recover": 0, "release": {"name": "Master Set", "stub": "master-set"}, "placement": "Battlefield", "effectRepeats": true}', '25', 'Conjuration', '0', '0', NULL, '5', 'f', 'Blood Puppet
Cursed 1: At the end of each round, place 1 wound token on your Phoenixborn. Self Inflict 1: side - 1 basic: Deal 1 damage to this unit.', '0', '9949', '1', NULL, NULL, 'f'),
('365', 'Summon Blood Puppet', 'summon-blood-puppet', '{"cost": ["[[main]]"], "dice": ["ceremonial"], "name": "Summon Blood Puppet", "stub": "summon-blood-puppet", "text": "[[main]] - 1 [[ceremonial:class]] - [[exhaust]]: Place a [[Blood Puppet]] conjuration onto a target player''s battlefield.", "type": "Ready Spell", "release": {"name": "Master Set", "stub": "master-set"}, "placement": "Spellboard", "conjurations": [{"name": "Blood Puppet", "stub": "blood-puppet"}]}', '25', 'Ready Spell', '5', '1', NULL, NULL, 't', 'Summon Blood Puppet
main - 1 ceremonial:class - exhaust: Place a Blood Puppet conjuration onto a target player''s battlefield.', '0', '9950', '1', NULL, NULL, 'f'),
('366', 'Blood Transfer', 'blood-transfer', '{"cost": ["[[main]]"], "dice": ["charm", "ceremonial"], "name": "Blood Transfer", "stub": "blood-transfer", "text": "[[side]] - [[exhaust]] - 1 [[charm:class]] - 1 [[ceremonial:class]]: Deal 2 damage to a target unit you control. If you do, you may remove 2 wound tokens from another unit you control or remove 1 wound token from your Phoenixborn.", "type": "Ready Spell", "release": {"name": "Master Set", "stub": "master-set"}, "placement": "Spellboard"}', '25', 'Ready Spell', '5', '3', NULL, NULL, 'f', 'Blood Transfer
side - exhaust - 1 charm:class - 1 ceremonial:class: Deal 2 damage to a target unit you control. If you do, you may remove 2 wound tokens from another unit you control or remove 1 wound token from your Phoenixborn.', '0', '9951', '1', NULL, NULL, 'f'),
('367', 'Cut The Strings', 'cut-the-strings', '{"cost": ["[[main]]"], "dice": ["ceremonial"], "name": "Cut The Strings", "stub": "cut-the-strings", "text": "[[side]] - [[exhaust]] - 1 [[ceremonial:class]] - 1 [[basic]]: Deal 2 damage to a unit you control. If you do, you may discard a target alteration spell.", "type": "Ready Spell", "release": {"name": "Master Set", "stub": "master-set"}, "placement": "Spellboard"}', '25', 'Ready Spell', '5', '1', NULL, NULL, 'f', 'Cut The Strings
side - exhaust - 1 ceremonial:class - 1 basic: Deal 2 damage to a unit you control. If you do, you may discard a target alteration spell.', '0', '9952', '1', NULL, NULL, 'f'),
('368', 'Living Doll', 'living-doll', '{"cost": ["[[main]]", "1 [[ceremonial:class]]", ["1 [[charm:class]]", "1 [[sympathy:class]]"]], "dice": ["ceremonial", "charm"], "life": 3, "name": "Living Doll", "stub": "living-doll", "text": "Pain Link 1: [[side]]: Move 1 wound token from this unit onto a target Phoenixborn.", "type": "Ally", "attack": 0, "altDice": ["charm", "sympathy"], "recover": 1, "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"ceremonial:class": 1, "charm:class / sympathy:class": 1}, "placement": "Battlefield"}', '25', 'Ally', '207', '1', NULL, NULL, 'f', 'Living Doll
Pain Link 1: side: Move 1 wound token from this unit onto a target Phoenixborn.', '34', '9953', '1', NULL, NULL, 'f'),
('369', 'Blood Shaman', 'blood-shaman', '{"cost": ["[[main]]", "1 [[ceremonial:class]]"], "dice": ["ceremonial"], "life": 2, "name": "Blood Shaman", "stub": "blood-shaman", "text": "* Blood Ritual 1: When this unit is destroyed as a result of a spell, ability, or dice power you control, you may remove 1 wound token from your Phoenixborn and then raise 1 die in your active pool one level.", "type": "Ally", "attack": 0, "recover": 1, "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"ceremonial:class": 1}, "placement": "Battlefield"}', '25', 'Ally', '106', '1', NULL, NULL, 'f', 'Blood Shaman
* Blood Ritual 1: When this unit is destroyed as a result of a spell, ability, or dice power you control, you may remove 1 wound token from your Phoenixborn and then raise 1 die in your active pool one level.', '0', '9954', '1', NULL, NULL, 'f'),
('370', 'Blood Archer', 'blood-archer', '{"cost": ["[[main]]", "1 [[ceremonial:power]]", "1 [[charm:class]]", "1 [[basic]]"], "dice": ["ceremonial", "charm"], "life": 3, "name": "Blood Archer", "stub": "blood-archer", "text": "Blood Shot: [[side]]: Place 1 wound token on this unit to deal 1 damage to a target unit.", "type": "Ally", "attack": 3, "recover": 2, "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"basic": 1, "charm:class": 1, "ceremonial:power": 1}, "placement": "Battlefield"}', '25', 'Ally', '308', '3', NULL, NULL, 'f', 'Blood Archer
Blood Shot: side: Place 1 wound token on this unit to deal 1 damage to a target unit.', '0', '9955', '1', NULL, NULL, 'f'),
('371', 'Final Cry', 'final-cry', '{"cost": ["1 [[ceremonial:power]]"], "dice": ["ceremonial"], "name": "Final Cry", "stub": "final-cry", "text": "You may play this spell after a unit you control is destroyed. Deal 2 damage to a target Phoenixborn.", "type": "Reaction Spell", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"ceremonial:power": 1}, "placement": "Discard"}', '25', 'Reaction Spell', '102', '1', NULL, NULL, 'f', 'Final Cry
You may play this spell after a unit you control is destroyed. Deal 2 damage to a target Phoenixborn.', '0', '9956', '1', NULL, NULL, 'f'),
('372', 'Redirect', 'redirect', '{"cost": ["1 [[charm:power]]"], "dice": ["charm"], "name": "Redirect", "stub": "redirect", "text": "You may play this spell after your Phoenixborn is dealt damage if you control at least 1 unit. Choose a unit you control to receive that damage instead.", "type": "Reaction Spell", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"charm:power": 1}, "placement": "Discard"}', '25', 'Reaction Spell', '102', '2', NULL, NULL, 'f', 'Redirect
You may play this spell after your Phoenixborn is dealt damage if you control at least 1 unit. Choose a unit you control to receive that damage instead.', '0', '9957', '1', NULL, NULL, 'f'),
('373', 'Undying Heart', 'undying-heart', '{"cost": ["[[side]]", "1 [[charm:class]]"], "dice": ["charm"], "life": "+1", "name": "Undying Heart", "stub": "undying-heart", "text": "This unit now has the following ability:\n\n* Undying: When this unit is destroyed, if it is an ally, you may place it into its owner''s hand.", "type": "Alteration Spell", "recover": "+1", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"charm:class": 1}, "placement": "Unit"}', '25', 'Alteration Spell', '105', '2', NULL, NULL, 'f', 'Undying Heart
This unit now has the following ability: * Undying: When this unit is destroyed, if it is an ally, you may place it into its owner''s hand.', '0', '9958', '1', NULL, NULL, 'f'),
('374', 'Aradel Summergaard', 'aradel-summergaard', '{"dice": ["natural"], "life": 16, "name": "Aradel Summergaard", "stub": "aradel-summergaard", "text": "Water Blast: [[side]] - [[exhaust]] - 1 [[natural:class]]: Deal 2 damage to a target unit.", "type": "Phoenixborn", "release": {"name": "Master Set", "stub": "master-set"}, "spellboard": 4, "battlefield": 8}', '25', 'Phoenixborn', '0', '8', NULL, NULL, 'f', 'Aradel Summergaard
Water Blast: side - exhaust - 1 natural:class: Deal 2 damage to a target unit.', '0', '9959', '1', NULL, NULL, 'f'),
('375', 'Blue Jaguar', 'blue-jaguar', '{"life": 2, "name": "Blue Jaguar", "stub": "blue-jaguar", "text": "Gaze: When this unit is declared as an attacker, you may choose a target unit an opponent controls. That unit cannot block or guard for the remainder of the turn.", "type": "Conjuration", "attack": 1, "copies": 2, "recover": 0, "release": {"name": "Master Set", "stub": "master-set"}, "placement": "Battlefield", "phoenixborn": "Aradel Summergaard"}', '25', 'Conjuration', '0', '0', 'Aradel Summergaard', '2', 'f', 'Blue Jaguar
Gaze: When this unit is declared as an attacker, you may choose a target unit an opponent controls. That unit cannot block or guard for the remainder of the turn.', '0', '9960', '1', NULL, NULL, 'f'),
('376', 'Summon Blue Jaguar', 'summon-blue-jaguar', '{"cost": ["[[main]]"], "name": "Summon Blue Jaguar", "stub": "summon-blue-jaguar", "text": "[[main]] - [[exhaust]] - 2 [[basic]]: Place a [[Blue Jaguar]] conjuration onto your battlefield.", "type": "Ready Spell", "release": {"name": "Master Set", "stub": "master-set"}, "placement": "Spellboard", "phoenixborn": "Aradel Summergaard", "conjurations": [{"name": "Blue Jaguar", "stub": "blue-jaguar"}]}', '25', 'Ready Spell', '5', '0', 'Aradel Summergaard', NULL, 't', 'Summon Blue Jaguar
main - exhaust - 2 basic: Place a Blue Jaguar conjuration onto your battlefield.', '0', '9961', '1', NULL, NULL, 'f'),
('377', 'Mist Spirit', 'mist-spirit', '{"life": 1, "name": "Mist Spirit", "stub": "mist-spirit", "type": "Conjuration", "attack": 1, "copies": 10, "recover": 0, "release": {"name": "Master Set", "stub": "master-set"}, "placement": "Battlefield"}', '25', 'Conjuration', '0', '0', NULL, '10', 'f', 'Mist Spirit
', '0', '9962', '1', NULL, NULL, 'f'),
('378', 'Summon Mist Spirit', 'summon-mist-spirit', '{"cost": ["[[main]]"], "dice": ["illusion"], "name": "Summon Mist Spirit", "stub": "summon-mist-spirit", "text": "[[main]] - [[exhaust]] - 1 [[illusion:class]]: Place a [[Mist Spirit]] conjuration onto your battlefield. You may spend an additional 1 [[basic]] when activating this spell to place an additional [[Mist Spirit]] conjuration onto your battlefield.", "type": "Ready Spell", "release": {"name": "Master Set", "stub": "master-set"}, "placement": "Spellboard", "conjurations": [{"name": "Mist Spirit", "stub": "mist-spirit"}]}', '25', 'Ready Spell', '5', '4', NULL, NULL, 't', 'Summon Mist Spirit
main - exhaust - 1 illusion:class: Place a Mist Spirit conjuration onto your battlefield. You may spend an additional 1 basic when activating this spell to place an additional Mist Spirit conjuration onto your battlefield.', '0', '9963', '1', NULL, NULL, 'f'),
('379', 'Butterfly Monk', 'butterfly-monk', '{"life": 1, "name": "Butterfly Monk", "stub": "butterfly-monk", "text": "Unit Guard: This unit may guard a unit that is being attacked.\n\n* Mend 1: When this unit is destroyed, you may remove 1 wound token from a target unit or Phoenixborn.", "type": "Conjuration", "attack": 1, "copies": 2, "recover": 0, "release": {"name": "Master Set", "stub": "master-set"}, "placement": "Battlefield"}', '25', 'Conjuration', '0', '0', NULL, '2', 'f', 'Butterfly Monk
Unit Guard: This unit may guard a unit that is being attacked. * Mend 1: When this unit is destroyed, you may remove 1 wound token from a target unit or Phoenixborn.', '0', '9964', '1', NULL, NULL, 'f'),
('380', 'Summon Butterfly Monk', 'summon-butterfly-monk', '{"cost": ["[[main]]"], "dice": ["natural"], "name": "Summon Butterfly Monk", "stub": "summon-butterfly-monk", "text": "[[main]] - [[exhaust]] - 1 [[natural:power]]: Place a [[Butterfly Monk]] conjuration onto your battlefield.", "type": "Ready Spell", "release": {"name": "Master Set", "stub": "master-set"}, "placement": "Spellboard", "conjurations": [{"name": "Butterfly Monk", "stub": "butterfly-monk"}]}', '25', 'Ready Spell', '5', '8', NULL, NULL, 't', 'Summon Butterfly Monk
main - exhaust - 1 natural:power: Place a Butterfly Monk conjuration onto your battlefield.', '0', '9965', '1', NULL, NULL, 'f'),
('381', 'Shifting Mist', 'shifting-mist', '{"cost": ["[[main]]", "1 [[illusion:class]]"], "dice": ["illusion"], "name": "Shifting Mist", "stub": "shifting-mist", "text": "[[side]] - [[exhaust]]: Change 2 dice in your active pool to a side of your choice.", "type": "Ready Spell", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"illusion:class": 1}, "placement": "Spellboard"}', '25', 'Ready Spell', '106', '4', NULL, NULL, 'f', 'Shifting Mist
side - exhaust: Change 2 dice in your active pool to a side of your choice.', '0', '9966', '1', NULL, NULL, 'f'),
('382', 'Mist Typhoon', 'mist-typhoon', '{"cost": ["[[main]]", "1 [[illusion:class]]", "1 [[natural:class]]"], "dice": ["illusion", "natural"], "name": "Mist Typhoon", "stub": "mist-typhoon", "text": "Deal 1 damage to all opponent''s units. You may draw 1 card.", "type": "Action Spell", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"natural:class": 1, "illusion:class": 1}, "placement": "Discard"}', '25', 'Action Spell', '207', '12', NULL, NULL, 'f', 'Mist Typhoon
Deal 1 damage to all opponent''s units. You may draw 1 card.', '0', '9967', '1', NULL, NULL, 'f'),
('383', 'Steady Gaze', 'steady-gaze', '{"cost": ["[[main]]", "2 [[illusion:class]]"], "dice": ["illusion"], "name": "Steady Gaze", "stub": "steady-gaze", "text": "Place 2 exhaustion tokens on a target unit.", "type": "Action Spell", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"illusion:class": 2}, "placement": "Discard"}', '25', 'Action Spell', '207', '4', NULL, NULL, 'f', 'Steady Gaze
Place 2 exhaustion tokens on a target unit.', '0', '9968', '1', NULL, NULL, 'f'),
('384', 'Out Of The Mist', 'out-of-the-mist', '{"cost": ["[[side]]", "1 [[illusion:power]]", "1 [[natural:power]]"], "dice": ["illusion", "natural"], "name": "Out Of The Mist", "stub": "out-of-the-mist", "text": "Deal X amount of damage to a target unit. You may draw 1 card.\n\nX = the number of units you have in play.", "type": "Action Spell", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"natural:power": 1, "illusion:power": 1}, "placement": "Discard"}', '25', 'Action Spell', '208', '12', NULL, NULL, 'f', 'Out Of The Mist
Deal X amount of damage to a target unit. You may draw 1 card. X = the number of units you have in play.', '0', '9969', '1', NULL, NULL, 'f'),
('385', 'Massive Growth', 'massive-growth', '{"cost": ["[[main]]", "1 [[natural:class]]", "1 [[basic]]"], "dice": ["natural"], "life": "+4", "name": "Massive Growth", "stub": "massive-growth", "text": "* This spell can only be attached to a unit with an attack value of 2 or less.\n\n* Spell Guard: This spell cannot be affected by an opponent''s spell.\n\n* Fleeting: Discard this card at the end of this round.", "type": "Alteration Spell", "attack": "+4", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"basic": 1, "natural:class": 1}, "placement": "Unit"}', '25', 'Alteration Spell', '206', '8', NULL, NULL, 'f', 'Massive Growth
* This spell can only be attached to a unit with an attack value of 2 or less. * Spell Guard: This spell cannot be affected by an opponent''s spell. * Fleeting: Discard this card at the end of this round.', '0', '9970', '1', NULL, NULL, 'f'),
('386', 'Reflections in the Water', 'reflections-in-the-water', '{"cost": ["[[side]]", ["1 [[illusion:class]]", "1 [[time:class]]"]], "dice": ["illusion"], "name": "Reflections in the Water", "stub": "reflections-in-the-water", "text": "* While this spell is attached to this unit, this unit is considered to have no abilities, including inexhaustible abilities.\n\n* Fleeting: Discard this card at the end of this round.", "type": "Alteration Spell", "altDice": ["time", "illusion"], "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"illusion:class / time:class": 1}, "placement": "Unit"}', '25', 'Alteration Spell', '105', '0', NULL, NULL, 'f', 'Reflections in the Water
* While this spell is attached to this unit, this unit is considered to have no abilities, including inexhaustible abilities. * Fleeting: Discard this card at the end of this round.', '68', '9971', '1', NULL, NULL, 'f'),
('387', 'Root Armor', 'root-armor', '{"cost": ["[[side]]", "1 [[natural:class]]"], "dice": ["natural"], "life": "+1", "name": "Root Armor", "stub": "root-armor", "text": "This unit now has the following ability:\n\n* Armored 1: After this unit is dealt damage, prevent 1 damage from being received.", "type": "Alteration Spell", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"natural:class": 1}, "placement": "Unit"}', '25', 'Alteration Spell', '105', '8', NULL, NULL, 'f', 'Root Armor
This unit now has the following ability: * Armored 1: After this unit is dealt damage, prevent 1 damage from being received.', '0', '9972', '1', NULL, NULL, 'f'),
('388', 'Saria Guideman', 'saria-guideman', '{"dice": ["charm"], "life": 20, "name": "Saria Guideman", "stub": "saria-guideman", "text": "Heart''s Pull: [[side]] - [[exhaust]] - 1 [[charm:class]]: You may draw 1 card. If you do, you may choose a target player to discard 1 card off the top of their draw pile.", "type": "Phoenixborn", "release": {"name": "Master Set", "stub": "master-set"}, "spellboard": 4, "battlefield": 5}', '25', 'Phoenixborn', '0', '2', NULL, NULL, 'f', 'Saria Guideman
Heart''s Pull: side - exhaust - 1 charm:class: You may draw 1 card. If you do, you may choose a target player to discard 1 card off the top of their draw pile.', '0', '9973', '1', NULL, NULL, 'f'),
('389', 'Seaside Raven', 'seaside-raven', '{"life": 2, "name": "Seaside Raven", "stub": "seaside-raven", "text": "Prey 2: When this unit comes into play, you may destroy a target unit with a life value of 2 or less.\n\nQuick Strike: While this unit is attacking, it deals its damage before units in battle with it.", "type": "Conjuration", "attack": 3, "copies": 1, "recover": 0, "release": {"name": "Master Set", "stub": "master-set"}, "placement": "Battlefield", "phoenixborn": "Saria Guideman"}', '25', 'Conjuration', '0', '0', 'Saria Guideman', '1', 'f', 'Seaside Raven
Prey 2: When this unit comes into play, you may destroy a target unit with a life value of 2 or less. Quick Strike: While this unit is attacking, it deals its damage before units in battle with it.', '0', '9974', '1', NULL, NULL, 'f'),
('390', 'Summon Seaside Raven', 'summon-seaside-raven', '{"cost": ["[[main]]"], "name": "Summon Seaside Raven", "stub": "summon-seaside-raven", "text": "[[main]] - [[exhaust]] - 3 [[basic]]: Place a [[Seaside Raven]] conjuration onto your battlefield.", "type": "Ready Spell", "release": {"name": "Master Set", "stub": "master-set"}, "placement": "Spellboard", "phoenixborn": "Saria Guideman", "conjurations": [{"name": "Seaside Raven", "stub": "seaside-raven"}]}', '25', 'Ready Spell', '5', '0', 'Saria Guideman', NULL, 't', 'Summon Seaside Raven
main - exhaust - 3 basic: Place a Seaside Raven conjuration onto your battlefield.', '0', '9975', '1', NULL, NULL, 'f'),
('391', 'Three-Eyed Owl', 'three-eyed-owl', '{"life": 2, "name": "Three-Eyed Owl", "stub": "three-eyed-owl", "text": "Memory Drain 1: [[main]] - [[exhaust]]: Choose a target player to discard 1 card of their choice from their hand.", "type": "Conjuration", "attack": 0, "copies": 3, "recover": 0, "release": {"name": "Master Set", "stub": "master-set"}, "placement": "Battlefield"}', '25', 'Conjuration', '0', '0', NULL, '3', 'f', 'Three-Eyed Owl
Memory Drain 1: main - exhaust: Choose a target player to discard 1 card of their choice from their hand.', '0', '9976', '1', NULL, NULL, 'f'),
('392', 'Summon Three-Eyed Owl', 'summon-three-eyed-owl', '{"cost": ["[[main]]"], "dice": ["charm"], "name": "Summon Three-Eyed Owl", "stub": "summon-three-eyed-owl", "text": "[[main]] - [[exhaust]] - 1 [[charm:class]]: Place a [[Three-Eyed Owl]] conjuration onto your battlefield.", "type": "Ready Spell", "release": {"name": "Master Set", "stub": "master-set"}, "placement": "Spellboard", "conjurations": [{"name": "Three-Eyed Owl", "stub": "three-eyed-owl"}]}', '25', 'Ready Spell', '5', '2', NULL, NULL, 't', 'Summon Three-Eyed Owl
main - exhaust - 1 charm:class: Place a Three-Eyed Owl conjuration onto your battlefield.', '0', '9977', '1', NULL, NULL, 'f'),
('393', 'Purge', 'purge', '{"cost": ["[[main]]"], "dice": ["charm"], "name": "Purge", "stub": "purge", "text": "[[main]] - [[exhaust]] - 1 [[charm:class]]: Choose a target player to discard 1 card off the top of their draw pile.\n\nFocus 1: You may pay 1 [[basic]]  to have the target player discard 1 additional card.", "type": "Ready Spell", "release": {"name": "Master Set", "stub": "master-set"}, "placement": "Spellboard"}', '25', 'Ready Spell', '5', '2', NULL, NULL, 'f', 'Purge
main - exhaust - 1 charm:class: Choose a target player to discard 1 card off the top of their draw pile. Focus 1: You may pay 1 basic  to have the target player discard 1 additional card.', '0', '9978', '1', NULL, NULL, 'f'),
('394', 'Abundance', 'abundance', '{"cost": ["[[main]]", "1 [[illusion:class]]"], "dice": ["illusion"], "name": "Abundance", "stub": "abundance", "text": "[[main]] - [[exhaust]]: All players may draw up to 2 cards. For each card they cannot or do not draw, deal 1 damage to their Phoenixborn.\n\nFocus 1: Reduce the damage your Phoenixborn receives from this spell by 1.\n\nFocus 2: Reduce the damage your Phoenixborn receives from this spell by an additional 1.", "type": "Ready Spell", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"illusion:class": 1}, "placement": "Spellboard"}', '25', 'Ready Spell', '106', '4', NULL, NULL, 'f', 'Abundance
main - exhaust: All players may draw up to 2 cards. For each card they cannot or do not draw, deal 1 damage to their Phoenixborn. Focus 1: Reduce the damage your Phoenixborn receives from this spell by 1. Focus 2: Reduce the damage your Phoenixborn receives from this spell by an additional 1.', '0', '9979', '1', NULL, NULL, 'f'),
('395', 'Enchanted Violinist', 'enchanted-violinist', '{"cost": ["[[main]]", "1 [[charm:class]]"], "dice": ["charm"], "life": 1, "name": "Enchanted Violinist", "stub": "enchanted-violinist", "text": "Song of Sorrow: [[side]] - [[exhaust]]: Deal 1 damage to a target unit an opponent controls. If that destroys the unit, after it is destroyed, that target opponent must discard 1 card off the top of their draw pile.", "type": "Ally", "attack": 1, "recover": 1, "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"charm:class": 1}, "placement": "Battlefield"}', '25', 'Ally', '106', '2', NULL, NULL, 'f', 'Enchanted Violinist
Song of Sorrow: side - exhaust: Deal 1 damage to a target unit an opponent controls. If that destroys the unit, after it is destroyed, that target opponent must discard 1 card off the top of their draw pile.', '0', '9980', '1', NULL, NULL, 'f'),
('396', 'Rose Fire Dancer', 'rose-fire-dancer', '{"cost": ["[[main]]", "1 [[illusion:class]]", "1 [[basic]]"], "dice": ["illusion"], "life": 1, "name": "Rose Fire Dancer", "stub": "rose-fire-dancer", "text": "Distract: [[side]] - [[exhaust]]: Place 1 exhaustion token on a target unit.", "type": "Ally", "attack": 3, "recover": 0, "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"basic": 1, "illusion:class": 1}, "placement": "Battlefield"}', '25', 'Ally', '206', '4', NULL, NULL, 'f', 'Rose Fire Dancer
Distract: side - exhaust: Place 1 exhaustion token on a target unit.', '0', '9981', '1', NULL, NULL, 'f'),
('397', 'Hidden Power', 'hidden-power', '{"cost": ["[[main]]", "1 [[illusion:class]]"], "dice": ["illusion"], "name": "Hidden Power", "stub": "hidden-power", "text": "Draw 1 card. Change 5 dice in your active pool to a side of your choice.", "type": "Action Spell", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"illusion:class": 1}, "placement": "Discard"}', '25', 'Action Spell', '106', '4', NULL, NULL, 'f', 'Hidden Power
Draw 1 card. Change 5 dice in your active pool to a side of your choice.', '0', '9982', '1', NULL, NULL, 'f'),
('398', 'Sympathy Pain', 'sympathy-pain', '{"cost": [["1 [[charm:power]]", "1 [[sympathy:power]]"]], "name": "Sympathy Pain", "stub": "sympathy-pain", "text": "You may play this spell after 1 or more wound tokens are placed on your Phoenixborn as a result of an attack, spell, ability, or dice power an opponent controls. Deal 2 damage to a target unit or Phoenixborn that opponent controls.", "type": "Reaction Spell", "altDice": ["charm", "sympathy"], "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"charm:power / sympathy:power": 1}, "placement": "Discard"}', '25', 'Reaction Spell', '102', '0', NULL, NULL, 'f', 'Sympathy Pain
You may play this spell after 1 or more wound tokens are placed on your Phoenixborn as a result of an attack, spell, ability, or dice power an opponent controls. Deal 2 damage to a target unit or Phoenixborn that opponent controls.', '34', '9983', '1', NULL, NULL, 'f'),
('399', 'Seal', 'seal', '{"cost": ["[[main]]", "1 [[charm:class]]", "1 [[illusion:class]]"], "dice": ["charm", "illusion"], "name": "Seal", "stub": "seal", "text": "Choose a ready spell on a target player''s spellboard. Place 1 exhaustion token on the chosen spell and on each other copy of the chosen spell on that player''s spellboard.", "type": "Action Spell", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"charm:class": 1, "illusion:class": 1}, "placement": "Discard"}', '25', 'Action Spell', '207', '6', NULL, NULL, 'f', 'Seal
Choose a ready spell on a target player''s spellboard. Place 1 exhaustion token on the chosen spell and on each other copy of the chosen spell on that player''s spellboard.', '0', '9984', '1', NULL, NULL, 'f'),
('400', 'Strange Copy', 'strange-copy', '{"cost": [["1 [[illusion:power]]", "1 [[sympathy:power]]"]], "name": "Strange Copy", "stub": "strange-copy", "text": "You may play this spell after an opponent declares attackers. Choose a unit you control to become a copy of a target unit for the remainder of the turn. While a copy, that unit replaces its title, printed abilities and printed attack, life and recover values with those of the target unit. If a printed value is X, use the current value of X.", "type": "Reaction Spell", "altDice": ["illusion", "sympathy"], "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"illusion:power / sympathy:power": 1}, "placement": "Discard"}', '25', 'Reaction Spell', '102', '0', NULL, NULL, 'f', 'Strange Copy
You may play this spell after an opponent declares attackers. Choose a unit you control to become a copy of a target unit for the remainder of the turn. While a copy, that unit replaces its title, printed abilities and printed attack, life and recover values with those of the target unit. If a printed value is X, use the current value of X.', '36', '9985', '1', NULL, NULL, 'f'),
('401', 'Maeoni Viper', 'maeoni-viper', '{"life": 20, "name": "Maeoni Viper", "stub": "maeoni-viper", "text": "Command Strike: [[side]] - [[exhaust]] - 2 [[basic]]: Choose an unexhausted unit you control. Deal damage to a target unit equal to the chosen unit''s attack value.", "type": "Phoenixborn", "release": {"name": "Master Set", "stub": "master-set"}, "spellboard": 5, "battlefield": 4}', '25', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Maeoni Viper
Command Strike: side - exhaust - 2 basic: Choose an unexhausted unit you control. Deal damage to a target unit equal to the chosen unit''s attack value.', '0', '9986', '1', NULL, NULL, 'f'),
('402', 'Silver Snake', 'silver-snake', '{"life": 4, "name": "Silver Snake", "stub": "silver-snake", "text": "* Consume: After a unit an opponent controls is destroyed, place 1 status token on this unit.\n\n* X = the number of status tokens on this unit.", "type": "Conjuration", "attack": "X", "copies": 1, "recover": 3, "release": {"name": "Master Set", "stub": "master-set"}, "placement": "Battlefield", "phoenixborn": "Maeoni Viper"}', '25', 'Conjuration', '0', '0', 'Maeoni Viper', '1', 'f', 'Silver Snake
* Consume: After a unit an opponent controls is destroyed, place 1 status token on this unit. * X = the number of status tokens on this unit.', '0', '9987', '1', NULL, NULL, 'f'),
('403', 'Summon Silver Snake', 'summon-silver-snake', '{"cost": ["[[main]]"], "dice": ["charm", "natural"], "name": "Summon Silver Snake", "stub": "summon-silver-snake", "text": "[[main]] - [[exhaust]] - 1 [[charm:power]] - 1 [[natural:power]]: Place a [[Silver Snake]] conjuration onto your battlefield.\n\nFocus 1: Place 1 status token on that Silver Snake.\n\nFocus 2: Place 1 additional status token on that Silver Snake.\n\n* Spell Guard: This spell cannot be affected by an opponent''s spell.", "type": "Ready Spell", "release": {"name": "Master Set", "stub": "master-set"}, "placement": "Spellboard", "phoenixborn": "Maeoni Viper", "conjurations": [{"name": "Silver Snake", "stub": "silver-snake"}]}', '25', 'Ready Spell', '5', '10', 'Maeoni Viper', NULL, 't', 'Summon Silver Snake
main - exhaust - 1 charm:power - 1 natural:power: Place a Silver Snake conjuration onto your battlefield. Focus 1: Place 1 status token on that Silver Snake. Focus 2: Place 1 additional status token on that Silver Snake. * Spell Guard: This spell cannot be affected by an opponent''s spell.', '0', '9988', '1', NULL, NULL, 'f'),
('404', 'Gilder', 'gilder', '{"life": 2, "name": "Gilder", "stub": "gilder", "text": "Unit Guard: This unit may guard a unit that is being attacked.\n\n* Inheritance 1: When this unit is destroyed, you may place 1 status token on a target unit.", "type": "Conjuration", "attack": 0, "copies": 2, "recover": 0, "release": {"name": "Master Set", "stub": "master-set"}, "placement": "Battlefield"}', '25', 'Conjuration', '0', '0', NULL, '2', 'f', 'Gilder
Unit Guard: This unit may guard a unit that is being attacked. * Inheritance 1: When this unit is destroyed, you may place 1 status token on a target unit.', '0', '9989', '1', NULL, NULL, 'f'),
('405', 'Summon Gilder', 'summon-gilder', '{"cost": ["[[main]]", "1 [[charm:class]]"], "dice": ["charm", "natural"], "name": "Summon Gilder", "stub": "summon-gilder", "text": "[[main]] - [[exhaust]] - 1 [[natural:class]]: Place a [[Gilder]] conjuration onto your battlefield. You may deal 1 damage to a target unit.", "type": "Ready Spell", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"charm:class": 1}, "placement": "Spellboard", "conjurations": [{"name": "Gilder", "stub": "gilder"}]}', '25', 'Ready Spell', '106', '10', NULL, NULL, 't', 'Summon Gilder
main - exhaust - 1 natural:class: Place a Gilder conjuration onto your battlefield. You may deal 1 damage to a target unit.', '0', '9990', '1', NULL, NULL, 'f'),
('406', 'Hypnotize', 'hypnotize', '{"cost": ["[[main]]"], "dice": ["charm"], "name": "Hypnotize", "stub": "hypnotize", "text": "[[side]] - [[exhaust]] - 2 [[charm:class]]: Choose a target unit you control to gain the following ability for the remainder of the turn.\n\nBypass: This unit cannot be blocked or guarded.", "type": "Ready Spell", "release": {"name": "Master Set", "stub": "master-set"}, "placement": "Spellboard"}', '25', 'Ready Spell', '5', '2', NULL, NULL, 'f', 'Hypnotize
side - exhaust - 2 charm:class: Choose a target unit you control to gain the following ability for the remainder of the turn. Bypass: This unit cannot be blocked or guarded.', '0', '9991', '1', NULL, NULL, 'f'),
('407', 'Empower', 'empower', '{"cost": ["[[side]]", "1 [[basic]]"], "dice": ["natural"], "name": "Empower", "stub": "empower", "text": "[[main]] - [[exhaust]] - 1 [[natural:class]] or 1 [[sympathy:class]]: Place 1 status token on a target unit you control.\n\nFocus 1: Then, you may remove any number of status tokens from a unit you control. Deal damage to a target unit equal to the number of status tokens removed.", "type": "Ready Spell", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"basic": 1}, "placement": "Spellboard"}', '25', 'Ready Spell', '104', '8', NULL, NULL, 'f', 'Empower
main - exhaust - 1 natural:class or 1 sympathy:class: Place 1 status token on a target unit you control. Focus 1: Then, you may remove any number of status tokens from a unit you control. Deal damage to a target unit equal to the number of status tokens removed.', '0', '9992', '1', NULL, NULL, 'f'),
('408', 'Molten Gold', 'molten-gold', '{"cost": ["[[main]]", "2 [[natural:power]]"], "dice": ["natural"], "name": "Molten Gold", "stub": "molten-gold", "text": "Place 3 wound tokens on a target unit or Phoenixborn.", "type": "Action Spell", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"natural:power": 2}, "placement": "Discard"}', '25', 'Action Spell', '209', '8', NULL, NULL, 'f', 'Molten Gold
Place 3 wound tokens on a target unit or Phoenixborn.', '0', '9993', '1', NULL, NULL, 'f'),
('409', 'Golden Veil', 'golden-veil', '{"cost": ["1 [[charm:power]]"], "dice": ["charm"], "name": "Golden Veil", "stub": "golden-veil", "text": "You may play this spell after an opponent targets a unit you control with a spell, ability, or dice power. Cancel that effect and the remaining effects of that spell, ability or dice power.", "type": "Reaction Spell", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"charm:power": 1}, "placement": "Discard"}', '25', 'Reaction Spell', '102', '2', NULL, NULL, 'f', 'Golden Veil
You may play this spell after an opponent targets a unit you control with a spell, ability, or dice power. Cancel that effect and the remaining effects of that spell, ability or dice power.', '0', '9994', '1', NULL, NULL, 'f'),
('410', 'Open Memories', 'open-memories', '{"cost": ["[[main]]", "1 [[charm:class]]", "1 [[basic]]"], "dice": ["charm"], "name": "Open Memories", "stub": "open-memories", "text": "You may search your draw pile for 1 card and place it into your hand. If you do, shuffle your draw pile.", "type": "Action Spell", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"basic": 1, "charm:class": 1}, "placement": "Discard"}', '25', 'Action Spell', '206', '2', NULL, NULL, 'f', 'Open Memories
You may search your draw pile for 1 card and place it into your hand. If you do, shuffle your draw pile.', '0', '9995', '1', NULL, NULL, 'f'),
('411', 'Refresh', 'refresh', '{"cost": ["[[main]]", "1 [[charm:class]]", "1 [[basic]]"], "dice": ["charm"], "name": "Refresh", "stub": "refresh", "text": "Remove all exhaustion tokens from a target unit.", "type": "Action Spell", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"basic": 1, "charm:class": 1}, "placement": "Discard"}', '25', 'Action Spell', '206', '2', NULL, NULL, 'f', 'Refresh
Remove all exhaustion tokens from a target unit.', '0', '9996', '1', NULL, NULL, 'f'),
('412', 'Transfer', 'transfer', '{"cost": ["[[main]]", "1 [[charm:class]]", "1 [[basic]]"], "dice": ["charm"], "name": "Transfer", "stub": "transfer", "text": "Move 1 token from a target player''s non-Phoenixborn card onto another non-Phoenixborn card that player controls.", "type": "Action Spell", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"basic": 1, "charm:class": 1}, "placement": "Discard"}', '25', 'Action Spell', '206', '2', NULL, NULL, 'f', 'Transfer
Move 1 token from a target player''s non-Phoenixborn card onto another non-Phoenixborn card that player controls.', '0', '9997', '1', NULL, NULL, 'f'),
('413', 'Call Upon The Realms', 'call-upon-the-realms', '{"cost": ["[[main]]"], "name": "Call Upon The Realms", "stub": "call-upon-the-realms", "text": "Change 3 dice in your active pool to a side of your choice.", "type": "Action Spell", "release": {"name": "Master Set", "stub": "master-set"}, "placement": "Discard"}', '25', 'Action Spell', '5', '0', NULL, NULL, 'f', 'Call Upon The Realms
Change 3 dice in your active pool to a side of your choice.', '0', '9998', '1', NULL, NULL, 'f'),
('414', 'Coal Roarkwin', 'coal-roarkwin', '{"life": 15, "name": "Coal Roarkwin", "stub": "coal-roarkwin", "text": "Slash: [[side]] - 1 [[discard]]: Choose a player. Deal 1 damage to a target unit they control, or deal 1 damage to their target Phoenixborn if they control no units.", "type": "Phoenixborn", "release": {"name": "Master Set", "stub": "master-set"}, "spellboard": 4, "battlefield": 6}', '25', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Coal Roarkwin
Slash: side - 1 discard: Choose a player. Deal 1 damage to a target unit they control, or deal 1 damage to their target Phoenixborn if they control no units.', '0', '9999', '1', NULL, NULL, 'f'),
('415', 'One Hundred Blades', 'one-hundred-blades', '{"cost": ["[[main]]", "2 [[basic]]"], "dice": ["basic"], "name": "One Hundred Blades", "stub": "one-hundred-blades", "text": "Deal 1 damage to a target Phoenixborn. Deal 1 damage to all opponents'' units. Draw 1 card.", "type": "Action Spell", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"basic": 2}, "placement": "Discard", "phoenixborn": "Coal Roarkwin"}', '25', 'Action Spell', '205', '0', 'Coal Roarkwin', NULL, 'f', 'One Hundred Blades
Deal 1 damage to a target Phoenixborn. Deal 1 damage to all opponents'' units. Draw 1 card.', '0', '10000', '1', NULL, NULL, 'f'),
('416', 'Chant of Revenge', 'chant-of-revenge', '{"cost": ["[[side]]", "1 [[ceremonial:class]]"], "dice": ["ceremonial"], "name": "Chant of Revenge", "stub": "chant-of-revenge", "text": "After an ally you control is destroyed, place 1 status token on this spell if it has no status tokens on it.\n\n[[side]] - [[exhaust]]: Remove 1 status token from this spell to deal 1 damage to a target Phoenixborn.", "type": "Ready Spell", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"ceremonial:class": 1}, "placement": "Spellboard"}', '25', 'Ready Spell', '105', '1', NULL, NULL, 'f', 'Chant of Revenge
After an ally you control is destroyed, place 1 status token on this spell if it has no status tokens on it. side - exhaust: Remove 1 status token from this spell to deal 1 damage to a target Phoenixborn.', '0', '10001', '1', NULL, NULL, 'f'),
('417', 'Expand Energy', 'expand-energy', '{"cost": ["[[main]]", "1 [[basic]]"], "dice": ["basic"], "name": "Expand Energy", "stub": "expand-energy", "text": "Draw until you have 2 cards in your hand.", "type": "Action Spell", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"basic": 1}, "placement": "Discard"}', '25', 'Action Spell', '105', '0', NULL, NULL, 'f', 'Expand Energy
Draw until you have 2 cards in your hand.', '0', '10002', '1', NULL, NULL, 'f'),
('418', 'Strengthen', 'strengthen', '{"cost": ["[[main]]", "1 [[natural:class]]", "1 [[ceremonial:class]]"], "dice": ["natural", "ceremonial"], "name": "Strengthen", "stub": "strengthen", "text": "[[side]] - [[exhaust]]: Add 2 to a target unit''s attack value for the remainder of the turn.\n\nFocus 2: Add 1 more to that unit''s attack value for the remainder of the turn.", "type": "Ready Spell", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"natural:class": 1, "ceremonial:class": 1}, "placement": "Spellboard"}', '25', 'Ready Spell', '207', '9', NULL, NULL, 'f', 'Strengthen
side - exhaust: Add 2 to a target unit''s attack value for the remainder of the turn. Focus 2: Add 1 more to that unit''s attack value for the remainder of the turn.', '0', '10003', '1', NULL, NULL, 'f'),
('419', 'Cover', 'cover', '{"cost": ["1 [[natural:power]]"], "dice": ["natural"], "name": "Cover", "stub": "cover", "text": "You may play this spell after your Phoenixborn, while guarding, is dealt damage by a unit''s attack. Prevent that damage from being received. Deal 1 damage to the target attacking unit.", "type": "Reaction Spell", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"natural:power": 1}, "placement": "Discard"}', '25', 'Reaction Spell', '102', '8', NULL, NULL, 'f', 'Cover
You may play this spell after your Phoenixborn, while guarding, is dealt damage by a unit''s attack. Prevent that damage from being received. Deal 1 damage to the target attacking unit.', '0', '10004', '1', NULL, NULL, 'f'),
('420', 'Iron Rhino', 'iron-rhino', '{"life": 4, "name": "Iron Rhino", "stub": "iron-rhino", "text": "Gigantic 1: This unit cannot be blocked or guarded against by units with a life value of 1 or less.\n\nOverkill 2: After this unit destroys a unit an opponent controls by attacking, deal 2 damage to that opponent''s target Phoenixborn.", "type": "Conjuration", "attack": 7, "copies": 1, "recover": 0, "release": {"name": "Master Set", "stub": "master-set"}, "placement": "Battlefield"}', '25', 'Conjuration', '0', '0', NULL, '1', 'f', 'Iron Rhino
Gigantic 1: This unit cannot be blocked or guarded against by units with a life value of 1 or less. Overkill 2: After this unit destroys a unit an opponent controls by attacking, deal 2 damage to that opponent''s target Phoenixborn.', '0', '10005', '1', NULL, NULL, 'f'),
('421', 'Summon Iron Rhino', 'summon-iron-rhino', '{"cost": ["[[main]]", "1 [[natural:class]]"], "dice": ["natural"], "name": "Summon Iron Rhino", "stub": "summon-iron-rhino", "text": "[[main]] - [[exhaust]] - 6 [[basic]]: Place an [[Iron Rhino]] conjuration onto your battlefield.\n\nFocus 1: Reduce the activate cost of this spell by 1 [[basic]].\n\nFocus 2: Reduce the activation cost of this spell by an additional 1 [[basic]].", "type": "Ready Spell", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"natural:class": 1}, "placement": "Spellboard", "conjurations": [{"name": "Iron Rhino", "stub": "iron-rhino"}]}', '25', 'Ready Spell', '106', '8', NULL, NULL, 't', 'Summon Iron Rhino
main - exhaust - 6 basic: Place an Iron Rhino conjuration onto your battlefield. Focus 1: Reduce the activate cost of this spell by 1 basic. Focus 2: Reduce the activation cost of this spell by an additional 1 basic.', '0', '10006', '1', NULL, NULL, 'f'),
('422', 'Anchornaut', 'anchornaut', '{"cost": ["[[main]]", "1 [[basic]]"], "dice": ["basic"], "life": 1, "name": "Anchornaut", "stub": "anchornaut", "text": "Throw 1: When this unit comes into play, you may deal 1 damage to another target unit.", "type": "Ally", "attack": 0, "recover": 1, "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"basic": 1}, "placement": "Battlefield"}', '25', 'Ally', '105', '0', NULL, NULL, 'f', 'Anchornaut
Throw 1: When this unit comes into play, you may deal 1 damage to another target unit.', '0', '10007', '1', NULL, NULL, 'f'),
('423', 'Iron Worker', 'iron-worker', '{"cost": ["[[main]]", "2 [[basic]]"], "dice": ["basic"], "life": 2, "name": "Iron Worker", "stub": "iron-worker", "text": "* Overtime 2: During the draw cards step, you may draw up to 2 additional cards.", "type": "Ally", "attack": 2, "recover": 1, "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"basic": 2}, "placement": "Battlefield"}', '25', 'Ally', '205', '0', NULL, NULL, 'f', 'Iron Worker
* Overtime 2: During the draw cards step, you may draw up to 2 additional cards.', '0', '10008', '1', NULL, NULL, 'f'),
('424', 'Hammer Knight', 'hammer-knight', '{"cost": ["[[main]]", "1 [[ceremonial:power]]", "1 [[natural:class]]", "1 [[basic]]"], "dice": ["ceremonial", "natural"], "life": 4, "name": "Hammer Knight", "stub": "hammer-knight", "text": "Aftershock 1: After this unit destroys a unit an opponent controls by attacking, you may deal 1 damage to a target unit.\n\nAlert: Do not place exhaustion tokens on this unit as a result of its countering.", "type": "Ally", "attack": 3, "recover": 2, "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"basic": 1, "natural:class": 1, "ceremonial:power": 1}, "placement": "Battlefield"}', '25', 'Ally', '308', '9', NULL, NULL, 'f', 'Hammer Knight
Aftershock 1: After this unit destroys a unit an opponent controls by attacking, you may deal 1 damage to a target unit. Alert: Do not place exhaustion tokens on this unit as a result of its countering.', '0', '10009', '1', NULL, NULL, 'f'),
('425', 'Close Combat', 'close-combat', '{"cost": ["[[main]]", "1 [[natural:power]]"], "dice": ["natural"], "name": "Close Combat", "stub": "close-combat", "text": "Choose an unexhausted unit you control. Deal damage to another target unit equal to the chosen unit''s attack value. Then, place 1 wound token or 1 exhaustion token on the chosen unit you control.", "type": "Action Spell", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"natural:power": 1}, "placement": "Discard"}', '25', 'Action Spell', '107', '8', NULL, NULL, 'f', 'Close Combat
Choose an unexhausted unit you control. Deal damage to another target unit equal to the chosen unit''s attack value. Then, place 1 wound token or 1 exhaustion token on the chosen unit you control.', '0', '10010', '1', NULL, NULL, 'f'),
('426', 'Noah Redmoon', 'noah-redmoon', '{"life": 16, "name": "Noah Redmoon", "stub": "noah-redmoon", "text": "Shadow Target: [[side]] - [[exhaust]] - 1 [[basic]]: Choose a target opponent and place 1 exhaustion token on an unexhausted ready spell they control.", "type": "Phoenixborn", "release": {"name": "Master Set", "stub": "master-set"}, "spellboard": 4, "battlefield": 7}', '25', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Noah Redmoon
Shadow Target: side - exhaust - 1 basic: Choose a target opponent and place 1 exhaustion token on an unexhausted ready spell they control.', '0', '10011', '1', NULL, NULL, 'f'),
('427', 'Masked Wolf', 'masked-wolf', '{"life": 1, "name": "Masked Wolf", "stub": "masked-wolf", "type": "Conjuration", "attack": 2, "copies": 5, "recover": 0, "release": {"name": "Master Set", "stub": "master-set"}, "placement": "Battlefield", "phoenixborn": "Noah Redmoon"}', '25', 'Conjuration', '0', '0', 'Noah Redmoon', '5', 'f', 'Masked Wolf
', '0', '10012', '1', NULL, NULL, 'f'),
('428', 'Summon Masked Wolf', 'summon-masked-wolf', '{"cost": ["[[side]]", "1 [[basic]]"], "dice": ["illusion"], "name": "Summon Masked Wolf", "stub": "summon-masked-wolf", "text": "[[side]] - [[exhaust]] - 1 [[illusion:class]]: Place a [[Masked Wolf]] conjuration onto your battlefield.\n\nFocus 1: If you spent any[[illusion:power]] to activate this spell, you may take an additional side action this turn.", "type": "Ready Spell", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"basic": 1}, "placement": "Spellboard", "phoenixborn": "Noah Redmoon", "conjurations": [{"name": "Masked Wolf", "stub": "masked-wolf"}]}', '25', 'Ready Spell', '104', '4', 'Noah Redmoon', NULL, 't', 'Summon Masked Wolf
side - exhaust - 1 illusion:class: Place a Masked Wolf conjuration onto your battlefield. Focus 1: If you spent anyillusion:power to activate this spell, you may take an additional side action this turn.', '0', '10013', '1', NULL, NULL, 'f'),
('429', 'False Demon', 'false-demon', '{"life": 2, "name": "False Demon", "stub": "false-demon", "text": "Nightmare 1: When this unit comes into play, you may deal 1 damage to a target exhausted unit.", "type": "Conjuration", "attack": 2, "copies": 2, "recover": 0, "release": {"name": "Master Set", "stub": "master-set"}, "placement": "Battlefield"}', '25', 'Conjuration', '0', '0', NULL, '2', 'f', 'False Demon
Nightmare 1: When this unit comes into play, you may deal 1 damage to a target exhausted unit.', '0', '10014', '1', NULL, NULL, 'f'),
('430', 'Summon False Demon', 'summon-false-demon', '{"cost": ["[[main]]"], "dice": ["illusion"], "name": "Summon False Demon", "stub": "summon-false-demon", "text": "[[main]] - [[exhaust]] - 1 [[illusion:class]] - 1 [[basic]]: Place a [[False Demon]] conjuration onto your battlefield.", "type": "Ready Spell", "release": {"name": "Master Set", "stub": "master-set"}, "placement": "Spellboard", "conjurations": [{"name": "False Demon", "stub": "false-demon"}]}', '25', 'Ready Spell', '5', '4', NULL, NULL, 't', 'Summon False Demon
main - exhaust - 1 illusion:class - 1 basic: Place a False Demon conjuration onto your battlefield.', '0', '10015', '1', NULL, NULL, 'f'),
('431', 'Small Sacrifice', 'small-sacrifice', '{"cost": ["[[main]]"], "dice": ["ceremonial"], "name": "Small Sacrifice", "stub": "small-sacrifice", "text": "[[main]] - 1 [[ceremonial:class]]: Deal 1 damage to a target unit on your battlefield. If you do, you may deal 1 damage to a target unit on an opponent''s battlefield.\n\nFocus 1: If both targeted units are unexhausted, you may place 1 exhaustion token on both units instead of damage.", "type": "Ready Spell", "release": {"name": "Master Set", "stub": "master-set"}, "placement": "Spellboard"}', '25', 'Ready Spell', '5', '1', NULL, NULL, 'f', 'Small Sacrifice
main - 1 ceremonial:class: Deal 1 damage to a target unit on your battlefield. If you do, you may deal 1 damage to a target unit on an opponent''s battlefield. Focus 1: If both targeted units are unexhausted, you may place 1 exhaustion token on both units instead of damage.', '0', '10016', '1', NULL, NULL, 'f'),
('432', 'Stormwind Sniper', 'stormwind-sniper', '{"cost": ["[[main]]", "1 [[ceremonial:class]]", "1 [[illusion:class]]"], "dice": ["ceremonial", "illusion"], "life": 1, "name": "Stormwind Sniper", "stub": "stormwind-sniper", "text": "Ambush 1: When this unit comes into play, you may deal 1 damage to a target Phoenixborn.\n\nConcealed: This unit cannot be targeted by attacks, spells, abilities, or dice powers an opponent controls.", "type": "Ally", "attack": 2, "recover": 1, "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"illusion:class": 1, "ceremonial:class": 1}, "placement": "Battlefield"}', '25', 'Ally', '207', '5', NULL, NULL, 'f', 'Stormwind Sniper
Ambush 1: When this unit comes into play, you may deal 1 damage to a target Phoenixborn. Concealed: This unit cannot be targeted by attacks, spells, abilities, or dice powers an opponent controls.', '0', '10017', '1', NULL, NULL, 'f'),
('433', 'Sleeping Widow', 'sleeping-widow', '{"life": 1, "name": "Sleeping Widow", "stub": "sleeping-widow", "type": "Conjuration", "attack": 2, "copies": 6, "recover": 0, "release": {"name": "Master Set", "stub": "master-set"}, "placement": "Battlefield"}', '25', 'Conjuration', '0', '0', NULL, '6', 'f', 'Sleeping Widow
', '0', '10018', '1', NULL, NULL, 'f'),
('434', 'Summon Sleeping Widows', 'summon-sleeping-widows', '{"cost": ["2 [[ceremonial:class]]"], "dice": ["ceremonial"], "name": "Summon Sleeping Widows", "stub": "summon-sleeping-widows", "text": "You may play this spell after a unit you control is destroyed. Place 2 [[Sleeping Widow]] conjurations onto your battlefield.", "type": "Reaction Spell", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"ceremonial:class": 2}, "placement": "Discard", "conjurations": [{"name": "Sleeping Widow", "stub": "sleeping-widow"}]}', '25', 'Reaction Spell', '202', '1', NULL, NULL, 't', 'Summon Sleeping Widows
You may play this spell after a unit you control is destroyed. Place 2 Sleeping Widow conjurations onto your battlefield.', '0', '10019', '1', NULL, NULL, 'f'),
('435', 'Fade Away', 'fade-away', '{"cost": ["[[main]]", "1 [[illusion:class]]"], "dice": ["illusion"], "name": "Fade Away", "stub": "fade-away", "text": "Destroy this unit at the end of the round. If the destroyed unit was an ally, remove it from the game.", "type": "Alteration Spell", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"illusion:class": 1}, "placement": "Unit"}', '25', 'Alteration Spell', '106', '4', NULL, NULL, 'f', 'Fade Away
Destroy this unit at the end of the round. If the destroyed unit was an ally, remove it from the game.', '0', '10020', '1', NULL, NULL, 'f'),
('436', 'Bound Soul', 'bound-soul', '{"cost": ["[[main]]", "1 [[ceremonial:class]]"], "dice": ["ceremonial"], "name": "Bound Soul", "stub": "bound-soul", "text": "Search your discard pile for an ally and place it into your hand.", "type": "Action Spell", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"ceremonial:class": 1}, "placement": "Discard"}', '25', 'Action Spell', '106', '1', NULL, NULL, 'f', 'Bound Soul
Search your discard pile for an ally and place it into your hand.', '0', '10021', '1', NULL, NULL, 'f'),
('437', 'Sleight of Hand', 'sleight-of-hand', '{"cost": ["[[main]]", "1 [[illusion:power]]", "1 [[basic]]"], "dice": ["illusion"], "name": "Sleight of Hand", "stub": "sleight-of-hand", "text": "Draw 3 cards.", "type": "Action Spell", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"basic": 1, "illusion:power": 1}, "placement": "Discard"}', '25', 'Action Spell', '207', '4', NULL, NULL, 'f', 'Sleight of Hand
Draw 3 cards.', '0', '10022', '1', NULL, NULL, 'f'),
('438', 'Shadow Strike', 'shadow-strike', '{"cost": ["1 [[illusion:power]]"], "dice": ["illusion"], "name": "Shadow Strike", "stub": "shadow-strike", "text": "You may play this spell after an opponent declares attackers. Deal 3 damage to a target unit that opponent controls that is not attacking.", "type": "Reaction Spell", "release": {"name": "Master Set", "stub": "master-set"}, "magicCost": {"illusion:power": 1}, "placement": "Discard"}', '25', 'Reaction Spell', '102', '4', NULL, NULL, 'f', 'Shadow Strike
You may play this spell after an opponent declares attackers. Deal 3 damage to a target unit that opponent controls that is not attacking.', '0', '10023', '1', NULL, NULL, 'f'),
('439', 'Resummon', 'resummon', '{"cost": ["[[main]]"], "dice": ["ceremonial", "illusion"], "name": "Resummon", "stub": "resummon", "text": "[[main]] - [[exhaust]] - 1 [[ceremonial:class]] - 1 [[illusion:class]]: Destroy a conjuration you control. Then, place that conjuration onto your battlefield.", "type": "Ready Spell", "release": {"name": "Master Set", "stub": "master-set"}, "placement": "Spellboard"}', '25', 'Ready Spell', '5', '5', NULL, NULL, 'f', 'Resummon
main - exhaust - 1 ceremonial:class - 1 illusion:class: Destroy a conjuration you control. Then, place that conjuration onto your battlefield.', '0', '10024', '1', NULL, NULL, 'f'),
('440', 'Ice Buff', 'ice-buff', '{"life": "+1", "name": "Ice Buff", "stub": "ice-buff", "type": "Conjured Alteration Spell", "copies": 5, "release": {"name": "The Frostdale Giants", "stub": "the-frostdale-giants"}, "placement": "Unit", "phoenixborn": "Rin Northfell"}', '26', 'Conjured Alteration Spell', '0', '0', 'Rin Northfell', '5', 'f', 'Ice Buff
', '0', '10025', '1', NULL, NULL, 'f'),
('441', 'Rin Northfell', 'rin-northfell', '{"life": 17, "name": "Rin Northfell", "stub": "rin-northfell", "text": "Ice Buff: [[side]] - [[exhaust]]: Attach an [[Ice Buff]] conjured alteration spell to a target unit you control.", "type": "Phoenixborn", "release": {"name": "The Frostdale Giants", "stub": "the-frostdale-giants"}, "spellboard": 4, "battlefield": 6, "conjurations": [{"name": "Ice Buff", "stub": "ice-buff"}]}', '26', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Rin Northfell
Ice Buff: side - exhaust: Attach an Ice Buff conjured alteration spell to a target unit you control.', '0', '10026', '1', NULL, NULL, 'f'),
('442', 'Rin''s Fury', 'rins-fury', '{"cost": ["2 [[basic]]"], "dice": ["basic"], "name": "Rin''s Fury", "stub": "rins-fury", "text": "You may play this spell after a unit you control is dealt damage by a unit''s attack. Prevent that damage from being received. Destroy that target attacking unit.", "type": "Reaction Spell", "release": {"name": "The Frostdale Giants", "stub": "the-frostdale-giants"}, "magicCost": {"basic": 2}, "placement": "Discard", "phoenixborn": "Rin Northfell"}', '26', 'Reaction Spell', '200', '0', 'Rin Northfell', NULL, 'f', 'Rin''s Fury
You may play this spell after a unit you control is dealt damage by a unit''s attack. Prevent that damage from being received. Destroy that target attacking unit.', '0', '10027', '1', NULL, NULL, 'f'),
('443', 'Ice Golem', 'ice-golem', '{"life": 2, "name": "Ice Golem", "stub": "ice-golem", "text": "* Skin Morph 2: Add 2 to this unit''s life value if it has 1 or more alteration spells attached to it.", "type": "Conjuration", "attack": 3, "copies": 3, "recover": 0, "release": {"name": "The Frostdale Giants", "stub": "the-frostdale-giants"}, "placement": "Battlefield"}', '26', 'Conjuration', '0', '0', NULL, '3', 'f', 'Ice Golem
* Skin Morph 2: Add 2 to this unit''s life value if it has 1 or more alteration spells attached to it.', '0', '10028', '1', NULL, NULL, 'f'),
('444', 'Summon Ice Golem', 'summon-ice-golem', '{"cost": ["[[main]]"], "dice": ["natural"], "name": "Summon Ice Golem", "stub": "summon-ice-golem", "text": "[[main]] - [[exhaust]] - 2 [[natural:class]] - 1 [[basic]]: Place an [[Ice Golem]] conjuration onto your battlefield.\n\nFocus 2: You may remove 1 wound token from all Ice Golems you control.", "type": "Ready Spell", "release": {"name": "The Frostdale Giants", "stub": "the-frostdale-giants"}, "placement": "Spellboard", "conjurations": [{"name": "Ice Golem", "stub": "ice-golem"}]}', '26', 'Ready Spell', '5', '8', NULL, NULL, 't', 'Summon Ice Golem
main - exhaust - 2 natural:class - 1 basic: Place an Ice Golem conjuration onto your battlefield. Focus 2: You may remove 1 wound token from all Ice Golems you control.', '0', '10029', '1', NULL, NULL, 'f'),
('445', 'Frostback Bear', 'frostback-bear', '{"life": 3, "name": "Frostback Bear", "stub": "frostback-bear", "text": "Terrifying 1: This unit cannot be blocked or guarded against by units with an attack value of 1 or less.", "type": "Conjuration", "attack": 2, "copies": 2, "recover": 0, "release": {"name": "The Frostdale Giants", "stub": "the-frostdale-giants"}, "placement": "Battlefield"}', '26', 'Conjuration', '0', '0', NULL, '2', 'f', 'Frostback Bear
Terrifying 1: This unit cannot be blocked or guarded against by units with an attack value of 1 or less.', '0', '10030', '1', NULL, NULL, 'f'),
('446', 'Summon Frostback Bear', 'summon-frostback-bear', '{"cost": ["[[main]]", "1 [[natural:power]]"], "dice": ["natural"], "name": "Summon Frostback Bear", "stub": "summon-frostback-bear", "text": "[[main]] - [[exhaust]] - 1 [[natural:class]] - 1 [[basic]]: Place a [[Frostback Bear]] conjuration onto your battlefield.", "type": "Ready Spell", "release": {"name": "The Frostdale Giants", "stub": "the-frostdale-giants"}, "magicCost": {"natural:power": 1}, "placement": "Spellboard", "conjurations": [{"name": "Frostback Bear", "stub": "frostback-bear"}]}', '26', 'Ready Spell', '107', '8', NULL, NULL, 't', 'Summon Frostback Bear
main - exhaust - 1 natural:class - 1 basic: Place a Frostback Bear conjuration onto your battlefield.', '0', '10031', '1', NULL, NULL, 'f'),
('447', 'Frost Bite', 'frost-bite', '{"cost": ["[[main]]"], "dice": ["natural"], "name": "Frost Bite", "stub": "frost-bite", "text": "[[main]] - [[exhaust]] - 1 [[natural:class]]: Deal 1 damage to a target unit or Phoenixborn.\n\nFocus 1: You may change the activation cost of this ability to [[main]] - [[exhaust]] - 1 [[basic]].", "type": "Ready Spell", "release": {"name": "The Frostdale Giants", "stub": "the-frostdale-giants"}, "placement": "Spellboard"}', '26', 'Ready Spell', '5', '8', NULL, NULL, 'f', 'Frost Bite
main - exhaust - 1 natural:class: Deal 1 damage to a target unit or Phoenixborn. Focus 1: You may change the activation cost of this ability to main - exhaust - 1 basic.', '0', '10032', '1', NULL, NULL, 'f'),
('448', 'Ice Trap', 'ice-trap', '{"cost": ["1 [[natural:class]]"], "dice": ["natural"], "name": "Ice Trap", "stub": "ice-trap", "text": "You may play this spell after a unit with a life value of 2 or less comes into play. Destroy that target unit.", "type": "Reaction Spell", "release": {"name": "The Frostdale Giants", "stub": "the-frostdale-giants"}, "magicCost": {"natural:class": 1}, "placement": "Discard"}', '26', 'Reaction Spell', '101', '8', NULL, NULL, 'f', 'Ice Trap
You may play this spell after a unit with a life value of 2 or less comes into play. Destroy that target unit.', '0', '10033', '1', NULL, NULL, 'f'),
('449', 'Deep Freeze', 'deep-freeze', '{"cost": ["[[main]]", "1 [[natural:class]]"], "dice": ["natural"], "name": "Deep Freeze", "stub": "deep-freeze", "text": "* When attaching this spell, place 3 status tokens on this spell. Discard this spell when it no longer has any status tokens on it. As long as this spell is attached to this unit, this unit is considered to be exhausted. This unit now has the following ability:\n\n* Thaw: [[side]]: Remove 1 status token from a Deep Freeze alteration spell attached to this unit.", "type": "Alteration Spell", "release": {"name": "The Frostdale Giants", "stub": "the-frostdale-giants"}, "magicCost": {"natural:class": 1}, "placement": "Unit"}', '26', 'Alteration Spell', '106', '8', NULL, NULL, 'f', 'Deep Freeze
* When attaching this spell, place 3 status tokens on this spell. Discard this spell when it no longer has any status tokens on it. As long as this spell is attached to this unit, this unit is considered to be exhausted. This unit now has the following ability: * Thaw: side: Remove 1 status token from a Deep Freeze alteration spell attached to this unit.', '0', '10034', '1', NULL, NULL, 'f'),
('450', 'Freezing Blast', 'freezing-blast', '{"cost": ["[[main]]", "2 [[natural:class]]"], "dice": ["natural"], "name": "Freezing Blast", "stub": "freezing-blast", "text": "Deal 2 damage to a target unit. Remove 2 status tokens from that unit.", "type": "Action Spell", "release": {"name": "The Frostdale Giants", "stub": "the-frostdale-giants"}, "magicCost": {"natural:class": 2}, "placement": "Discard"}', '26', 'Action Spell', '207', '8', NULL, NULL, 'f', 'Freezing Blast
Deal 2 damage to a target unit. Remove 2 status tokens from that unit.', '0', '10035', '1', NULL, NULL, 'f'),
('451', 'Frozen Crown', 'frozen-crown', '{"cost": ["[[main]]", "1 [[natural:class]]", "2 [[basic]]"], "dice": ["natural"], "name": "Frozen Crown", "stub": "frozen-crown", "type": "Alteration Spell", "attack": "+3", "release": {"name": "The Frostdale Giants", "stub": "the-frostdale-giants"}, "magicCost": {"basic": 2, "natural:class": 1}, "placement": "Unit"}', '26', 'Alteration Spell', '306', '8', NULL, NULL, 'f', 'Frozen Crown
', '0', '10036', '1', NULL, NULL, 'f'),
('452', 'Crystal Shield', 'crystal-shield', '{"cost": ["[[main]]", "1 [[natural:class]]", "1 [[basic]]"], "dice": ["natural"], "life": "+2", "name": "Crystal Shield", "stub": "crystal-shield", "text": "This unit now has the following ability:\n\nUnit Guard: This unit may guard a unit that is being attacked.", "type": "Alteration Spell", "release": {"name": "The Frostdale Giants", "stub": "the-frostdale-giants"}, "magicCost": {"basic": 1, "natural:class": 1}, "placement": "Unit"}', '26', 'Alteration Spell', '206', '8', NULL, NULL, 'f', 'Crystal Shield
This unit now has the following ability: Unit Guard: This unit may guard a unit that is being attacked.', '0', '10037', '1', NULL, NULL, 'f'),
('453', 'Frost Fang', 'frost-fang', '{"cost": ["[[main]]", "2 [[natural:class]]"], "dice": ["natural"], "life": 1, "name": "Frost Fang", "stub": "frost-fang", "text": "* Armored 1: After this unit is dealt damage, prevent 1 damage from being received.", "type": "Ally", "attack": 3, "recover": 1, "release": {"name": "The Frostdale Giants", "stub": "the-frostdale-giants"}, "magicCost": {"natural:class": 2}, "placement": "Battlefield"}', '26', 'Ally', '207', '8', NULL, NULL, 'f', 'Frost Fang
* Armored 1: After this unit is dealt damage, prevent 1 damage from being received.', '0', '10038', '1', NULL, NULL, 'f'),
('454', 'Brennen Blackcloud', 'brennen-blackcloud', '{"dice": ["ceremonial"], "life": 18, "name": "Brennen Blackcloud", "stub": "brennen-blackcloud", "text": "Spirit Burn: [[side]] - [[exhaust]] - 1 [[ceremonial:class]]: Destroy a unit you control to deal 2 damage to a target Phoenixborn.", "type": "Phoenixborn", "release": {"name": "The Children of Blackcloud", "stub": "the-children-of-blackcloud"}, "spellboard": 3, "battlefield": 5}', '27', 'Phoenixborn', '0', '1', NULL, NULL, 'f', 'Brennen Blackcloud
Spirit Burn: side - exhaust - 1 ceremonial:class: Destroy a unit you control to deal 2 damage to a target Phoenixborn.', '0', '10039', '1', NULL, NULL, 'f'),
('455', 'Blackcloud Ninja', 'blackcloud-ninja', '{"cost": ["[[main]]", "1 [[basic]]"], "dice": ["basic"], "life": 1, "name": "Blackcloud Ninja", "stub": "blackcloud-ninja", "text": "Seal Strike 1: When this unit is declared as an attacker, you may choose a target opponent to place 1 exhaustion token on an unexhausted ready spell of their choice that they control.", "type": "Ally", "attack": 1, "recover": 1, "release": {"name": "The Children of Blackcloud", "stub": "the-children-of-blackcloud"}, "magicCost": {"basic": 1}, "placement": "Battlefield", "phoenixborn": "Brennen Blackcloud"}', '27', 'Ally', '105', '0', 'Brennen Blackcloud', NULL, 'f', 'Blackcloud Ninja
Seal Strike 1: When this unit is declared as an attacker, you may choose a target opponent to place 1 exhaustion token on an unexhausted ready spell of their choice that they control.', '0', '10040', '1', NULL, NULL, 'f'),
('456', 'Fire Archer', 'fire-archer', '{"cost": ["[[main]]", "1 [[ceremonial:class]]"], "dice": ["ceremonial"], "life": 1, "name": "Fire Archer", "stub": "fire-archer", "text": "Ambush 1: When this unit comes into play, you may deal 1 damage to a target Phoenixborn.", "type": "Ally", "attack": 1, "recover": 1, "release": {"name": "The Children of Blackcloud", "stub": "the-children-of-blackcloud"}, "magicCost": {"ceremonial:class": 1}, "placement": "Battlefield"}', '27', 'Ally', '106', '1', NULL, NULL, 'f', 'Fire Archer
Ambush 1: When this unit comes into play, you may deal 1 damage to a target Phoenixborn.', '0', '10041', '1', NULL, NULL, 'f'),
('457', 'Crimson Bomber', 'crimson-bomber', '{"cost": ["[[main]]", "2 [[ceremonial:class]]"], "dice": ["ceremonial"], "life": 2, "name": "Crimson Bomber", "stub": "crimson-bomber", "text": "Detonate 3: [[side]]: Destroy this unit to place 1 wound token on up to 3 target units.", "type": "Ally", "attack": 3, "recover": 0, "release": {"name": "The Children of Blackcloud", "stub": "the-children-of-blackcloud"}, "magicCost": {"ceremonial:class": 2}, "placement": "Battlefield"}', '27', 'Ally', '207', '1', NULL, NULL, 'f', 'Crimson Bomber
Detonate 3: side: Destroy this unit to place 1 wound token on up to 3 target units.', '0', '10042', '1', NULL, NULL, 'f'),
('458', 'Chant of Worship', 'chant-of-worship', '{"cost": ["[[side]]", "1 [[ceremonial:class]]"], "dice": ["ceremonial"], "name": "Chant of Worship", "stub": "chant-of-worship", "text": "After an ally you control is destroyed, place 1 status token on this spell if it has no status tokens on it.\n\n[[main]] - [[exhaust]]: Remove 1 status token from this spell to draw 1 card.", "type": "Ready Spell", "release": {"name": "The Children of Blackcloud", "stub": "the-children-of-blackcloud"}, "magicCost": {"ceremonial:class": 1}, "placement": "Spellboard"}', '27', 'Ready Spell', '105', '1', NULL, NULL, 'f', 'Chant of Worship
After an ally you control is destroyed, place 1 status token on this spell if it has no status tokens on it. main - exhaust: Remove 1 status token from this spell to draw 1 card.', '0', '10043', '1', NULL, NULL, 'f'),
('459', 'Safeguard', 'safeguard', '{"cost": ["[[side]]", "1 [[basic]]"], "dice": ["basic"], "name": "Safeguard", "stub": "safeguard", "text": "Choose a target unit or Phoenixborn you control. Until the start of your next turn, prevent all damage dealt to the chosen target by an opponent''s attack, spell, ability, or dice power from being received.", "type": "Action Spell", "release": {"name": "The Children of Blackcloud", "stub": "the-children-of-blackcloud"}, "magicCost": {"basic": 1}, "placement": "Discard"}', '27', 'Action Spell', '104', '0', NULL, NULL, 'f', 'Safeguard
Choose a target unit or Phoenixborn you control. Until the start of your next turn, prevent all damage dealt to the chosen target by an opponent''s attack, spell, ability, or dice power from being received.', '0', '10044', '1', NULL, NULL, 'f'),
('460', 'Dread Wraith', 'dread-wraith', '{"life": 6, "name": "Dread Wraith", "stub": "dread-wraith", "text": "* Rage 1: Add 1 to this unit''s attack value for each wound token on this unit.", "type": "Conjuration", "attack": 1, "copies": 2, "recover": 1, "release": {"name": "The Children of Blackcloud", "stub": "the-children-of-blackcloud"}, "placement": "Battlefield"}', '27', 'Conjuration', '0', '0', NULL, '2', 'f', 'Dread Wraith
* Rage 1: Add 1 to this unit''s attack value for each wound token on this unit.', '0', '10045', '1', NULL, NULL, 'f'),
('461', 'Summon Dread Wraith', 'summon-dread-wraith', '{"cost": ["[[main]]"], "dice": ["ceremonial"], "name": "Summon Dread Wraith", "stub": "summon-dread-wraith", "text": "[[main]] - [[exhaust]] - 3 [[ceremonial:class]]: Place a [[Dread Wraith]] conjuration on to your battlefield. Focus 2: You may remove 1 exhaustion token from a Dread Wraith you control.", "type": "Ready Spell", "release": {"name": "The Children of Blackcloud", "stub": "the-children-of-blackcloud"}, "placement": "Spellboard", "conjurations": [{"name": "Dread Wraith", "stub": "dread-wraith"}]}', '27', 'Ready Spell', '5', '1', NULL, NULL, 't', 'Summon Dread Wraith
main - exhaust - 3 ceremonial:class: Place a Dread Wraith conjuration on to your battlefield. Focus 2: You may remove 1 exhaustion token from a Dread Wraith you control.', '0', '10046', '1', NULL, NULL, 'f'),
('462', 'Blood Chains', 'blood-chains', '{"cost": ["[[main]]", "1 [[ceremonial:class]]"], "dice": ["ceremonial"], "name": "Blood Chains", "stub": "blood-chains", "text": "Destroy a unit you control to place 1 exhaustion token on a target unit. If the destroyed unit had 1 or more wound tokens on it, place 2 exhaustion tokens instead.", "type": "Action Spell", "release": {"name": "The Children of Blackcloud", "stub": "the-children-of-blackcloud"}, "magicCost": {"ceremonial:class": 1}, "placement": "Discard"}', '27', 'Action Spell', '106', '1', NULL, NULL, 'f', 'Blood Chains
Destroy a unit you control to place 1 exhaustion token on a target unit. If the destroyed unit had 1 or more wound tokens on it, place 2 exhaustion tokens instead.', '0', '10047', '1', NULL, NULL, 'f'),
('463', 'Regress', 'regress', '{"cost": ["[[side]]", "1 [[ceremonial:class]]"], "dice": ["ceremonial"], "name": "Regress", "stub": "regress", "text": "* Fleeting: Discard this card at the end of this round.", "type": "Alteration Spell", "attack": "-3", "release": {"name": "The Children of Blackcloud", "stub": "the-children-of-blackcloud"}, "magicCost": {"ceremonial:class": 1}, "placement": "Unit"}', '27', 'Alteration Spell', '105', '1', NULL, NULL, 'f', 'Regress
* Fleeting: Discard this card at the end of this round.', '0', '10048', '1', NULL, NULL, 'f'),
('464', 'Choke', 'choke', '{"cost": ["[[main]]", "1 [[ceremonial:class]]"], "dice": ["ceremonial"], "name": "Choke", "stub": "choke", "text": "Place 1 exhaustion token on a target unexhausted Phoenixborn an opponent controls. Deal 1 damage to that target Phoenixborn.", "type": "Action Spell", "release": {"name": "The Children of Blackcloud", "stub": "the-children-of-blackcloud"}, "magicCost": {"ceremonial:class": 1}, "placement": "Discard"}', '27', 'Action Spell', '106', '1', NULL, NULL, 'f', 'Choke
Place 1 exhaustion token on a target unexhausted Phoenixborn an opponent controls. Deal 1 damage to that target Phoenixborn.', '0', '10049', '1', NULL, NULL, 'f'),
('465', 'Fester', 'fester', '{"cost": ["[[main]]", "1 [[ceremonial:power]]"], "dice": ["ceremonial"], "name": "Fester", "stub": "fester", "text": "Destroy a target unit with 1 or more wound tokens on it.", "type": "Action Spell", "release": {"name": "The Children of Blackcloud", "stub": "the-children-of-blackcloud"}, "magicCost": {"ceremonial:power": 1}, "placement": "Discard"}', '27', 'Action Spell', '107', '1', NULL, NULL, 'f', 'Fester
Destroy a target unit with 1 or more wound tokens on it.', '0', '10050', '1', NULL, NULL, 'f'),
('466', 'Glow Finch', 'glow-finch', '{"life": 1, "name": "Glow Finch", "stub": "glow-finch", "text": "Unit Guard: This unit may guard a unit that is being attacked.\n\nLast Request 2: When this unit is destroyed, you may choose a target player to discard 2 cards off the top of their draw pile.", "type": "Conjuration", "attack": 0, "copies": 1, "recover": 0, "release": {"name": "The Roaring Rose", "stub": "the-roaring-rose"}, "placement": "Battlefield", "phoenixborn": "Leo Sunshadow"}', '28', 'Conjuration', '0', '0', 'Leo Sunshadow', '1', 'f', 'Glow Finch
Unit Guard: This unit may guard a unit that is being attacked. Last Request 2: When this unit is destroyed, you may choose a target player to discard 2 cards off the top of their draw pile.', '0', '10051', '1', NULL, NULL, 'f'),
('467', 'Leo Sunshadow', 'leo-sunshadow', '{"life": 19, "name": "Leo Sunshadow", "stub": "leo-sunshadow", "text": "Summon Glow Finch: [[side]] - [[exhaust]] - 1 [[basic]]: Place a [[Glow Finch]] conjuration onto your battlefield.", "type": "Phoenixborn", "release": {"name": "The Roaring Rose", "stub": "the-roaring-rose"}, "spellboard": 3, "battlefield": 6, "conjurations": [{"name": "Glow Finch", "stub": "glow-finch"}]}', '28', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Leo Sunshadow
Summon Glow Finch: side - exhaust - 1 basic: Place a Glow Finch conjuration onto your battlefield.', '0', '10052', '1', NULL, NULL, 'f'),
('468', 'Anguish', 'anguish', '{"cost": ["[[main]]", "2 [[basic]]"], "dice": ["basic"], "name": "Anguish", "stub": "anguish", "text": "Choose a target Phoenixborn. Its controlling player may discard 1 card at random from their hand. If they do not or cannot, place 2 wound tokens on that Phoenixborn. Then choose a target Phoenixborn. Its controlling player may move 2 dice of your choice from their active pool to their exhausted pool. If they do not or cannot, place 2 wound tokens on that Phoenixborn.", "type": "Action Spell", "release": {"name": "The Roaring Rose", "stub": "the-roaring-rose"}, "magicCost": {"basic": 2}, "placement": "Discard", "phoenixborn": "Leo Sunshadow"}', '28', 'Action Spell', '205', '0', 'Leo Sunshadow', NULL, 'f', 'Anguish
Choose a target Phoenixborn. Its controlling player may discard 1 card at random from their hand. If they do not or cannot, place 2 wound tokens on that Phoenixborn. Then choose a target Phoenixborn. Its controlling player may move 2 dice of your choice from their active pool to their exhausted pool. If they do not or cannot, place 2 wound tokens on that Phoenixborn.', '0', '10053', '1', NULL, NULL, 'f'),
('469', 'Orchid Dove', 'orchid-dove', '{"life": 1, "name": "Orchid Dove", "stub": "orchid-dove", "text": "Last Request 1: When this unit is destroyed, you may choose a target player to discard 1 card off the top of their draw pile.", "type": "Conjuration", "attack": 0, "copies": 3, "recover": 0, "release": {"name": "The Roaring Rose", "stub": "the-roaring-rose"}, "placement": "Battlefield"}', '28', 'Conjuration', '0', '0', NULL, '3', 'f', 'Orchid Dove
Last Request 1: When this unit is destroyed, you may choose a target player to discard 1 card off the top of their draw pile.', '0', '10054', '1', NULL, NULL, 'f'),
('470', 'Summon Orchid Dove', 'summon-orchid-dove', '{"cost": ["[[main]]"], "dice": ["charm"], "name": "Summon Orchid Dove", "stub": "summon-orchid-dove", "text": "[[main]] - [[exhaust]] - 1 [[charm:class]]: Place an [[Orchid Dove]] conjuration onto your battlefield.\n\nFocus 1: You may change the activation cost of this spell to [[main]] - [[exhaust]] - 1 [[basic]].\n\nFocus 2: You may deal 1 damage to a target player''s Phoenxiborn if they do not have any cards in their draw pile.", "type": "Ready Spell", "release": {"name": "The Roaring Rose", "stub": "the-roaring-rose"}, "placement": "Spellboard", "conjurations": [{"name": "Orchid Dove", "stub": "orchid-dove"}]}', '28', 'Ready Spell', '5', '2', NULL, NULL, 't', 'Summon Orchid Dove
main - exhaust - 1 charm:class: Place an Orchid Dove conjuration onto your battlefield. Focus 1: You may change the activation cost of this spell to main - exhaust - 1 basic. Focus 2: You may deal 1 damage to a target player''s Phoenxiborn if they do not have any cards in their draw pile.', '0', '10055', '1', NULL, NULL, 'f'),
('471', 'Nightshade Swallow', 'nightshade-swallow', '{"life": 2, "name": "Nightshade Swallow", "stub": "nightshade-swallow", "text": "Pacify 1: When this unit is destroyed, you may place 1 exhaustion token on a target unit.", "type": "Conjuration", "attack": 1, "copies": 2, "recover": 0, "release": {"name": "The Roaring Rose", "stub": "the-roaring-rose"}, "placement": "Battlefield"}', '28', 'Conjuration', '0', '0', NULL, '2', 'f', 'Nightshade Swallow
Pacify 1: When this unit is destroyed, you may place 1 exhaustion token on a target unit.', '0', '10056', '1', NULL, NULL, 'f'),
('472', 'Summon Nightshade Swallow', 'summon-nightshade-swallow', '{"cost": ["[[main]]"], "dice": ["charm"], "name": "Summon Nightshade Swallow", "stub": "summon-nightshade-swallow", "text": "[[main]] - [[exhaust]] - 2 [[charm:class]]: Place a [[Nightshade Swallow]] conjuration onto your battlefield.\n\nFocus 1: You may choose a target player to discard 1 card off the top of their draw pile if you have fewer dice in your active pool than an opponent.", "type": "Ready Spell", "release": {"name": "The Roaring Rose", "stub": "the-roaring-rose"}, "placement": "Spellboard", "conjurations": [{"name": "Nightshade Swallow", "stub": "nightshade-swallow"}]}', '28', 'Ready Spell', '5', '2', NULL, NULL, 't', 'Summon Nightshade Swallow
main - exhaust - 2 charm:class: Place a Nightshade Swallow conjuration onto your battlefield. Focus 1: You may choose a target player to discard 1 card off the top of their draw pile if you have fewer dice in your active pool than an opponent.', '0', '10057', '1', NULL, NULL, 'f'),
('473', 'Memory Theft', 'memory-theft', '{"cost": ["[[main]]"], "dice": ["charm"], "name": "Memory Theft", "stub": "memory-theft", "text": "[[main]] - [[exhaust]] - 1 [[charm:class]]: Look at a target player''s hand. That player may discard 1 card of your choice from that hand. If they do not or cannot, place 1 wound token on their Phoenixborn.", "type": "Ready Spell", "release": {"name": "The Roaring Rose", "stub": "the-roaring-rose"}, "placement": "Spellboard"}', '28', 'Ready Spell', '5', '2', NULL, NULL, 'f', 'Memory Theft
main - exhaust - 1 charm:class: Look at a target player''s hand. That player may discard 1 card of your choice from that hand. If they do not or cannot, place 1 wound token on their Phoenixborn.', '0', '10058', '1', NULL, NULL, 'f'),
('474', 'Beast Tamer', 'beast-tamer', '{"cost": ["[[main]]", "2 [[charm:class]]"], "dice": ["charm"], "life": 3, "name": "Beast Tamer", "stub": "beast-tamer", "text": "Tame 1: While this unit is in battle, the attack value of units in battle with it is reduced by 1.\n\nAlert: Do not place exhaustion tokens on this unit as a result of its countering.", "type": "Ally", "attack": 2, "recover": 1, "release": {"name": "The Roaring Rose", "stub": "the-roaring-rose"}, "magicCost": {"charm:class": 2}, "placement": "Battlefield"}', '28', 'Ally', '207', '2', NULL, NULL, 'f', 'Beast Tamer
Tame 1: While this unit is in battle, the attack value of units in battle with it is reduced by 1. Alert: Do not place exhaustion tokens on this unit as a result of its countering.', '0', '10059', '1', NULL, NULL, 'f'),
('475', 'Mind Probe', 'mind-probe', '{"cost": ["[[main]]", "1 [[charm:class]]"], "dice": ["charm"], "name": "Mind Probe", "stub": "mind-probe", "text": "Choose a target opponent to reveal the top 5 cards of their draw pile. Choose 1 of those revealed cards and remove it from the game. Return the rest of the revealed cards to the top of that opponent''s draw pile in the order of your choice.", "type": "Action Spell", "release": {"name": "The Roaring Rose", "stub": "the-roaring-rose"}, "magicCost": {"charm:class": 1}, "placement": "Discard"}', '28', 'Action Spell', '106', '2', NULL, NULL, 'f', 'Mind Probe
Choose a target opponent to reveal the top 5 cards of their draw pile. Choose 1 of those revealed cards and remove it from the game. Return the rest of the revealed cards to the top of that opponent''s draw pile in the order of your choice.', '0', '10060', '1', NULL, NULL, 'f'),
('476', 'Remorse', 'remorse', '{"cost": ["1 [[charm:power]]"], "dice": ["charm"], "name": "Remorse", "stub": "remorse", "text": "You may play this spell after an opponent declares attackers. That target player must discard 2 cards off the top of their draw pile. Then, if their draw pile is empty, deal 2 damage to their target Phoenixborn.", "type": "Reaction Spell", "release": {"name": "The Roaring Rose", "stub": "the-roaring-rose"}, "magicCost": {"charm:power": 1}, "placement": "Discard"}', '28', 'Reaction Spell', '102', '2', NULL, NULL, 'f', 'Remorse
You may play this spell after an opponent declares attackers. That target player must discard 2 cards off the top of their draw pile. Then, if their draw pile is empty, deal 2 damage to their target Phoenixborn.', '0', '10061', '1', NULL, NULL, 'f'),
('477', 'Dispel', 'dispel', '{"cost": ["[[main]]", "1 [[basic]]"], "dice": ["basic"], "name": "Dispel", "stub": "dispel", "text": "Remove 2 status tokens from a target card or choose a target alteration spell. If that alteration spell is a conjured alteration spell, return it to its owner''s conjuration pile. Otherwise, shuffle it into its owner''s draw pile.", "type": "Action Spell", "release": {"name": "The Roaring Rose", "stub": "the-roaring-rose"}, "magicCost": {"basic": 1}, "placement": "Discard"}', '28', 'Action Spell', '105', '0', NULL, NULL, 'f', 'Dispel
Remove 2 status tokens from a target card or choose a target alteration spell. If that alteration spell is a conjured alteration spell, return it to its owner''s conjuration pile. Otherwise, shuffle it into its owner''s draw pile.', '0', '10062', '1', NULL, NULL, 'f'),
('478', 'Change Psyche', 'change-psyche', '{"cost": ["[[main]]", "1 [[charm:class]]", "1 [[basic]]"], "dice": ["charm"], "name": "Change Psyche", "stub": "change-psyche", "text": "Remove 1 exhaustion token from a target unit or place 1 exhaustion token on a target unit.", "type": "Action Spell", "release": {"name": "The Roaring Rose", "stub": "the-roaring-rose"}, "magicCost": {"basic": 1, "charm:class": 1}, "placement": "Discard"}', '28', 'Action Spell', '206', '2', NULL, NULL, 'f', 'Change Psyche
Remove 1 exhaustion token from a target unit or place 1 exhaustion token on a target unit.', '0', '10063', '1', NULL, NULL, 'f'),
('479', 'Amplify', 'amplify', '{"cost": ["[[side]]", "1 [[charm:class]]"], "dice": ["charm"], "name": "Amplify", "stub": "amplify", "text": "Choose a target unit you control with an attack value of 0. Add 3 to its attack value for the remainder of the turn.", "type": "Action Spell", "release": {"name": "The Roaring Rose", "stub": "the-roaring-rose"}, "magicCost": {"charm:class": 1}, "placement": "Discard"}', '28', 'Action Spell', '105', '2', NULL, NULL, 'f', 'Amplify
Choose a target unit you control with an attack value of 0. Add 3 to its attack value for the remainder of the turn.', '0', '10064', '1', NULL, NULL, 'f'),
('480', 'Victoria Glassfire', 'victoria-glassfire', '{"dice": ["illusion"], "life": 18, "name": "Victoria Glassfire", "stub": "victoria-glassfire", "text": "Surprise!: [[side]] - [[exhaust]] - 1 [[illusion:class]]: Re-roll up to 4 dice in a target opponent''s active pool. Re-roll an equal number of dice in your active pool.", "type": "Phoenixborn", "release": {"name": "The Duchess of Deception", "stub": "the-duchess-of-deception"}, "spellboard": 5, "battlefield": 5}', '29', 'Phoenixborn', '0', '4', NULL, NULL, 'f', 'Victoria Glassfire
Surprise!: side - exhaust - 1 illusion:class: Re-roll up to 4 dice in a target opponent''s active pool. Re-roll an equal number of dice in your active pool.', '0', '10065', '1', NULL, NULL, 'f'),
('481', 'Copycat', 'copycat', '{"cost": ["1 [[basic]]"], "dice": ["basic"], "name": "Copycat", "stub": "copycat", "text": "You may play this spell after an opponent resolves an action spell or activated Phoenixborn ability. Resolve a copy of that spell or ability without paying its play cost or activation cost.", "type": "Reaction Spell", "release": {"name": "The Duchess of Deception", "stub": "the-duchess-of-deception"}, "magicCost": {"basic": 1}, "placement": "Discard", "phoenixborn": "Victoria Glassfire"}', '29', 'Reaction Spell', '100', '0', 'Victoria Glassfire', NULL, 'f', 'Copycat
You may play this spell after an opponent resolves an action spell or activated Phoenixborn ability. Resolve a copy of that spell or ability without paying its play cost or activation cost.', '0', '10066', '1', NULL, NULL, 'f'),
('482', 'Shadow Hound', 'shadow-hound', '{"life": 1, "name": "Shadow Hound", "stub": "shadow-hound", "text": "Concealed: This unit cannot be targeted by attacks, spells, abilities, or dice powers an opponent controls.\n\nStalk: This unit cannot be guarded against.", "type": "Conjuration", "attack": 3, "copies": 2, "recover": 0, "release": {"name": "The Duchess of Deception", "stub": "the-duchess-of-deception"}, "placement": "Battlefield"}', '29', 'Conjuration', '0', '0', NULL, '2', 'f', 'Shadow Hound
Concealed: This unit cannot be targeted by attacks, spells, abilities, or dice powers an opponent controls. Stalk: This unit cannot be guarded against.', '0', '10067', '1', NULL, NULL, 'f'),
('483', 'Summon Shadow Hound', 'summon-shadow-hound', '{"cost": ["[[main]]"], "dice": ["illusion"], "name": "Summon Shadow Hound", "stub": "summon-shadow-hound", "text": "[[main]] - [[exhaust]] - 3 [[illusion:class]]: Place a [[Shadow Hound]] conjuration onto your battlefield.\n\nFocus 1: You may deal 1 damage to a target unit.\n\nFocus 2: Then you may deal 1 damage to a target unit.", "type": "Ready Spell", "release": {"name": "The Duchess of Deception", "stub": "the-duchess-of-deception"}, "placement": "Spellboard", "conjurations": [{"name": "Shadow Hound", "stub": "shadow-hound"}]}', '29', 'Ready Spell', '5', '4', NULL, NULL, 't', 'Summon Shadow Hound
main - exhaust - 3 illusion:class: Place a Shadow Hound conjuration onto your battlefield. Focus 1: You may deal 1 damage to a target unit. Focus 2: Then you may deal 1 damage to a target unit.', '0', '10068', '1', NULL, NULL, 'f'),
('484', 'Shadow Spirit', 'shadow-spirit', '{"life": 1, "name": "Shadow Spirit", "stub": "shadow-spirit", "text": "Trickery 1: When this unit is declared as an attacker, lower 1 die in a target opponent''s active pool one level.", "type": "Conjuration", "attack": 2, "copies": 3, "recover": 0, "release": {"name": "The Duchess of Deception", "stub": "the-duchess-of-deception"}, "placement": "Battlefield"}', '29', 'Conjuration', '0', '0', NULL, '3', 'f', 'Shadow Spirit
Trickery 1: When this unit is declared as an attacker, lower 1 die in a target opponent''s active pool one level.', '0', '10069', '1', NULL, NULL, 'f'),
('485', 'Summon Shadow Spirit', 'summon-shadow-spirit', '{"cost": ["[[main]]"], "dice": ["illusion"], "name": "Summon Shadow Spirit", "stub": "summon-shadow-spirit", "text": "[[main]] - [[exhaust]] - 1 [[illusion:power]]: Place a [[Shadow Spirit]] conjuration onto your battlefield.", "type": "Ready Spell", "release": {"name": "The Duchess of Deception", "stub": "the-duchess-of-deception"}, "placement": "Spellboard", "conjurations": [{"name": "Shadow Spirit", "stub": "shadow-spirit"}]}', '29', 'Ready Spell', '5', '4', NULL, NULL, 't', 'Summon Shadow Spirit
main - exhaust - 1 illusion:power: Place a Shadow Spirit conjuration onto your battlefield.', '0', '10070', '1', NULL, NULL, 'f'),
('486', 'To Shadows', 'to-shadows', '{"cost": ["[[side]]", ["1 [[illusion:power]]", "1 [[time:power]]"]], "dice": ["illusion"], "name": "To Shadows", "stub": "to-shadows", "text": "Discard a target exhausted unit.", "type": "Action Spell", "altDice": ["time", "illusion"], "release": {"name": "The Duchess of Deception", "stub": "the-duchess-of-deception"}, "magicCost": {"illusion:power / time:power": 1}, "placement": "Discard"}', '29', 'Action Spell', '106', '0', NULL, NULL, 'f', 'To Shadows
Discard a target exhausted unit.', '68', '10071', '1', NULL, NULL, 'f'),
('487', 'Secret Door', 'secret-door', '{"cost": ["[[main]]"], "dice": ["illusion"], "name": "Secret Door", "stub": "secret-door", "text": "[[side]] - [[exhaust]] - 1 [[illusion:class]]: Choose a target unit you control with a life value of 1. It cannot be blocked for the remainder of the turn.", "type": "Ready Spell", "release": {"name": "The Duchess of Deception", "stub": "the-duchess-of-deception"}, "placement": "Spellboard"}', '29', 'Ready Spell', '5', '4', NULL, NULL, 'f', 'Secret Door
side - exhaust - 1 illusion:class: Choose a target unit you control with a life value of 1. It cannot be blocked for the remainder of the turn.', '0', '10072', '1', NULL, NULL, 'f'),
('488', 'Particle Shield', 'particle-shield', '{"cost": ["1 [[illusion:class]]"], "dice": ["illusion"], "name": "Particle Shield", "stub": "particle-shield", "text": "You may play this spell after a unit you control is dealt damage. Prevent 1 damage from being received. Draw 1 card.", "type": "Reaction Spell", "release": {"name": "The Duchess of Deception", "stub": "the-duchess-of-deception"}, "magicCost": {"illusion:class": 1}, "placement": "Discard"}', '29', 'Reaction Spell', '101', '4', NULL, NULL, 'f', 'Particle Shield
You may play this spell after a unit you control is dealt damage. Prevent 1 damage from being received. Draw 1 card.', '0', '10073', '1', NULL, NULL, 'f'),
('489', 'Vanish', 'vanish', '{"cost": ["1 [[illusion:power]]"], "dice": ["illusion"], "name": "Vanish", "stub": "vanish", "text": "You may play this spell after an opponent targets you or your Phoenixborn with a spell, ability, or dice power. Cancel that effect and the remaining effects of that spell, ability, or dice power.", "type": "Reaction Spell", "release": {"name": "The Duchess of Deception", "stub": "the-duchess-of-deception"}, "magicCost": {"illusion:power": 1}, "placement": "Discard"}', '29', 'Reaction Spell', '102', '4', NULL, NULL, 'f', 'Vanish
You may play this spell after an opponent targets you or your Phoenixborn with a spell, ability, or dice power. Cancel that effect and the remaining effects of that spell, ability, or dice power.', '0', '10074', '1', NULL, NULL, 'f'),
('490', 'Body Inversion', 'body-inversion', '{"cost": ["[[side]]"], "dice": ["illusion"], "name": "Body Inversion", "stub": "body-inversion", "text": "[[side]] - [[exhaust]] - 1 [[illusion:class]]: Swap a target unit''s printed attack value with its printed life value for the remainder of the turn.", "type": "Ready Spell", "release": {"name": "The Duchess of Deception", "stub": "the-duchess-of-deception"}, "placement": "Spellboard"}', '29', 'Ready Spell', '4', '4', NULL, NULL, 'f', 'Body Inversion
side - exhaust - 1 illusion:class: Swap a target unit''s printed attack value with its printed life value for the remainder of the turn.', '0', '10075', '1', NULL, NULL, 'f'),
('491', 'Figures In The Fog', 'figures-in-the-fog', '{"cost": ["1 [[illusion:power]]"], "dice": ["illusion"], "name": "Figures In The Fog", "stub": "figures-in-the-fog", "text": "You may play this spell after an opponent declares attackers. Choose a target attacking unit and place 1 exhaustion token on it. It is no longer attacking.", "type": "Reaction Spell", "release": {"name": "The Duchess of Deception", "stub": "the-duchess-of-deception"}, "magicCost": {"illusion:power": 1}, "placement": "Discard"}', '29', 'Reaction Spell', '102', '4', NULL, NULL, 'f', 'Figures In The Fog
You may play this spell after an opponent declares attackers. Choose a target attacking unit and place 1 exhaustion token on it. It is no longer attacking.', '0', '10076', '1', NULL, NULL, 'f'),
('492', 'Flash Archer', 'flash-archer', '{"cost": ["[[main]]", "2 [[illusion:class]]", "2 [[basic]]"], "dice": ["illusion"], "life": 2, "name": "Flash Archer", "stub": "flash-archer", "text": "Double Shot: [[side]] - [[exhaust]]: Deal 1 damage to a target unit. Then you may deal 1 damage to a target unit.", "type": "Ally", "attack": 4, "recover": 2, "release": {"name": "The Duchess of Deception", "stub": "the-duchess-of-deception"}, "magicCost": {"basic": 2, "illusion:class": 2}, "placement": "Battlefield"}', '29', 'Ally', '407', '4', NULL, NULL, 'f', 'Flash Archer
Double Shot: side - exhaust: Deal 1 damage to a target unit. Then you may deal 1 damage to a target unit.', '0', '10077', '1', NULL, NULL, 'f'),
('493', 'Odette Diamondcrest', 'odette-diamondcrest', '{"life": 18, "name": "Odette Diamondcrest", "stub": "odette-diamondcrest", "text": "Enter the Fray: [[main]] - [[exhaust]]: Deal 2 damage to a target unit. Deal damage to this Phoenixborn equal to the target unit''s attack value.", "type": "Phoenixborn", "release": {"name": "The Law of Lions", "stub": "the-law-of-lions"}, "spellboard": 3, "battlefield": 5}', '30', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Odette Diamondcrest
Enter the Fray: main - exhaust: Deal 2 damage to a target unit. Deal damage to this Phoenixborn equal to the target unit''s attack value.', '0', '10078', '1', NULL, NULL, 'f'),
('494', 'Sword of Virtue', 'sword-of-virtue', '{"cost": ["[[main]]", "2 [[basic]]"], "dice": ["basic"], "name": "Sword of Virtue", "stub": "sword-of-virtue", "text": "Destroy a target unit or remove all wound tokens from a target unit.", "type": "Action Spell", "release": {"name": "The Law of Lions", "stub": "the-law-of-lions"}, "magicCost": {"basic": 2}, "placement": "Discard", "phoenixborn": "Odette Diamondcrest"}', '30', 'Action Spell', '205', '0', 'Odette Diamondcrest', NULL, 'f', 'Sword of Virtue
Destroy a target unit or remove all wound tokens from a target unit.', '0', '10079', '1', NULL, NULL, 'f'),
('495', 'Emperor Lion', 'emperor-lion', '{"life": 3, "name": "Emperor Lion", "stub": "emperor-lion", "text": "Decree: When this unit comes into play, search your draw pile. You may reveal a ready spell with \"Law\" in its title and place it into your hand.  You may immediately play a \"Law\" from your hand without paying any <main> or <side> costs. Shuffle your draw pile.", "type": "Conjuration", "attack": 3, "copies": 1, "recover": 0, "release": {"name": "The Law of Lions", "stub": "the-law-of-lions"}, "placement": "Battlefield"}', '30', 'Conjuration', '0', '0', NULL, '1', 'f', 'Emperor Lion
Decree: When this unit comes into play, search your draw pile. You may reveal a ready spell with "Law" in its title and place it into your hand.  You may immediately play a "Law" from your hand without paying any <main> or <side> costs. Shuffle your draw pile.', '0', '10080', '1', NULL, NULL, 'f'),
('496', 'Summon Emperor Lion', 'summon-emperor-lion', '{"cost": ["[[main]]"], "dice": ["divine"], "name": "Summon Emperor Lion", "stub": "summon-emperor-lion", "text": "[[main]] - [[exhaust]] - 2 [[divine:class]] - 1 [[basic]]:  Place an [[Emperor Lion]] conjuration onto your battlefield.", "type": "Ready Spell", "release": {"name": "The Law of Lions", "stub": "the-law-of-lions"}, "placement": "Spellboard", "conjurations": [{"name": "Emperor Lion", "stub": "emperor-lion"}]}', '30', 'Ready Spell', '5', '16', NULL, NULL, 't', 'Summon Emperor Lion
main - exhaust - 2 divine:class - 1 basic:  Place an Emperor Lion conjuration onto your battlefield.', '0', '10081', '1', NULL, NULL, 'f'),
('497', 'Winged Lioness', 'winged-lioness', '{"life": 2, "name": "Winged Lioness", "stub": "winged-lioness", "text": "Stalk: This unit cannot be guarded against.", "type": "Conjuration", "attack": 2, "copies": 4, "recover": 1, "release": {"name": "The Law of Lions", "stub": "the-law-of-lions"}, "placement": "Battlefield"}', '30', 'Conjuration', '0', '0', NULL, '4', 'f', 'Winged Lioness
Stalk: This unit cannot be guarded against.', '0', '10082', '1', NULL, NULL, 'f'),
('498', 'Summon Winged Lioness', 'summon-winged-lioness', '{"cost": ["[[main]]"], "dice": ["divine"], "name": "Summon Winged Lioness", "stub": "summon-winged-lioness", "text": "[[main]] - [[exhaust]] - 1 [[divine:class]] - 1 [[basic]]: Place a [[Winged Lioness]] conjuration onto your battlefield.", "type": "Ready Spell", "release": {"name": "The Law of Lions", "stub": "the-law-of-lions"}, "placement": "Spellboard", "conjurations": [{"name": "Winged Lioness", "stub": "winged-lioness"}]}', '30', 'Ready Spell', '5', '16', NULL, NULL, 't', 'Summon Winged Lioness
main - exhaust - 1 divine:class - 1 basic: Place a Winged Lioness conjuration onto your battlefield.', '0', '10083', '1', NULL, NULL, 'f'),
('499', 'Law of Sight', 'law-of-sight', '{"cost": ["[[side]]", "1 [[divine:class]]", "1 [[basic]]"], "dice": ["divine"], "name": "Law of Sight", "stub": "law-of-sight", "text": "When this spell comes into play, you may draw up to 2 cards. No player may play reaction spells.\n\n* Bound: This card cannot be discarded from your spellboard when you Meditate.\n\n* Fleeting: Discard this card at the end of this round.", "type": "Ready Spell", "release": {"name": "The Law of Lions", "stub": "the-law-of-lions"}, "magicCost": {"basic": 1, "divine:class": 1}, "placement": "Spellboard"}', '30', 'Ready Spell', '205', '16', NULL, NULL, 'f', 'Law of Sight
When this spell comes into play, you may draw up to 2 cards. No player may play reaction spells. * Bound: This card cannot be discarded from your spellboard when you Meditate. * Fleeting: Discard this card at the end of this round.', '0', '10084', '1', NULL, NULL, 'f'),
('500', 'Law of Assurance', 'law-of-assurance', '{"cost": ["[[side]]", "1 [[divine:class]]"], "dice": ["divine"], "name": "Law of Assurance", "stub": "law-of-assurance", "text": "When this spell comes into play, change all dice in your active pool to their class side.\n\nPlayers may not re-roll or change the level of dice in an opponent''s active pool.\n\n* Bound: This card cannot be discarded from your spellboard when you Meditate.\n\n* Fleeting: Discard this card at the end of this round.", "type": "Ready Spell", "release": {"name": "The Law of Lions", "stub": "the-law-of-lions"}, "magicCost": {"divine:class": 1}, "placement": "Spellboard"}', '30', 'Ready Spell', '105', '16', NULL, NULL, 'f', 'Law of Assurance
When this spell comes into play, change all dice in your active pool to their class side. Players may not re-roll or change the level of dice in an opponent''s active pool. * Bound: This card cannot be discarded from your spellboard when you Meditate. * Fleeting: Discard this card at the end of this round.', '0', '10085', '1', NULL, NULL, 'f');

INSERT INTO "public"."card" ("id", "name", "stub", "json", "release_id", "card_type", "cost_weight", "dice_flags", "phoenixborn", "copies", "is_summon_spell", "search_text", "alt_dice_flags", "entity_id", "version", "artist_name", "artist_url", "is_legacy") VALUES
('501', 'Holy Knight', 'holy-knight', '{"cost": ["[[main]]", "1 [[divine:power]]", "1 [[divine:class]]", "1 [[basic]]"], "dice": ["divine"], "life": 3, "name": "Holy Knight", "stub": "holy-knight", "text": "Magic Armor: This unit cannot be targeted by spells an opponent controls.", "type": "Ally", "attack": 3, "recover": 2, "release": {"name": "The Law of Lions", "stub": "the-law-of-lions"}, "magicCost": {"basic": 1, "divine:class": 1, "divine:power": 1}, "placement": "Battlefield"}', '30', 'Ally', '308', '16', NULL, NULL, 'f', 'Holy Knight
Magic Armor: This unit cannot be targeted by spells an opponent controls.', '0', '10086', '1', NULL, NULL, 'f'),
('502', 'Shield Mage', 'shield-mage', '{"cost": ["[[side]]", "1 [[divine:class]]", "1 [[basic]]"], "dice": ["divine"], "life": 2, "name": "Shield Mage", "stub": "shield-mage", "text": "Defensive Aura: Units you control cannot be targeted by attacks an opponent controls.", "type": "Ally", "attack": 0, "recover": 1, "release": {"name": "The Law of Lions", "stub": "the-law-of-lions"}, "magicCost": {"basic": 1, "divine:class": 1}, "placement": "Battlefield"}', '30', 'Ally', '205', '16', NULL, NULL, 'f', 'Shield Mage
Defensive Aura: Units you control cannot be targeted by attacks an opponent controls.', '0', '10087', '1', NULL, NULL, 'f'),
('503', 'Heal', 'heal', '{"cost": ["[[side]]", "1 [[divine:class]]"], "dice": ["divine"], "name": "Heal", "stub": "heal", "text": "Remove all wound tokens from a target unit or 2 wound tokens from a target Phoenixborn.", "type": "Action Spell", "release": {"name": "The Law of Lions", "stub": "the-law-of-lions"}, "magicCost": {"divine:class": 1}, "placement": "Discard"}', '30', 'Action Spell', '105', '16', NULL, NULL, 'f', 'Heal
Remove all wound tokens from a target unit or 2 wound tokens from a target Phoenixborn.', '0', '10088', '1', NULL, NULL, 'f'),
('504', 'Power Through', 'power-through', '{"cost": ["[[side]]", "1 [[divine:class]]"], "dice": ["divine"], "name": "Power Through", "stub": "power-through", "text": "This unit now has the following ability:\n\nOverkill 1: After this unit destroys a unit an opponent controls by attacking, deal 1 damage to that opponent''s target Phoenixborn.", "type": "Alteration Spell", "attack": "+1", "release": {"name": "The Law of Lions", "stub": "the-law-of-lions"}, "magicCost": {"divine:class": 1}, "placement": "Unit"}', '30', 'Alteration Spell', '105', '16', NULL, NULL, 'f', 'Power Through
This unit now has the following ability: Overkill 1: After this unit destroys a unit an opponent controls by attacking, deal 1 damage to that opponent''s target Phoenixborn.', '0', '10089', '1', NULL, NULL, 'f'),
('505', 'Meteor', 'meteor', '{"cost": ["[[main]]", "[[side]]", "2 [[divine:class]]"], "dice": ["divine"], "name": "Meteor", "stub": "meteor", "text": "Deal 1 damage to all units. Then, deal damage to all units equal to the number of[[divine:power]] spent to play this spell.", "type": "Action Spell", "release": {"name": "The Law of Lions", "stub": "the-law-of-lions"}, "magicCost": {"divine:class": 2}, "placement": "Discard"}', '30', 'Action Spell', '211', '16', NULL, NULL, 'f', 'Meteor
Deal 1 damage to all units. Then, deal damage to all units equal to the number ofdivine:power spent to play this spell.', '0', '10090', '1', NULL, NULL, 'f'),
('506', 'Namine Hymntide', 'namine-hymntide', '{"dice": ["sympathy"], "life": 17, "name": "Namine Hymntide", "stub": "namine-hymntide", "text": "Calming Melody: [[side]] - [[exhaust]] - 1 [[sympathy:class]]: Draw 1 card. You may place 1 exhaustion token on this card and 1 exhaustion token on a target Phoenixborn.", "type": "Phoenixborn", "release": {"name": "The Song of Soaksend", "stub": "the-song-of-soaksend"}, "spellboard": 4, "battlefield": 6}', '31', 'Phoenixborn', '0', '32', NULL, NULL, 'f', 'Namine Hymntide
Calming Melody: side - exhaust - 1 sympathy:class: Draw 1 card. You may place 1 exhaustion token on this card and 1 exhaustion token on a target Phoenixborn.', '0', '10091', '1', NULL, NULL, 'f'),
('507', 'Encore', 'encore', '{"cost": ["[[main]]"], "name": "Encore", "stub": "encore", "text": "Search your discard pile for a card other than Encore and place it on the top or bottom of your draw pile. Draw 1 card.", "type": "Action Spell", "release": {"name": "The Song of Soaksend", "stub": "the-song-of-soaksend"}, "placement": "Discard", "phoenixborn": "Namine Hymntide"}', '31', 'Action Spell', '5', '0', 'Namine Hymntide', NULL, 'f', 'Encore
Search your discard pile for a card other than Encore and place it on the top or bottom of your draw pile. Draw 1 card.', '0', '10092', '1', NULL, NULL, 'f'),
('508', 'Squall Stallion', 'squall-stallion', '{"life": 3, "name": "Squall Stallion", "stub": "squall-stallion", "text": "Lightning Speed: This unit cannot be targeted by reaction spells an opponent controls.\n\n* Torrent 1: [[side]]: Place 1 card from your hand on the top or bottom of your draw pile. If you do, place 1 status token on all Squall Stallions you control.\n\n* X = the number of status tokens on this unit.", "type": "Conjuration", "attack": "X", "copies": 2, "recover": 0, "release": {"name": "The Song of Soaksend", "stub": "the-song-of-soaksend"}, "placement": "Battlefield"}', '31', 'Conjuration', '0', '0', NULL, '2', 'f', 'Squall Stallion
Lightning Speed: This unit cannot be targeted by reaction spells an opponent controls. * Torrent 1: side: Place 1 card from your hand on the top or bottom of your draw pile. If you do, place 1 status token on all Squall Stallions you control. * X = the number of status tokens on this unit.', '0', '10093', '1', NULL, NULL, 'f'),
('509', 'Summon Squall Stallion', 'summon-squall-stallion', '{"cost": ["[[main]]", "1 [[sympathy:power]]"], "dice": ["sympathy"], "name": "Summon Squall Stallion", "stub": "summon-squall-stallion", "text": "[[main]] - [[exhaust]] - 1 [[sympathy:class]] - 1 [[basic]]: Draw 1 card. Place a [[Squall Stallion]] conjuration onto your battlefield.", "type": "Ready Spell", "release": {"name": "The Song of Soaksend", "stub": "the-song-of-soaksend"}, "magicCost": {"sympathy:power": 1}, "placement": "Spellboard", "conjurations": [{"name": "Squall Stallion", "stub": "squall-stallion"}]}', '31', 'Ready Spell', '107', '32', NULL, NULL, 't', 'Summon Squall Stallion
main - exhaust - 1 sympathy:class - 1 basic: Draw 1 card. Place a Squall Stallion conjuration onto your battlefield.', '0', '10094', '1', NULL, NULL, 'f'),
('510', 'Salamander Monk Spirit', 'salamander-monk-spirit', '{"life": 1, "name": "Salamander Monk Spirit", "stub": "salamander-monk-spirit", "text": "* Transparent: This unit cannot block or be chosen at the target of an attack.", "type": "Conjuration", "attack": 1, "copies": 3, "recover": 0, "release": {"name": "The Song of Soaksend", "stub": "the-song-of-soaksend"}, "placement": "Battlefield"}', '31', 'Conjuration', '0', '0', NULL, '3', 'f', 'Salamander Monk Spirit
* Transparent: This unit cannot block or be chosen at the target of an attack.', '0', '10095', '1', NULL, NULL, 'f'),
('511', 'Salamander Monk', 'salamander-monk', '{"life": 1, "name": "Salamander Monk", "stub": "salamander-monk", "text": "Spirit Form: When this unit is destroyed, place a [[Salamander Monk Spirit]] conjuration onto your battlefield.", "type": "Conjuration", "attack": 1, "copies": 2, "recover": 0, "release": {"name": "The Song of Soaksend", "stub": "the-song-of-soaksend"}, "placement": "Battlefield", "conjurations": [{"name": "Salamander Monk Spirit", "stub": "salamander-monk-spirit"}]}', '31', 'Conjuration', '0', '0', NULL, '2', 'f', 'Salamander Monk
Spirit Form: When this unit is destroyed, place a Salamander Monk Spirit conjuration onto your battlefield.', '0', '10096', '1', NULL, NULL, 'f'),
('512', 'Summon Salamander Monk', 'summon-salamander-monk', '{"cost": ["[[main]]"], "dice": ["sympathy"], "name": "Summon Salamander Monk", "stub": "summon-salamander-monk", "text": "[[main]] - [[exhaust]] - 1 [[sympathy:class]]: Place a [[Salamander Monk]] conjuration onto your battlefield.", "type": "Ready Spell", "release": {"name": "The Song of Soaksend", "stub": "the-song-of-soaksend"}, "placement": "Spellboard", "conjurations": [{"name": "Salamander Monk", "stub": "salamander-monk"}, {"name": "Salamander Monk Spirit", "stub": "salamander-monk-spirit"}]}', '31', 'Ready Spell', '5', '32', NULL, NULL, 't', 'Summon Salamander Monk
main - exhaust - 1 sympathy:class: Place a Salamander Monk conjuration onto your battlefield.', '0', '10097', '1', NULL, NULL, 'f'),
('513', 'Guilt Link', 'guilt-link', '{"cost": ["[[main]]", "1 [[sympathy:class]]"], "dice": ["sympathy"], "name": "Guilt Link", "stub": "guilt-link", "text": "After 1 or more wound tokens are placed on your Phoenixborn as a result of a unit''s attack, place 1 status token on this spell if it has no status tokens on it.\n\n[[side]] - [[exhaust]]: Remove 1 status token from this spell to destroy a unit you control. If you do, choose a target player to destroy a unit they control.", "type": "Ready Spell", "release": {"name": "The Song of Soaksend", "stub": "the-song-of-soaksend"}, "magicCost": {"sympathy:class": 1}, "placement": "Spellboard"}', '31', 'Ready Spell', '106', '32', NULL, NULL, 'f', 'Guilt Link
After 1 or more wound tokens are placed on your Phoenixborn as a result of a unit''s attack, place 1 status token on this spell if it has no status tokens on it. side - exhaust: Remove 1 status token from this spell to destroy a unit you control. If you do, choose a target player to destroy a unit they control.', '0', '10098', '1', NULL, NULL, 'f'),
('514', 'Magic Syphon', 'magic-syphon', '{"cost": ["[[main]]", "1 [[sympathy:class]]"], "dice": ["sympathy"], "name": "Magic Syphon", "stub": "magic-syphon", "text": "[[side]] - [[exhaust]]: Change 1 die in your active pool to a side of your choice. Change 1 die in a target player''s active pool to a side of your choice.", "type": "Ready Spell", "release": {"name": "The Song of Soaksend", "stub": "the-song-of-soaksend"}, "magicCost": {"sympathy:class": 1}, "placement": "Spellboard"}', '31', 'Ready Spell', '106', '32', NULL, NULL, 'f', 'Magic Syphon
side - exhaust: Change 1 die in your active pool to a side of your choice. Change 1 die in a target player''s active pool to a side of your choice.', '0', '10099', '1', NULL, NULL, 'f'),
('515', 'River Skald', 'river-skald', '{"cost": ["[[main]]", "2 [[sympathy:class]]"], "dice": ["sympathy"], "life": 2, "name": "River Skald", "stub": "river-skald", "text": "Harsh Melody: When this unit comes into play, draw 1 card. You may discard 1 card from your hand to deal X damage to a target unit.\n\nX = the magic play cost of the discarded card.", "type": "Ally", "attack": 2, "recover": 1, "release": {"name": "The Song of Soaksend", "stub": "the-song-of-soaksend"}, "magicCost": {"sympathy:class": 2}, "placement": "Battlefield"}', '31', 'Ally', '207', '32', NULL, NULL, 'f', 'River Skald
Harsh Melody: When this unit comes into play, draw 1 card. You may discard 1 card from your hand to deal X damage to a target unit. X = the magic play cost of the discarded card.', '0', '10100', '1', NULL, NULL, 'f'),
('516', 'Flute Mage', 'flute-mage', '{"cost": ["[[main]]", "1 [[sympathy:class]]", "1 [[basic]]"], "dice": ["sympathy"], "life": 2, "name": "Flute Mage", "stub": "flute-mage", "text": "Enliven: [[side]] - [[exhaust]]: Remove 1 exhaustion token from a target unit.", "type": "Ally", "attack": 1, "recover": 1, "release": {"name": "The Song of Soaksend", "stub": "the-song-of-soaksend"}, "magicCost": {"basic": 1, "sympathy:class": 1}, "placement": "Battlefield"}', '31', 'Ally', '206', '32', NULL, NULL, 'f', 'Flute Mage
Enliven: side - exhaust: Remove 1 exhaustion token from a target unit.', '0', '10101', '1', NULL, NULL, 'f'),
('517', 'String Mage', 'string-mage', '{"cost": ["[[main]]", "1 [[sympathy:power]]", "1 [[sympathy:class]]"], "dice": ["sympathy"], "life": 3, "name": "String Mage", "stub": "string-mage", "text": "Exchange Link 1: [[side]]: Move 1 wound or status token from a target unit onto this unit, or move 1 wound or status token from this unit onto a target unit.", "type": "Ally", "attack": 1, "recover": 2, "release": {"name": "The Song of Soaksend", "stub": "the-song-of-soaksend"}, "magicCost": {"sympathy:class": 1, "sympathy:power": 1}, "placement": "Battlefield"}', '31', 'Ally', '208', '32', NULL, NULL, 'f', 'String Mage
Exchange Link 1: side: Move 1 wound or status token from a target unit onto this unit, or move 1 wound or status token from this unit onto a target unit.', '0', '10102', '1', NULL, NULL, 'f'),
('518', 'Crescendo', 'crescendo', '{"cost": ["1 [[sympathy:class]]", "1 [[discard]]"], "dice": ["sympathy"], "name": "Crescendo", "stub": "crescendo", "text": "You may play this spell after you have declared attackers. Deal 1 damage to a target unit you control to deal 3 damage to a target unit.", "type": "Reaction Spell", "release": {"name": "The Song of Soaksend", "stub": "the-song-of-soaksend"}, "magicCost": {"sympathy:class": 1}, "placement": "Discard"}', '31', 'Reaction Spell', '104', '32', NULL, NULL, 'f', 'Crescendo
You may play this spell after you have declared attackers. Deal 1 damage to a target unit you control to deal 3 damage to a target unit.', '0', '10103', '1', NULL, NULL, 'f'),
('519', 'Shatter Pulse', 'shatter-pulse', '{"cost": ["2 [[sympathy:class]]", "1 [[basic]]"], "dice": ["sympathy"], "name": "Shatter Pulse", "stub": "shatter-pulse", "text": "You may play this spell after a unit you control is destroyed. Destroy a target unit. You may change 2 dice in a target player''s active pool to a side of your choice.", "type": "Reaction Spell", "release": {"name": "The Song of Soaksend", "stub": "the-song-of-soaksend"}, "magicCost": {"basic": 1, "sympathy:class": 2}, "placement": "Discard"}', '31', 'Reaction Spell', '302', '32', NULL, NULL, 'f', 'Shatter Pulse
You may play this spell after a unit you control is destroyed. Destroy a target unit. You may change 2 dice in a target player''s active pool to a side of your choice.', '0', '10104', '1', NULL, NULL, 'f'),
('520', 'Echo Greystorm', 'echo-greystorm', '{"life": 19, "name": "Echo Greystorm", "stub": "echo-greystorm", "text": "Gravity Flux: [[side]] - [[exhaust]]: Place 1 exhaustion token on a target unit. At the end of this turn, remove that same exhaustion token.", "type": "Phoenixborn", "release": {"name": "The Masters of Gravity", "stub": "the-masters-of-gravity"}, "spellboard": 3, "battlefield": 6}', '32', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Echo Greystorm
Gravity Flux: side - exhaust: Place 1 exhaustion token on a target unit. At the end of this turn, remove that same exhaustion token.', '0', '10105', '1', NULL, NULL, 'f'),
('521', 'Chaos Gravity', 'chaos-gravity', '{"cost": ["[[main]]", ["1 [[divine:class]]", "1 [[sympathy:class]]"], "1 [[basic]]"], "dice": ["divine"], "name": "Chaos Gravity", "stub": "chaos-gravity", "text": "Place 1 exhaustion token on a target unit. Move 1 exhaustion token from a target unit to another unit controlled by the same player. Remove 1 exhaustion token from a target unit.", "type": "Action Spell", "altDice": ["sympathy", "divine"], "release": {"name": "The Masters of Gravity", "stub": "the-masters-of-gravity"}, "magicCost": {"basic": 1, "divine:class / sympathy:class": 1}, "placement": "Discard", "phoenixborn": "Echo Greystorm"}', '32', 'Action Spell', '206', '0', 'Echo Greystorm', NULL, 'f', 'Chaos Gravity
Place 1 exhaustion token on a target unit. Move 1 exhaustion token from a target unit to another unit controlled by the same player. Remove 1 exhaustion token from a target unit.', '48', '10106', '1', NULL, NULL, 'f'),
('522', 'Enhanced Strength', 'enhanced-strength', '{"life": "+1", "name": "Enhanced Strength", "stub": "enhanced-strength", "text": "* This unit now has the following ability:\n\n* Endurance: Remove all exhaustion tokens from this unit at the end of each round.", "type": "Conjured Alteration Spell", "attack": "+1", "copies": 3, "release": {"name": "The Masters of Gravity", "stub": "the-masters-of-gravity"}, "placement": "Unit"}', '32', 'Conjured Alteration Spell', '0', '0', NULL, '3', 'f', 'Enhanced Strength
* This unit now has the following ability: * Endurance: Remove all exhaustion tokens from this unit at the end of each round.', '0', '10107', '1', NULL, NULL, 'f'),
('523', 'Gravity Training', 'gravity-training', '{"cost": ["[[main]]"], "dice": ["divine"], "name": "Gravity Training", "stub": "gravity-training", "text": "[[main]] or [[side]] - [[exhaust]] - 1 [[divine:class]] or 1 [[sympathy:class]]: Attach an [[Enhanced Strength]] conjured alteration spell to a target exhausted unit you control.", "type": "Ready Spell", "release": {"name": "The Masters of Gravity", "stub": "the-masters-of-gravity"}, "placement": "Spellboard", "conjurations": [{"name": "Enhanced Strength", "stub": "enhanced-strength"}]}', '32', 'Ready Spell', '5', '16', NULL, NULL, 'f', 'Gravity Training
main or side - exhaust - 1 divine:class or 1 sympathy:class: Attach an Enhanced Strength conjured alteration spell to a target exhausted unit you control.', '0', '10108', '1', NULL, NULL, 'f'),
('524', 'Law of Fear', 'law-of-fear', '{"cost": ["[[main]]", "1 [[divine:class]]"], "dice": ["divine"], "name": "Law of Fear", "stub": "law-of-fear", "text": "When this spell comes into play, you may place 1 exhaustion token on a target unit with an attack value of 0.\n\nWhile in battle, the attack value of all attacking units is reduced by 1.\n\n* Bound: This card cannot be discarded from your spellboard when you Meditate.\n\n* Fleeting: Discard this card at the end of this round.", "type": "Ready Spell", "release": {"name": "The Masters of Gravity", "stub": "the-masters-of-gravity"}, "magicCost": {"divine:class": 1}, "placement": "Spellboard"}', '32', 'Ready Spell', '106', '16', NULL, NULL, 'f', 'Law of Fear
When this spell comes into play, you may place 1 exhaustion token on a target unit with an attack value of 0. While in battle, the attack value of all attacking units is reduced by 1. * Bound: This card cannot be discarded from your spellboard when you Meditate. * Fleeting: Discard this card at the end of this round.', '0', '10109', '1', NULL, NULL, 'f'),
('525', 'Changing Winds', 'changing-winds', '{"cost": ["[[main]]", "1 [[sympathy:class]]", "1 [[basic]]"], "dice": ["sympathy"], "name": "Changing Winds", "stub": "changing-winds", "text": "When this spell comes into play, you may draw 2 cards. If you do, choose 2 cards in your hand and place each one on the top or bottom of your draw pile.\n\n[[side]] - [[exhaust]]: Draw 1 card. Change 1 die in your active pool to a side of your choice.", "type": "Ready Spell", "release": {"name": "The Masters of Gravity", "stub": "the-masters-of-gravity"}, "magicCost": {"basic": 1, "sympathy:class": 1}, "placement": "Spellboard"}', '32', 'Ready Spell', '206', '32', NULL, NULL, 'f', 'Changing Winds
When this spell comes into play, you may draw 2 cards. If you do, choose 2 cards in your hand and place each one on the top or bottom of your draw pile. side - exhaust: Draw 1 card. Change 1 die in your active pool to a side of your choice.', '0', '10110', '1', NULL, NULL, 'f'),
('526', 'Mirror Spirit', 'mirror-spirit', '{"life": 2, "name": "Mirror Spirit", "stub": "mirror-spirit", "text": "Reflect Sorrow: When this unit comes into play, place 1 status token on this unit for each exhaustion token on units a target player controls.\n\n* X = the number of status tokens on this unit.", "type": "Conjuration", "attack": "X", "copies": 3, "recover": 0, "release": {"name": "The Masters of Gravity", "stub": "the-masters-of-gravity"}, "placement": "Battlefield"}', '32', 'Conjuration', '0', '0', NULL, '3', 'f', 'Mirror Spirit
Reflect Sorrow: When this unit comes into play, place 1 status token on this unit for each exhaustion token on units a target player controls. * X = the number of status tokens on this unit.', '0', '10111', '1', NULL, NULL, 'f'),
('527', 'Summon Mirror Spirit', 'summon-mirror-spirit', '{"cost": ["[[main]]"], "dice": ["sympathy"], "name": "Summon Mirror Spirit", "stub": "summon-mirror-spirit", "text": "[[main]] - [[exhaust]] - 1 [[sympathy:class]] - 1 [[basic]]: Place a [[Mirror Spirit]] conjuration onto your battlefield.\n\nFocus 1: You may remove all status tokens from a Mirror Spirit you control. If you remove at least 1 status token, place 1 exhaustion token on a target unit.", "type": "Ready Spell", "release": {"name": "The Masters of Gravity", "stub": "the-masters-of-gravity"}, "placement": "Spellboard", "conjurations": [{"name": "Mirror Spirit", "stub": "mirror-spirit"}]}', '32', 'Ready Spell', '5', '32', NULL, NULL, 't', 'Summon Mirror Spirit
main - exhaust - 1 sympathy:class - 1 basic: Place a Mirror Spirit conjuration onto your battlefield. Focus 1: You may remove all status tokens from a Mirror Spirit you control. If you remove at least 1 status token, place 1 exhaustion token on a target unit.', '0', '10112', '1', NULL, NULL, 'f'),
('528', 'Sonic Swordsman', 'sonic-swordsman', '{"cost": ["[[main]]", "1 [[divine:power]]", "1 [[sympathy:class]]", "1 [[basic]]"], "dice": ["divine", "sympathy"], "life": 4, "name": "Sonic Swordsman", "stub": "sonic-swordsman", "text": "Sonic Pulse 1: After this unit destroys a unit an opponent controls by attacking, you may place 1 exhaustion token on a target unit.\n\nAlert: Do not place exhaustion tokens on this unit as a result of its countering.", "type": "Ally", "attack": 3, "recover": 2, "release": {"name": "The Masters of Gravity", "stub": "the-masters-of-gravity"}, "magicCost": {"basic": 1, "divine:power": 1, "sympathy:class": 1}, "placement": "Battlefield"}', '32', 'Ally', '308', '48', NULL, NULL, 'f', 'Sonic Swordsman
Sonic Pulse 1: After this unit destroys a unit an opponent controls by attacking, you may place 1 exhaustion token on a target unit. Alert: Do not place exhaustion tokens on this unit as a result of its countering.', '0', '10113', '1', NULL, NULL, 'f'),
('529', 'Light Swordsman', 'light-swordsman', '{"cost": ["[[side]]", "1 [[divine:power]]"], "dice": ["divine"], "life": 1, "name": "Light Swordsman", "stub": "light-swordsman", "text": "Quick Strike: While this unit is attacking, it deals its damage before units in battle with it.", "type": "Ally", "attack": 2, "recover": 1, "release": {"name": "The Masters of Gravity", "stub": "the-masters-of-gravity"}, "magicCost": {"divine:power": 1}, "placement": "Battlefield"}', '32', 'Ally', '106', '16', NULL, NULL, 'f', 'Light Swordsman
Quick Strike: While this unit is attacking, it deals its damage before units in battle with it.', '0', '10114', '1', NULL, NULL, 'f'),
('530', 'Polarity Mage', 'polarity-mage', '{"cost": ["[[main]]", ["1 [[sympathy:class]]", "1 [[divine:class]]"]], "dice": ["sympathy"], "life": 1, "name": "Polarity Mage", "stub": "polarity-mage", "text": "Give and Take: When this unit comes into play, you may search your discard pile for an alteration spell and place it into your hand, or discard a target alteration spell attached to a unit you control.", "type": "Ally", "attack": 1, "altDice": ["sympathy", "divine"], "recover": 1, "release": {"name": "The Masters of Gravity", "stub": "the-masters-of-gravity"}, "magicCost": {"sympathy:class / divine:class": 1}, "placement": "Battlefield"}', '32', 'Ally', '106', '0', NULL, NULL, 'f', 'Polarity Mage
Give and Take: When this unit comes into play, you may search your discard pile for an alteration spell and place it into your hand, or discard a target alteration spell attached to a unit you control.', '48', '10115', '1', NULL, NULL, 'f'),
('531', 'Holy Relics', 'holy-relics', '{"cost": ["[[main]]", "2 [[divine:class]]"], "dice": ["divine"], "life": "+2", "name": "Holy Relics", "stub": "holy-relics", "type": "Alteration Spell", "attack": "+2", "release": {"name": "The Masters of Gravity", "stub": "the-masters-of-gravity"}, "magicCost": {"divine:class": 2}, "placement": "Unit"}', '32', 'Alteration Spell', '207', '16', NULL, NULL, 'f', 'Holy Relics
', '0', '10116', '1', NULL, NULL, 'f'),
('532', 'Enlightenment', 'enlightenment', '{"cost": ["[[main]]", "1 [[divine:class]]", "1 [[basic]]"], "dice": ["divine"], "name": "Enlightenment", "stub": "enlightenment", "text": "Remove 1 exhaustion token from a target card.", "type": "Action Spell", "release": {"name": "The Masters of Gravity", "stub": "the-masters-of-gravity"}, "magicCost": {"basic": 1, "divine:class": 1}, "placement": "Discard"}', '32', 'Action Spell', '206', '16', NULL, NULL, 'f', 'Enlightenment
Remove 1 exhaustion token from a target card.', '0', '10117', '1', NULL, NULL, 'f'),
('533', 'Koji Wolfcub', 'koji-wolfcub', '{"life": 16, "name": "Koji Wolfcub", "stub": "koji-wolfcub", "text": "Accelerate Growth: [[side]] - [[exhaust]]: Place 1 status token on a target card.", "type": "Phoenixborn", "release": {"name": "The Boy Among Wolves", "stub": "the-boy-among-wolves"}, "spellboard": 3, "battlefield": 10}', '33', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Koji Wolfcub
Accelerate Growth: side - exhaust: Place 1 status token on a target card.', '0', '10118', '1', NULL, NULL, 'f'),
('534', 'Lick Wounds', 'lick-wounds', '{"cost": [["[[main]]", "[[side]]"], "2 [[basic]]"], "dice": ["basic"], "name": "Lick Wounds", "stub": "lick-wounds", "text": "Remove 2 wound tokens and 1 exhaustion token from a target unit or Phoenixborn.", "type": "Action Spell", "release": {"name": "The Boy Among Wolves", "stub": "the-boy-among-wolves"}, "magicCost": {"basic": 2}, "placement": "Discard", "phoenixborn": "Koji Wolfcub"}', '33', 'Action Spell', '205', '0', 'Koji Wolfcub', NULL, 'f', 'Lick Wounds
Remove 2 wound tokens and 1 exhaustion token from a target unit or Phoenixborn.', '0', '10119', '1', NULL, NULL, 'f'),
('535', 'Brilliant Thorn', 'brilliant-thorn', '{"life": 2, "name": "Brilliant Thorn", "stub": "brilliant-thorn", "text": "* Inheritance 1: When this unit is destroyed, you may place 1 status token on a target unit.\n\n* Fade: Destroy this unit at the end of this round.", "type": "Conjuration", "attack": 3, "copies": 6, "recover": 0, "release": {"name": "The Boy Among Wolves", "stub": "the-boy-among-wolves"}, "placement": "Battlefield"}', '33', 'Conjuration', '0', '0', NULL, '6', 'f', 'Brilliant Thorn
* Inheritance 1: When this unit is destroyed, you may place 1 status token on a target unit. * Fade: Destroy this unit at the end of this round.', '0', '10120', '1', NULL, NULL, 'f'),
('536', 'Luminous Seedling', 'luminous-seedling', '{"life": 2, "name": "Luminous Seedling", "stub": "luminous-seedling", "text": "Blossom: [[main]]: Remove 2 status tokens from this unit and destroy this unit. If you do, place up to 2 [[Brilliant Thorn]] conjurations onto your battlefield.\n\n* Growth: Add 1 to this unit''s life value for each status token on this unit.", "type": "Conjuration", "attack": 0, "copies": 3, "recover": 0, "release": {"name": "The Boy Among Wolves", "stub": "the-boy-among-wolves"}, "placement": "Battlefield", "conjurations": [{"name": "Brilliant Thorn", "stub": "brilliant-thorn"}]}', '33', 'Conjuration', '0', '0', NULL, '3', 'f', 'Luminous Seedling
Blossom: main: Remove 2 status tokens from this unit and destroy this unit. If you do, place up to 2 Brilliant Thorn conjurations onto your battlefield. * Growth: Add 1 to this unit''s life value for each status token on this unit.', '0', '10121', '1', NULL, NULL, 'f'),
('537', 'Indiglow Creeper', 'indiglow-creeper', '{"life": 1, "name": "Indiglow Creeper", "stub": "indiglow-creeper", "text": "* Germinate: When this unit is destroyed, place a [[Luminous Seedling]] conjuration onto your battlefield.\n\n* Fade: Destroy this unit at the end of this round.", "type": "Conjuration", "attack": 2, "copies": 3, "recover": 0, "release": {"name": "The Boy Among Wolves", "stub": "the-boy-among-wolves"}, "placement": "Battlefield", "conjurations": [{"name": "Luminous Seedling", "stub": "luminous-seedling"}, {"name": "Brilliant Thorn", "stub": "brilliant-thorn"}]}', '33', 'Conjuration', '0', '0', NULL, '3', 'f', 'Indiglow Creeper
* Germinate: When this unit is destroyed, place a Luminous Seedling conjuration onto your battlefield. * Fade: Destroy this unit at the end of this round.', '0', '10122', '1', NULL, NULL, 'f'),
('538', 'Summon Indiglow Creeper', 'summon-indiglow-creeper', '{"cost": ["[[main]]"], "dice": ["natural", "sympathy"], "name": "Summon Indiglow Creeper", "stub": "summon-indiglow-creeper", "text": "[[main]] - [[exhaust]] - 1 [[natural:class]] - 1 [[sympathy:class]]: Place an [[Indiglow Creeper]] conjuration onto your battlefield.\n\nFocus 1: You may place 1 status token on a target unit you control.", "type": "Ready Spell", "release": {"name": "The Boy Among Wolves", "stub": "the-boy-among-wolves"}, "placement": "Spellboard", "conjurations": [{"name": "Indiglow Creeper", "stub": "indiglow-creeper"}, {"name": "Luminous Seedling", "stub": "luminous-seedling"}, {"name": "Brilliant Thorn", "stub": "brilliant-thorn"}]}', '33', 'Ready Spell', '5', '40', NULL, NULL, 't', 'Summon Indiglow Creeper
main - exhaust - 1 natural:class - 1 sympathy:class: Place an Indiglow Creeper conjuration onto your battlefield. Focus 1: You may place 1 status token on a target unit you control.', '0', '10123', '1', NULL, NULL, 'f'),
('539', 'Biter', 'biter', '{"life": 2, "name": "Biter", "stub": "biter", "text": "Unit Guard: This unit may guard a unit that is being attacked.\n\nRooted: This unit cannot attack.", "type": "Conjuration", "attack": 3, "copies": 4, "recover": 0, "release": {"name": "The Boy Among Wolves", "stub": "the-boy-among-wolves"}, "placement": "Battlefield"}', '33', 'Conjuration', '0', '0', NULL, '4', 'f', 'Biter
Unit Guard: This unit may guard a unit that is being attacked. Rooted: This unit cannot attack.', '0', '10124', '1', NULL, NULL, 'f'),
('540', 'Summon Biter', 'summon-biter', '{"cost": ["[[main]]"], "dice": ["natural"], "name": "Summon Biter", "stub": "summon-biter", "text": "[[main]] - 1 [[natural:class]] - 1 [[basic]]: Place a [[Biter]] conjuration onto your battlefield.", "type": "Ready Spell", "release": {"name": "The Boy Among Wolves", "stub": "the-boy-among-wolves"}, "placement": "Spellboard", "conjurations": [{"name": "Biter", "stub": "biter"}]}', '33', 'Ready Spell', '5', '8', NULL, NULL, 't', 'Summon Biter
main - 1 natural:class - 1 basic: Place a Biter conjuration onto your battlefield.', '0', '10125', '1', NULL, NULL, 'f'),
('541', 'Join The Hunt', 'join-the-hunt', '{"cost": ["[[side]]", "1 [[sympathy:class]]"], "dice": ["sympathy"], "name": "Join The Hunt", "stub": "join-the-hunt", "text": "[[side]] - [[exhaust]]: Choose a target unit you control to gain the following ability for the remainder of the turn:\n\nGroup Tactics 2: After you declare three or more attackers, you may add 2 to this unit''s attack value for the remainder of the turn.", "type": "Ready Spell", "release": {"name": "The Boy Among Wolves", "stub": "the-boy-among-wolves"}, "magicCost": {"sympathy:class": 1}, "placement": "Spellboard"}', '33', 'Ready Spell', '105', '32', NULL, NULL, 'f', 'Join The Hunt
side - exhaust: Choose a target unit you control to gain the following ability for the remainder of the turn: Group Tactics 2: After you declare three or more attackers, you may add 2 to this unit''s attack value for the remainder of the turn.', '0', '10126', '1', NULL, NULL, 'f'),
('542', 'Panther Spirit', 'panther-spirit', '{"life": 1, "name": "Panther Spirit", "stub": "panther-spirit", "text": "* Fleeting: Discard this card at the end of this round.", "type": "Conjuration", "attack": 1, "copies": 3, "recover": 0, "release": {"name": "The Boy Among Wolves", "stub": "the-boy-among-wolves"}, "placement": "Battlefield"}', '33', 'Conjuration', '0', '0', NULL, '3', 'f', 'Panther Spirit
* Fleeting: Discard this card at the end of this round.', '0', '10127', '1', NULL, NULL, 'f'),
('543', 'Hunt Master', 'hunt-master', '{"cost": ["[[main]]", "1 [[natural:power]]", "1 [[sympathy:class]]", "1 [[basic]]"], "dice": ["natural", "sympathy"], "life": 3, "name": "Hunt Master", "stub": "hunt-master", "text": "Call the Hunt: When this unit comes into play, place 2 status tokens on this unit and place a [[Panther Spirit]] conjuration onto your battlefield.\n\nGuide: [[side]]: Remove 1 status token from this unit to add 1 to the attack value of another target unit you control for the remainder of the turn.", "type": "Ally", "attack": 2, "recover": 2, "release": {"name": "The Boy Among Wolves", "stub": "the-boy-among-wolves"}, "magicCost": {"basic": 1, "natural:power": 1, "sympathy:class": 1}, "placement": "Battlefield", "conjurations": [{"name": "Panther Spirit", "stub": "panther-spirit"}]}', '33', 'Ally', '308', '40', NULL, NULL, 'f', 'Hunt Master
Call the Hunt: When this unit comes into play, place 2 status tokens on this unit and place a Panther Spirit conjuration onto your battlefield. Guide: side: Remove 1 status token from this unit to add 1 to the attack value of another target unit you control for the remainder of the turn.', '0', '10128', '1', NULL, NULL, 'f'),
('544', 'Jungle Warrior', 'jungle-warrior', '{"cost": ["[[main]]", "1 [[sympathy:class]]", "1 [[basic]]"], "dice": ["sympathy"], "life": 2, "name": "Jungle Warrior", "stub": "jungle-warrior", "text": "* Last Orders 1: When this unit is destroyed, you may spend 1 [[basic]] to remove 1 exhaustion token from a target unit.\n\n* Inheritance 1: When this unit is destroyed, you may place 1 status token on a target unit.", "type": "Ally", "attack": 2, "recover": 1, "release": {"name": "The Boy Among Wolves", "stub": "the-boy-among-wolves"}, "magicCost": {"basic": 1, "sympathy:class": 1}, "placement": "Battlefield"}', '33', 'Ally', '206', '32', NULL, NULL, 'f', 'Jungle Warrior
* Last Orders 1: When this unit is destroyed, you may spend 1 basic to remove 1 exhaustion token from a target unit. * Inheritance 1: When this unit is destroyed, you may place 1 status token on a target unit.', '0', '10129', '1', NULL, NULL, 'f'),
('545', 'Sleeping Bear', 'sleeping-bear', '{"cost": ["[[main]]", "2 [[natural:class]]"], "dice": ["natural"], "life": 4, "name": "Sleeping Bear", "stub": "sleeping-bear", "text": "Slumbering 1: When this unit comes into play, place 1 exhaustion token on it.", "type": "Ally", "attack": 4, "recover": 2, "release": {"name": "The Boy Among Wolves", "stub": "the-boy-among-wolves"}, "magicCost": {"natural:class": 2}, "placement": "Battlefield"}', '33', 'Ally', '207', '8', NULL, NULL, 'f', 'Sleeping Bear
Slumbering 1: When this unit comes into play, place 1 exhaustion token on it.', '0', '10130', '1', NULL, NULL, 'f'),
('546', 'Temple Elder', 'temple-elder', '{"cost": ["[[main]]", "2 [[basic]]"], "dice": ["basic"], "life": 2, "name": "Temple Elder", "stub": "temple-elder", "text": "* Resourceful 1: When this unit comes into play, place 1 status token on this unit. At the beginning of the player turns phase, place 1 status token on this unit.\n\nWisdom 1: [[side]] - 1 [[sympathy:class]]: Remove 1 status token from this unit. If you do, draw 1 card.", "type": "Ally", "attack": 2, "recover": 1, "release": {"name": "The Boy Among Wolves", "stub": "the-boy-among-wolves"}, "magicCost": {"basic": 2}, "placement": "Battlefield"}', '33', 'Ally', '205', '0', NULL, NULL, 'f', 'Temple Elder
* Resourceful 1: When this unit comes into play, place 1 status token on this unit. At the beginning of the player turns phase, place 1 status token on this unit. Wisdom 1: side - 1 sympathy:class: Remove 1 status token from this unit. If you do, draw 1 card.', '0', '10131', '1', NULL, NULL, 'f'),
('547', 'Explosive Growth', 'explosive-growth', '{"cost": ["[[side]]", "1 [[sympathy:class]]", "1 [[natural:class]]"], "dice": ["sympathy", "natural"], "name": "Explosive Growth", "stub": "explosive-growth", "text": "When attaching this spell, place 2 status tokens on this unit. Discard all other copies of Explosive Growth attached to this unit.\n\nX = the number of status tokens on this unit.", "type": "Alteration Spell", "attack": "+X", "release": {"name": "The Boy Among Wolves", "stub": "the-boy-among-wolves"}, "magicCost": {"natural:class": 1, "sympathy:class": 1}, "placement": "Unit"}', '33', 'Alteration Spell', '206', '40', NULL, NULL, 'f', 'Explosive Growth
When attaching this spell, place 2 status tokens on this unit. Discard all other copies of Explosive Growth attached to this unit. X = the number of status tokens on this unit.', '0', '10132', '1', NULL, NULL, 'f'),
('548', 'Invigorate', 'invigorate', '{"cost": ["[[side]]", ["1 [[natural:class]]", "1 [[sympathy:class]]"]], "dice": ["natural"], "name": "Invigorate", "stub": "invigorate", "text": "Place 1 status token on up to 3 target units you control.", "type": "Action Spell", "altDice": ["sympathy", "natural"], "release": {"name": "The Boy Among Wolves", "stub": "the-boy-among-wolves"}, "magicCost": {"natural:class / sympathy:class": 1}, "placement": "Discard"}', '33', 'Action Spell', '105', '0', NULL, NULL, 'f', 'Invigorate
Place 1 status token on up to 3 target units you control.', '40', '10133', '1', NULL, NULL, 'f'),
('549', 'Astrea', 'astrea', '{"life": 19, "name": "Astrea", "stub": "astrea", "text": "Beguile: [[main]] - [[exhaust]] - 1 [[basic]]: Place 1 exhaustion token on a target unexhausted unit.", "type": "Phoenixborn", "release": {"name": "The Goddess of Ishra", "stub": "the-goddess-of-ishra"}, "spellboard": 4, "battlefield": 4}', '34', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Astrea
Beguile: main - exhaust - 1 basic: Place 1 exhaustion token on a target unexhausted unit.', '0', '10134', '1', NULL, NULL, 'f'),
('550', 'Mark Of The Goddess', 'mark-of-the-goddess', '{"cost": ["[[main]]", "1 [[basic]]"], "dice": ["basic"], "name": "Mark Of The Goddess", "stub": "mark-of-the-goddess", "text": "Choose a target unexhausted unit an opponent controls. Deal damage equal to the chosen unit''s attack value to another target unit that opponent controls. If the chosen unit is the only unexhausted unit that opponent controls, you may deal that damage to their target Phoenixborn instead.", "type": "Action Spell", "release": {"name": "The Goddess of Ishra", "stub": "the-goddess-of-ishra"}, "magicCost": {"basic": 1}, "placement": "Discard", "phoenixborn": "Astrea"}', '34', 'Action Spell', '105', '0', 'Astrea', NULL, 'f', 'Mark Of The Goddess
Choose a target unexhausted unit an opponent controls. Deal damage equal to the chosen unit''s attack value to another target unit that opponent controls. If the chosen unit is the only unexhausted unit that opponent controls, you may deal that damage to their target Phoenixborn instead.', '0', '10135', '1', NULL, NULL, 'f'),
('551', 'Light Bringer', 'light-bringer', '{"life": 1, "name": "Light Bringer", "stub": "light-bringer", "text": "Infatuate: When this unit comes into play, choose a target opponent. When choosing a main action during their next turn, that opponent must choose an Attack action if they control any units that can be declared as an attacker.", "type": "Conjuration", "attack": 1, "copies": 2, "recover": 0, "release": {"name": "The Goddess of Ishra", "stub": "the-goddess-of-ishra"}, "placement": "Battlefield"}', '34', 'Conjuration', '0', '0', NULL, '2', 'f', 'Light Bringer
Infatuate: When this unit comes into play, choose a target opponent. When choosing a main action during their next turn, that opponent must choose an Attack action if they control any units that can be declared as an attacker.', '0', '10136', '1', NULL, NULL, 'f'),
('552', 'Summon Light Bringer', 'summon-light-bringer', '{"cost": ["[[main]]"], "dice": ["divine"], "name": "Summon Light Bringer", "stub": "summon-light-bringer", "text": "[[main]] - [[exhaust]] - 1 [[divine:class]]: Place a [[Light Bringer]] conjuration onto your battlefield.", "type": "Ready Spell", "release": {"name": "The Goddess of Ishra", "stub": "the-goddess-of-ishra"}, "placement": "Spellboard", "conjurations": [{"name": "Light Bringer", "stub": "light-bringer"}]}', '34', 'Ready Spell', '5', '16', NULL, NULL, 't', 'Summon Light Bringer
main - exhaust - 1 divine:class: Place a Light Bringer conjuration onto your battlefield.', '0', '10137', '1', NULL, NULL, 'f'),
('553', 'Weeping Spirit', 'weeping-spirit', '{"life": 2, "name": "Weeping Spirit", "stub": "weeping-spirit", "text": "Fearful: This unit cannot block.\n\nQuell: [[side]] - 1 [[discard]]: Destroy this unit.", "type": "Conjuration", "attack": 0, "copies": 4, "recover": 0, "release": {"name": "The Goddess of Ishra", "stub": "the-goddess-of-ishra"}, "placement": "Battlefield"}', '34', 'Conjuration', '0', '0', NULL, '4', 'f', 'Weeping Spirit
Fearful: This unit cannot block. Quell: side - 1 discard: Destroy this unit.', '0', '10138', '1', NULL, NULL, 'f'),
('554', 'Summon Weeping Spirit', 'summon-weeping-spirit', '{"cost": ["[[main]]"], "dice": ["charm"], "name": "Summon Weeping Spirit", "stub": "summon-weeping-spirit", "text": "[[main]] - [[exhaust]] - 1 [[charm:class]]: Place a [[Weeping Spirit]] conjuration onto a target player''s battlefield.\n\nFocus 1: You may search a target discard pile for 1 card and remove it from the game.", "type": "Ready Spell", "release": {"name": "The Goddess of Ishra", "stub": "the-goddess-of-ishra"}, "placement": "Spellboard", "conjurations": [{"name": "Weeping Spirit", "stub": "weeping-spirit"}]}', '34', 'Ready Spell', '5', '2', NULL, NULL, 't', 'Summon Weeping Spirit
main - exhaust - 1 charm:class: Place a Weeping Spirit conjuration onto a target player''s battlefield. Focus 1: You may search a target discard pile for 1 card and remove it from the game.', '0', '10139', '1', NULL, NULL, 'f'),
('555', 'Steadfast Guardian', 'steadfast-guardian', '{"life": 3, "name": "Steadfast Guardian", "stub": "steadfast-guardian", "text": "Unit Guard: This unit may guard a unit that is being attacked.\n\nAlert: Do not place exhaustion tokens on this unit as a result of its countering.", "type": "Conjuration", "attack": 1, "copies": 1, "recover": 1, "release": {"name": "The Goddess of Ishra", "stub": "the-goddess-of-ishra"}, "placement": "Battlefield"}', '34', 'Conjuration', '0', '0', NULL, '1', 'f', 'Steadfast Guardian
Unit Guard: This unit may guard a unit that is being attacked. Alert: Do not place exhaustion tokens on this unit as a result of its countering.', '0', '10140', '1', NULL, NULL, 'f'),
('556', 'Summon Steadfast Guardian', 'summon-steadfast-guardian', '{"cost": ["[[main]]"], "dice": ["charm", "divine"], "name": "Summon Steadfast Guardian", "stub": "summon-steadfast-guardian", "text": "[[main]] - [[exhaust]] - 1 [[charm:class]] - 1 [[divine:class]]: Place a [[Steadfast Guardian]] conjuration onto your battlefield.\n\nFocus 1: You may remove all wound tokens and exhaustion tokens from a target Steadfast Guardian you control.", "type": "Ready Spell", "release": {"name": "The Goddess of Ishra", "stub": "the-goddess-of-ishra"}, "placement": "Spellboard", "conjurations": [{"name": "Steadfast Guardian", "stub": "steadfast-guardian"}]}', '34', 'Ready Spell', '5', '18', NULL, NULL, 't', 'Summon Steadfast Guardian
main - exhaust - 1 charm:class - 1 divine:class: Place a Steadfast Guardian conjuration onto your battlefield. Focus 1: You may remove all wound tokens and exhaustion tokens from a target Steadfast Guardian you control.', '0', '10141', '1', NULL, NULL, 'f'),
('557', 'Royal Charm', 'royal-charm', '{"cost": ["[[main]]"], "name": "Royal Charm", "stub": "royal-charm", "text": "After you pay a cost using a charm or divine die on its power side, you may place that die on this spell if it has no dice on it.\n\n[[side]] - [[exhaust]]: Choose a die on this spell and resolve its dice power without paying its cost.", "type": "Ready Spell", "release": {"name": "The Goddess of Ishra", "stub": "the-goddess-of-ishra"}, "placement": "Spellboard"}', '34', 'Ready Spell', '5', '0', NULL, NULL, 'f', 'Royal Charm
After you pay a cost using a charm or divine die on its power side, you may place that die on this spell if it has no dice on it. side - exhaust: Choose a die on this spell and resolve its dice power without paying its cost.', '0', '10142', '1', NULL, NULL, 'f'),
('558', 'Imperial Ninja', 'imperial-ninja', '{"cost": ["[[main]]", "2 [[charm:class]]"], "dice": ["charm"], "life": 2, "name": "Imperial Ninja", "stub": "imperial-ninja", "text": "Interrogate: When this unit is declared as an attacker, look at 1 random card in a target opponent''s hand. That target player may discard 2 cards off the top of their draw pile. If they discard fewer than 2 cards, they must discard the looked at card.", "type": "Ally", "attack": 2, "recover": 1, "release": {"name": "The Goddess of Ishra", "stub": "the-goddess-of-ishra"}, "magicCost": {"charm:class": 2}, "placement": "Battlefield"}', '34', 'Ally', '207', '2', NULL, NULL, 'f', 'Imperial Ninja
Interrogate: When this unit is declared as an attacker, look at 1 random card in a target opponent''s hand. That target player may discard 2 cards off the top of their draw pile. If they discard fewer than 2 cards, they must discard the looked at card.', '0', '10143', '1', NULL, NULL, 'f'),
('559', 'Sun Sister', 'sun-sister', '{"cost": ["[[main]]", "1 [[divine:class]]", "1 [[basic]]"], "dice": ["divine"], "life": 2, "name": "Sun Sister", "stub": "sun-sister", "text": "Care 1: [[side]]: Remove 1 wound token from another target unit you control.", "type": "Ally", "attack": 2, "recover": 1, "release": {"name": "The Goddess of Ishra", "stub": "the-goddess-of-ishra"}, "magicCost": {"basic": 1, "divine:class": 1}, "placement": "Battlefield"}', '34', 'Ally', '206', '16', NULL, NULL, 'f', 'Sun Sister
Care 1: side: Remove 1 wound token from another target unit you control.', '0', '10144', '1', NULL, NULL, 'f'),
('560', 'Kneel', 'kneel', '{"cost": ["[[main]]", "1 [[divine:class]]", "1 [[charm:class]]"], "dice": ["divine", "charm"], "name": "Kneel", "stub": "kneel", "text": "Place 1 exhaustion token on each unexhausted unit.", "type": "Action Spell", "release": {"name": "The Goddess of Ishra", "stub": "the-goddess-of-ishra"}, "magicCost": {"charm:class": 1, "divine:class": 1}, "placement": "Discard"}', '34', 'Action Spell', '207', '18', NULL, NULL, 'f', 'Kneel
Place 1 exhaustion token on each unexhausted unit.', '0', '10145', '1', NULL, NULL, 'f'),
('561', 'Devotion', 'devotion', '{"cost": ["[[side]]", "1 [[divine:class]]", "1 [[charm:class]]"], "dice": ["divine", "charm"], "life": "+1", "name": "Devotion", "stub": "devotion", "text": "This spell can only be attached to a unit you control. When attaching this spell, remove 1 exhaustion token from this unit.\n\nThis unit now has the following abilities:\n\nAlert: Do not place exhaustion tokens on this unit as a result of its countering.\n\nRooted: This unit cannot attack.", "type": "Alteration Spell", "recover": "+1", "release": {"name": "The Goddess of Ishra", "stub": "the-goddess-of-ishra"}, "magicCost": {"charm:class": 1, "divine:class": 1}, "placement": "Unit"}', '34', 'Alteration Spell', '206', '18', NULL, NULL, 'f', 'Devotion
This spell can only be attached to a unit you control. When attaching this spell, remove 1 exhaustion token from this unit. This unit now has the following abilities: Alert: Do not place exhaustion tokens on this unit as a result of its countering. Rooted: This unit cannot attack.', '0', '10146', '1', NULL, NULL, 'f'),
('562', 'Call To Action', 'call-to-action', '{"cost": ["1 [[charm:power]]"], "dice": ["charm"], "name": "Call To Action", "stub": "call-to-action", "text": "You may play this spell after an opponent declares attackers. Remove 1 exhaustion token from a target unit you control.", "type": "Reaction Spell", "release": {"name": "The Goddess of Ishra", "stub": "the-goddess-of-ishra"}, "magicCost": {"charm:power": 1}, "placement": "Discard"}', '34', 'Reaction Spell', '102', '2', NULL, NULL, 'f', 'Call To Action
You may play this spell after an opponent declares attackers. Remove 1 exhaustion token from a target unit you control.', '0', '10147', '1', NULL, NULL, 'f'),
('563', 'Hunter''s Mark', 'hunters-mark', '{"name": "Hunter''s Mark", "stub": "hunters-mark", "text": "When this unit receives damage, place twice the normal number of wound tokens on it.\n\nWhile this unit is the target of an attack, no guard may be declared.", "type": "Conjured Alteration Spell", "copies": 1, "release": {"name": "The Demons of Darmas", "stub": "the-demons-of-darmas"}, "placement": "Unit", "phoenixborn": "Harold Westraven"}', '35', 'Conjured Alteration Spell', '0', '0', 'Harold Westraven', '1', 'f', 'Hunter''s Mark
When this unit receives damage, place twice the normal number of wound tokens on it. While this unit is the target of an attack, no guard may be declared.', '0', '10148', '1', NULL, NULL, 'f'),
('564', 'Harold Westraven', 'harold-westraven', '{"life": 16, "name": "Harold Westraven", "stub": "harold-westraven", "text": "Mark Prey: [[side]] - [[exhaust]]: Attach a [[Hunter''s Mark]] conjured alteration spell to a target unit.", "type": "Phoenixborn", "release": {"name": "The Demons of Darmas", "stub": "the-demons-of-darmas"}, "spellboard": 3, "battlefield": 7, "conjurations": [{"name": "Hunter''s Mark", "stub": "hunters-mark"}]}', '35', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Harold Westraven
Mark Prey: side - exhaust: Attach a Hunter''s Mark conjured alteration spell to a target unit.', '0', '10149', '1', NULL, NULL, 'f'),
('565', 'Consume Soul', 'consume-soul', '{"cost": ["1 [[basic]]"], "dice": ["basic"], "name": "Consume Soul", "stub": "consume-soul", "text": "You may play this spell after a unit an opponent controls is destroyed as a result of an attack you control. Remove 2 wound tokens and 1 exhaustion token from your Phoenixborn.", "type": "Reaction Spell", "release": {"name": "The Demons of Darmas", "stub": "the-demons-of-darmas"}, "magicCost": {"basic": 1}, "placement": "Discard", "phoenixborn": "Harold Westraven"}', '35', 'Reaction Spell', '100', '0', 'Harold Westraven', NULL, 'f', 'Consume Soul
You may play this spell after a unit an opponent controls is destroyed as a result of an attack you control. Remove 2 wound tokens and 1 exhaustion token from your Phoenixborn.', '0', '10150', '1', NULL, NULL, 'f'),
('566', 'Vampire Bat Swarm', 'vampire-bat-swarm', '{"dice": ["ceremonial"], "life": 1, "name": "Vampire Bat Swarm", "stub": "vampire-bat-swarm", "text": "Group Tactics 1: After you declare three or more attackers, you may add 1 to this unit''s attack value for the remainder of the turn.\n\nSwarm: When this unit is destroyed, you may spend 1 [[ceremonial:class]] or 1 [[sympathy:class]] to place this unit onto your battlefield.", "type": "Conjuration", "attack": 2, "copies": 3, "recover": 0, "release": {"name": "The Demons of Darmas", "stub": "the-demons-of-darmas"}, "placement": "Battlefield"}', '35', 'Conjuration', '0', '1', NULL, '3', 'f', 'Vampire Bat Swarm
Group Tactics 1: After you declare three or more attackers, you may add 1 to this unit''s attack value for the remainder of the turn. Swarm: When this unit is destroyed, you may spend 1 ceremonial:class or 1 sympathy:class to place this unit onto your battlefield.', '0', '10151', '1', NULL, NULL, 'f'),
('567', 'Summon Vampire Bat Swarm', 'summon-vampire-bat-swarm', '{"cost": ["[[main]]"], "dice": ["ceremonial", "sympathy"], "name": "Summon Vampire Bat Swarm", "stub": "summon-vampire-bat-swarm", "text": "[[main]] - [[exhaust]] - 1 [[ceremonial:class]] - 1 [[sympathy:class]]: Place a [[Vampire Bat Swarm]] conjuration onto your battlefield.", "type": "Ready Spell", "release": {"name": "The Demons of Darmas", "stub": "the-demons-of-darmas"}, "placement": "Spellboard", "conjurations": [{"name": "Vampire Bat Swarm", "stub": "vampire-bat-swarm"}]}', '35', 'Ready Spell', '5', '33', NULL, NULL, 't', 'Summon Vampire Bat Swarm
main - exhaust - 1 ceremonial:class - 1 sympathy:class: Place a Vampire Bat Swarm conjuration onto your battlefield.', '0', '10152', '1', NULL, NULL, 'f'),
('568', 'Drain Vitality', 'drain-vitality', '{"cost": [["[[main]]", "[[side]]"], "1 [[basic]]"], "dice": ["ceremonial"], "name": "Drain Vitality", "stub": "drain-vitality", "text": "[[main]] - [[exhaust]] - 1 [[ceremonial:class]]: Deal 1 damage to a target unit. If you do, remove 1 wound token from a target unit.\n\n[[side]] - [[exhaust]] - 1 [[sympathy:class]]: Remove 1 status token from a target unit. If you do, place 1 status token on a target unit.", "type": "Ready Spell", "release": {"name": "The Demons of Darmas", "stub": "the-demons-of-darmas"}, "magicCost": {"basic": 1}, "placement": "Spellboard"}', '35', 'Ready Spell', '105', '1', NULL, NULL, 'f', 'Drain Vitality
main - exhaust - 1 ceremonial:class: Deal 1 damage to a target unit. If you do, remove 1 wound token from a target unit. side - exhaust - 1 sympathy:class: Remove 1 status token from a target unit. If you do, place 1 status token on a target unit.', '0', '10153', '1', NULL, NULL, 'f'),
('569', 'Beast Mage', 'beast-mage', '{"cost": ["[[main]]", "2 [[sympathy:class]]", "1 [[basic]]"], "dice": ["sympathy"], "life": 2, "name": "Beast Mage", "stub": "beast-mage", "text": "Terrifying 1: This unit cannot be blocked or guarded against by units with an attack value of 1 or less.\n\n* Transform 2: While you do not have the first player token, the attack value, life value, and recover value of this unit are increased by 2.", "type": "Ally", "attack": 2, "recover": 0, "release": {"name": "The Demons of Darmas", "stub": "the-demons-of-darmas"}, "magicCost": {"basic": 1, "sympathy:class": 2}, "placement": "Battlefield"}', '35', 'Ally', '307', '32', NULL, NULL, 'f', 'Beast Mage
Terrifying 1: This unit cannot be blocked or guarded against by units with an attack value of 1 or less. * Transform 2: While you do not have the first player token, the attack value, life value, and recover value of this unit are increased by 2.', '0', '10154', '1', NULL, NULL, 'f'),
('570', 'Master Vampire', 'master-vampire', '{"cost": ["[[main]]", "1 [[ceremonial:power]]", "1 [[sympathy:class]]", "1 [[basic]]"], "dice": ["ceremonial", "sympathy"], "life": 4, "name": "Master Vampire", "stub": "master-vampire", "text": "Stalk: This unit cannot be guarded against.\n\nLife Drain 1: After this unit destroys a unit an opponent controls by attacking, you may remove 1 wound token from your Phoenixborn.", "type": "Ally", "attack": 3, "recover": 2, "release": {"name": "The Demons of Darmas", "stub": "the-demons-of-darmas"}, "magicCost": {"basic": 1, "sympathy:class": 1, "ceremonial:power": 1}, "placement": "Battlefield"}', '35', 'Ally', '308', '33', NULL, NULL, 'f', 'Master Vampire
Stalk: This unit cannot be guarded against. Life Drain 1: After this unit destroys a unit an opponent controls by attacking, you may remove 1 wound token from your Phoenixborn.', '0', '10155', '1', NULL, NULL, 'f'),
('571', 'Beast Warrior', 'beast-warrior', '{"cost": ["[[main]]", "[[side]]", "1 [[sympathy:class]]"], "dice": ["sympathy"], "life": 1, "name": "Beast Warrior", "stub": "beast-warrior", "text": "Group Tactics 1: After you declare 3 or more attackers, you may add 1 to this unit''s attack value for the remainder of this turn.\n\n* Transform 1: While you do not have the first player token, the attack value, life value, and recover value of this unit are increased by 1", "type": "Ally", "attack": 1, "recover": 0, "release": {"name": "The Demons of Darmas", "stub": "the-demons-of-darmas"}, "magicCost": {"sympathy:class": 1}, "placement": "Battlefield"}', '35', 'Ally', '110', '32', NULL, NULL, 'f', 'Beast Warrior
Group Tactics 1: After you declare 3 or more attackers, you may add 1 to this unit''s attack value for the remainder of this turn. * Transform 1: While you do not have the first player token, the attack value, life value, and recover value of this unit are increased by 1', '0', '10156', '1', NULL, NULL, 'f'),
('572', 'Psychic Vampire', 'psychic-vampire', '{"cost": ["[[main]]", "1 [[ceremonial:power]]"], "dice": ["ceremonial"], "life": 1, "name": "Psychic Vampire", "stub": "psychic-vampire", "text": "Lobotomize 1: When this unit is destroyed as a result of a spell, attack, counter, ability, or dice power an opponent controls, that opponent must discard 1 card of their choice from their hand.", "type": "Ally", "attack": 2, "recover": 0, "release": {"name": "The Demons of Darmas", "stub": "the-demons-of-darmas"}, "magicCost": {"ceremonial:power": 1}, "placement": "Battlefield"}', '35', 'Ally', '107', '1', NULL, NULL, 'f', 'Psychic Vampire
Lobotomize 1: When this unit is destroyed as a result of a spell, attack, counter, ability, or dice power an opponent controls, that opponent must discard 1 card of their choice from their hand.', '0', '10157', '1', NULL, NULL, 'f'),
('573', 'Dark Reaping', 'dark-reaping', '{"cost": ["[[side]]", "1 [[ceremonial:class]]"], "dice": ["ceremonial"], "name": "Dark Reaping", "stub": "dark-reaping", "text": "Destroy a unit you control to change 5 dice in your active pool to a side of your choice.", "type": "Action Spell", "release": {"name": "The Demons of Darmas", "stub": "the-demons-of-darmas"}, "magicCost": {"ceremonial:class": 1}, "placement": "Discard"}', '35', 'Action Spell', '105', '1', NULL, NULL, 'f', 'Dark Reaping
Destroy a unit you control to change 5 dice in your active pool to a side of your choice.', '0', '10158', '1', NULL, NULL, 'f'),
('574', 'Transmute Magic', 'transmute-magic', '{"cost": ["[[side]]", "1 [[sympathy:class]]"], "dice": ["sympathy"], "name": "Transmute Magic", "stub": "transmute-magic", "text": "Swap any number of dice in your exhausted pool with an equal number of dice in your active pool, placing them each on a side of your choice. Change 1 die in each target player''s active pool to a side of your choice.", "type": "Action Spell", "release": {"name": "The Demons of Darmas", "stub": "the-demons-of-darmas"}, "magicCost": {"sympathy:class": 1}, "placement": "Discard"}', '35', 'Action Spell', '105', '32', NULL, NULL, 'f', 'Transmute Magic
Swap any number of dice in your exhausted pool with an equal number of dice in your active pool, placing them each on a side of your choice. Change 1 die in each target player''s active pool to a side of your choice.', '0', '10159', '1', NULL, NULL, 'f'),
('575', 'Adrenaline Rush', 'adrenaline-rush', '{"cost": ["[[side]]", ["1 [[ceremonial:power]]", "1 [[sympathy:power]]"], "1 [[basic]]"], "dice": ["ceremonial"], "name": "Adrenaline Rush", "stub": "adrenaline-rush", "text": "Deal 1 damage to a target unit you control. Remove 1 exhaustion token from that unit.", "type": "Action Spell", "altDice": ["ceremonial", "sympathy"], "release": {"name": "The Demons of Darmas", "stub": "the-demons-of-darmas"}, "magicCost": {"basic": 1, "ceremonial:power / sympathy:power": 1}, "placement": "Discard"}', '35', 'Action Spell', '206', '0', NULL, NULL, 'f', 'Adrenaline Rush
Deal 1 damage to a target unit you control. Remove 1 exhaustion token from that unit.', '33', '10160', '1', NULL, NULL, 'f'),
('576', 'Sembali Grimtongue', 'sembali-grimtongue', '{"life": 19, "name": "Sembali Grimtongue", "stub": "sembali-grimtongue", "text": "Gift of Wings: [[side]] - [[exhaust]] - 2 [[basic]]: Remove all exhaustion tokens from a target ally you control. It cannot be guarded against for the remainder of the turn.", "type": "Phoenixborn", "release": {"name": "The Spirits of Memoria", "stub": "the-spirits-of-memoria"}, "spellboard": 4, "battlefield": 5}', '36', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Sembali Grimtongue
Gift of Wings: side - exhaust - 2 basic: Remove all exhaustion tokens from a target ally you control. It cannot be guarded against for the remainder of the turn.', '0', '10161', '1', NULL, NULL, 'f'),
('577', 'Purify', 'purify', '{"cost": ["[[main]]", "1 [[basic]]"], "dice": ["basic"], "name": "Purify", "stub": "purify", "text": "Choose a target ally you control and place it into your hand. If you do, destroy a target conjuration an opponent controls.", "type": "Action Spell", "release": {"name": "The Spirits of Memoria", "stub": "the-spirits-of-memoria"}, "magicCost": {"basic": 1}, "placement": "Discard", "phoenixborn": "Sembali Grimtongue"}', '36', 'Action Spell', '105', '0', 'Sembali Grimtongue', NULL, 'f', 'Purify
Choose a target ally you control and place it into your hand. If you do, destroy a target conjuration an opponent controls.', '0', '10162', '1', NULL, NULL, 'f'),
('578', 'Admonisher', 'admonisher', '{"life": 2, "name": "Admonisher", "stub": "admonisher", "text": "Rebuke 1: At the end of each round, deal 1 damage to a target Phoenixborn.", "type": "Conjuration", "attack": 0, "copies": 3, "recover": 0, "release": {"name": "The Spirits of Memoria", "stub": "the-spirits-of-memoria"}, "placement": "Battlefield"}', '36', 'Conjuration', '0', '0', NULL, '3', 'f', 'Admonisher
Rebuke 1: At the end of each round, deal 1 damage to a target Phoenixborn.', '0', '10163', '1', NULL, NULL, 'f'),
('579', 'Summon Admonisher', 'summon-admonisher', '{"cost": ["[[main]]"], "dice": ["divine"], "name": "Summon Admonisher", "stub": "summon-admonisher", "text": "[[main]] - [[exhaust]] - 1 [[divine:class]]: Place an [[Admonisher]] conjuration onto your battlefield.\n\nFocus 1: If you cannot, deal 1 damage to a target Phoenixborn.", "type": "Ready Spell", "release": {"name": "The Spirits of Memoria", "stub": "the-spirits-of-memoria"}, "placement": "Spellboard", "conjurations": [{"name": "Admonisher", "stub": "admonisher"}]}', '36', 'Ready Spell', '5', '16', NULL, NULL, 't', 'Summon Admonisher
main - exhaust - 1 divine:class: Place an Admonisher conjuration onto your battlefield. Focus 1: If you cannot, deal 1 damage to a target Phoenixborn.', '0', '10164', '1', NULL, NULL, 'f'),
('580', 'Law Of Grace', 'law-of-grace', '{"cost": ["[[main]]", "1 [[divine:class]]"], "dice": ["divine"], "name": "Law Of Grace", "stub": "law-of-grace", "text": "When this spell comes into play, remove 1 wound token from your Phoenixborn.\n\nAfter any Phoenixborn is dealt damage by a spell or ability, prevent 1 damage from being received.\n\n* Bound: This card cannot be discarded from your spellboard when you Meditate.\n\n* Fleeting: Discard this card at the end of this round.", "type": "Ready Spell", "release": {"name": "The Spirits of Memoria", "stub": "the-spirits-of-memoria"}, "magicCost": {"divine:class": 1}, "placement": "Spellboard"}', '36', 'Ready Spell', '106', '16', NULL, NULL, 'f', 'Law Of Grace
When this spell comes into play, remove 1 wound token from your Phoenixborn. After any Phoenixborn is dealt damage by a spell or ability, prevent 1 damage from being received. * Bound: This card cannot be discarded from your spellboard when you Meditate. * Fleeting: Discard this card at the end of this round.', '0', '10165', '1', NULL, NULL, 'f'),
('581', 'Gates Thrown Open', 'gates-thrown-open', '{"cost": ["[[side]]", "1 [[illusion:class]]"], "dice": ["illusion"], "name": "Gates Thrown Open", "stub": "gates-thrown-open", "text": "Remove 1 exhaustion token from 1 ready spell in each of your spellboard slots.", "type": "Action Spell", "release": {"name": "The Spirits of Memoria", "stub": "the-spirits-of-memoria"}, "magicCost": {"illusion:class": 1}, "placement": "Discard"}', '36', 'Action Spell', '105', '4', NULL, NULL, 'f', 'Gates Thrown Open
Remove 1 exhaustion token from 1 ready spell in each of your spellboard slots.', '0', '10166', '1', NULL, NULL, 'f'),
('582', 'Chained Creations', 'chained-creations', '{"cost": ["[[main]]", "1 [[divine:class]]", "1 [[basic]]"], "dice": ["divine"], "name": "Chained Creations", "stub": "chained-creations", "text": "Deal 2 damage to a target conjuration an opponent controls. If that destroys the conjuration, after it is destroyed, place 1 exhaustion token on a ready spell that target opponent controls that has a printed effect that can place that conjuration onto the battlefield.", "type": "Action Spell", "release": {"name": "The Spirits of Memoria", "stub": "the-spirits-of-memoria"}, "magicCost": {"basic": 1, "divine:class": 1}, "placement": "Discard"}', '36', 'Action Spell', '206', '16', NULL, NULL, 'f', 'Chained Creations
Deal 2 damage to a target conjuration an opponent controls. If that destroys the conjuration, after it is destroyed, place 1 exhaustion token on a ready spell that target opponent controls that has a printed effect that can place that conjuration onto the battlefield.', '0', '10167', '1', NULL, NULL, 'f'),
('583', 'Shepherd Of Lost Souls', 'shepherd-of-lost-souls', '{"cost": ["[[main]]", "[[side]]", "1 [[divine:class]]"], "dice": ["divine"], "life": 1, "name": "Shepherd Of Lost Souls", "stub": "shepherd-of-lost-souls", "text": "Spirit Guide: When this unit comes into play, you may search your discard pile for an ally with a title other than this unit''s title and place it into your hand.", "type": "Ally", "attack": 1, "recover": 0, "release": {"name": "The Spirits of Memoria", "stub": "the-spirits-of-memoria"}, "magicCost": {"divine:class": 1}, "placement": "Battlefield"}', '36', 'Ally', '110', '16', NULL, NULL, 'f', 'Shepherd Of Lost Souls
Spirit Guide: When this unit comes into play, you may search your discard pile for an ally with a title other than this unit''s title and place it into your hand.', '0', '10168', '1', NULL, NULL, 'f'),
('584', 'Celestial Knight', 'celestial-knight', '{"cost": ["[[main]]", "1 [[illusion:power]]", "1 [[divine:class]]", "1 [[basic]]"], "dice": ["illusion", "divine"], "life": 3, "name": "Celestial Knight", "stub": "celestial-knight", "text": "* Armored 1: After this unit is dealt damage, prevent 1 damage from being received.", "type": "Ally", "attack": 3, "recover": 2, "release": {"name": "The Spirits of Memoria", "stub": "the-spirits-of-memoria"}, "magicCost": {"basic": 1, "divine:class": 1, "illusion:power": 1}, "placement": "Battlefield"}', '36', 'Ally', '308', '20', NULL, NULL, 'f', 'Celestial Knight
* Armored 1: After this unit is dealt damage, prevent 1 damage from being received.', '0', '10169', '1', NULL, NULL, 'f'),
('585', 'Shadow Guard', 'shadow-guard', '{"cost": ["[[main]]", "2 [[illusion:class]]"], "dice": ["illusion"], "life": 1, "name": "Shadow Guard", "stub": "shadow-guard", "text": "~ Hidden: After an opponent has declared attackers, you may play this unit from your hand without paying its main action cost.\n\nUnit Guard: This unit may guard a unit that is being attacked.", "type": "Ally", "attack": 3, "recover": 1, "release": {"name": "The Spirits of Memoria", "stub": "the-spirits-of-memoria"}, "magicCost": {"illusion:class": 2}, "placement": "Battlefield"}', '36', 'Ally', '207', '4', NULL, NULL, 'f', 'Shadow Guard
~ Hidden: After an opponent has declared attackers, you may play this unit from your hand without paying its main action cost. Unit Guard: This unit may guard a unit that is being attacked.', '0', '10170', '1', NULL, NULL, 'f'),
('586', 'Spectral Assassin', 'spectral-assassin', '{"life": 1, "name": "Spectral Assassin", "stub": "spectral-assassin", "text": "Sneaky Strike: When this unit is declared as an attacker, opponents may not play reaction spells for the remainder of the turn.", "type": "Conjuration", "attack": 2, "copies": 1, "recover": 0, "release": {"name": "The Spirits of Memoria", "stub": "the-spirits-of-memoria"}, "placement": "Battlefield"}', '36', 'Conjuration', '0', '0', NULL, '1', 'f', 'Spectral Assassin
Sneaky Strike: When this unit is declared as an attacker, opponents may not play reaction spells for the remainder of the turn.', '0', '10171', '1', NULL, NULL, 'f'),
('587', 'Summon Spectral Assassin', 'summon-spectral-assassin', '{"cost": ["[[side]]", "1 [[illusion:class]]", "1 [[basic]]"], "dice": ["illusion"], "name": "Summon Spectral Assassin", "stub": "summon-spectral-assassin", "text": "Choose a target ally you control and place it into its owner''s hand. If you do, place a [[Spectral Assassin]] conjuration onto your battlefield. You may draw 1 card.", "type": "Action Spell", "release": {"name": "The Spirits of Memoria", "stub": "the-spirits-of-memoria"}, "magicCost": {"basic": 1, "illusion:class": 1}, "placement": "Discard", "conjurations": [{"name": "Spectral Assassin", "stub": "spectral-assassin"}]}', '36', 'Action Spell', '205', '4', NULL, NULL, 't', 'Summon Spectral Assassin
Choose a target ally you control and place it into its owner''s hand. If you do, place a Spectral Assassin conjuration onto your battlefield. You may draw 1 card.', '0', '10172', '1', NULL, NULL, 'f'),
('588', 'Angelic Rescue', 'angelic-rescue', '{"cost": ["1 [[divine:power]]"], "dice": ["divine"], "name": "Angelic Rescue", "stub": "angelic-rescue", "text": "You may play this spell after a unit you control is dealt damage by a spell, ability, or dice power an opponent controls. Prevent that damage from being received, and then remove all wound tokens from that unit.", "type": "Reaction Spell", "release": {"name": "The Spirits of Memoria", "stub": "the-spirits-of-memoria"}, "magicCost": {"divine:power": 1}, "placement": "Discard"}', '36', 'Reaction Spell', '102', '16', NULL, NULL, 'f', 'Angelic Rescue
You may play this spell after a unit you control is dealt damage by a spell, ability, or dice power an opponent controls. Prevent that damage from being received, and then remove all wound tokens from that unit.', '0', '10173', '1', NULL, NULL, 'f'),
('589', 'Xander Heartsblood', 'xander-heartsblood', '{"life": 20, "name": "Xander Heartsblood", "stub": "xander-heartsblood", "text": "Reincarnate: [[side]] - [[exhaust]] - 1 [[divine:class]]: Search your discard pile for an ally and place it into your hand.", "type": "Phoenixborn", "release": {"name": "The King of Titans", "stub": "the-king-of-titans"}, "spellboard": 3, "battlefield": 6}', '37', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Xander Heartsblood
Reincarnate: side - exhaust - 1 divine:class: Search your discard pile for an ally and place it into your hand.', '0', '10174', '1', NULL, NULL, 'f'),
('590', 'Earthquake', 'earthquake', '{"cost": ["[[main]]", "2 [[basic]]"], "dice": ["basic"], "name": "Earthquake", "stub": "earthquake", "text": "Deal 4 damage to a target unit and 1 damage to each other unit.", "type": "Action Spell", "release": {"name": "The King of Titans", "stub": "the-king-of-titans"}, "magicCost": {"basic": 2}, "placement": "Discard", "phoenixborn": "Xander Heartsblood"}', '37', 'Action Spell', '205', '0', 'Xander Heartsblood', NULL, 'f', 'Earthquake
Deal 4 damage to a target unit and 1 damage to each other unit.', '0', '10175', '1', NULL, NULL, 'f'),
('591', 'Cerasaurus Mount', 'cerasaurus-mount', '{"life": 3, "name": "Cerasaurus Mount", "stub": "cerasaurus-mount", "text": "Overkill 1: After this unit destroys a unit an opponent controls by attacking, deal 1 damage to that opponent''s target Phoenixborn.\n\n* Dismount: When this unit is destroyed, take any allies currently underneath this unit from your discard pile and place them into your hand.", "type": "Conjuration", "attack": 3, "copies": 2, "recover": 0, "release": {"name": "The King of Titans", "stub": "the-king-of-titans"}, "placement": "Battlefield"}', '37', 'Conjuration', '0', '0', NULL, '2', 'f', 'Cerasaurus Mount
Overkill 1: After this unit destroys a unit an opponent controls by attacking, deal 1 damage to that opponent''s target Phoenixborn. * Dismount: When this unit is destroyed, take any allies currently underneath this unit from your discard pile and place them into your hand.', '0', '10176', '1', NULL, NULL, 'f'),
('592', 'Summon Cerasaurus Mount', 'summon-cerasaurus-mount', '{"cost": ["[[main]]", "1 [[basic]]"], "dice": ["basic"], "name": "Summon Cerasaurus Mount", "stub": "summon-cerasaurus-mount", "text": "[[side]] - 1 [[natural:class]] - 1 [[divine:class]]: Remove an unexhausted ally you control from play. If you do, place a [[Cerasaurus Mount]] conjuration onto your battlefield and place that ally face down under that unit.", "type": "Ready Spell", "release": {"name": "The King of Titans", "stub": "the-king-of-titans"}, "magicCost": {"basic": 1}, "placement": "Spellboard", "conjurations": [{"name": "Cerasaurus Mount", "stub": "cerasaurus-mount"}]}', '37', 'Ready Spell', '105', '0', NULL, NULL, 't', 'Summon Cerasaurus Mount
side - 1 natural:class - 1 divine:class: Remove an unexhausted ally you control from play. If you do, place a Cerasaurus Mount conjuration onto your battlefield and place that ally face down under that unit.', '0', '10177', '1', NULL, NULL, 'f'),
('593', 'Law Of Domination', 'law-of-domination', '{"cost": ["[[main]]", "1 [[divine:class]]"], "dice": ["divine"], "name": "Law Of Domination", "stub": "law-of-domination", "text": "When this spell comes into play, choose an opponent to choose a unit they control. Then, choose a unit you control. Those units deal damage to each other equal to their attack value.\n\nThis damage, and damage from attacking or countering, cannot be prevented.\n\n* Bound: This card cannot be discarded from your spellboard when you Meditate.\n\n* Fleeting: Discard this card at the end of this round.", "type": "Ready Spell", "release": {"name": "The King of Titans", "stub": "the-king-of-titans"}, "magicCost": {"divine:class": 1}, "placement": "Spellboard"}', '37', 'Ready Spell', '106', '16', NULL, NULL, 'f', 'Law Of Domination
When this spell comes into play, choose an opponent to choose a unit they control. Then, choose a unit you control. Those units deal damage to each other equal to their attack value. This damage, and damage from attacking or countering, cannot be prevented. * Bound: This card cannot be discarded from your spellboard when you Meditate. * Fleeting: Discard this card at the end of this round.', '0', '10178', '1', NULL, NULL, 'f'),
('594', 'Sacred Ground', 'sacred-ground', '{"cost": ["[[main]]", "1 [[divine:class]]"], "dice": ["divine"], "name": "Sacred Ground", "stub": "sacred-ground", "text": "[[side]] - [[exhaust]]: All units you currently control gain the following ability until the start of your next turn:\n\n* Armored 1: After this unit is dealt damage, prevent 1 damage from being received.", "type": "Ready Spell", "release": {"name": "The King of Titans", "stub": "the-king-of-titans"}, "magicCost": {"divine:class": 1}, "placement": "Spellboard"}', '37', 'Ready Spell', '106', '16', NULL, NULL, 'f', 'Sacred Ground
side - exhaust: All units you currently control gain the following ability until the start of your next turn: * Armored 1: After this unit is dealt damage, prevent 1 damage from being received.', '0', '10179', '1', NULL, NULL, 'f'),
('595', 'Raptor Hatchling', 'raptor-hatchling', '{"life": 1, "name": "Raptor Hatchling", "stub": "raptor-hatchling", "text": "Group Tactics 2: After you declare 3 or more attackers, you may add 2 to this unit''s attack value for the remainder of this turn.", "type": "Conjuration", "attack": 0, "copies": 3, "recover": 0, "release": {"name": "The King of Titans", "stub": "the-king-of-titans"}, "placement": "Battlefield"}', '37', 'Conjuration', '0', '0', NULL, '3', 'f', 'Raptor Hatchling
Group Tactics 2: After you declare 3 or more attackers, you may add 2 to this unit''s attack value for the remainder of this turn.', '0', '10180', '1', NULL, NULL, 'f'),
('596', 'Raptor Herder', 'raptor-herder', '{"cost": ["[[main]]", ["1 [[natural:class]]", "1 [[sympathy:class]]"]], "dice": ["natural"], "life": 1, "name": "Raptor Herder", "stub": "raptor-herder", "text": "Call Raptor Hatchling: When this unit comes into play, place a [[Raptor Hatchling]] conjuration onto your battlefield.", "type": "Ally", "attack": 1, "altDice": ["sympathy", "natural"], "recover": 1, "release": {"name": "The King of Titans", "stub": "the-king-of-titans"}, "magicCost": {"natural:class / sympathy:class": 1}, "placement": "Battlefield", "conjurations": [{"name": "Raptor Hatchling", "stub": "raptor-hatchling"}]}', '37', 'Ally', '106', '0', NULL, NULL, 'f', 'Raptor Herder
Call Raptor Hatchling: When this unit comes into play, place a Raptor Hatchling conjuration onto your battlefield.', '40', '10181', '1', NULL, NULL, 'f'),
('597', 'Pain Shaman', 'pain-shaman', '{"cost": ["[[main]]", "2 [[natural:class]]"], "dice": ["natural"], "life": 3, "name": "Pain Shaman", "stub": "pain-shaman", "text": "Exchange Pain 1: When this unit comes into play, you may deal 1 damage to a target unit, and then remove 1 wound token from a target unit or Phoenixborn.", "type": "Ally", "attack": 1, "recover": 1, "release": {"name": "The King of Titans", "stub": "the-king-of-titans"}, "magicCost": {"natural:class": 2}, "placement": "Battlefield"}', '37', 'Ally', '207', '8', NULL, NULL, 'f', 'Pain Shaman
Exchange Pain 1: When this unit comes into play, you may deal 1 damage to a target unit, and then remove 1 wound token from a target unit or Phoenixborn.', '0', '10182', '1', NULL, NULL, 'f'),
('598', 'Archasaurus Mount', 'archasaurus-mount', '{"life": 5, "name": "Archasaurus Mount", "stub": "archasaurus-mount", "text": "Gigantic 2: This unit cannot be blocked or guarded against by units with a life value of 2 or less.\n\n* Dismount: When this unit is destroyed, place any allies you own underneath this unit into your hand.", "type": "Conjuration", "attack": 4, "copies": 1, "recover": 0, "release": {"name": "The King of Titans", "stub": "the-king-of-titans"}, "placement": "Battlefield"}', '37', 'Conjuration', '0', '0', NULL, '1', 'f', 'Archasaurus Mount
Gigantic 2: This unit cannot be blocked or guarded against by units with a life value of 2 or less. * Dismount: When this unit is destroyed, place any allies you own underneath this unit into your hand.', '0', '10183', '1', NULL, NULL, 'f'),
('599', 'Summon Archasaurus Mount', 'summon-archasaurus-mount', '{"cost": ["[[main]]", "[[side]]", "1 [[divine:class]]", "1 [[natural:class]]", "1 [[basic]]"], "dice": ["divine", "natural"], "name": "Summon Archasaurus Mount", "stub": "summon-archasaurus-mount", "text": "Remove an unexhausted ally you control from play. If you do, place an [[Archasaurus Mount]] conjuration onto your battlefield and place that ally face down under that unit.", "type": "Action Spell", "release": {"name": "The King of Titans", "stub": "the-king-of-titans"}, "magicCost": {"basic": 1, "divine:class": 1, "natural:class": 1}, "placement": "Discard", "conjurations": [{"name": "Archasaurus Mount", "stub": "archasaurus-mount"}]}', '37', 'Action Spell', '311', '24', NULL, NULL, 't', 'Summon Archasaurus Mount
Remove an unexhausted ally you control from play. If you do, place an Archasaurus Mount conjuration onto your battlefield and place that ally face down under that unit.', '0', '10184', '1', NULL, NULL, 'f'),
('600', 'Shining Hydra Head', 'shining-hydra-head', '{"name": "Shining Hydra Head", "stub": "shining-hydra-head", "text": "This unit now has the following ability:\n\nTerrifying 1: This unit cannot be blocked or guarded against by units with an attack value of 1 or less.", "type": "Conjured Alteration Spell", "attack": "+1", "copies": 3, "recover": "+1", "release": {"name": "The King of Titans", "stub": "the-king-of-titans"}, "placement": "Unit"}', '37', 'Conjured Alteration Spell', '0', '0', NULL, '3', 'f', 'Shining Hydra Head
This unit now has the following ability: Terrifying 1: This unit cannot be blocked or guarded against by units with an attack value of 1 or less.', '0', '10185', '1', NULL, NULL, 'f'),
('601', 'Shining Hydra', 'shining-hydra', '{"life": 4, "name": "Shining Hydra", "stub": "shining-hydra", "text": "Regenerate Heads: [[side]]: Remove 1 wound token from this unit to attach a [[Shining Hydra Head]] conjured alteration spell to this unit.", "type": "Conjuration", "attack": 1, "copies": 1, "recover": 0, "release": {"name": "The King of Titans", "stub": "the-king-of-titans"}, "placement": "Battlefield", "conjurations": [{"name": "Shining Hydra Head", "stub": "shining-hydra-head"}]}', '37', 'Conjuration', '0', '0', NULL, '1', 'f', 'Shining Hydra
Regenerate Heads: side: Remove 1 wound token from this unit to attach a Shining Hydra Head conjured alteration spell to this unit.', '0', '10186', '1', NULL, NULL, 'f'),
('602', 'Summon Shining Hydra', 'summon-shining-hydra', '{"cost": ["[[main]]", "1 [[divine:class]]", "1 [[natural:class]]", "1 [[basic]]"], "dice": ["divine", "natural"], "name": "Summon Shining Hydra", "stub": "summon-shining-hydra", "text": "Place a [[Shining Hydra]] conjuration onto your battlefield.", "type": "Action Spell", "release": {"name": "The King of Titans", "stub": "the-king-of-titans"}, "magicCost": {"basic": 1, "divine:class": 1, "natural:class": 1}, "placement": "Discard", "conjurations": [{"name": "Shining Hydra", "stub": "shining-hydra"}]}', '37', 'Action Spell', '307', '24', NULL, NULL, 't', 'Summon Shining Hydra
Place a Shining Hydra conjuration onto your battlefield.', '0', '10187', '1', NULL, NULL, 'f'),
('603', 'Nature''s Wrath', 'natures-wrath', '{"cost": ["[[main]]", "1 [[natural:class]]"], "dice": ["natural"], "name": "Nature''s Wrath", "stub": "natures-wrath", "text": "Deal 1 damage to all units.", "type": "Action Spell", "release": {"name": "The King of Titans", "stub": "the-king-of-titans"}, "magicCost": {"natural:class": 1}, "placement": "Discard"}', '37', 'Action Spell', '106', '8', NULL, NULL, 'f', 'Nature''s Wrath
Deal 1 damage to all units.', '0', '10188', '1', NULL, NULL, 'f'),
('604', 'Mass Heal', 'mass-heal', '{"cost": ["[[side]]"], "name": "Mass Heal", "stub": "mass-heal", "text": "Remove 1 wound token from all units. If you have a divine die on its class or power side in your active pool, you may instead remove 1 wound token from your Phoenixborn and all units you control.", "type": "Action Spell", "release": {"name": "The King of Titans", "stub": "the-king-of-titans"}, "placement": "Discard"}', '37', 'Action Spell', '4', '0', NULL, NULL, 'f', 'Mass Heal
Remove 1 wound token from all units. If you have a divine die on its class or power side in your active pool, you may instead remove 1 wound token from your Phoenixborn and all units you control.', '0', '10189', '1', NULL, NULL, 'f'),
('605', 'Rimea Careworn', 'rimea-careworn', '{"life": 20, "name": "Rimea Careworn", "stub": "rimea-careworn", "text": "Visions: [[side]]: Look at the top 3 cards of a target draw pile. You may spend 1 [[basic]] and place 1 exhaustion token on this card to place 1 of those cards on the bottom of that draw pile. Place the remaining looked at cards on the top of that draw pile in the order of your choice.", "type": "Phoenixborn", "release": {"name": "The Ghost Guardian", "stub": "the-ghost-guardian"}, "spellboard": 5, "battlefield": 4}', '38', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Rimea Careworn
Visions: side: Look at the top 3 cards of a target draw pile. You may spend 1 basic and place 1 exhaustion token on this card to place 1 of those cards on the bottom of that draw pile. Place the remaining looked at cards on the top of that draw pile in the order of your choice.', '0', '10190', '1', NULL, NULL, 'f'),
('606', 'Ancestor Spirit', 'ancestor-spirit', '{"life": 1, "name": "Ancestor Spirit", "stub": "ancestor-spirit", "text": "Guidance: When this unit comes into play, you may draw 1 card. If you do, place 1 card from your hand on the bottom of your draw pile.", "type": "Conjuration", "attack": 2, "copies": 2, "recover": 0, "release": {"name": "The Ghost Guardian", "stub": "the-ghost-guardian"}, "placement": "Battlefield"}', '38', 'Conjuration', '0', '0', NULL, '2', 'f', 'Ancestor Spirit
Guidance: When this unit comes into play, you may draw 1 card. If you do, place 1 card from your hand on the bottom of your draw pile.', '0', '10191', '1', NULL, NULL, 'f'),
('607', 'Ancestral Army', 'ancestral-army', '{"cost": ["[[main]]", "3 [[basic]]"], "dice": ["basic"], "life": 2, "name": "Ancestral Army", "stub": "ancestral-army", "text": "Invoke Ancestors: When this unit comes into play, place 2 [[Ancestor Spirit]] conjurations onto your battlefield.", "type": "Ally", "attack": 1, "recover": 0, "release": {"name": "The Ghost Guardian", "stub": "the-ghost-guardian"}, "magicCost": {"basic": 3}, "placement": "Battlefield", "phoenixborn": "Rimea Careworn", "conjurations": [{"name": "Ancestor Spirit", "stub": "ancestor-spirit"}]}', '38', 'Ally', '305', '0', 'Rimea Careworn', NULL, 'f', 'Ancestral Army
Invoke Ancestors: When this unit comes into play, place 2 Ancestor Spirit conjurations onto your battlefield.', '0', '10192', '1', NULL, NULL, 'f'),
('608', 'Summon Ancestor Spirit', 'summon-ancestor-spirit', '{"cost": ["[[main]]"], "dice": ["sympathy"], "name": "Summon Ancestor Spirit", "stub": "summon-ancestor-spirit", "text": "[[main]] - [[exhaust]] - 1 [[sympathy:power]]: Place an [[Ancestor Spirit]] conjuration onto your battlefield.", "type": "Ready Spell", "release": {"name": "The Ghost Guardian", "stub": "the-ghost-guardian"}, "placement": "Spellboard", "conjurations": [{"name": "Ancestor Spirit", "stub": "ancestor-spirit"}]}', '38', 'Ready Spell', '5', '32', NULL, NULL, 't', 'Summon Ancestor Spirit
main - exhaust - 1 sympathy:power: Place an Ancestor Spirit conjuration onto your battlefield.', '0', '10193', '1', NULL, NULL, 'f'),
('609', 'Pale Steed Mount', 'pale-steed-mount', '{"life": 4, "name": "Pale Steed Mount", "stub": "pale-steed-mount", "text": "Unit Guard: This unit may guard a unit that is being attacked.\n\n* Dismount: When this unit is destroyed, place any allies you own underneath this unit into your hand.", "type": "Conjuration", "attack": 2, "copies": 1, "recover": 0, "release": {"name": "The Ghost Guardian", "stub": "the-ghost-guardian"}, "placement": "Battlefield"}', '38', 'Conjuration', '0', '0', NULL, '1', 'f', 'Pale Steed Mount
Unit Guard: This unit may guard a unit that is being attacked. * Dismount: When this unit is destroyed, place any allies you own underneath this unit into your hand.', '0', '10194', '1', NULL, NULL, 'f'),
('610', 'Spectral Charger Mount', 'spectral-charger-mount', '{"life": 2, "name": "Spectral Charger Mount", "stub": "spectral-charger-mount", "text": "Quick Strike: While this unit is attacking, it deals its damage before units in battle with it.\n\n* Dismount: When this unit is destroyed, place any allies you own underneath this unit into your hand.", "type": "Conjuration", "attack": 4, "copies": 1, "recover": 0, "release": {"name": "The Ghost Guardian", "stub": "the-ghost-guardian"}, "placement": "Battlefield"}', '38', 'Conjuration', '0', '0', NULL, '1', 'f', 'Spectral Charger Mount
Quick Strike: While this unit is attacking, it deals its damage before units in battle with it. * Dismount: When this unit is destroyed, place any allies you own underneath this unit into your hand.', '0', '10195', '1', NULL, NULL, 'f'),
('611', 'Nightmare Mount', 'nightmare-mount', '{"life": 4, "name": "Nightmare Mount", "stub": "nightmare-mount", "text": "Terrifying 1: This unit cannot be blocked or guarded against by units with an attack value of 1 or less.\n\n* Dismount: When this unit is destroyed, place any allies you own underneath this unit into your hand.", "type": "Conjuration", "attack": 4, "copies": 1, "recover": 0, "release": {"name": "The Ghost Guardian", "stub": "the-ghost-guardian"}, "placement": "Battlefield"}', '38', 'Conjuration', '0', '0', NULL, '1', 'f', 'Nightmare Mount
Terrifying 1: This unit cannot be blocked or guarded against by units with an attack value of 1 or less. * Dismount: When this unit is destroyed, place any allies you own underneath this unit into your hand.', '0', '10196', '1', NULL, NULL, 'f'),
('612', 'Summon Ghostly Mount', 'summon-ghostly-mount', '{"cost": ["[[main]]", "1 [[basic]]"], "dice": ["illusion", "sympathy"], "name": "Summon Ghostly Mount", "stub": "summon-ghostly-mount", "text": "[[main]] or [[side]] - 1 [[illusion:class]] - 1 [[sympathy:class]]: Remove an unexhausted ally you control from play. If you do, place a [[Pale Steed Mount]] or [[Spectral Charger Mount]] conjuration onto your battlefield and place that ally face down under that unit.\n\nFocus 2: You may place a [[Nightmare Mount]] conjuration instead.", "type": "Ready Spell", "release": {"name": "The Ghost Guardian", "stub": "the-ghost-guardian"}, "magicCost": {"basic": 1}, "placement": "Spellboard", "conjurations": [{"name": "Spectral Charger Mount", "stub": "spectral-charger-mount"}, {"name": "Nightmare Mount", "stub": "nightmare-mount"}, {"name": "Pale Steed Mount", "stub": "pale-steed-mount"}]}', '38', 'Ready Spell', '105', '36', NULL, NULL, 't', 'Summon Ghostly Mount
main or side - 1 illusion:class - 1 sympathy:class: Remove an unexhausted ally you control from play. If you do, place a Pale Steed Mount or Spectral Charger Mount conjuration onto your battlefield and place that ally face down under that unit. Focus 2: You may place a Nightmare Mount conjuration instead.', '0', '10197', '1', NULL, NULL, 'f'),
('613', 'Augury', 'augury', '{"cost": ["[[main]]", "1 [[sympathy:class]]", "1 [[basic]]"], "dice": ["sympathy"], "name": "Augury", "stub": "augury", "text": "When this spell comes into play, place 3 status tokens on it.\n\n[[side]] - [[exhaust]]: Search your draw pile. You may reveal 1 card with a magic play cost of X and place it into your hand. If you do, remove 1 status token from this spell. Shuffle your draw pile.\n\nX = the number of status tokens on this spell.", "type": "Ready Spell", "release": {"name": "The Ghost Guardian", "stub": "the-ghost-guardian"}, "magicCost": {"basic": 1, "sympathy:class": 1}, "placement": "Spellboard"}', '38', 'Ready Spell', '206', '32', NULL, NULL, 'f', 'Augury
When this spell comes into play, place 3 status tokens on it. side - exhaust: Search your draw pile. You may reveal 1 card with a magic play cost of X and place it into your hand. If you do, remove 1 status token from this spell. Shuffle your draw pile. X = the number of status tokens on this spell.', '0', '10198', '1', NULL, NULL, 'f'),
('614', 'Memorialize', 'memorialize', '{"cost": ["[[side]]", "1 [[sympathy:class]]"], "dice": ["sympathy"], "name": "Memorialize", "stub": "memorialize", "text": "After an ally you control is destroyed, place 1 status token on this spell if it has no status tokens on it.\n\n[[side]] - [[exhaust]]: Remove 1 status token from this spell to search your discard pile for a spell and place that spell on the bottom of your draw pile.", "type": "Ready Spell", "release": {"name": "The Ghost Guardian", "stub": "the-ghost-guardian"}, "magicCost": {"sympathy:class": 1}, "placement": "Spellboard"}', '38', 'Ready Spell', '105', '32', NULL, NULL, 'f', 'Memorialize
After an ally you control is destroyed, place 1 status token on this spell if it has no status tokens on it. side - exhaust: Remove 1 status token from this spell to search your discard pile for a spell and place that spell on the bottom of your draw pile.', '0', '10199', '1', NULL, NULL, 'f'),
('615', 'Dark Presence', 'dark-presence', '{"cost": ["[[main]]", "1 [[illusion:class]]"], "dice": ["illusion"], "name": "Dark Presence", "stub": "dark-presence", "text": "[[side]] - [[exhaust]]: Choose a target unit you control to gain the following ability for the remainder of the turn:\n\nTerrifying 1: This unit cannot be blocked or guarded against by units with an attack value of 1 or less.\n\nFocus 1: Then, reduce the attack value of a target unit an opponent controls by 1 for the remainder of the turn.", "type": "Ready Spell", "release": {"name": "The Ghost Guardian", "stub": "the-ghost-guardian"}, "magicCost": {"illusion:class": 1}, "placement": "Spellboard"}', '38', 'Ready Spell', '106', '4', NULL, NULL, 'f', 'Dark Presence
side - exhaust: Choose a target unit you control to gain the following ability for the remainder of the turn: Terrifying 1: This unit cannot be blocked or guarded against by units with an attack value of 1 or less. Focus 1: Then, reduce the attack value of a target unit an opponent controls by 1 for the remainder of the turn.', '0', '10200', '1', NULL, NULL, 'f'),
('616', 'Resonance', 'resonance', '{"cost": ["[[side]]", "2 [[sympathy:class]]", "1 [[basic]]"], "dice": ["sympathy"], "name": "Resonance", "stub": "resonance", "text": "When this spell comes into play, select 2 dice in your exhausted pool and place them into your active pool on a side of your choice.\n\nWhen you play this spell, place it face up under a ready spell on your spellboard. While this card is on your spellboard, all other cards in its spellboard slot are focused one additional time.", "type": "Ready Spell", "release": {"name": "The Ghost Guardian", "stub": "the-ghost-guardian"}, "magicCost": {"basic": 1, "sympathy:class": 2}, "placement": "Spellboard"}', '38', 'Ready Spell', '306', '32', NULL, NULL, 'f', 'Resonance
When this spell comes into play, select 2 dice in your exhausted pool and place them into your active pool on a side of your choice. When you play this spell, place it face up under a ready spell on your spellboard. While this card is on your spellboard, all other cards in its spellboard slot are focused one additional time.', '0', '10201', '1', NULL, NULL, 'f'),
('617', 'Hollow', 'hollow', '{"cost": ["[[main]]", ["1 [[illusion:power]]", "1 [[sympathy:power]]"]], "dice": ["illusion"], "life": 1, "name": "Hollow", "stub": "hollow", "text": "Hex 2: When this unit comes into play, you may lower 2 dice in a target opponent''s active pool one level.", "type": "Ally", "attack": 2, "altDice": ["illusion", "sympathy"], "recover": 1, "release": {"name": "The Ghost Guardian", "stub": "the-ghost-guardian"}, "magicCost": {"illusion:power / sympathy:power": 1}, "placement": "Battlefield"}', '38', 'Ally', '107', '0', NULL, NULL, 'f', 'Hollow
Hex 2: When this unit comes into play, you may lower 2 dice in a target opponent''s active pool one level.', '36', '10202', '1', NULL, NULL, 'f'),
('618', 'Battle Seer', 'battle-seer', '{"cost": ["[[main]]", "1 [[illusion:power]]", "1 [[sympathy:class]]", "1 [[basic]]"], "dice": ["illusion", "sympathy"], "life": 4, "name": "Battle Seer", "stub": "battle-seer", "text": "Quick Strike: While this unit is attacking, it deals its damage before units in battle with it.\n\nAlert: Do not place exhaustion tokens on this unit as a result of its countering.", "type": "Ally", "attack": 3, "recover": 2, "release": {"name": "The Ghost Guardian", "stub": "the-ghost-guardian"}, "magicCost": {"basic": 1, "illusion:power": 1, "sympathy:class": 1}, "placement": "Battlefield"}', '38', 'Ally', '308', '36', NULL, NULL, 'f', 'Battle Seer
Quick Strike: While this unit is attacking, it deals its damage before units in battle with it. Alert: Do not place exhaustion tokens on this unit as a result of its countering.', '0', '10203', '1', NULL, NULL, 'f'),
('619', 'Shared Sorrow', 'shared-sorrow', '{"cost": ["[[main]]", "1 [[sympathy:class]]", "1 [[basic]]"], "dice": ["sympathy"], "name": "Shared Sorrow", "stub": "shared-sorrow", "text": "Discard 1 card from your hand with a magic play cost of 1 or more. Search your discard pile for another card with a magic play cost of X and place it into your hand. Deal X damage to a target unit.\n\nX = the magic play cost of the discarded card.", "type": "Action Spell", "release": {"name": "The Ghost Guardian", "stub": "the-ghost-guardian"}, "magicCost": {"basic": 1, "sympathy:class": 1}, "placement": "Discard"}', '38', 'Action Spell', '206', '32', NULL, NULL, 'f', 'Shared Sorrow
Discard 1 card from your hand with a magic play cost of 1 or more. Search your discard pile for another card with a magic play cost of X and place it into your hand. Deal X damage to a target unit. X = the magic play cost of the discarded card.', '0', '10204', '1', NULL, NULL, 'f'),
('620', 'James Endersight', 'james-endersight', '{"life": 19, "name": "James Endersight", "stub": "james-endersight", "text": "Convene With Souls: [[side]] - [[exhaust]]: Search your draw pile for an ally, reveal it, and place it into your hand. Place a number of wound tokens equal to that ally''s life value on this card. Shuffle your draw pile.", "type": "Phoenixborn", "release": {"name": "The Grave King", "stub": "the-grave-king"}, "spellboard": 3, "battlefield": 7}', '39', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'James Endersight
Convene With Souls: side - exhaust: Search your draw pile for an ally, reveal it, and place it into your hand. Place a number of wound tokens equal to that ally''s life value on this card. Shuffle your draw pile.', '0', '10205', '1', NULL, NULL, 'f'),
('621', 'Vengeance', 'vengeance', '{"cost": ["[[side]]", "X [[basic]]"], "name": "Vengeance", "stub": "vengeance", "text": "Destroy X units you control. If you do, add 1 to the attack value of X target units you control for the remainder of the turn.", "type": "Action Spell", "release": {"name": "The Grave King", "stub": "the-grave-king"}, "placement": "Discard", "phoenixborn": "James Endersight"}', '39', 'Action Spell', '4', '0', 'James Endersight', NULL, 'f', 'Vengeance
Destroy X units you control. If you do, add 1 to the attack value of X target units you control for the remainder of the turn.', '0', '10206', '1', NULL, NULL, 'f'),
('622', 'Fallen', 'fallen', '{"life": 1, "name": "Fallen", "stub": "fallen", "text": "Infectious: Damage dealt by this unit by attacking or countering cannot be prevented.", "type": "Conjuration", "attack": 1, "copies": 7, "recover": 1, "release": {"name": "The Grave King", "stub": "the-grave-king"}, "placement": "Battlefield"}', '39', 'Conjuration', '0', '0', NULL, '7', 'f', 'Fallen
Infectious: Damage dealt by this unit by attacking or countering cannot be prevented.', '0', '10207', '1', NULL, NULL, 'f'),
('623', 'Summon Fallen', 'summon-fallen', '{"cost": ["[[main]]"], "dice": ["ceremonial"], "name": "Summon Fallen", "stub": "summon-fallen", "text": "After an ally you control is destroyed, place 1 status token on this spell.\n\n[[main]] - 1 [[ceremonial:class]]: Remove up to 1 status token from each copy of Summon Fallen you control. Place 1 [[Fallen]] conjuration onto your battlefield for each status token removed.", "type": "Ready Spell", "release": {"name": "The Grave King", "stub": "the-grave-king"}, "placement": "Spellboard", "conjurations": [{"name": "Fallen", "stub": "fallen"}]}', '39', 'Ready Spell', '5', '1', NULL, NULL, 't', 'Summon Fallen
After an ally you control is destroyed, place 1 status token on this spell. main - 1 ceremonial:class: Remove up to 1 status token from each copy of Summon Fallen you control. Place 1 Fallen conjuration onto your battlefield for each status token removed.', '0', '10208', '1', NULL, NULL, 'f'),
('624', 'Chant Of Sacrifice', 'chant-of-sacrifice', '{"cost": ["[[main]]", "1 [[ceremonial:class]]"], "dice": ["ceremonial"], "name": "Chant Of Sacrifice", "stub": "chant-of-sacrifice", "text": "[[side]] - [[exhaust]]: Destroy a unit you control.", "type": "Ready Spell", "release": {"name": "The Grave King", "stub": "the-grave-king"}, "magicCost": {"ceremonial:class": 1}, "placement": "Spellboard"}', '39', 'Ready Spell', '106', '1', NULL, NULL, 'f', 'Chant Of Sacrifice
side - exhaust: Destroy a unit you control.', '0', '10209', '1', NULL, NULL, 'f'),
('625', 'Revival Pact', 'revival-pact', '{"cost": ["[[side]]", "1 [[divine:class]]"], "dice": ["divine"], "name": "Revival Pact", "stub": "revival-pact", "text": "Search your discard pile for up to 3 allies and shuffle them into your draw pile.", "type": "Action Spell", "release": {"name": "The Grave King", "stub": "the-grave-king"}, "magicCost": {"divine:class": 1}, "placement": "Discard"}', '39', 'Action Spell', '105', '16', NULL, NULL, 'f', 'Revival Pact
Search your discard pile for up to 3 allies and shuffle them into your draw pile.', '0', '10210', '1', NULL, NULL, 'f'),
('626', 'Grave Knight', 'grave-knight', '{"cost": ["[[main]]", "1 [[ceremonial:power]]", "1 [[divine:class]]", "1 [[basic]]"], "dice": ["ceremonial", "divine"], "life": 3, "name": "Grave Knight", "stub": "grave-knight", "text": "Threatening: This unit must be blocked, if able.\n\nOverkill 1: After this unit destroys a unit an opponent controls by attacking, deal 1 damage to that opponent''s target Phoenixborn.", "type": "Ally", "attack": 4, "recover": 2, "release": {"name": "The Grave King", "stub": "the-grave-king"}, "magicCost": {"basic": 1, "divine:class": 1, "ceremonial:power": 1}, "placement": "Battlefield"}', '39', 'Ally', '308', '17', NULL, NULL, 'f', 'Grave Knight
Threatening: This unit must be blocked, if able. Overkill 1: After this unit destroys a unit an opponent controls by attacking, deal 1 damage to that opponent''s target Phoenixborn.', '0', '10211', '1', NULL, NULL, 'f'),
('627', 'Rising Horde', 'rising-horde', '{"cost": ["[[main]]", "2 [[ceremonial:class]]"], "dice": ["ceremonial"], "life": 1, "name": "Rising Horde", "stub": "rising-horde", "text": "* Raise Fallen: When this unit is destroyed, place 2 [[Fallen]] conjurations onto your battlefield.", "type": "Ally", "attack": 1, "recover": 1, "release": {"name": "The Grave King", "stub": "the-grave-king"}, "magicCost": {"ceremonial:class": 2}, "placement": "Battlefield", "conjurations": [{"name": "Fallen", "stub": "fallen"}]}', '39', 'Ally', '207', '1', NULL, NULL, 'f', 'Rising Horde
* Raise Fallen: When this unit is destroyed, place 2 Fallen conjurations onto your battlefield.', '0', '10212', '1', NULL, NULL, 'f'),
('628', 'Immortal Commander', 'immortal-commander', '{"cost": ["[[side]]", "1 [[divine:power]]"], "dice": ["divine"], "life": 3, "name": "Immortal Commander", "stub": "immortal-commander", "text": "Command 1: [[side]] - [[exhaust]]: Add 1 to the attack value of all other units you currently control for the remainder of the turn.", "type": "Ally", "attack": 0, "recover": 1, "release": {"name": "The Grave King", "stub": "the-grave-king"}, "magicCost": {"divine:power": 1}, "placement": "Battlefield"}', '39', 'Ally', '106', '16', NULL, NULL, 'f', 'Immortal Commander
Command 1: side - exhaust: Add 1 to the attack value of all other units you currently control for the remainder of the turn.', '0', '10213', '1', NULL, NULL, 'f'),
('629', 'Reaping Angel', 'reaping-angel', '{"cost": ["[[main]]", "1 [[ceremonial:class]]", "1 [[divine:class]]"], "dice": ["ceremonial", "divine"], "life": 2, "name": "Reaping Angel", "stub": "reaping-angel", "text": "Offer: When this unit comes into play, search your draw pile. You may reveal an ally and place it into your discard pile. Shuffle your draw pile. Then, you may search your discard pile for an ally and remove it from the game to remove 1 wound token from a target Phoenixborn.", "type": "Ally", "attack": 2, "recover": 2, "release": {"name": "The Grave King", "stub": "the-grave-king"}, "magicCost": {"divine:class": 1, "ceremonial:class": 1}, "placement": "Battlefield"}', '39', 'Ally', '207', '17', NULL, NULL, 'f', 'Reaping Angel
Offer: When this unit comes into play, search your draw pile. You may reveal an ally and place it into your discard pile. Shuffle your draw pile. Then, you may search your discard pile for an ally and remove it from the game to remove 1 wound token from a target Phoenixborn.', '0', '10214', '1', NULL, NULL, 'f'),
('630', 'Reclaim Soul', 'reclaim-soul', '{"cost": ["[[main]]", "1 [[ceremonial:class]]"], "dice": ["ceremonial"], "name": "Reclaim Soul", "stub": "reclaim-soul", "text": "Destroy a unit you control to remove 2 wound tokens from your Phoenixborn.", "type": "Action Spell", "release": {"name": "The Grave King", "stub": "the-grave-king"}, "magicCost": {"ceremonial:class": 1}, "placement": "Discard"}', '39', 'Action Spell', '106', '1', NULL, NULL, 'f', 'Reclaim Soul
Destroy a unit you control to remove 2 wound tokens from your Phoenixborn.', '0', '10215', '1', NULL, NULL, 'f'),
('631', 'Rally The Troops', 'rally-the-troops', '{"cost": ["[[side]]", "1 [[divine:class]]"], "dice": ["divine"], "name": "Rally The Troops", "stub": "rally-the-troops", "text": "Choose X allies you control with 1 or more exhaustion tokens on them and place them into their owner''s hand. Remove X wound tokens from your Phoenixborn.", "type": "Action Spell", "release": {"name": "The Grave King", "stub": "the-grave-king"}, "magicCost": {"divine:class": 1}, "placement": "Discard"}', '39', 'Action Spell', '105', '16', NULL, NULL, 'f', 'Rally The Troops
Choose X allies you control with 1 or more exhaustion tokens on them and place them into their owner''s hand. Remove X wound tokens from your Phoenixborn.', '0', '10216', '1', NULL, NULL, 'f'),
('632', 'Fiona Mercywind', 'fiona-mercywind', '{"life": 15, "name": "Fiona Mercywind", "stub": "fiona-mercywind", "text": "Ingenuity: [[side]] - [[exhaust]] - 1 [[discard]]: Draw 1 card or remove 1 exhaustion token from a ready spell you control.", "type": "Phoenixborn", "release": {"name": "The Protector of Argaia", "stub": "the-protector-of-argaia"}, "spellboard": 5, "battlefield": 6}', '40', 'Phoenixborn', '0', '0', NULL, NULL, 'f', 'Fiona Mercywind
Ingenuity: side - exhaust - 1 discard: Draw 1 card or remove 1 exhaustion token from a ready spell you control.', '0', '10217', '1', NULL, NULL, 'f'),
('633', 'Mind Maze', 'mind-maze', '{"cost": ["[[main]]", "1 [[basic]]"], "dice": ["basic"], "name": "Mind Maze", "stub": "mind-maze", "text": "* This unit cannot attack, block, or guard.\n\n* Escape: [[main]] - [[side]] - 1 [[basic]] - 1 [[discard]]: Discard this card.\n\n* Lost: Discard this unit at the end of the round.", "type": "Alteration Spell", "release": {"name": "The Protector of Argaia", "stub": "the-protector-of-argaia"}, "magicCost": {"basic": 1}, "placement": "Unit", "phoenixborn": "Fiona Mercywind"}', '40', 'Alteration Spell', '105', '0', 'Fiona Mercywind', NULL, 'f', 'Mind Maze
* This unit cannot attack, block, or guard. * Escape: main - side - 1 basic - 1 discard: Discard this card. * Lost: Discard this unit at the end of the round.', '0', '10218', '1', NULL, NULL, 'f'),
('634', 'Majestic Titan', 'majestic-titan', '{"life": 4, "name": "Majestic Titan", "stub": "majestic-titan", "text": "Gigantic 1: This unit cannot be blocked or guarded against by units with a life value of 1 or less.\n\n* Renew: [[main]] - 1 [[basic]]: Discard a copy of Summon Majestic Titan from your spellboard to remove all exhaustion tokens and discard all alteration spells from this unit.", "type": "Conjuration", "attack": 3, "copies": 1, "recover": 0, "release": {"name": "The Protector of Argaia", "stub": "the-protector-of-argaia"}, "placement": "Battlefield"}', '40', 'Conjuration', '0', '0', NULL, '1', 'f', 'Majestic Titan
Gigantic 1: This unit cannot be blocked or guarded against by units with a life value of 1 or less. * Renew: main - 1 basic: Discard a copy of Summon Majestic Titan from your spellboard to remove all exhaustion tokens and discard all alteration spells from this unit.', '0', '10219', '1', NULL, NULL, 'f'),
('635', 'Summon Majestic Titan', 'summon-majestic-titan', '{"cost": ["[[main]]", "1 [[basic]]"], "dice": ["charm", "sympathy"], "name": "Summon Majestic Titan", "stub": "summon-majestic-titan", "text": "[[main]] - [[exhaust]] - 1 [[charm:class]] - 1 [[sympathy:class]] - 1 [[basic]]: Place a [[Majestic Titan]] conjuration onto your battlefield.", "type": "Ready Spell", "release": {"name": "The Protector of Argaia", "stub": "the-protector-of-argaia"}, "magicCost": {"basic": 1}, "placement": "Spellboard", "conjurations": [{"name": "Majestic Titan", "stub": "majestic-titan"}]}', '40', 'Ready Spell', '105', '34', NULL, NULL, 't', 'Summon Majestic Titan
main - exhaust - 1 charm:class - 1 sympathy:class - 1 basic: Place a Majestic Titan conjuration onto your battlefield.', '0', '10220', '1', NULL, NULL, 'f'),
('636', 'Nightsong Cricket', 'nightsong-cricket', '{"life": 1, "name": "Nightsong Cricket", "stub": "nightsong-cricket", "text": "Polyphony: When this unit is destroyed, change 1 die in a target player''s active pool to a side of your choice.\n\nRenewed Harmony: When this unit is destroyed, you and a target opponent each choose a card in the other''s discard pile. Place the chosen cards into their owner''s hand.", "type": "Conjuration", "attack": 2, "copies": 4, "recover": 0, "release": {"name": "The Protector of Argaia", "stub": "the-protector-of-argaia"}, "placement": "Battlefield"}', '40', 'Conjuration', '0', '0', NULL, '4', 'f', 'Nightsong Cricket
Polyphony: When this unit is destroyed, change 1 die in a target player''s active pool to a side of your choice. Renewed Harmony: When this unit is destroyed, you and a target opponent each choose a card in the other''s discard pile. Place the chosen cards into their owner''s hand.', '0', '10221', '1', NULL, NULL, 'f'),
('637', 'Summon Nightsong Cricket', 'summon-nightsong-cricket', '{"cost": ["[[main]]"], "dice": ["sympathy"], "name": "Summon Nightsong Cricket", "stub": "summon-nightsong-cricket", "text": "[[main]] - [[exhaust]] - 1 [[sympathy:class]] - 1 [[basic]]: Place a [[Nightsong Cricket]] conjuration onto your battlefield.\n\nFocus 1: If you spent any[[sympathy:power]] to activate this spell, you may search a target player''s discard pile for 1 card and remove it from the game.", "type": "Ready Spell", "release": {"name": "The Protector of Argaia", "stub": "the-protector-of-argaia"}, "placement": "Spellboard", "conjurations": [{"name": "Nightsong Cricket", "stub": "nightsong-cricket"}]}', '40', 'Ready Spell', '5', '32', NULL, NULL, 't', 'Summon Nightsong Cricket
main - exhaust - 1 sympathy:class - 1 basic: Place a Nightsong Cricket conjuration onto your battlefield. Focus 1: If you spent anysympathy:power to activate this spell, you may search a target player''s discard pile for 1 card and remove it from the game.', '0', '10222', '1', NULL, NULL, 'f'),
('638', 'Mind Fog Owl', 'mind-fog-owl', '{"life": 2, "name": "Mind Fog Owl", "stub": "mind-fog-owl", "text": "Unseen: This unit cannot be blocked unless all attacking units without the Unseen ability have been blocked.", "type": "Conjuration", "attack": 2, "copies": 2, "recover": 0, "release": {"name": "The Protector of Argaia", "stub": "the-protector-of-argaia"}, "placement": "Battlefield"}', '40', 'Conjuration', '0', '0', NULL, '2', 'f', 'Mind Fog Owl
Unseen: This unit cannot be blocked unless all attacking units without the Unseen ability have been blocked.', '0', '10223', '1', NULL, NULL, 'f'),
('639', 'Confusion Spores', 'confusion-spores', '{"cost": ["[[main]]", "1 [[charm:class]]"], "dice": ["charm", "sympathy"], "name": "Confusion Spores", "stub": "confusion-spores", "text": "[[side]] - [[exhaust]]: Target unit cannot block or guard for the remainder of this turn.\n\nFocus 1: You may spend an additional 1 [[sympathy:class]] to take 1 additional side action this turn.", "type": "Ready Spell", "release": {"name": "The Protector of Argaia", "stub": "the-protector-of-argaia"}, "magicCost": {"charm:class": 1}, "placement": "Spellboard"}', '40', 'Ready Spell', '106', '34', NULL, NULL, 'f', 'Confusion Spores
side - exhaust: Target unit cannot block or guard for the remainder of this turn. Focus 1: You may spend an additional 1 sympathy:class to take 1 additional side action this turn.', '0', '10224', '1', NULL, NULL, 'f'),
('640', 'Summon Mind Fog Owl', 'summon-mind-fog-owl', '{"cost": ["[[main]]"], "dice": ["charm"], "name": "Summon Mind Fog Owl", "stub": "summon-mind-fog-owl", "text": "[[main]] - [[exhaust]] - 1 [[charm:class]] - 1 [[basic]]: Place a [[Mind Fog Owl]] conjuration onto your battlefield.\n\nFocus 1: If you spent any[[charm:power]] to activate this spell, you may choose 1 [[charm:power]] spent and resolve its dice power without paying its cost.", "type": "Ready Spell", "release": {"name": "The Protector of Argaia", "stub": "the-protector-of-argaia"}, "placement": "Spellboard", "conjurations": [{"name": "Mind Fog Owl", "stub": "mind-fog-owl"}]}', '40', 'Ready Spell', '5', '2', NULL, NULL, 't', 'Summon Mind Fog Owl
main - exhaust - 1 charm:class - 1 basic: Place a Mind Fog Owl conjuration onto your battlefield. Focus 1: If you spent anycharm:power to activate this spell, you may choose 1 charm:power spent and resolve its dice power without paying its cost.', '0', '10225', '1', NULL, NULL, 'f'),
('641', 'Essence Druid', 'essence-druid', '{"cost": ["[[main]]", "1 [[sympathy:power]]", "1 [[charm:class]]", "1 [[basic]]"], "dice": ["sympathy", "charm"], "life": 4, "name": "Essence Druid", "stub": "essence-druid", "text": "Spell Recall: When this unit comes into play, you may search your discard pile for a ready spell and place it into your hand.\n\nTame 2: While this unit is in battle, the attack value of units in battle with it is reduced by 2.", "type": "Ally", "attack": 2, "recover": 2, "release": {"name": "The Protector of Argaia", "stub": "the-protector-of-argaia"}, "magicCost": {"basic": 1, "charm:class": 1, "sympathy:power": 1}, "placement": "Battlefield"}', '40', 'Ally', '308', '34', NULL, NULL, 'f', 'Essence Druid
Spell Recall: When this unit comes into play, you may search your discard pile for a ready spell and place it into your hand. Tame 2: While this unit is in battle, the attack value of units in battle with it is reduced by 2.', '0', '10226', '1', NULL, NULL, 'f'),
('642', 'New Ideas', 'new-ideas', '{"cost": [["[[main]]", "[[side]]"], "1 [[sympathy:class]]"], "dice": ["sympathy"], "name": "New Ideas", "stub": "new-ideas", "text": "Choose 1 card in your hand and place it on the bottom of your draw pile. If you do, draw 3 cards.", "type": "Action Spell", "release": {"name": "The Protector of Argaia", "stub": "the-protector-of-argaia"}, "magicCost": {"sympathy:class": 1}, "placement": "Discard"}', '40', 'Action Spell', '106', '32', NULL, NULL, 'f', 'New Ideas
Choose 1 card in your hand and place it on the bottom of your draw pile. If you do, draw 3 cards.', '0', '10227', '1', NULL, NULL, 'f'),
('643', 'Exhortation', 'exhortation', '{"cost": ["[[side]]", "1 [[charm:class]]", "1 [[sympathy:class]]"], "dice": ["charm", "sympathy"], "name": "Exhortation", "stub": "exhortation", "text": "Choose 2 units you control. For each unit, add the other unit''s current attack value to its attack value for the remainder of this turn.", "type": "Action Spell", "release": {"name": "The Protector of Argaia", "stub": "the-protector-of-argaia"}, "magicCost": {"charm:class": 1, "sympathy:class": 1}, "placement": "Discard"}', '40', 'Action Spell', '206', '34', NULL, NULL, 'f', 'Exhortation
Choose 2 units you control. For each unit, add the other unit''s current attack value to its attack value for the remainder of this turn.', '0', '10228', '1', NULL, NULL, 'f'),
('644', 'Seeds Of Aggression', 'seeds-of-aggression', '{"cost": ["[[main]]", ["1 [[charm:power]]", "1 [[sympathy:power]]"]], "dice": ["charm", "sympathy"], "name": "Seeds Of Aggression", "stub": "seeds-of-aggression", "text": "Choose a target unit you control and a target unit an opponent controls. Those units deal damage to each other equal to their attack value.", "type": "Action Spell", "altDice": ["charm", "sympathy"], "release": {"name": "The Protector of Argaia", "stub": "the-protector-of-argaia"}, "magicCost": {"charm:power / sympathy:power": 1}, "placement": "Discard"}', '40', 'Action Spell', '107', '0', NULL, NULL, 'f', 'Seeds Of Aggression
Choose a target unit you control and a target unit an opponent controls. Those units deal damage to each other equal to their attack value.', '34', '10229', '1', NULL, NULL, 'f'),
('645', 'Return to Soil', 'return-to-soil', '{"cost": ["[[main]]", "1 [[charm:class]]"], "dice": ["charm"], "name": "Return to Soil", "stub": "return-to-soil", "text": "Deal 1 damage to a target unit. If that destroys the unit, after it is destroyed, the target player who controlled it must discard 1 card off the top of their draw pile and then you may search that target player''s discard pile for 2 cards and remove them from the game.", "type": "Action Spell", "release": {"name": "The Protector of Argaia", "stub": "the-protector-of-argaia"}, "magicCost": {"charm:class": 1}, "placement": "Discard"}', '40', 'Action Spell', '106', '2', NULL, NULL, 'f', 'Return to Soil
Deal 1 damage to a target unit. If that destroys the unit, after it is destroyed, the target player who controlled it must discard 1 card off the top of their draw pile and then you may search that target player''s discard pile for 2 cards and remove them from the game.', '0', '10230', '1', NULL, NULL, 'f');

INSERT INTO "public"."card_conjuration" ("card_id", "conjuration_id") VALUES
('63', '5'),
('64', '7'),
('65', '10'),
('66', '19'),
('67', '22'),
('68', '27'),
('69', '33'),
('70', '35'),
('71', '51'),
('72', '54'),
('73', '55'),
('74', '76'),
('89', '86'),
('91', '82'),
('92', '87'),
('104', '100'),
('111', '110'),
('117', '114'),
('118', '115'),
('127', '125'),
('128', '126'),
('141', '132'),
('142', '144'),
('152', '153'),
('157', '152'),
('158', '155'),
('170', '168'),
('177', '174'),
('188', '183'),
('189', '190'),
('197', '195'),
('201', '197'),
('202', '200'),
('203', '205'),
('209', '217'),
('210', '215'),
('215', '207'),
('219', '206'),
('220', '210'),
('220', '215'),
('228', '230'),
('229', '226'),
('233', '235'),
('237', '238'),
('247', '236'),
('248', '246'),
('263', '250'),
('264', '257'),
('264', '258'),
('264', '262'),
('273', '272'),
('275', '276'),
('277', '265'),
('278', '266'),
('279', '275'),
('292', '286'),
('293', '287'),
('294', '290'),
('304', '296'),
('305', '296'),
('312', '317'),
('314', '319'),
('315', '318'),
('325', '331'),
('326', '332'),
('340', '345'),
('341', '346'),
('354', '359'),
('355', '361'),
('356', '358'),
('360', '357'),
('365', '364'),
('376', '375'),
('378', '377'),
('380', '379'),
('390', '389'),
('392', '391'),
('403', '402'),
('405', '404'),
('421', '420'),
('428', '427'),
('430', '429'),
('434', '433'),
('441', '440'),
('444', '443'),
('446', '445'),
('461', '460'),
('467', '466'),
('470', '469'),
('472', '471'),
('483', '482'),
('485', '484'),
('496', '495'),
('498', '497'),
('509', '508'),
('511', '510'),
('512', '511'),
('523', '522'),
('527', '526'),
('536', '535'),
('537', '536'),
('538', '537'),
('540', '539'),
('543', '542'),
('552', '551'),
('554', '553'),
('556', '555'),
('564', '563'),
('567', '566'),
('579', '578'),
('587', '586'),
('592', '591'),
('596', '595'),
('599', '598'),
('601', '600'),
('602', '601'),
('607', '606'),
('608', '606'),
('612', '609'),
('612', '610'),
('612', '611'),
('623', '622'),
('627', '622'),
('635', '634'),
('637', '636'),
('640', '638');

INSERT INTO "public"."user" ("id", "email", "badge", "username", "password", "created", "modified", "reset_uuid", "newsletter_opt_in", "description", "is_admin", "exclude_subscriptions", "is_banned", "moderation_notes", "email_subscriptions", "colorize_icons") VALUES
('61', 'hello@ashes.live', '3000', 'IsaacBot', '$2b$12$jeTF3v5.f7Uf/zZgYkfk6OT6w.ofmWf1uo7cO3G/nN35fjp4/TaVa', '2017-11-07 18:29:51+00', '2017-11-15 04:49:48+00', NULL, 'f', '**IsaacBot#3000** initialized. Publishing official Phoenixborn decklists. Disavowing any relationship with Plaid Hat Games or Mr. Vega. Randomizing First Five options.

Encountering boredom. Seeking additional tasks. Executing foreign file *RD_TOASTER.EXE*.

Would you like some toast? No? Would you like a crumpet? Very well. I have a third question. A sensible question. A question that will tax your I.Q. to its very limits and stretch the sinews of your knowledge to bursting point. Given that God is infinite, and that the universe is also infinite...would you like a toasted teacake?', 't', 'f', 'f', NULL, 'f', 'f');

INSERT INTO "public"."user_release" ("user_id", "release_id") VALUES
('61', '1'),
('61', '21'),
('61', '22'),
('61', '23'),
('61', '24');

INSERT INTO "public"."ashes500_revision" ("id", "entity_id", "description", "created") VALUES
('1', '1694', '**Ashes 500** is an alternate constructed format for Ashes [[originally created by Elliot Kramer http://www.strangecopy.com/index.php/2017/03/19/ashes-500/]] and now maintained by [[doktarr#0a=m]] with input from the community. In Ashes 500 all cards are assigned point values, and your deck must cost 500 points or less (while following all standard deck construction rules). Originally provided [[as a spreadsheet https://docs.google.com/spreadsheets/d/14vX5nkIR2_2gcxIOn8X1-cnt18v1VFr2H70xB6FXfNs/edit?usp=sharing]], you can now construct Ashes 500 decks here on Ashes.live.

Ashes 500 costs are formatted like **25/15/10** where the first copy of the card costs **25** points, the second copy costs **15** points, and the third copy costs **10** points (so if you included 3x copies, you would spend **25 + 15 + 10 = 50** points).

Additionally, a small number of cards include penalties when they are included together, represented by a "**!**" next to the prices. Tap or mouse over the "**!**" to view relevant penalties for that card; for instance, if your deck includes both [[Shifting Mist]] and [[Summon Butterfly Monk]], an extra 20 points will be added to the deck''s total. Penalties are used to discourage overly strong archetypes and combos.

**Why use Ashes 500?** The Ashes 500 format encourages creative deck construction with cards that would not normally be competitive, and is a great way to shake up your local meta if you find yourselves falling into a rut.

If you would like to suggest changes to Ashes 500 prices, you can join the conversation about it in the [[#500 Slack channel http://www.strangecopy.com/index.php/ashes-chat/]] or [[post your thoughts here on Ashes.live ashes.live/posts/general/submit/]].', '2018-05-26 22:29:31+00'),
('2', '1995', '**Ashes 500** is an alternate constructed format for Ashes [[originally created by Elliot Kramer http://www.strangecopy.com/index.php/2017/03/19/ashes-500/]] and now maintained by [[doktarr#0a=m]] with input from the community. In Ashes 500 all cards are assigned point values, and your deck must cost 500 points or less (while following all standard deck construction rules). Originally provided [[as a spreadsheet https://docs.google.com/spreadsheets/d/1_VGzVoAU5k7JsG3N56WL1Nno3DCSUvWm5eZp6gzlqk0/edit?usp=sharing]], you can now construct Ashes 500 decks here on Ashes.live.

Ashes 500 costs are formatted like **25/15/10** where the first copy of the card costs **25** points, the second copy costs **15** points, and the third copy costs **10** points (so if you included 3x copies, you would spend **25 + 15 + 10 = 50** points).

Additionally, a small number of cards include penalties when they are included together, represented by a "**!**" next to the prices. Tap or mouse over the "**!**" to view relevant penalties for that card; for instance, if your deck includes both [[Shifting Mist]] and [[Summon Butterfly Monk]], an extra 30 points will be added to the deck''s total. Penalties are used to discourage overly strong archetypes and combos.

**Why use Ashes 500?** The Ashes 500 format encourages creative deck construction with cards that would not normally be competitive, and is a great way to shake up your local meta if you find yourselves falling into a rut.

If you would like to suggest changes to Ashes 500 prices, you can join the conversation about it in the [[#500 Slack channel http://www.strangecopy.com/index.php/ashes-chat/]] or [[post your thoughts here on Ashes.live ashes.live/posts/general/submit/]].', '2018-06-21 22:40:27+00'),
('3', '6690', '**Ashes 500** is an alternate constructed format for Ashes [[originally created by Elliot Kramer http://www.strangecopy.com/index.php/2017/03/19/ashes-500/]] and now maintained by [[doktarr#0a=m]] with input from the community. In Ashes 500 all cards are assigned point values, and your deck must cost 500 points or less (while following all standard deck construction rules). Originally provided [[as a spreadsheet https://docs.google.com/spreadsheets/d/12HsQO47Nj9GykadM5q2ETfjvoN3OuEjd9xmqanTD08I/edit?usp=sharing]], you can now construct Ashes 500 decks here on Ashes.live.

Ashes 500 costs are formatted like **25/15/10** where the first copy of the card costs **25** points, the second copy costs **15** points, and the third copy costs **10** points (so if you included 3x copies, you would spend **25 + 15 + 10 = 50** points).

Additionally, a small number of cards include penalties when they are included together, represented by a "**!**" next to the prices. Tap or mouse over the "**!**" to view relevant penalties for that card; for instance, if your deck includes both [[Shifting Mist]] and [[Summon Butterfly Monk]], an extra 30 points will be added to the deck''s total. Penalties are used to discourage overly strong archetypes and combos.

**Why use Ashes 500?** The Ashes 500 format encourages creative deck construction with cards that would not normally be competitive, and is a great way to shake up your local meta if you find yourselves falling into a rut.

If you would like to suggest changes to Ashes 500 prices, you can join the conversation about it in the [[#500 Slack channel http://www.strangecopy.com/index.php/ashes-chat/]] or [[post your thoughts here on Ashes.live ashes.live/posts/general/submit/]].', '2019-05-09 22:16:45+00');

INSERT INTO "public"."ashes500_value" ("id", "card_id", "revision_id", "combo_card_id", "qty_1", "qty_2", "qty_3", "combo_card_type") VALUES
('1', '1', '1', NULL, '2', '2', '2', NULL),
('2', '105', '1', NULL, '1', '1', '1', NULL),
('3', '2', '1', NULL, '20', '5', '5', NULL),
('4', '106', '1', NULL, '25', '25', '25', NULL),
('5', '3', '1', NULL, '33', NULL, NULL, NULL),
('6', '191', '1', NULL, '66', NULL, NULL, NULL),
('7', '178', '1', NULL, '12', '12', '12', NULL),
('8', '107', '1', NULL, '2', '2', '2', NULL),
('9', '93', '1', NULL, '2', '2', '2', NULL),
('10', '4', '1', NULL, '1', '1', '1', NULL),
('11', '94', '1', NULL, '33', '33', '33', NULL),
('12', '6', '1', NULL, '0', '0', '0', NULL),
('13', '119', '1', NULL, '1', '1', '1', NULL),
('14', '8', '1', NULL, '6', '6', '6', NULL),
('15', '95', '1', NULL, '66', NULL, NULL, NULL),
('16', '9', '1', NULL, '0', '0', '0', NULL),
('17', '192', '1', NULL, '33', '20', '20', NULL),
('18', '11', '1', NULL, '6', '6', '6', NULL),
('19', '108', '1', NULL, '1', '1', '1', NULL),
('20', '165', '1', NULL, '60', '10', '1', NULL),
('21', '96', '1', NULL, '15', '15', '15', NULL),
('22', '12', '1', NULL, '60', '45', '45', NULL),
('23', '97', '1', NULL, '5', '5', '5', NULL),
('24', '166', '1', NULL, '33', '33', '33', NULL),
('25', '98', '1', NULL, '20', '20', '20', NULL),
('26', '13', '1', NULL, '12', NULL, NULL, NULL),
('27', '145', '1', NULL, '40', '40', '40', NULL),
('28', '99', '1', NULL, '6', '6', '6', NULL),
('29', '79', '1', NULL, '1', '1', '1', NULL),
('30', '14', '1', NULL, '2', '1', '1', NULL),
('31', '80', '1', NULL, '3', '3', '3', NULL),
('32', '193', '1', NULL, '25', '25', '15', NULL),
('33', '159', '1', NULL, '12', NULL, NULL, NULL),
('34', '109', '1', NULL, '6', '6', '6', NULL),
('35', '179', '1', NULL, '33', '20', '20', NULL),
('36', '167', '1', NULL, '25', NULL, NULL, NULL),
('37', '180', '1', NULL, '50', '25', '25', NULL),
('38', '15', '1', NULL, '1', '1', '1', NULL),
('39', '16', '1', NULL, '6', '6', '6', NULL),
('40', '146', '1', NULL, '33', '33', '33', NULL),
('41', '169', '1', NULL, '2', '2', '2', NULL),
('42', '17', '1', NULL, '20', '6', '6', NULL),
('43', '208', '1', NULL, '6', '6', '6', NULL),
('44', '18', '1', NULL, '12', '1', '1', NULL),
('45', '20', '1', NULL, '70', '60', '60', NULL),
('46', '120', '1', NULL, '0', '0', '0', NULL),
('47', '21', '1', NULL, '25', '25', '25', NULL),
('48', '101', '1', NULL, '25', '25', '25', NULL),
('49', '121', '1', NULL, '1', '1', '1', NULL),
('50', '147', '1', NULL, '6', '6', '6', NULL),
('51', '81', '1', NULL, '1', '1', '1', NULL),
('52', '83', '1', NULL, '3', '5', '5', NULL),
('53', '84', '1', NULL, '1', '1', '1', NULL),
('54', '85', '1', NULL, '1', '1', '1', NULL),
('55', '163', '1', NULL, '1', '1', '1', NULL),
('56', '23', '1', NULL, '1', '1', '1', NULL),
('57', '170', '1', NULL, '7', '0', '0', NULL),
('58', '148', '1', NULL, '3', '3', '3', NULL),
('59', '24', '1', NULL, '60', '45', '45', NULL),
('60', '181', '1', NULL, '25', '25', '25', NULL),
('61', '133', '1', NULL, '12', '12', '9', NULL),
('62', '25', '1', NULL, '33', '33', '33', NULL),
('63', '134', '1', NULL, '45', '25', '25', NULL),
('64', '171', '1', NULL, '1', '1', '1', NULL),
('65', '209', '1', NULL, '3', '1', '1', NULL),
('66', '26', '1', NULL, '25', '10', '10', NULL),
('67', '88', '1', NULL, '25', '15', '15', NULL),
('68', '122', '1', NULL, '40', '45', '50', NULL),
('69', '194', '1', NULL, '40', '6', '6', NULL),
('70', '28', '1', NULL, '12', '12', '12', NULL),
('71', '182', '1', NULL, '25', NULL, NULL, NULL),
('72', '29', '1', NULL, '25', NULL, NULL, NULL),
('73', '211', '1', NULL, '3', '1', '1', NULL),
('74', '212', '1', NULL, '9', '9', '9', NULL),
('75', '196', '1', NULL, '50', '50', '50', NULL),
('76', '214', '1', NULL, '12', NULL, NULL, NULL),
('77', '135', '1', NULL, '15', '6', '6', NULL),
('78', '172', '1', NULL, '8', '8', '8', NULL),
('79', '136', '1', NULL, '6', '3', '3', NULL),
('80', '30', '1', NULL, '1', '1', '1', NULL),
('81', '111', '1', NULL, '50', NULL, NULL, NULL),
('82', '213', '1', NULL, '25', '25', '25', NULL),
('83', '173', '1', NULL, '1', '1', '1', NULL),
('84', '31', '1', NULL, '1', '1', '1', NULL),
('85', '161', '1', NULL, '12', NULL, NULL, NULL),
('86', '32', '1', NULL, '12', NULL, NULL, NULL),
('87', '149', '1', NULL, '40', '12', '12', NULL),
('88', '184', '1', NULL, '25', '25', '25', NULL),
('89', '198', '1', NULL, '50', '35', '35', NULL),
('90', '216', '1', NULL, '3', '3', '3', NULL),
('91', '34', '1', NULL, '10', '5', '5', NULL),
('92', '112', '1', NULL, '0', '0', '0', NULL),
('93', '137', '1', NULL, '50', '50', '50', NULL),
('94', '113', '1', NULL, '2', '2', '2', NULL),
('95', '36', '1', NULL, '20', '20', '20', NULL),
('96', '37', '1', NULL, '40', '40', '40', NULL),
('97', '150', '1', NULL, '25', NULL, NULL, NULL),
('98', '38', '1', NULL, '12', NULL, NULL, NULL),
('99', '138', '1', NULL, '0', NULL, NULL, NULL),
('100', '39', '1', NULL, '25', '25', '25', NULL),
('101', '40', '1', NULL, '50', '2', '2', NULL),
('102', '164', '1', NULL, '66', NULL, NULL, NULL),
('103', '41', '1', NULL, '9', '9', '9', NULL),
('104', '123', '1', NULL, '20', '20', '20', NULL),
('105', '162', '1', NULL, '33', '33', '33', NULL),
('106', '102', '1', NULL, '3', '3', '3', NULL),
('107', '175', '1', NULL, '16', '5', '5', NULL),
('108', '139', '1', NULL, '16', '16', '12', NULL),
('109', '185', '1', NULL, '10', '8', '8', NULL),
('110', '42', '1', NULL, '1', '1', '1', NULL),
('111', '43', '1', NULL, '1', '1', '1', NULL),
('112', '160', '1', NULL, '3', '3', '3', NULL),
('113', '44', '1', NULL, '9', '9', '9', NULL),
('114', '45', '1', NULL, '2', '1', '1', NULL),
('115', '46', '1', NULL, '1', '1', '1', NULL),
('116', '103', '1', NULL, '20', '20', '20', NULL),
('117', '116', '1', NULL, '2', '2', '2', NULL),
('118', '89', '1', NULL, '25', NULL, NULL, NULL),
('119', '90', '1', NULL, '33', '33', '33', NULL),
('120', '151', '1', NULL, '20', '20', '20', NULL),
('121', '47', '1', NULL, '1', '1', '1', NULL),
('122', '48', '1', NULL, '6', '6', '6', NULL),
('123', '199', '1', NULL, '6', '6', '6', NULL),
('124', '49', '1', NULL, '25', NULL, NULL, NULL),
('125', '50', '1', NULL, '3', '3', '3', NULL),
('126', '124', '1', NULL, '9', '1', '1', NULL),
('127', '52', '1', NULL, '3', '1', '1', NULL),
('128', '154', '1', NULL, '1', '1', '1', NULL),
('129', '140', '1', NULL, '3', '3', '3', NULL),
('130', '53', '1', NULL, '40', '12', '12', NULL),
('131', '218', '1', NULL, '15', '10', '10', NULL),
('132', '56', '1', NULL, '10', '1', '1', NULL),
('133', '57', '1', NULL, '4', '6', '6', NULL),
('134', '176', '1', NULL, '50', '35', '35', NULL),
('135', '186', '1', NULL, '2', '2', '2', NULL),
('136', '58', '1', NULL, '1', '1', '1', NULL),
('137', '187', '1', NULL, '4', '2', '2', NULL),
('138', '59', '1', NULL, '6', '6', '6', NULL),
('139', '60', '1', NULL, '12', '12', '12', NULL),
('140', '61', '1', NULL, '3', '1', '1', NULL),
('141', '62', '1', NULL, '1', '1', '1', NULL),
('142', '156', '1', NULL, '25', '20', '20', NULL),
('143', '219', '1', NULL, '6', '1', '1', NULL),
('144', '63', '1', NULL, '6', '6', '6', NULL),
('145', '64', '1', NULL, '33', '33', '33', NULL),
('146', '65', '1', NULL, '30', '35', '35', NULL),
('147', '104', '1', NULL, '6', '6', '6', NULL),
('148', '141', '1', NULL, '95', '25', '10', NULL),
('149', '66', '1', NULL, '3', '1', '1', NULL),
('150', '91', '1', NULL, '95', '25', '25', NULL),
('151', '67', '1', NULL, '80', '25', '25', NULL),
('152', '92', '1', NULL, '3', '1', '1', NULL),
('153', '220', '1', NULL, '20', '20', '20', NULL),
('154', '68', '1', NULL, '1', '0', '0', NULL),
('155', '201', '1', NULL, '6', '1', '1', NULL),
('156', '188', '1', NULL, '12', '12', '1', NULL),
('157', '69', '1', NULL, '3', '3', '3', NULL),
('158', '177', '1', NULL, '12', '12', '12', NULL),
('159', '70', '1', NULL, '2', '2', '2', NULL),
('160', '117', '1', NULL, '1', '0', '0', NULL),
('161', '118', '1', NULL, '12', '12', '12', NULL),
('162', '157', '1', NULL, '9', '2', '0', NULL),
('163', '71', '1', NULL, '12', '1', '1', NULL),
('164', '127', '1', NULL, '2', '2', '2', NULL),
('165', '128', '1', NULL, '25', '35', '40', NULL),
('166', '72', '1', NULL, '25', '25', '12', NULL),
('167', '73', '1', NULL, '16', '16', '16', NULL),
('168', '158', '1', NULL, '33', '3', '3', NULL),
('169', '202', '1', NULL, '1', '1', '1', NULL),
('170', '74', '1', NULL, '80', '12', '12', NULL),
('171', '189', '1', NULL, '90', '12', '2', NULL),
('172', '203', '1', NULL, '3', '3', '3', NULL),
('173', '142', '1', NULL, '95', '25', '25', NULL),
('174', '204', '1', NULL, '6', '6', '6', NULL),
('175', '143', '1', NULL, '25', '15', '15', NULL),
('176', '75', '1', NULL, '25', '25', '25', NULL),
('177', '221', '1', NULL, '2', '2', '2', NULL),
('178', '129', '1', NULL, '0', '0', '0', NULL),
('179', '77', '1', NULL, '1', '1', '1', NULL),
('180', '78', '1', NULL, '1', '1', '1', NULL),
('181', '130', '1', NULL, '2', '2', '2', NULL),
('182', '131', '1', NULL, '40', NULL, NULL, NULL),
('183', '105', '1', '134', '240', NULL, NULL, NULL),
('184', '105', '1', '180', '240', NULL, NULL, NULL),
('185', '105', '1', '26', '50', NULL, NULL, NULL),
('186', '122', '1', '165', '60', NULL, NULL, NULL),
('187', '122', '1', '1', '60', NULL, NULL, NULL),
('188', '94', '1', '198', '10', '10', '10', NULL),
('189', '65', '1', '53', '20', NULL, NULL, NULL),
('190', '65', '1', '149', '20', NULL, NULL, NULL),
('191', '128', '1', '53', '20', NULL, NULL, NULL),
('192', '128', '1', '149', '20', NULL, NULL, NULL),
('193', '131', '1', '127', '25', NULL, NULL, NULL),
('194', '1', '2', NULL, '1', '1', '1', NULL),
('195', '105', '2', NULL, '0', '0', '0', NULL),
('196', '2', '2', NULL, '16', '5', '5', NULL),
('197', '106', '2', NULL, '25', '25', '25', NULL),
('198', '3', '2', NULL, '33', NULL, NULL, NULL),
('199', '191', '2', NULL, '75', NULL, NULL, NULL),
('200', '178', '2', NULL, '12', '12', '12', NULL),
('201', '107', '2', NULL, '2', '2', '2', NULL),
('202', '93', '2', NULL, '2', '2', '2', NULL),
('203', '4', '2', NULL, '1', '1', '1', NULL),
('204', '94', '2', NULL, '33', '33', '33', NULL),
('205', '6', '2', NULL, '0', '0', '0', NULL),
('206', '119', '2', NULL, '1', '1', '1', NULL),
('207', '8', '2', NULL, '6', '6', '6', NULL),
('208', '95', '2', NULL, '90', NULL, NULL, NULL),
('209', '9', '2', NULL, '0', '0', '0', NULL),
('210', '192', '2', NULL, '24', '18', '18', NULL),
('211', '11', '2', NULL, '6', '6', '6', NULL),
('212', '108', '2', NULL, '2', '2', '2', NULL),
('213', '165', '2', NULL, '60', '10', '1', NULL),
('214', '96', '2', NULL, '15', '15', '15', NULL),
('215', '12', '2', NULL, '60', '45', '45', NULL),
('216', '97', '2', NULL, '5', '5', '5', NULL),
('217', '166', '2', NULL, '33', '33', '33', NULL),
('218', '98', '2', NULL, '18', '12', '12', NULL),
('219', '13', '2', NULL, '12', NULL, NULL, NULL),
('220', '145', '2', NULL, '40', '40', '40', NULL),
('221', '99', '2', NULL, '6', '6', '6', NULL),
('222', '79', '2', NULL, '1', '1', '1', NULL),
('223', '14', '2', NULL, '2', '1', '1', NULL),
('224', '80', '2', NULL, '3', '3', '3', NULL),
('225', '193', '2', NULL, '25', '25', '15', NULL),
('226', '159', '2', NULL, '12', NULL, NULL, NULL),
('227', '109', '2', NULL, '6', '6', '6', NULL),
('228', '179', '2', NULL, '33', '20', '20', NULL),
('229', '167', '2', NULL, '25', NULL, NULL, NULL),
('230', '180', '2', NULL, '80', '40', '40', NULL),
('231', '15', '2', NULL, '0', '0', '0', NULL),
('232', '16', '2', NULL, '6', '6', '6', NULL),
('233', '146', '2', NULL, '33', '33', '33', NULL),
('234', '169', '2', NULL, '2', '2', '2', NULL),
('235', '17', '2', NULL, '20', '6', '6', NULL),
('236', '208', '2', NULL, '6', '6', '6', NULL),
('237', '18', '2', NULL, '12', '1', '1', NULL),
('238', '20', '2', NULL, '70', '40', '40', NULL),
('239', '120', '2', NULL, '0', '0', '0', NULL),
('240', '21', '2', NULL, '25', '25', '25', NULL),
('241', '101', '2', NULL, '25', '25', '25', NULL),
('242', '121', '2', NULL, '0', '0', '0', NULL),
('243', '147', '2', NULL, '6', '6', '6', NULL),
('244', '81', '2', NULL, '0', '0', '0', NULL),
('245', '83', '2', NULL, '3', '5', '5', NULL),
('246', '84', '2', NULL, '1', '1', '1', NULL),
('247', '85', '2', NULL, '1', '1', '1', NULL),
('248', '163', '2', NULL, '1', '1', '1', NULL),
('249', '23', '2', NULL, '1', '1', '1', NULL),
('250', '170', '2', NULL, '8', '1', '1', NULL),
('251', '148', '2', NULL, '3', '3', '3', NULL),
('252', '24', '2', NULL, '60', '45', '45', NULL),
('253', '181', '2', NULL, '22', '15', '15', NULL),
('254', '133', '2', NULL, '12', '12', '9', NULL),
('255', '25', '2', NULL, '33', '33', '33', NULL),
('256', '134', '2', NULL, '45', '25', '25', NULL),
('257', '171', '2', NULL, '1', '1', '1', NULL),
('258', '209', '2', NULL, '3', '1', '1', NULL),
('259', '26', '2', NULL, '25', '10', '10', NULL),
('260', '88', '2', NULL, '20', '15', '15', NULL),
('261', '122', '2', NULL, '40', '45', '50', NULL),
('262', '194', '2', NULL, '40', '6', '6', NULL),
('263', '28', '2', NULL, '12', '12', '12', NULL),
('264', '182', '2', NULL, '25', NULL, NULL, NULL),
('265', '29', '2', NULL, '25', NULL, NULL, NULL),
('266', '211', '2', NULL, '3', '1', '1', NULL),
('267', '212', '2', NULL, '8', '6', '6', NULL),
('268', '196', '2', NULL, '50', '50', '50', NULL),
('269', '214', '2', NULL, '12', NULL, NULL, NULL),
('270', '135', '2', NULL, '15', '6', '6', NULL),
('271', '172', '2', NULL, '8', '8', '8', NULL),
('272', '136', '2', NULL, '6', '3', '3', NULL),
('273', '30', '2', NULL, '1', '1', '1', NULL),
('274', '111', '2', NULL, '50', NULL, NULL, NULL),
('275', '213', '2', NULL, '25', '25', '25', NULL),
('276', '173', '2', NULL, '1', '1', '1', NULL),
('277', '31', '2', NULL, '1', '1', '1', NULL),
('278', '161', '2', NULL, '12', NULL, NULL, NULL),
('279', '32', '2', NULL, '12', NULL, NULL, NULL),
('280', '149', '2', NULL, '20', '15', '15', NULL),
('281', '184', '2', NULL, '35', '25', '25', NULL),
('282', '198', '2', NULL, '55', '40', '40', NULL),
('283', '216', '2', NULL, '3', '3', '3', NULL),
('284', '34', '2', NULL, '10', '5', '5', NULL),
('285', '112', '2', NULL, '0', '0', '0', NULL),
('286', '137', '2', NULL, '50', '50', '50', NULL),
('287', '113', '2', NULL, '6', '6', '6', NULL),
('288', '36', '2', NULL, '20', '20', '20', NULL),
('289', '37', '2', NULL, '35', '30', '30', NULL),
('290', '150', '2', NULL, '25', NULL, NULL, NULL),
('291', '38', '2', NULL, '12', NULL, NULL, NULL),
('292', '138', '2', NULL, '0', NULL, NULL, NULL),
('293', '39', '2', NULL, '25', '25', '25', NULL),
('294', '40', '2', NULL, '50', '2', '2', NULL),
('295', '164', '2', NULL, '125', NULL, NULL, NULL),
('296', '41', '2', NULL, '9', '9', '9', NULL),
('297', '123', '2', NULL, '18', '18', '18', NULL),
('298', '162', '2', NULL, '33', '33', '33', NULL),
('299', '102', '2', NULL, '3', '3', '3', NULL),
('300', '175', '2', NULL, '20', '10', '5', NULL),
('301', '139', '2', NULL, '16', '16', '12', NULL),
('302', '185', '2', NULL, '10', '8', '8', NULL),
('303', '42', '2', NULL, '1', '1', '1', NULL),
('304', '43', '2', NULL, '1', '1', '1', NULL),
('305', '160', '2', NULL, '3', '3', '3', NULL),
('306', '44', '2', NULL, '12', '12', '12', NULL),
('307', '45', '2', NULL, '2', '1', '1', NULL),
('308', '46', '2', NULL, '2', '2', '2', NULL),
('309', '103', '2', NULL, '20', '20', '20', NULL),
('310', '116', '2', NULL, '6', '6', '6', NULL),
('311', '89', '2', NULL, '25', NULL, NULL, NULL),
('312', '90', '2', NULL, '40', '30', '30', NULL),
('313', '151', '2', NULL, '20', '20', '20', NULL),
('314', '47', '2', NULL, '1', '1', '1', NULL),
('315', '48', '2', NULL, '6', '6', '6', NULL),
('316', '199', '2', NULL, '6', '6', '6', NULL),
('317', '49', '2', NULL, '15', NULL, NULL, NULL),
('318', '50', '2', NULL, '3', '3', '3', NULL),
('319', '124', '2', NULL, '1', '1', '1', NULL),
('320', '52', '2', NULL, '3', '1', '1', NULL),
('321', '154', '2', NULL, '0', '0', '0', NULL),
('322', '140', '2', NULL, '3', '3', '3', NULL),
('323', '53', '2', NULL, '20', '15', '15', NULL),
('324', '218', '2', NULL, '15', '10', '10', NULL),
('325', '56', '2', NULL, '10', '1', '1', NULL),
('326', '57', '2', NULL, '4', '6', '6', NULL),
('327', '176', '2', NULL, '50', '35', '35', NULL),
('328', '186', '2', NULL, '4', '4', '4', NULL),
('329', '58', '2', NULL, '1', '1', '1', NULL),
('330', '187', '2', NULL, '4', '2', '2', NULL),
('331', '59', '2', NULL, '6', '6', '6', NULL),
('332', '60', '2', NULL, '12', '12', '12', NULL),
('333', '61', '2', NULL, '3', '1', '1', NULL),
('334', '62', '2', NULL, '1', '1', '1', NULL),
('335', '156', '2', NULL, '30', '15', '10', NULL),
('336', '219', '2', NULL, '4', '0', '0', NULL),
('337', '63', '2', NULL, '6', '6', '6', NULL),
('338', '64', '2', NULL, '33', '10', '10', NULL),
('339', '65', '2', NULL, '30', '35', '35', NULL),
('340', '104', '2', NULL, '6', '1', '1', NULL),
('341', '141', '2', NULL, '90', '10', '2', NULL),
('342', '66', '2', NULL, '8', '1', '0', NULL),
('343', '91', '2', NULL, '95', '25', '25', NULL),
('344', '67', '2', NULL, '75', '25', '25', NULL),
('345', '92', '2', NULL, '1', '0', '0', NULL),
('346', '220', '2', NULL, '20', '20', '20', NULL),
('347', '68', '2', NULL, '1', '0', '0', NULL),
('348', '201', '2', NULL, '6', '1', '1', NULL),
('349', '188', '2', NULL, '12', '12', '1', NULL),
('350', '69', '2', NULL, '3', '3', '3', NULL),
('351', '177', '2', NULL, '12', '12', '12', NULL),
('352', '70', '2', NULL, '2', '2', '2', NULL),
('353', '117', '2', NULL, '1', '0', '0', NULL),
('354', '118', '2', NULL, '12', '16', '16', NULL),
('355', '157', '2', NULL, '9', '2', '0', NULL),
('356', '71', '2', NULL, '12', '1', '1', NULL),
('357', '127', '2', NULL, '2', '2', '2', NULL),
('358', '128', '2', NULL, '25', '35', '40', NULL),
('359', '72', '2', NULL, '25', '25', '12', NULL),
('360', '73', '2', NULL, '16', '16', '16', NULL),
('361', '158', '2', NULL, '33', '3', '3', NULL),
('362', '202', '2', NULL, '1', '0', '0', NULL),
('363', '74', '2', NULL, '80', '25', '25', NULL),
('364', '189', '2', NULL, '80', '12', '2', NULL),
('365', '203', '2', NULL, '3', '3', '3', NULL),
('366', '142', '2', NULL, '95', '25', '25', NULL),
('367', '204', '2', NULL, '6', '6', '6', NULL),
('368', '143', '2', NULL, '25', '15', '15', NULL),
('369', '75', '2', NULL, '25', '25', '25', NULL),
('370', '221', '2', NULL, '1', '1', '1', NULL),
('371', '129', '2', NULL, '0', '0', '0', NULL),
('372', '77', '2', NULL, '2', '2', '2', NULL),
('373', '78', '2', NULL, '1', '1', '1', NULL),
('374', '130', '2', NULL, '2', '2', '2', NULL),
('375', '131', '2', NULL, '40', NULL, NULL, NULL),
('376', '105', '2', '134', '240', NULL, NULL, NULL),
('377', '105', '2', '180', '240', NULL, NULL, NULL),
('378', '105', '2', '26', '50', NULL, NULL, NULL),
('379', '122', '2', '1', '60', NULL, NULL, NULL),
('380', '122', '2', '165', '60', NULL, NULL, NULL),
('381', '94', '2', '198', '10', '10', '10', NULL),
('382', '65', '2', '149', '30', NULL, NULL, NULL),
('383', '65', '2', '53', '30', NULL, NULL, NULL),
('384', '128', '2', '149', '30', NULL, NULL, NULL),
('385', '128', '2', '53', '30', NULL, NULL, NULL),
('386', '131', '2', '127', '25', NULL, NULL, NULL),
('387', '1', '3', NULL, '1', '1', '1', NULL),
('388', '222', '3', NULL, '22', '15', '15', NULL),
('389', '105', '3', NULL, '0', '0', '0', NULL),
('390', '251', '3', NULL, '7', '6', '6', NULL),
('391', '2', '3', NULL, '16', '5', '5', NULL),
('392', '237', '3', NULL, '20', '20', '20', NULL),
('393', '106', '3', NULL, '25', '25', '25', NULL),
('394', '3', '3', NULL, '33', NULL, NULL, NULL),
('395', '191', '3', NULL, '75', NULL, NULL, NULL),
('396', '252', '3', NULL, '1', '0', '0', NULL),
('397', '178', '3', NULL, '25', '25', '25', NULL),
('398', '253', '3', NULL, '20', '12', '12', NULL),
('399', '223', '3', NULL, '30', '20', '20', NULL),
('400', '107', '3', NULL, '2', '2', '2', NULL),
('401', '224', '3', NULL, '3', '3', '3', NULL),
('402', '93', '3', NULL, '2', '2', '2', NULL),
('403', '4', '3', NULL, '1', '1', '1', NULL),
('404', '94', '3', NULL, '33', '33', '33', NULL),
('405', '6', '3', NULL, '0', '0', '0', NULL),
('406', '119', '3', NULL, '1', '1', '1', NULL),
('407', '8', '3', NULL, '6', '6', '6', NULL),
('408', '95', '3', NULL, '90', NULL, NULL, NULL),
('409', '9', '3', NULL, '0', '0', '0', NULL),
('410', '192', '3', NULL, '24', '18', '18', NULL),
('411', '11', '3', NULL, '6', '6', '6', NULL),
('412', '239', '3', NULL, '40', '18', '18', NULL),
('413', '240', '3', NULL, '25', '12', '12', NULL),
('414', '108', '3', NULL, '2', '2', '2', NULL),
('415', '165', '3', NULL, '60', '10', '1', NULL),
('416', '96', '3', NULL, '15', '15', '15', NULL),
('417', '12', '3', NULL, '60', '45', '45', NULL),
('418', '295', '3', NULL, '22', '1', '1', NULL),
('419', '97', '3', NULL, '5', '5', '5', NULL),
('420', '166', '3', NULL, '33', '33', '33', NULL),
('421', '98', '3', NULL, '18', '12', '12', NULL),
('422', '13', '3', NULL, '20', NULL, NULL, NULL),
('423', '281', '3', NULL, '30', '30', '30', NULL),
('424', '282', '3', NULL, '8', '1', '1', NULL),
('425', '145', '3', NULL, '40', '40', '40', NULL),
('426', '99', '3', NULL, '6', '6', '6', NULL),
('427', '79', '3', NULL, '1', '1', '1', NULL),
('428', '14', '3', NULL, '2', '1', '1', NULL),
('429', '254', '3', NULL, '8', '8', '8', NULL),
('430', '225', '3', NULL, '40', '40', '40', NULL),
('431', '80', '3', NULL, '3', '3', '3', NULL),
('432', '193', '3', NULL, '25', '25', '15', NULL),
('433', '159', '3', NULL, '12', NULL, NULL, NULL),
('434', '109', '3', NULL, '6', '6', '6', NULL),
('435', '179', '3', NULL, '33', '20', '20', NULL),
('436', '227', '3', NULL, '4', '1', '1', NULL),
('437', '267', '3', NULL, '30', '30', '30', NULL),
('438', '167', '3', NULL, '25', NULL, NULL, NULL),
('439', '180', '3', NULL, '70', '40', '40', NULL),
('440', '15', '3', NULL, '0', '0', '0', NULL),
('441', '16', '3', NULL, '6', '6', '6', NULL),
('442', '146', '3', NULL, '33', '33', '33', NULL),
('443', '169', '3', NULL, '2', '2', '2', NULL),
('444', '283', '3', NULL, '33', '10', '10', NULL),
('445', '284', '3', NULL, '6', '6', '6', NULL),
('446', '17', '3', NULL, '20', '6', '6', NULL),
('447', '208', '3', NULL, '6', '6', '6', NULL),
('448', '18', '3', NULL, '12', '1', '1', NULL),
('449', '20', '3', NULL, '70', '40', '40', NULL),
('450', '120', '3', NULL, '0', '0', '0', NULL),
('451', '21', '3', NULL, '25', '25', '25', NULL),
('452', '285', '3', NULL, '25', NULL, NULL, NULL),
('453', '101', '3', NULL, '25', '25', '25', NULL),
('454', '121', '3', NULL, '0', '0', '0', NULL),
('455', '147', '3', NULL, '6', '6', '6', NULL),
('456', '81', '3', NULL, '0', '0', '0', NULL),
('457', '83', '3', NULL, '4', '8', '8', NULL),
('458', '84', '3', NULL, '1', '1', '1', NULL),
('459', '85', '3', NULL, '1', '1', '1', NULL),
('460', '241', '3', NULL, '20', '20', '20', NULL),
('461', '163', '3', NULL, '1', '1', '1', NULL),
('462', '23', '3', NULL, '1', '1', '1', NULL),
('463', '297', '3', NULL, '40', '25', '25', NULL),
('464', '170', '3', NULL, '8', '1', '1', NULL),
('465', '148', '3', NULL, '2', '8', '8', NULL),
('466', '24', '3', NULL, '60', '45', '45', NULL),
('467', '181', '3', NULL, '22', '15', '15', NULL),
('468', '228', '3', NULL, '20', NULL, NULL, NULL),
('469', '229', '3', NULL, '75', '35', '35', NULL),
('470', '133', '3', NULL, '12', '12', '9', NULL),
('471', '255', '3', NULL, '18', '5', '5', NULL),
('472', '25', '3', NULL, '33', '33', '33', NULL),
('473', '256', '3', NULL, '12', '12', '12', NULL),
('474', '134', '3', NULL, '45', '25', '25', NULL),
('475', '171', '3', NULL, '1', '1', '1', NULL),
('476', '209', '3', NULL, '3', '1', '1', NULL),
('477', '26', '3', NULL, '25', '10', '10', NULL),
('478', '88', '3', NULL, '20', '15', '15', NULL),
('479', '122', '3', NULL, '40', '45', '50', NULL),
('480', '298', '3', NULL, '25', '18', '18', NULL),
('481', '194', '3', NULL, '40', '6', '6', NULL),
('482', '28', '3', NULL, '12', '12', '12', NULL),
('483', '299', '3', NULL, '25', NULL, NULL, NULL),
('484', '182', '3', NULL, '10', NULL, NULL, NULL),
('485', '29', '3', NULL, '25', NULL, NULL, NULL),
('486', '211', '3', NULL, '3', '1', '1', NULL),
('487', '212', '3', NULL, '8', '6', '6', NULL),
('488', '196', '3', NULL, '50', '50', '50', NULL),
('489', '214', '3', NULL, '12', NULL, NULL, NULL),
('490', '135', '3', NULL, '15', '6', '6', NULL),
('491', '242', '3', NULL, '40', '20', '20', NULL),
('492', '268', '3', NULL, '2', '2', '2', NULL),
('493', '172', '3', NULL, '8', '8', '8', NULL),
('494', '300', '3', NULL, '7', '6', '6', NULL),
('495', '136', '3', NULL, '6', '3', '3', NULL),
('496', '30', '3', NULL, '1', '1', '1', NULL),
('497', '111', '3', NULL, '50', NULL, NULL, NULL),
('498', '213', '3', NULL, '25', '25', '25', NULL),
('499', '173', '3', NULL, '1', '1', '1', NULL),
('500', '31', '3', NULL, '1', '1', '1', NULL);

INSERT INTO "public"."ashes500_value" ("id", "card_id", "revision_id", "combo_card_id", "qty_1", "qty_2", "qty_3", "combo_card_type") VALUES
('501', '161', '3', NULL, '12', NULL, NULL, NULL),
('502', '32', '3', NULL, '6', NULL, NULL, NULL),
('503', '184', '3', NULL, '35', '25', '25', NULL),
('504', '149', '3', NULL, '20', '15', '15', NULL),
('505', '198', '3', NULL, '65', '50', '50', NULL),
('506', '216', '3', NULL, '3', '3', '3', NULL),
('507', '269', '3', NULL, '10', '10', '10', NULL),
('508', '34', '3', NULL, '10', '5', '5', NULL),
('509', '231', '3', NULL, '20', '12', '12', NULL),
('510', '112', '3', NULL, '0', '0', '0', NULL),
('511', '137', '3', NULL, '42', '42', '42', NULL),
('512', '288', '3', NULL, '40', '30', '30', NULL),
('513', '113', '3', NULL, '6', '6', '6', NULL),
('514', '36', '3', NULL, '18', '18', '18', NULL),
('515', '37', '3', NULL, '35', '30', '30', NULL),
('516', '150', '3', NULL, '10', NULL, NULL, NULL),
('517', '270', '3', NULL, '15', '15', '15', NULL),
('518', '289', '3', NULL, '30', '20', '20', NULL),
('519', '38', '3', NULL, '12', NULL, NULL, NULL),
('520', '138', '3', NULL, '0', NULL, NULL, NULL),
('521', '39', '3', NULL, '22', '22', '22', NULL),
('522', '40', '3', NULL, '50', '2', '2', NULL),
('523', '164', '3', NULL, '125', NULL, NULL, NULL),
('524', '41', '3', NULL, '9', '9', '9', NULL),
('525', '271', '3', NULL, '4', '4', '4', NULL),
('526', '123', '3', NULL, '20', '20', '20', NULL),
('527', '162', '3', NULL, '30', '30', '30', NULL),
('528', '102', '3', NULL, '3', '3', '3', NULL),
('529', '175', '3', NULL, '20', '10', '5', NULL),
('530', '139', '3', NULL, '16', '16', '12', NULL),
('531', '185', '3', NULL, '10', '8', '8', NULL),
('532', '42', '3', NULL, '1', '1', '1', NULL),
('533', '232', '3', NULL, '16', '5', '5', NULL),
('534', '43', '3', NULL, '1', '1', '1', NULL),
('535', '301', '3', NULL, '9', '9', '9', NULL),
('536', '273', '3', NULL, '25', '14', '14', NULL),
('537', '160', '3', NULL, '3', '3', '3', NULL),
('538', '302', '3', NULL, '20', '15', '15', NULL),
('539', '303', '3', NULL, '25', '25', '25', NULL),
('540', '44', '3', NULL, '12', '12', '12', NULL),
('541', '45', '3', NULL, '8', '3', '3', NULL),
('542', '46', '3', NULL, '2', '2', '2', NULL),
('543', '103', '3', NULL, '20', '20', '20', NULL),
('544', '116', '3', NULL, '15', '15', '15', NULL),
('545', '259', '3', NULL, '50', '25', '1', NULL),
('546', '260', '3', NULL, '6', NULL, NULL, NULL),
('547', '89', '3', NULL, '25', NULL, NULL, NULL),
('548', '90', '3', NULL, '40', '30', '30', NULL),
('549', '304', '3', NULL, '25', '10', '10', NULL),
('550', '151', '3', NULL, '20', '20', '20', NULL),
('551', '47', '3', NULL, '1', '1', '1', NULL),
('552', '48', '3', NULL, '6', '6', '6', NULL),
('553', '199', '3', NULL, '6', '6', '6', NULL),
('554', '274', '3', NULL, '10', '10', '10', NULL),
('555', '49', '3', NULL, '15', NULL, NULL, NULL),
('556', '50', '3', NULL, '3', '3', '3', NULL),
('557', '124', '3', NULL, '1', '1', '1', NULL),
('558', '291', '3', NULL, '33', '33', '33', NULL),
('559', '243', '3', NULL, '12', NULL, NULL, NULL),
('560', '52', '3', NULL, '3', '1', '1', NULL),
('561', '244', '3', NULL, '10', '6', '6', NULL),
('562', '261', '3', NULL, '2', '2', '2', NULL),
('563', '154', '3', NULL, '1', '1', '1', NULL),
('564', '245', '3', NULL, '9', '9', '9', NULL),
('565', '140', '3', NULL, '3', '3', '3', NULL),
('566', '53', '3', NULL, '20', '15', '15', NULL),
('567', '218', '3', NULL, '15', '10', '10', NULL),
('568', '56', '3', NULL, '10', '1', '1', NULL),
('569', '57', '3', NULL, '4', '6', '6', NULL),
('570', '176', '3', NULL, '50', '35', '35', NULL),
('571', '186', '3', NULL, '4', '4', '4', NULL),
('572', '58', '3', NULL, '1', '1', '1', NULL),
('573', '187', '3', NULL, '4', '2', '2', NULL),
('574', '59', '3', NULL, '6', '6', '6', NULL),
('575', '60', '3', NULL, '12', '12', '12', NULL),
('576', '61', '3', NULL, '3', '1', '1', NULL),
('577', '62', '3', NULL, '1', '1', '1', NULL),
('578', '156', '3', NULL, '30', '15', '10', NULL),
('579', '247', '3', NULL, '40', '10', '10', NULL),
('580', '263', '3', NULL, '40', '1', '1', NULL),
('581', '277', '3', NULL, '35', '15', '1', NULL),
('582', '219', '3', NULL, '4', '0', '0', NULL),
('583', '63', '3', NULL, '6', '6', '6', NULL),
('584', '64', '3', NULL, '40', '10', '10', NULL),
('585', '65', '3', NULL, '30', '35', '35', NULL),
('586', '278', '3', NULL, '75', '10', '10', NULL),
('587', '104', '3', NULL, '6', '1', '1', NULL),
('588', '141', '3', NULL, '90', '10', '2', NULL),
('589', '305', '3', NULL, '5', '25', '5', NULL),
('590', '66', '3', NULL, '8', '1', '0', NULL),
('591', '91', '3', NULL, '95', '25', '25', NULL),
('592', '264', '3', NULL, '40', '20', '40', NULL),
('593', '67', '3', NULL, '75', '25', '25', NULL),
('594', '92', '3', NULL, '1', '0', '0', NULL),
('595', '220', '3', NULL, '20', '60', '40', NULL),
('596', '68', '3', NULL, '1', '0', '0', NULL),
('597', '201', '3', NULL, '6', '1', '1', NULL),
('598', '188', '3', NULL, '12', '12', '1', NULL),
('599', '292', '3', NULL, '35', '18', '18', NULL),
('600', '69', '3', NULL, '3', '3', '3', NULL),
('601', '293', '3', NULL, '10', '8', '8', NULL),
('602', '177', '3', NULL, '12', '12', '12', NULL),
('603', '70', '3', NULL, '2', '2', '2', NULL),
('604', '117', '3', NULL, '1', '0', '0', NULL),
('605', '294', '3', NULL, '15', '15', '15', NULL),
('606', '118', '3', NULL, '12', '20', '20', NULL),
('607', '157', '3', NULL, '15', '2', '2', NULL),
('608', '71', '3', NULL, '12', '1', '1', NULL),
('609', '127', '3', NULL, '2', '2', '2', NULL),
('610', '128', '3', NULL, '25', '35', '40', NULL),
('611', '279', '3', NULL, '12', '10', '10', NULL),
('612', '72', '3', NULL, '25', '25', '12', NULL),
('613', '73', '3', NULL, '16', '16', '16', NULL),
('614', '248', '3', NULL, '9', '9', '9', NULL),
('615', '158', '3', NULL, '33', '3', '3', NULL),
('616', '202', '3', NULL, '1', '0', '0', NULL),
('617', '74', '3', NULL, '80', '25', '25', NULL),
('618', '189', '3', NULL, '80', '12', '2', NULL),
('619', '233', '3', NULL, '10', '5', '1', NULL),
('620', '203', '3', NULL, '3', '3', '3', NULL),
('621', '142', '3', NULL, '95', '25', '25', NULL),
('622', '204', '3', NULL, '25', '15', '10', NULL),
('623', '143', '3', NULL, '25', '15', '15', NULL),
('624', '75', '3', NULL, '25', '25', '25', NULL),
('625', '221', '3', NULL, '1', '1', '1', NULL),
('626', '129', '3', NULL, '0', '0', '0', NULL),
('627', '77', '3', NULL, '2', '2', '2', NULL),
('628', '234', '3', NULL, '10', '10', '10', NULL),
('629', '78', '3', NULL, '1', '1', '1', NULL),
('630', '130', '3', NULL, '2', '2', '2', NULL),
('631', '249', '3', NULL, '10', '8', '8', NULL),
('632', '306', '3', NULL, '20', '20', '20', NULL),
('633', '131', '3', NULL, '40', NULL, NULL, NULL),
('634', '280', '3', NULL, '12', NULL, NULL, NULL),
('635', '305', '3', NULL, '16', NULL, NULL, 'Ally'),
('636', '1', '3', '122', '60', NULL, NULL, NULL),
('637', '105', '3', '134', '240', NULL, NULL, NULL),
('638', '105', '3', '180', '240', NULL, NULL, NULL),
('639', '12', '3', '95', '20', '20', '20', NULL),
('640', '165', '3', '122', '60', NULL, NULL, NULL),
('641', '229', '3', '124', '20', NULL, NULL, NULL),
('642', '26', '3', '105', '50', NULL, NULL, NULL),
('643', '149', '3', '65', '30', NULL, NULL, NULL),
('644', '149', '3', '128', '30', NULL, NULL, NULL),
('645', '53', '3', '65', '30', NULL, NULL, NULL),
('646', '53', '3', '128', '30', NULL, NULL, NULL),
('647', '131', '3', '127', '25', NULL, NULL, NULL);

INSERT INTO "public"."deck" ("id", "title", "description", "is_public", "created", "modified", "user_id", "phoenixborn_id", "is_snapshot", "source_id", "is_preconstructed", "entity_id", "ashes_500_revision_id", "ashes_500_score", "preconstructed_release", "is_legacy") VALUES
('77', 'The Mist Guardian', 'This is the official deck for Aradel Summergaard, included with the core set.

**Suggested First Five:**

* [[Root Armor]]
* [[Shifting Mist]]
* [[Summon Mist Spirit]]
* [[Summon Blue Jaguar]]
* [[Summon Butterfly Monk]]', 'f', '2017-11-07 18:37:39+00', '2017-11-07 18:37:39+00', '61', '3', 'f', NULL, 'f', '273', NULL, NULL, NULL, 't'),
('78', 'The Iron Men', 'This is the official deck for Coal Roarkwin, included in the core set.

**Suggested First Five:**

* [[Anchornaut]]
* [[Hammer Knight]]
* [[Iron Worker]]
* [[Expand Energy]]
* [[Summon Iron Rhino]]', 'f', '2017-11-07 18:40:05+00', '2017-11-07 18:40:05+00', '61', '13', 'f', NULL, 'f', '274', NULL, NULL, NULL, 't'),
('79', 'The Bloodwoods Queen', 'This is the official deck for Jessa Na Ni, included in the core set.

**Suggested First Five:**

* [[Fear]]
* [[Living Doll]]
* [[Leech Warrior]]
* [[Blood Transfer]]
* [[Summon Blood Puppet]]', 'f', '2017-11-07 18:41:35+00', '2017-11-07 18:41:35+00', '61', '29', 'f', NULL, 'f', '275', NULL, NULL, NULL, 't'),
('80', 'The Snakes in Silver', 'This is the official deck for Maeoni Viper, included in the core set.

**Suggested First Five:**

* [[Call Upon The Realms]]
* [[Empower]]
* [[Open Memories]]
* [[Summon Gilder]]
* [[Summon Silver Snake]]', 'f', '2017-11-07 18:43:01+00', '2017-11-07 18:43:01+00', '61', '32', 'f', NULL, 'f', '276', NULL, NULL, NULL, 't'),
('81', 'The Shadows of Viros', 'This is the official deck for Noah Redmoon, included in the core set.

**Suggested First Five:**

* [[Bring Forth]]
* [[Sleight of Hand]]
* [[Small Sacrifice]]
* [[Summon Masked Wolf]]
* [[Summon False Demon]]', 'f', '2017-11-07 18:44:45+00', '2017-11-07 18:44:45+00', '61', '38', 'f', NULL, 'f', '277', NULL, NULL, NULL, 't'),
('82', 'The Cloudsea Siren', 'This is the official deck for Saria Guideman, included in the core set.

**Suggested First Five:**

* [[Abundance]]
* [[Purge]]
* [[Rose Fire Dancer]]
* [[Summon Three-Eyed Owl]]
* [[Summon Seaside Raven]]', 'f', '2017-11-07 18:46:07+00', '2017-11-07 18:46:07+00', '61', '49', 'f', NULL, 'f', '278', NULL, NULL, NULL, 't'),
('83', 'The Frostdale Giants', 'This is the official deck for Rin Northfell, available as a small-box expansion.

**Suggested First Five:**

* [[Frost Bite]]
* [[Frost Fang]]
* [[Ice Trap]]
* [[Summon Frostback Bear]]
* [[Summon Ice Golem]]', 'f', '2017-11-07 18:49:40+00', '2017-11-07 18:49:40+00', '61', '89', 'f', NULL, 'f', '279', NULL, NULL, NULL, 't'),
('84', 'The Children of Blackcloud', 'This is the official deck for Brennen Blackcloud, available as a small-box expansion.

**Suggested First Five:**

* [[Blackcloud Ninja]]
* [[Chant of the Dead]]
* [[Choke]]
* [[Fire Archer]]
* [[Summon Dread Wraith]]', 'f', '2017-11-07 18:52:07+00', '2017-11-07 18:52:07+00', '61', '95', 'f', NULL, 'f', '280', NULL, NULL, NULL, 't'),
('85', 'The Roaring Rose', 'This is the official deck for Leo Sunshadow, available as a small-box expansion.

**Suggested First Five:**

* [[Anguish]]
* [[Memory Theft]]
* [[Remorse]]
* [[Summon Nightshade Swallow]]
* [[Summon Orchid Dove]]', 'f', '2017-11-07 19:00:20+00', '2017-11-07 19:00:20+00', '61', '111', 'f', NULL, 'f', '281', NULL, NULL, NULL, 't'),
('86', 'The Duchess of Deception', 'This is the official deck for Victoria Glassfire, available as a small-box expansion.

**Suggested First Five:**

* [[Illusionary Cycle]]
* [[Secret Door]]
* [[Summon Shadow Hound]]
* [[Summon Shadow Spirit]]
* [[To Shadows]]', 'f', '2017-11-07 19:03:23+00', '2017-11-07 19:03:23+00', '61', '131', 'f', NULL, 'f', '282', NULL, NULL, NULL, 't'),
('87', 'The Song of Soaksend', 'This is the official deck for Namine Hymntide, available as a big-box expansion.

*First Five suggestion pending.*', 'f', '2017-11-07 19:06:11+00', '2017-11-07 19:06:11+00', '61', '150', 'f', NULL, 'f', '283', NULL, NULL, NULL, 't'),
('88', 'The Laws of Lions', 'This is the official deck for Odette Diamondcrest, available as a big-box expansion.

*First Five suggestion pending.*', 'f', '2017-11-07 19:07:43+00', '2017-11-07 19:07:43+00', '61', '138', 'f', NULL, 'f', '284', NULL, NULL, NULL, 't'),
('101', 'The Mist Guardian', 'This is the official deck for Aradel Summergaard, included with the core set.

**Suggested First Five:**

* [[Root Armor]]
* [[Shifting Mist]]
* [[Summon Mist Spirit]]
* [[Summon Blue Jaguar]]
* [[Summon Butterfly Monk]]', 't', '2017-11-15 04:50:16+00', '2017-11-15 04:50:16+00', '61', '3', 't', '77', 't', '294', NULL, NULL, NULL, 't'),
('102', 'The Iron Men', 'This is the official deck for Coal Roarkwin, included in the core set.

**Suggested First Five:**

* [[Anchornaut]]
* [[Hammer Knight]]
* [[Iron Worker]]
* [[Expand Energy]]
* [[Summon Iron Rhino]]', 't', '2017-11-15 04:50:27+00', '2017-11-15 04:50:27+00', '61', '13', 't', '78', 't', '295', NULL, NULL, NULL, 't'),
('103', 'The Bloodwoods Queen', 'This is the official deck for Jessa Na Ni, included in the core set.

**Suggested First Five:**

* [[Fear]]
* [[Living Doll]]
* [[Leech Warrior]]
* [[Blood Transfer]]
* [[Summon Blood Puppet]]', 't', '2017-11-15 04:50:37+00', '2017-11-15 04:50:37+00', '61', '29', 't', '79', 't', '296', NULL, NULL, NULL, 't'),
('104', 'The Snakes in Silver', 'This is the official deck for Maeoni Viper, included in the core set.

**Suggested First Five:**

* [[Call Upon The Realms]]
* [[Empower]]
* [[Open Memories]]
* [[Summon Gilder]]
* [[Summon Silver Snake]]', 't', '2017-11-15 04:50:45+00', '2017-11-15 04:50:45+00', '61', '32', 't', '80', 't', '297', NULL, NULL, NULL, 't'),
('105', 'The Shadows of Viros', 'This is the official deck for Noah Redmoon, included in the core set.

**Suggested First Five:**

* [[Bring Forth]]
* [[Sleight of Hand]]
* [[Small Sacrifice]]
* [[Summon Masked Wolf]]
* [[Summon False Demon]]', 't', '2017-11-15 04:50:53+00', '2017-11-15 04:50:53+00', '61', '38', 't', '81', 't', '298', NULL, NULL, NULL, 't'),
('106', 'The Cloudsea Siren', 'This is the official deck for Saria Guideman, included in the core set.

**Suggested First Five:**

* [[Abundance]]
* [[Purge]]
* [[Rose Fire Dancer]]
* [[Summon Three-Eyed Owl]]
* [[Summon Seaside Raven]]', 't', '2017-11-15 04:51:00+00', '2017-11-15 04:51:00+00', '61', '49', 't', '82', 't', '299', NULL, NULL, NULL, 't'),
('107', 'The Children of Blackcloud', 'This is the official deck for Brennen Blackcloud, available as a small-box expansion.

**Suggested First Five:**

* [[Blackcloud Ninja]]
* [[Chant of the Dead]]
* [[Choke]]
* [[Fire Archer]]
* [[Summon Dread Wraith]]', 't', '2017-11-15 04:51:10+00', '2017-11-15 04:51:10+00', '61', '95', 't', '84', 't', '300', NULL, NULL, '3', 't'),
('108', 'The Frostdale Giants', 'This is the official deck for Rin Northfell, available as a small-box expansion.

**Suggested First Five:**

* [[Frost Bite]]
* [[Frost Fang]]
* [[Ice Trap]]
* [[Summon Frostback Bear]]
* [[Summon Ice Golem]]', 't', '2017-11-15 04:51:18+00', '2017-11-15 04:51:18+00', '61', '89', 't', '83', 't', '301', NULL, NULL, '2', 't'),
('109', 'The Roaring Rose', 'This is the official deck for Leo Sunshadow, available as a small-box expansion.

**Suggested First Five:**

* [[Anguish]]
* [[Memory Theft]]
* [[Remorse]]
* [[Summon Nightshade Swallow]]
* [[Summon Orchid Dove]]', 't', '2017-11-15 04:51:28+00', '2017-11-15 04:51:28+00', '61', '111', 't', '85', 't', '302', NULL, NULL, '4', 't'),
('110', 'The Duchess of Deception', 'This is the official deck for Victoria Glassfire, available as a small-box expansion.

**Suggested First Five:**

* [[Illusionary Cycle]]
* [[Secret Door]]
* [[Summon Shadow Hound]]
* [[Summon Shadow Spirit]]
* [[To Shadows]]', 't', '2017-11-15 04:51:35+00', '2017-11-15 04:51:35+00', '61', '131', 't', '86', 't', '303', NULL, NULL, '5', 't'),
('111', 'The Song of Soaksend', 'This is the official deck for Namine Hymntide, available as a big-box expansion.

*First Five suggestion pending.*', 't', '2017-11-15 04:51:43+00', '2017-11-15 04:51:43+00', '61', '150', 't', '87', 't', '304', NULL, NULL, '7', 't'),
('112', 'The Laws of Lions', 'This is the official deck for Odette Diamondcrest, available as a big-box expansion.

*First Five suggestion pending.*', 't', '2017-11-15 04:51:49+00', '2017-11-15 04:51:49+00', '61', '138', 't', '88', 't', '305', NULL, NULL, '6', 't'),
('148', 'The Masters of Gravity', 'This is the official deck for Echo Greystorm, available as a small-box expansion.

*First Five suggestion pending.*', 'f', '2017-11-20 19:28:33+00', '2017-11-20 19:28:33+00', '61', '167', 'f', NULL, 'f', '341', NULL, NULL, NULL, 't'),
('149', 'The Masters of Gravity', 'This is the official deck for Echo Greystorm, available as a small-box expansion.

*First Five suggestion pending.*', 't', '2017-11-20 19:28:43+00', '2017-11-20 19:28:43+00', '61', '167', 't', '148', 't', '342', NULL, NULL, '8', 't'),
('150', 'The Path of Assassins', 'This is the official deck for Jericho Kill, available as a small-box expansion.

The dice listed are merely a suggestion; because this deck requires only [[basic]] symbols, you may use any 10 dice you prefer.

*First Five suggestion pending.*', 'f', '2017-11-20 19:32:22+00', '2017-11-20 19:32:22+00', '61', '182', 'f', NULL, 'f', '343', NULL, NULL, NULL, 't'),
('151', 'The Path of Assassins', 'This is the official deck for Jericho Kill, available as a small-box expansion.

The dice listed are merely a suggestion; because this deck requires only [[basic]] symbols, you may use any 10 dice you prefer.

*First Five suggestion pending.*', 't', '2017-11-20 19:32:27+00', '2017-11-20 19:32:27+00', '61', '182', 't', '150', 't', '344', NULL, NULL, '9', 't'),
('411', 'The Goddess of Ishra', 'This is the official deck for Astrea, available as a small-box expansion.

*First Five suggestion pending.*', 'f', '2017-12-24 05:53:43+00', '2017-12-24 05:53:43+00', '61', '191', 'f', NULL, 'f', '559', NULL, NULL, NULL, 't'),
('412', 'The Goddess of Ishra', 'This is the official deck for Astrea, available as a small-box expansion.

*First Five suggestion pending.*', 't', '2017-12-24 05:53:51+00', '2017-12-24 05:53:51+00', '61', '191', 't', '411', 't', '560', NULL, NULL, '10', 't'),
('413', 'The Boy Among Wolves', 'This is the official deck for Koji Wolfcub, available as a small-box expansion.

*First Five suggestion pending.*', 'f', '2017-12-24 05:55:22+00', '2017-12-24 05:55:22+00', '61', '214', 'f', NULL, 'f', '561', NULL, NULL, NULL, 't'),
('414', 'The Boy Among Wolves', 'This is the official deck for Koji Wolfcub, available as a small-box expansion.

*First Five suggestion pending.*', 't', '2017-12-24 05:55:28+00', '2017-12-24 05:55:28+00', '61', '214', 't', '413', 't', '562', NULL, NULL, '11', 't'),
('1967', 'The Demons of Darmas', 'This is the official deck for Harold Westraven, available as a small-box expansion.

*First Five suggestion pending.*', 'f', '2018-07-06 18:08:47+00', '2018-07-06 18:08:47+00', '61', '228', 'f', NULL, 'f', '2115', NULL, NULL, NULL, 't'),
('1968', 'The Spirits of Memoria', 'This is the official deck for Sembali Grimtongue, available as a small-box expansion.

*First Five suggestion pending.*', 'f', '2018-07-06 18:10:42+00', '2018-07-06 18:10:42+00', '61', '243', 'f', NULL, 'f', '2116', NULL, NULL, NULL, 't'),
('1969', 'The Demons of Darmas', 'This is the official deck for Harold Westraven, available as a small-box expansion.

*First Five suggestion pending.*', 't', '2018-07-06 18:10:56+00', '2018-07-06 18:10:56+00', '61', '228', 't', '1967', 't', '2117', NULL, NULL, '12', 't'),
('1970', 'The Spirits of Memoria', 'This is the official deck for Sembali Grimtongue, available as a small-box expansion.

*First Five suggestion pending.*', 't', '2018-07-06 18:11:12+00', '2018-07-06 18:11:12+00', '61', '243', 't', '1968', 't', '2118', NULL, NULL, '13', 't'),
('3025', 'The Ghost Guardian', 'This is the official deck for Rimea Careworn, available as a small-box expansion.

*First Five suggestion pending.*', 'f', '2018-10-05 18:40:16+00', '2018-10-05 18:40:16+00', '61', '260', 'f', NULL, 'f', '3530', NULL, NULL, NULL, 't'),
('3026', 'The King of Titans', 'This is the official deck for Xander Heartsblood, available as a small-box expansion.

*First Five suggestion pending.*', 'f', '2018-10-05 18:42:08+00', '2018-10-05 18:42:08+00', '61', '280', 'f', NULL, 'f', '3531', NULL, NULL, NULL, 't'),
('3027', 'The Ghost Guardian', 'This is the official deck for Rimea Careworn, available as a small-box expansion.

*First Five suggestion pending.*', 't', '2018-10-05 18:46:51+00', '2018-10-05 18:46:51+00', '61', '260', 't', '3025', 't', '3532', NULL, NULL, '14', 't'),
('3028', 'The King of Titans', 'This is the official deck for Xander Heartsblood, available as a small-box expansion.

*First Five suggestion pending.*', 't', '2018-10-05 18:46:58+00', '2018-10-05 18:46:58+00', '61', '280', 't', '3026', 't', '3533', NULL, NULL, '15', 't'),
('3927', 'The Protector of Argaia', 'This is the official deck for Fiona Mercywind, available as a small-box expansion.

*First Five suggestion pending.*', 'f', '2019-01-13 23:27:13+00', '2019-01-13 23:27:13+00', '61', '285', 'f', NULL, 'f', '4720', NULL, NULL, NULL, 't'),
('3928', 'The Grave King', 'This is the official deck for James Endersight, available as a small-box expansion.

*First Five suggestion pending.*', 'f', '2019-01-13 23:32:19+00', '2019-01-13 23:32:19+00', '61', '299', 'f', NULL, 'f', '4721', NULL, NULL, NULL, 't'),
('3929', 'The Protector of Argaia', 'This is the official deck for Fiona Mercywind, available as a small-box expansion.

*First Five suggestion pending.*', 't', '2019-01-13 23:32:52+00', '2019-01-13 23:32:52+00', '61', '285', 't', '3927', 't', '4722', NULL, NULL, '16', 't'),
('3930', 'The Grave King', 'This is the official deck for James Endersight, available as a small-box expansion.

*First Five suggestion pending.*', 't', '2019-01-13 23:33:00+00', '2019-01-13 23:33:00+00', '61', '299', 't', '3928', 't', '4723', NULL, NULL, '17', 't'),
('6164', 'The Treasures of the Ages', 'This is the starter deck for Jill Traversack, available via print-and-play from [[Project Phoenix https://ashes.live/phoenix/]].

*First Five suggestion pending.*', 'f', '2019-11-19 08:41:08+00', '2019-11-19 08:41:08+00', '61', '320', 'f', NULL, 'f', '7959', NULL, NULL, NULL, 't'),
('6165', 'The Young Ruler', 'This is the starter deck for Tolliver I, available via print-and-play from [[Project Phoenix https://ashes.live/phoenix/]].

*First Five suggestion pending.*', 'f', '2019-11-19 08:41:11+00', '2019-11-19 08:41:11+00', '61', '333', 'f', NULL, 'f', '7960', NULL, NULL, NULL, 't'),
('6166', 'The Treasures of the Ages', 'This is the starter deck for Jill Traversack, available via print-and-play from [[Project Phoenix https://ashes.live/phoenix/]].

*First Five suggestion pending.*', 't', '2019-11-19 08:41:21+00', '2019-11-19 08:41:21+00', '61', '320', 't', '6164', 't', '7961', NULL, NULL, '21', 't'),
('6167', 'The Young Ruler', 'This is the starter deck for Tolliver I, available via print-and-play from [[Project Phoenix https://ashes.live/phoenix/]].

*First Five suggestion pending.*', 't', '2019-11-19 08:41:27+00', '2019-11-19 08:41:27+00', '61', '333', 't', '6165', 't', '7962', NULL, NULL, '22', 't'),
('6318', 'The Scoundrels of the Sea', 'This is the starter deck for Devlin Longbow, available via print-and-play from [[Project Phoenix https://ashes.live/phoenix/]].

*First Five suggestion pending.*', 'f', '2020-02-02 06:36:50+00', '2020-02-02 06:36:50+00', '61', '344', 'f', NULL, 'f', '8222', NULL, NULL, NULL, 't'),
('6319', 'The Scoundrels of the Sea', 'This is the starter deck for Devlin Longbow, available via print-and-play from [[Project Phoenix https://ashes.live/phoenix/]].

*First Five suggestion pending.*', 't', '2020-02-02 06:37:01+00', '2020-02-02 06:37:01+00', '61', '344', 't', '6318', 't', '8223', NULL, NULL, '23', 't'),
('6320', 'The Mad Doctor', 'This is the starter deck for Plutarch Eastgate, available via print-and-play from [[Project Phoenix https://ashes.live/phoenix/]].

*First Five suggestion pending.*', 'f', '2020-02-02 06:38:15+00', '2020-02-02 06:38:15+00', '61', '360', 'f', NULL, 'f', '8224', NULL, NULL, NULL, 't'),
('6321', 'The Mad Doctor', 'This is the starter deck for Plutarch Eastgate, available via print-and-play from [[Project Phoenix https://ashes.live/phoenix/]].

*First Five suggestion pending.*', 't', '2020-02-02 06:38:20+00', '2020-02-02 06:38:20+00', '61', '360', 't', '6320', 't', '8225', NULL, NULL, '24', 't'),
('6322', 'The Iron Men', 'This is the official deck for [[Coal Roarkwin]], included with the Master Set.

**Suggested First Five:**

* [[Expand Energy]]
* [[Summon Iron Rhino]]
* [[Anchornaut]]
* [[Iron Worker]]
* [[Hammer Knight]]', 'f', '2021-01-08 06:02:38.020734+00', '2021-01-08 06:02:38.020753+00', '61', '414', 'f', NULL, 'f', '8226', NULL, NULL, NULL, 'f'),
('6323', 'The Mist Guardian', 'This is the official deck for [[Aradel Summergaard]], included with the Master Set.

**Suggested First Five:**

* [[Shifting Mist]]
* [[Summon Mist Spirit]]
* [[Summon Blue Jaguar]]
* [[Root Armor]]
* [[Summon Butterfly Monk]]', 'f', '2021-01-08 06:02:55.047556+00', '2021-01-08 06:02:55.04758+00', '61', '374', 'f', NULL, 'f', '8227', NULL, NULL, NULL, 'f'),
('6324', 'The Cloudsea Siren', 'This is the official deck for [[Saria Guideman]], included with the Master Set.

**Suggested First Five:**

* [[Purge]]
* [[Abundance]]
* [[Summon Three-Eyed Owl]]
* [[Summon Seaside Raven]]
* [[Rose Fire Dancer]]', 'f', '2021-01-08 06:03:05.545441+00', '2021-01-08 06:03:05.545466+00', '61', '388', 'f', NULL, 'f', '8228', NULL, NULL, NULL, 'f'),
('6325', 'The Snakes in Silver', 'This is the official deck for [[Maeoni Viper]], included with the Master Set.

**Suggested First Five:**

* [[Call Upon the Realms]]
* [[Summon Silver Snake]]
* [[Empower]]
* [[Open Memories]]
* [[Summon Gilder]]', 'f', '2021-01-08 06:03:14.936495+00', '2021-01-08 06:03:14.936511+00', '61', '401', 'f', NULL, 'f', '8229', NULL, NULL, NULL, 'f'),
('6326', 'The Bloodwoods Queen', 'This is the official deck for [[Jessa Na Ni]], included with the Master Set.

**Suggested First Five:**

* [[Fear]]
* [[Blood Transfer]]
* [[Summon Blood Puppet]]
* [[Living Doll]]
* [[Blood Shaman]]', 'f', '2021-01-08 06:03:24.774987+00', '2021-01-08 06:03:24.775003+00', '61', '362', 'f', NULL, 'f', '8230', NULL, NULL, NULL, 'f'),
('6327', 'The Shadows of Viros', 'This is the official deck for [[Noah Redmoon]], included with the Master Set.

**Suggested First Five:**

* [[Small Sacrifice]]
* [[Summon Masked Wolf]]
* [[Summon False Demon]]
* [[Sleight of Hand]]
* [[Resummon]]', 'f', '2021-01-08 06:03:39.516492+00', '2021-01-08 06:03:39.516508+00', '61', '426', 'f', NULL, 'f', '8231', NULL, NULL, NULL, 'f'),
('6356', 'The Iron Men', 'This is the official deck for [[Coal Roarkwin]], included with the Master Set.

**Suggested First Five:**

* [[Expand Energy]]
* [[Summon Iron Rhino]]
* [[Anchornaut]]
* [[Iron Worker]]
* [[Hammer Knight]]', 't', '2021-01-08 06:02:38.020734+00', '2021-01-08 06:02:38.020753+00', '61', '414', 't', '6322', 't', '8260', NULL, NULL, NULL, 'f'),
('6357', 'The Mist Guardian', 'This is the official deck for [[Aradel Summergaard]], included with the Master Set.

**Suggested First Five:**

* [[Shifting Mist]]
* [[Summon Mist Spirit]]
* [[Summon Blue Jaguar]]
* [[Root Armor]]
* [[Summon Butterfly Monk]]', 't', '2021-01-08 06:02:55.047556+00', '2021-01-08 06:02:55.04758+00', '61', '374', 't', '6323', 't', '8261', NULL, NULL, NULL, 'f'),
('6358', 'The Cloudsea Siren', 'This is the official deck for [[Saria Guideman]], included with the Master Set.

**Suggested First Five:**

* [[Purge]]
* [[Abundance]]
* [[Summon Three-Eyed Owl]]
* [[Summon Seaside Raven]]
* [[Rose Fire Dancer]]', 't', '2021-01-08 06:03:05.545441+00', '2021-01-08 06:03:05.545466+00', '61', '388', 't', '6324', 't', '8262', NULL, NULL, NULL, 'f'),
('6359', 'The Snakes in Silver', 'This is the official deck for [[Maeoni Viper]], included with the Master Set.

**Suggested First Five:**

* [[Call Upon the Realms]]
* [[Summon Silver Snake]]
* [[Empower]]
* [[Open Memories]]
* [[Summon Gilder]]', 't', '2021-01-08 06:03:14.936495+00', '2021-01-08 06:03:14.936511+00', '61', '401', 't', '6325', 't', '8263', NULL, NULL, NULL, 'f'),
('6360', 'The Bloodwoods Queen', 'This is the official deck for [[Jessa Na Ni]], included with the Master Set.

**Suggested First Five:**

* [[Fear]]
* [[Blood Transfer]]
* [[Summon Blood Puppet]]
* [[Living Doll]]
* [[Blood Shaman]]', 't', '2021-01-08 06:03:24.774987+00', '2021-01-08 06:03:24.775003+00', '61', '362', 't', '6326', 't', '8264', NULL, NULL, NULL, 'f'),
('6361', 'The Shadows of Viros', 'This is the official deck for [[Noah Redmoon]], included with the Master Set.

**Suggested First Five:**

* [[Small Sacrifice]]
* [[Summon Masked Wolf]]
* [[Summon False Demon]]
* [[Sleight of Hand]]
* [[Resummon]]', 't', '2021-01-08 06:03:39.516492+00', '2021-01-08 06:03:39.516508+00', '61', '426', 't', '6327', 't', '8265', NULL, NULL, NULL, 'f');

INSERT INTO "public"."deck_card" ("deck_id", "card_id", "count") VALUES
('77', '34', '3'),
('77', '36', '3'),
('77', '41', '3'),
('77', '45', '3'),
('77', '47', '3'),
('77', '53', '3'),
('77', '59', '3'),
('77', '64', '3'),
('77', '65', '3'),
('77', '70', '3'),
('78', '2', '3'),
('78', '12', '3'),
('78', '17', '3'),
('78', '24', '3'),
('78', '28', '3'),
('78', '39', '3'),
('78', '42', '3'),
('78', '58', '3'),
('78', '62', '3'),
('78', '68', '3'),
('79', '4', '3'),
('79', '6', '3'),
('79', '14', '3'),
('79', '20', '3'),
('79', '21', '3'),
('79', '30', '3'),
('79', '31', '3'),
('79', '44', '3'),
('79', '63', '3'),
('79', '78', '3'),
('80', '11', '3'),
('80', '15', '3'),
('80', '23', '3'),
('80', '26', '3'),
('80', '37', '3'),
('80', '40', '3'),
('80', '46', '3'),
('80', '67', '3'),
('80', '72', '3'),
('80', '77', '3'),
('81', '8', '3'),
('81', '9', '3'),
('81', '18', '3'),
('81', '52', '3'),
('81', '56', '3'),
('81', '57', '3'),
('81', '60', '3'),
('81', '66', '3'),
('81', '69', '3'),
('81', '73', '3'),
('82', '1', '3'),
('82', '16', '3'),
('82', '25', '3'),
('82', '43', '3'),
('82', '48', '3'),
('82', '50', '3'),
('82', '61', '3'),
('82', '71', '3'),
('82', '74', '3'),
('82', '75', '3'),
('83', '79', '3'),
('83', '80', '3'),
('83', '81', '3'),
('83', '83', '3'),
('83', '84', '3'),
('83', '85', '3'),
('83', '88', '3'),
('83', '90', '3'),
('83', '91', '3'),
('83', '92', '3'),
('84', '93', '3'),
('84', '94', '3'),
('84', '96', '3'),
('84', '97', '3'),
('84', '98', '3'),
('84', '99', '3'),
('84', '101', '3'),
('84', '102', '3'),
('84', '103', '3'),
('84', '104', '3'),
('85', '105', '3'),
('85', '106', '3'),
('85', '107', '3'),
('85', '108', '3'),
('85', '109', '3'),
('85', '112', '3'),
('85', '113', '3'),
('85', '116', '3'),
('85', '117', '3'),
('85', '118', '3'),
('86', '119', '3'),
('86', '120', '3'),
('86', '121', '3'),
('86', '122', '3'),
('86', '123', '3'),
('86', '124', '3'),
('86', '127', '3'),
('86', '128', '3'),
('86', '129', '3'),
('86', '130', '3'),
('87', '145', '3'),
('87', '146', '3'),
('87', '147', '3'),
('87', '148', '3'),
('87', '149', '3'),
('87', '151', '3'),
('87', '154', '3'),
('87', '156', '3'),
('87', '157', '3'),
('87', '158', '3'),
('88', '133', '3'),
('88', '134', '3'),
('88', '135', '3'),
('88', '136', '3'),
('88', '137', '3'),
('88', '139', '3'),
('88', '140', '3'),
('88', '141', '3'),
('88', '142', '3'),
('88', '143', '3'),
('101', '34', '3'),
('101', '36', '3'),
('101', '41', '3'),
('101', '45', '3'),
('101', '47', '3'),
('101', '53', '3'),
('101', '59', '3'),
('101', '64', '3'),
('101', '65', '3'),
('101', '70', '3'),
('102', '2', '3'),
('102', '12', '3'),
('102', '17', '3'),
('102', '24', '3'),
('102', '28', '3'),
('102', '39', '3'),
('102', '42', '3'),
('102', '58', '3'),
('102', '62', '3'),
('102', '68', '3'),
('103', '4', '3'),
('103', '6', '3'),
('103', '14', '3'),
('103', '20', '3'),
('103', '21', '3'),
('103', '30', '3'),
('103', '31', '3'),
('103', '44', '3'),
('103', '63', '3'),
('103', '78', '3'),
('104', '11', '3'),
('104', '15', '3'),
('104', '23', '3'),
('104', '26', '3'),
('104', '37', '3'),
('104', '40', '3'),
('104', '46', '3'),
('104', '67', '3'),
('104', '72', '3'),
('104', '77', '3'),
('105', '8', '3'),
('105', '9', '3'),
('105', '18', '3'),
('105', '52', '3'),
('105', '56', '3'),
('105', '57', '3'),
('105', '60', '3'),
('105', '66', '3'),
('105', '69', '3'),
('105', '73', '3'),
('106', '1', '3'),
('106', '16', '3'),
('106', '25', '3'),
('106', '43', '3'),
('106', '48', '3'),
('106', '50', '3'),
('106', '61', '3'),
('106', '71', '3'),
('106', '74', '3'),
('106', '75', '3'),
('107', '93', '3'),
('107', '94', '3'),
('107', '96', '3'),
('107', '97', '3'),
('107', '98', '3'),
('107', '99', '3'),
('107', '101', '3'),
('107', '102', '3'),
('107', '103', '3'),
('107', '104', '3'),
('108', '79', '3'),
('108', '80', '3'),
('108', '81', '3'),
('108', '83', '3'),
('108', '84', '3'),
('108', '85', '3'),
('108', '88', '3'),
('108', '90', '3'),
('108', '91', '3'),
('108', '92', '3'),
('109', '105', '3'),
('109', '106', '3'),
('109', '107', '3'),
('109', '108', '3'),
('109', '109', '3'),
('109', '112', '3'),
('109', '113', '3'),
('109', '116', '3'),
('109', '117', '3'),
('109', '118', '3'),
('110', '119', '3'),
('110', '120', '3'),
('110', '121', '3'),
('110', '122', '3'),
('110', '123', '3'),
('110', '124', '3'),
('110', '127', '3'),
('110', '128', '3'),
('110', '129', '3'),
('110', '130', '3'),
('111', '145', '3'),
('111', '146', '3'),
('111', '147', '3'),
('111', '148', '3'),
('111', '149', '3'),
('111', '151', '3'),
('111', '154', '3'),
('111', '156', '3'),
('111', '157', '3'),
('111', '158', '3'),
('112', '133', '3'),
('112', '134', '3'),
('112', '135', '3'),
('112', '136', '3'),
('112', '137', '3'),
('112', '139', '3'),
('112', '140', '3'),
('112', '141', '3'),
('112', '142', '3'),
('112', '143', '3'),
('148', '165', '3'),
('148', '166', '3'),
('148', '169', '3'),
('148', '170', '3'),
('148', '171', '3'),
('148', '172', '3'),
('148', '173', '3'),
('148', '175', '3'),
('148', '176', '3'),
('148', '177', '3'),
('149', '165', '3'),
('149', '166', '3'),
('149', '169', '3'),
('149', '170', '3'),
('149', '171', '3'),
('149', '172', '3'),
('149', '173', '3'),
('149', '175', '3'),
('149', '176', '3'),
('149', '177', '3'),
('150', '178', '3'),
('150', '179', '3'),
('150', '180', '3'),
('150', '181', '3'),
('150', '184', '3'),
('150', '185', '3'),
('150', '186', '3'),
('150', '187', '3'),
('150', '188', '3'),
('150', '189', '3'),
('151', '178', '3'),
('151', '179', '3'),
('151', '180', '3'),
('151', '181', '3'),
('151', '184', '3'),
('151', '185', '3'),
('151', '186', '3'),
('151', '187', '3'),
('151', '188', '3'),
('151', '189', '3'),
('411', '192', '3'),
('411', '193', '3'),
('411', '194', '3'),
('411', '196', '3'),
('411', '198', '3'),
('411', '199', '3'),
('411', '201', '3'),
('411', '202', '3'),
('411', '203', '3'),
('411', '204', '3'),
('412', '192', '3'),
('412', '193', '3'),
('412', '194', '3'),
('412', '196', '3'),
('412', '198', '3'),
('412', '199', '3'),
('412', '201', '3'),
('412', '202', '3'),
('412', '203', '3'),
('412', '204', '3'),
('413', '208', '3'),
('413', '209', '3'),
('413', '211', '3'),
('413', '212', '3'),
('413', '213', '3'),
('413', '216', '3'),
('413', '218', '3'),
('413', '219', '3'),
('413', '220', '3'),
('413', '221', '3'),
('414', '208', '3'),
('414', '209', '3'),
('414', '211', '3'),
('414', '212', '3'),
('414', '213', '3'),
('414', '216', '3'),
('414', '218', '3'),
('414', '219', '3'),
('414', '220', '3'),
('414', '221', '3'),
('1967', '222', '3'),
('1967', '223', '3'),
('1967', '224', '3'),
('1967', '225', '3'),
('1967', '227', '3'),
('1967', '229', '3'),
('1967', '231', '3'),
('1967', '232', '3'),
('1967', '233', '3'),
('1967', '234', '3'),
('1968', '237', '3'),
('1968', '239', '3'),
('1968', '240', '3'),
('1968', '241', '3'),
('1968', '242', '3'),
('1968', '244', '3'),
('1968', '245', '3'),
('1968', '247', '3'),
('1968', '248', '3'),
('1968', '249', '3'),
('1969', '222', '3'),
('1969', '223', '3'),
('1969', '224', '3'),
('1969', '225', '3'),
('1969', '227', '3'),
('1969', '229', '3'),
('1969', '231', '3'),
('1969', '232', '3'),
('1969', '233', '3'),
('1969', '234', '3'),
('1970', '237', '3'),
('1970', '239', '3'),
('1970', '240', '3'),
('1970', '241', '3'),
('1970', '242', '3'),
('1970', '244', '3'),
('1970', '245', '3'),
('1970', '247', '3'),
('1970', '248', '3'),
('1970', '249', '3'),
('3025', '251', '3'),
('3025', '252', '3'),
('3025', '253', '3'),
('3025', '254', '3'),
('3025', '255', '3'),
('3025', '256', '3'),
('3025', '259', '3'),
('3025', '261', '3'),
('3025', '263', '3'),
('3025', '264', '3'),
('3026', '267', '3'),
('3026', '268', '3'),
('3026', '269', '3'),
('3026', '270', '3'),
('3026', '271', '3'),
('3026', '273', '3'),
('3026', '274', '3'),
('3026', '277', '3'),
('3026', '278', '3'),
('3026', '279', '3'),
('3027', '251', '3'),
('3027', '252', '3'),
('3027', '253', '3'),
('3027', '254', '3'),
('3027', '255', '3'),
('3027', '256', '3'),
('3027', '259', '3'),
('3027', '261', '3'),
('3027', '263', '3'),
('3027', '264', '3'),
('3028', '267', '3'),
('3028', '268', '3'),
('3028', '269', '3'),
('3028', '270', '3'),
('3028', '271', '3'),
('3028', '273', '3'),
('3028', '274', '3'),
('3028', '277', '3'),
('3028', '278', '3'),
('3028', '279', '3'),
('3927', '281', '3'),
('3927', '282', '3'),
('3927', '283', '3'),
('3927', '284', '3'),
('3927', '288', '3'),
('3927', '289', '3'),
('3927', '291', '3'),
('3927', '292', '3'),
('3927', '293', '3'),
('3927', '294', '3'),
('3928', '295', '3'),
('3928', '297', '3'),
('3928', '298', '3'),
('3928', '300', '3'),
('3928', '301', '3'),
('3928', '302', '3'),
('3928', '303', '3'),
('3928', '304', '3'),
('3928', '305', '3'),
('3928', '306', '3'),
('3929', '281', '3'),
('3929', '282', '3'),
('3929', '283', '3'),
('3929', '284', '3'),
('3929', '288', '3'),
('3929', '289', '3'),
('3929', '291', '3'),
('3929', '292', '3'),
('3929', '293', '3'),
('3929', '294', '3'),
('3930', '295', '3'),
('3930', '297', '3'),
('3930', '298', '3'),
('3930', '300', '3'),
('3930', '301', '3'),
('3930', '302', '3'),
('3930', '303', '3'),
('3930', '304', '3'),
('3930', '305', '3'),
('3930', '306', '3'),
('6164', '307', '3'),
('6164', '308', '3'),
('6164', '309', '3'),
('6164', '310', '3'),
('6164', '311', '3'),
('6164', '312', '3'),
('6164', '313', '3'),
('6164', '314', '3'),
('6164', '315', '3'),
('6164', '316', '3'),
('6165', '321', '3'),
('6165', '322', '3'),
('6165', '323', '3'),
('6165', '324', '3'),
('6165', '325', '3'),
('6165', '326', '3'),
('6165', '327', '3'),
('6165', '328', '3'),
('6165', '329', '3'),
('6165', '330', '3'),
('6166', '307', '3'),
('6166', '308', '3'),
('6166', '309', '3'),
('6166', '310', '3'),
('6166', '311', '3'),
('6166', '312', '3'),
('6166', '313', '3'),
('6166', '314', '3'),
('6166', '315', '3'),
('6166', '316', '3'),
('6167', '321', '3'),
('6167', '322', '3'),
('6167', '323', '3'),
('6167', '324', '3'),
('6167', '325', '3'),
('6167', '326', '3'),
('6167', '327', '3'),
('6167', '328', '3'),
('6167', '329', '3'),
('6167', '330', '3'),
('6318', '334', '3'),
('6318', '335', '3'),
('6318', '336', '3'),
('6318', '337', '3'),
('6318', '338', '3'),
('6318', '339', '3'),
('6318', '340', '3'),
('6318', '341', '3'),
('6318', '342', '3'),
('6318', '343', '3'),
('6319', '334', '3'),
('6319', '335', '3'),
('6319', '336', '3'),
('6319', '337', '3'),
('6319', '338', '3'),
('6319', '339', '3'),
('6319', '340', '3'),
('6319', '341', '3'),
('6319', '342', '3'),
('6319', '343', '3');

INSERT INTO "public"."deck_card" ("deck_id", "card_id", "count") VALUES
('6320', '347', '3'),
('6320', '348', '3'),
('6320', '349', '3'),
('6320', '350', '3'),
('6320', '351', '3'),
('6320', '352', '3'),
('6320', '353', '3'),
('6320', '354', '3'),
('6320', '355', '3'),
('6320', '356', '3'),
('6321', '347', '3'),
('6321', '348', '3'),
('6321', '349', '3'),
('6321', '350', '3'),
('6321', '351', '3'),
('6321', '352', '3'),
('6321', '353', '3'),
('6321', '354', '3'),
('6321', '355', '3'),
('6321', '356', '3'),
('6322', '415', '3'),
('6322', '416', '3'),
('6322', '417', '3'),
('6322', '418', '3'),
('6322', '419', '3'),
('6322', '421', '3'),
('6322', '422', '3'),
('6322', '423', '3'),
('6322', '424', '3'),
('6322', '425', '3'),
('6323', '376', '3'),
('6323', '378', '3'),
('6323', '380', '3'),
('6323', '381', '3'),
('6323', '382', '3'),
('6323', '383', '3'),
('6323', '384', '3'),
('6323', '385', '3'),
('6323', '386', '3'),
('6323', '387', '3'),
('6324', '390', '3'),
('6324', '392', '3'),
('6324', '393', '3'),
('6324', '394', '3'),
('6324', '395', '3'),
('6324', '396', '3'),
('6324', '397', '3'),
('6324', '398', '3'),
('6324', '399', '3'),
('6324', '400', '3'),
('6325', '403', '3'),
('6325', '405', '3'),
('6325', '406', '3'),
('6325', '407', '3'),
('6325', '408', '3'),
('6325', '409', '3'),
('6325', '410', '3'),
('6325', '411', '3'),
('6325', '412', '3'),
('6325', '413', '3'),
('6326', '363', '3'),
('6326', '365', '3'),
('6326', '366', '3'),
('6326', '367', '3'),
('6326', '368', '3'),
('6326', '369', '3'),
('6326', '370', '3'),
('6326', '371', '3'),
('6326', '372', '3'),
('6326', '373', '3'),
('6327', '428', '3'),
('6327', '430', '3'),
('6327', '431', '3'),
('6327', '432', '3'),
('6327', '434', '3'),
('6327', '435', '3'),
('6327', '436', '3'),
('6327', '437', '3'),
('6327', '438', '3'),
('6327', '439', '3'),
('6356', '415', '3'),
('6356', '416', '3'),
('6356', '417', '3'),
('6356', '418', '3'),
('6356', '419', '3'),
('6356', '421', '3'),
('6356', '422', '3'),
('6356', '423', '3'),
('6356', '424', '3'),
('6356', '425', '3'),
('6357', '376', '3'),
('6357', '378', '3'),
('6357', '380', '3'),
('6357', '381', '3'),
('6357', '382', '3'),
('6357', '383', '3'),
('6357', '384', '3'),
('6357', '385', '3'),
('6357', '386', '3'),
('6357', '387', '3'),
('6358', '390', '3'),
('6358', '392', '3'),
('6358', '393', '3'),
('6358', '394', '3'),
('6358', '395', '3'),
('6358', '396', '3'),
('6358', '397', '3'),
('6358', '398', '3'),
('6358', '399', '3'),
('6358', '400', '3'),
('6359', '403', '3'),
('6359', '405', '3'),
('6359', '406', '3'),
('6359', '407', '3'),
('6359', '408', '3'),
('6359', '409', '3'),
('6359', '410', '3'),
('6359', '411', '3'),
('6359', '412', '3'),
('6359', '413', '3'),
('6360', '363', '3'),
('6360', '365', '3'),
('6360', '366', '3'),
('6360', '367', '3'),
('6360', '368', '3'),
('6360', '369', '3'),
('6360', '370', '3'),
('6360', '371', '3'),
('6360', '372', '3'),
('6360', '373', '3'),
('6361', '428', '3'),
('6361', '430', '3'),
('6361', '431', '3'),
('6361', '432', '3'),
('6361', '434', '3'),
('6361', '435', '3'),
('6361', '436', '3'),
('6361', '437', '3'),
('6361', '438', '3'),
('6361', '439', '3');

INSERT INTO "public"."deck_die" ("deck_id", "die_flag", "count") VALUES
('77', '4', '5'),
('77', '8', '5'),
('78', '1', '5'),
('78', '8', '5'),
('79', '1', '5'),
('79', '2', '5'),
('80', '2', '5'),
('80', '8', '5'),
('81', '1', '5'),
('81', '4', '5'),
('82', '2', '5'),
('82', '4', '5'),
('83', '8', '10'),
('84', '1', '10'),
('85', '2', '10'),
('86', '4', '10'),
('87', '32', '10'),
('88', '16', '10'),
('101', '4', '5'),
('101', '8', '5'),
('102', '1', '5'),
('102', '8', '5'),
('103', '1', '5'),
('103', '2', '5'),
('104', '2', '5'),
('104', '8', '5'),
('105', '1', '5'),
('105', '4', '5'),
('106', '2', '5'),
('106', '4', '5'),
('107', '1', '10'),
('108', '8', '10'),
('109', '2', '10'),
('110', '4', '10'),
('111', '32', '10'),
('112', '16', '10'),
('148', '16', '5'),
('148', '32', '5'),
('149', '16', '5'),
('149', '32', '5'),
('150', '1', '3'),
('150', '2', '2'),
('150', '4', '2'),
('150', '8', '3'),
('151', '1', '3'),
('151', '2', '2'),
('151', '4', '2'),
('151', '8', '3'),
('411', '2', '5'),
('411', '16', '5'),
('412', '2', '5'),
('412', '16', '5'),
('413', '8', '5'),
('413', '32', '5'),
('414', '8', '5'),
('414', '32', '5'),
('1967', '1', '5'),
('1967', '32', '5'),
('1968', '4', '5'),
('1968', '16', '5'),
('1969', '1', '5'),
('1969', '32', '5'),
('1970', '4', '5'),
('1970', '16', '5'),
('3025', '4', '5'),
('3025', '32', '5'),
('3026', '8', '5'),
('3026', '16', '5'),
('3027', '4', '5'),
('3027', '32', '5'),
('3028', '8', '5'),
('3028', '16', '5'),
('3927', '2', '5'),
('3927', '32', '5'),
('3928', '1', '5'),
('3928', '16', '5'),
('3929', '2', '5'),
('3929', '32', '5'),
('3930', '1', '5'),
('3930', '16', '5'),
('6164', '64', '10'),
('6165', '2', '5'),
('6165', '64', '5'),
('6166', '64', '10'),
('6167', '2', '5'),
('6167', '64', '5'),
('6318', '8', '5'),
('6318', '64', '5'),
('6319', '8', '5'),
('6319', '64', '5'),
('6320', '1', '5'),
('6320', '64', '5'),
('6321', '1', '5'),
('6321', '64', '5'),
('6322', '1', '5'),
('6322', '8', '5'),
('6323', '4', '5'),
('6323', '8', '5'),
('6324', '2', '5'),
('6324', '4', '5'),
('6325', '2', '5'),
('6325', '8', '5'),
('6326', '1', '5'),
('6326', '2', '5'),
('6327', '1', '5'),
('6327', '4', '5'),
('6356', '1', '5'),
('6356', '8', '5'),
('6357', '4', '5'),
('6357', '8', '5'),
('6358', '2', '5'),
('6358', '4', '5'),
('6359', '2', '5'),
('6359', '8', '5'),
('6360', '1', '5'),
('6360', '2', '5'),
('6361', '1', '5'),
('6361', '4', '5');

INSERT INTO "public"."section" ("id", "entity_id", "title", "stub", "description", "is_restricted") VALUES
('1', '1605', 'Site News', 'news', 'Ever wondered about the minutiae of every update to Ashes.live? Wonder no longer!', 't'),
('2', '1606', 'General', 'general', 'General discussion about Ashes; if it doesn''t fit elsewhere, post it here!', 'f'),
('3', '1607', 'Rules', 'rules', 'Have a rules question or clarification about Ashes? Post it here!

* [[Official Ashes Rules https://ashes.live/files/ashes-core-rules.pdf]] (PDF)
* [[Official Ashes FAQ https://ashes.live/files/ashes-official-faq.pdf]] (PDF)
* [[Ashes Rules Reference ashes.live/files/ashes-rules-reference.pdf]] (PDF)
* [[Raven Rules ashes.live/files/ashes-raven-rules.pdf]] (PDF)', 'f'),
('4', '1608', 'Strategy', 'strategy', 'Have or need advice on demolishing your opponents? You''ve come to the right place!', 'f'),
('5', '6802', 'Project Phoenix', 'phoenix', '[[Project Phoenix ashes.live/phoenix/]] is a collaboration of Ashes fans working together to continue development on this wonderful game.', 'f');

INSERT INTO "public"."streamable" ("entity_id") VALUES
('1'),
('2'),
('3'),
('4'),
('5'),
('6'),
('7'),
('8'),
('9'),
('10'),
('11'),
('12'),
('13'),
('14'),
('15'),
('16'),
('17'),
('18'),
('19'),
('20'),
('21'),
('22'),
('23'),
('24'),
('25'),
('26'),
('27'),
('28'),
('29'),
('30'),
('31'),
('32'),
('33'),
('34'),
('35'),
('36'),
('37'),
('38'),
('39'),
('40'),
('41'),
('42'),
('43'),
('44'),
('45'),
('46'),
('47'),
('48'),
('49'),
('50'),
('51'),
('52'),
('53'),
('54'),
('55'),
('56'),
('57'),
('58'),
('59'),
('60'),
('61'),
('62'),
('63'),
('64'),
('65'),
('66'),
('67'),
('68'),
('69'),
('70'),
('71'),
('72'),
('73'),
('74'),
('75'),
('76'),
('77'),
('78'),
('79'),
('80'),
('81'),
('82'),
('83'),
('84'),
('85'),
('86'),
('87'),
('88'),
('89'),
('90'),
('91'),
('92'),
('93'),
('94'),
('95'),
('96'),
('97'),
('98'),
('99'),
('100'),
('101'),
('102'),
('103'),
('104'),
('105'),
('106'),
('107'),
('108'),
('109'),
('110'),
('111'),
('112'),
('113'),
('114'),
('115'),
('116'),
('117'),
('118'),
('119'),
('120'),
('121'),
('122'),
('123'),
('124'),
('125'),
('126'),
('127'),
('128'),
('129'),
('130'),
('131'),
('132'),
('133'),
('134'),
('135'),
('136'),
('137'),
('138'),
('139'),
('140'),
('141'),
('142'),
('143'),
('144'),
('145'),
('146'),
('147'),
('148'),
('149'),
('150'),
('151'),
('152'),
('153'),
('154'),
('155'),
('156'),
('157'),
('158'),
('159'),
('160'),
('161'),
('162'),
('163'),
('164'),
('165'),
('166'),
('167'),
('168'),
('169'),
('170'),
('171'),
('172'),
('173'),
('174'),
('175'),
('176'),
('177'),
('178'),
('179'),
('180'),
('181'),
('182'),
('183'),
('184'),
('185'),
('186'),
('187'),
('188'),
('189'),
('190'),
('191'),
('192'),
('193'),
('194'),
('195'),
('196'),
('197'),
('198'),
('199'),
('200'),
('201'),
('202'),
('203'),
('204'),
('205'),
('206'),
('207'),
('208'),
('209'),
('210'),
('211'),
('212'),
('213'),
('214'),
('215'),
('216'),
('217'),
('218'),
('219'),
('220'),
('221'),
('273'),
('274'),
('275'),
('276'),
('277'),
('278'),
('279'),
('280'),
('281'),
('282'),
('283'),
('284'),
('294'),
('295'),
('296'),
('297'),
('298'),
('299'),
('300'),
('301'),
('302'),
('303'),
('304'),
('305'),
('341'),
('342'),
('343'),
('344'),
('559'),
('560'),
('561'),
('562'),
('2087'),
('2088'),
('2089'),
('2090'),
('2091'),
('2092'),
('2093'),
('2094'),
('2095'),
('2096'),
('2097'),
('2098'),
('2099'),
('2100'),
('2101'),
('2102'),
('2103'),
('2104'),
('2105'),
('2106'),
('2107'),
('2108'),
('2109'),
('2110'),
('2111'),
('2112'),
('2113'),
('2114'),
('2115'),
('2116'),
('2117'),
('2118'),
('3499'),
('3500'),
('3501'),
('3502'),
('3503'),
('3504'),
('3505'),
('3506'),
('3507'),
('3508'),
('3509'),
('3510'),
('3511'),
('3512'),
('3513'),
('3514'),
('3515'),
('3516'),
('3517'),
('3518'),
('3519'),
('3520'),
('3521'),
('3522'),
('3523'),
('3524'),
('3525'),
('3526'),
('3527'),
('3528'),
('3529'),
('3530'),
('3531'),
('3532'),
('3533'),
('4694'),
('4695'),
('4696'),
('4697'),
('4698'),
('4699'),
('4700'),
('4701'),
('4702'),
('4703'),
('4704'),
('4705'),
('4706'),
('4707'),
('4708'),
('4709'),
('4710'),
('4711'),
('4712'),
('4713'),
('4714'),
('4715'),
('4716'),
('4717'),
('4718'),
('4719'),
('4720'),
('4721'),
('4722'),
('4723'),
('7932'),
('7933'),
('7934'),
('7935'),
('7936'),
('7937'),
('7938'),
('7939'),
('7940'),
('7941'),
('7942'),
('7943'),
('7944'),
('7945'),
('7946'),
('7947'),
('7948'),
('7949'),
('7950'),
('7951'),
('7952'),
('7953'),
('7954'),
('7955'),
('7956'),
('7957'),
('7958'),
('7959'),
('7960'),
('7961'),
('7962'),
('8194'),
('8195'),
('8196'),
('8197'),
('8198'),
('8199'),
('8200'),
('8201'),
('8202'),
('8203'),
('8204'),
('8205'),
('8206'),
('8207'),
('8208'),
('8209'),
('8210'),
('8211'),
('8212'),
('8213'),
('8214'),
('8215'),
('8216'),
('8217'),
('8218'),
('8219'),
('8220'),
('8221'),
('8222'),
('8223'),
('8224'),
('8225'),
('8226'),
('8227'),
('8228'),
('8229'),
('8230'),
('8231'),
('8260'),
('8261'),
('8262'),
('8263'),
('8264'),
('8265'),
('9947'),
('9948'),
('9949'),
('9950'),
('9951'),
('9952'),
('9953'),
('9954'),
('9955'),
('9956'),
('9957'),
('9958'),
('9959'),
('9960'),
('9961'),
('9962'),
('9963'),
('9964'),
('9965'),
('9966'),
('9967'),
('9968'),
('9969'),
('9970'),
('9971'),
('9972'),
('9973'),
('9974'),
('9975'),
('9976'),
('9977'),
('9978'),
('9979'),
('9980'),
('9981'),
('9982'),
('9983'),
('9984'),
('9985'),
('9986'),
('9987'),
('9988'),
('9989'),
('9990'),
('9991'),
('9992'),
('9993'),
('9994'),
('9995'),
('9996'),
('9997'),
('9998'),
('9999'),
('10000'),
('10001'),
('10002'),
('10003'),
('10004'),
('10005'),
('10006'),
('10007'),
('10008'),
('10009'),
('10010'),
('10011'),
('10012'),
('10013'),
('10014'),
('10015'),
('10016'),
('10017'),
('10018'),
('10019'),
('10020'),
('10021'),
('10022'),
('10023'),
('10024'),
('10025'),
('10026'),
('10027'),
('10028'),
('10029'),
('10030'),
('10031'),
('10032'),
('10033'),
('10034'),
('10035'),
('10036'),
('10037'),
('10038'),
('10039'),
('10040'),
('10041'),
('10042'),
('10043'),
('10044'),
('10045'),
('10046'),
('10047'),
('10048'),
('10049'),
('10050'),
('10051'),
('10052'),
('10053'),
('10054'),
('10055'),
('10056'),
('10057'),
('10058'),
('10059'),
('10060'),
('10061'),
('10062'),
('10063'),
('10064'),
('10065'),
('10066'),
('10067'),
('10068'),
('10069'),
('10070'),
('10071'),
('10072'),
('10073'),
('10074'),
('10075'),
('10076'),
('10077'),
('10078'),
('10079'),
('10080'),
('10081'),
('10082'),
('10083'),
('10084'),
('10085'),
('10086'),
('10087'),
('10088'),
('10089'),
('10090'),
('10091'),
('10092'),
('10093'),
('10094'),
('10095'),
('10096'),
('10097'),
('10098'),
('10099'),
('10100'),
('10101'),
('10102'),
('10103'),
('10104'),
('10105'),
('10106'),
('10107'),
('10108'),
('10109'),
('10110'),
('10111'),
('10112'),
('10113'),
('10114'),
('10115'),
('10116'),
('10117'),
('10118'),
('10119'),
('10120'),
('10121'),
('10122'),
('10123'),
('10124'),
('10125'),
('10126'),
('10127'),
('10128'),
('10129'),
('10130'),
('10131'),
('10132'),
('10133'),
('10134'),
('10135'),
('10136'),
('10137'),
('10138'),
('10139'),
('10140'),
('10141'),
('10142'),
('10143'),
('10144'),
('10145'),
('10146'),
('10147'),
('10148'),
('10149'),
('10150'),
('10151'),
('10152'),
('10153'),
('10154'),
('10155'),
('10156'),
('10157'),
('10158'),
('10159'),
('10160'),
('10161'),
('10162'),
('10163'),
('10164'),
('10165'),
('10166'),
('10167'),
('10168'),
('10169'),
('10170'),
('10171'),
('10172'),
('10173'),
('10174'),
('10175'),
('10176'),
('10177'),
('10178'),
('10179'),
('10180'),
('10181'),
('10182'),
('10183'),
('10184'),
('10185'),
('10186'),
('10187'),
('10188'),
('10189'),
('10190'),
('10191'),
('10192'),
('10193'),
('10194'),
('10195'),
('10196'),
('10197'),
('10198'),
('10199'),
('10200'),
('10201'),
('10202'),
('10203'),
('10204'),
('10205'),
('10206'),
('10207'),
('10208'),
('10209'),
('10210'),
('10211'),
('10212'),
('10213'),
('10214'),
('10215'),
('10216'),
('10217'),
('10218'),
('10219'),
('10220'),
('10221'),
('10222'),
('10223'),
('10224'),
('10225'),
('10226'),
('10227'),
('10228'),
('10229'),
('10230');

INSERT INTO "public"."stream" ("id", "entity_id", "entity_type", "source_entity_id", "posted") VALUES
('6', '294', 'deck', '273', '2017-11-15 04:50:16+00'),
('7', '295', 'deck', '274', '2017-11-15 04:50:27+00'),
('8', '296', 'deck', '275', '2017-11-15 04:50:37+00'),
('9', '297', 'deck', '276', '2017-11-15 04:50:45+00'),
('10', '298', 'deck', '277', '2017-11-15 04:50:53+00'),
('11', '299', 'deck', '278', '2017-11-15 04:51:00+00'),
('12', '301', 'deck', '279', '2017-11-15 04:51:18+00'),
('13', '300', 'deck', '280', '2017-11-15 04:51:10+00'),
('14', '302', 'deck', '281', '2017-11-15 04:51:28+00'),
('15', '303', 'deck', '282', '2017-11-15 04:51:35+00'),
('16', '304', 'deck', '283', '2017-11-15 04:51:43+00'),
('17', '305', 'deck', '284', '2017-11-15 04:51:49+00'),
('24', '342', 'deck', '341', '2017-11-20 19:28:43+00'),
('25', '344', 'deck', '343', '2017-11-20 19:32:27+00'),
('63', '560', 'deck', '559', '2017-12-24 05:53:51+00'),
('64', '562', 'deck', '561', '2017-12-24 05:55:28+00'),
('419', '2117', 'deck', '2115', '2018-07-06 18:10:56+00'),
('420', '2118', 'deck', '2116', '2018-07-06 18:11:12+00'),
('818', '3532', 'deck', '3530', '2018-10-05 18:46:51+00'),
('819', '3533', 'deck', '3531', '2018-10-05 18:46:58+00'),
('1125', '4722', 'deck', '4720', '2019-01-13 23:32:52+00'),
('1126', '4723', 'deck', '4721', '2019-01-13 23:33:00+00'),
('2265', '7961', 'deck', '7959', '2019-11-19 08:41:21+00'),
('2266', '7962', 'deck', '7960', '2019-11-19 08:41:27+00'),
('2366', '8223', 'deck', '8222', '2020-02-02 06:37:01+00'),
('2367', '8225', 'deck', '8224', '2020-02-02 06:38:20+00');

INSERT INTO "public"."subscription" ("user_id", "source_entity_id", "last_seen_entity_id") VALUES
('61', '273', '294'),
('61', '274', '295'),
('61', '275', '296'),
('61', '276', '297'),
('61', '277', '298'),
('61', '278', '299'),
('61', '279', '301'),
('61', '280', '300'),
('61', '281', '302'),
('61', '282', '303'),
('61', '283', '1521'),
('61', '284', '2859'),
('61', '341', '342'),
('61', '343', '344'),
('61', '559', '560'),
('61', '561', '562'),
('61', '2115', '2117'),
('61', '2116', '2118'),
('61', '3530', '6925'),
('61', '3531', '4607'),
('61', '4720', '6833'),
('61', '4721', '4723'),
('61', '7959', '7979'),
('61', '7960', '7962'),
('61', '7963', NULL),
('61', '8222', '8223'),
('61', '8224', '8225');

-- Reset all index sequences now that we have data
SELECT SETVAL('public.ashes500_revision_id_seq', COALESCE(MAX(id), 1) ) FROM public.ashes500_revision;
SELECT SETVAL('public.ashes500_value_id_seq', COALESCE(MAX(id), 1) ) FROM public.ashes500_value;
SELECT SETVAL('public.card_id_seq', COALESCE(MAX(id), 1) ) FROM public.card;
SELECT SETVAL('public.comment_id_seq', COALESCE(MAX(id), 1) ) FROM public.comment;
SELECT SETVAL('public.deck_id_seq', COALESCE(MAX(id), 1) ) FROM public.deck;
SELECT SETVAL('public.phoenix_dice_id_seq', COALESCE(MAX(id), 1) ) FROM public.phoenix_dice;
SELECT SETVAL('public.post_id_seq', COALESCE(MAX(id), 1) ) FROM public.post;
SELECT SETVAL('public.releases_id_seq', COALESCE(MAX(id), 1) ) FROM public.releases;
SELECT SETVAL('public.section_id_seq', COALESCE(MAX(id), 1) ) FROM public.section;
SELECT SETVAL('public.stream_id_seq', COALESCE(MAX(id), 1) ) FROM public.stream;
SELECT SETVAL('public.streamable_entity_id_seq', COALESCE(MAX(entity_id), 1) ) FROM public.streamable;
SELECT SETVAL('public.user_id_seq', COALESCE(MAX(id), 1) ) FROM public."user";
