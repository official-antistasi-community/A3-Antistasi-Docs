.. _concept_trainfia:

Train FIA
=================

The calculation for your army’s skill is:

Friendly AI Skill = (0.6 / [Skill Multiplier] + 0.015 * [Army Training Level]);

**Skill Multiplier Values**

* Easy 1
* Normal 2
* Hard 3

**Rules on Max Army Training**

* Hard Cap = 20 (Only available at War Level 10)
* Dynamic Cap = [War Level] * 2 (Ex: At War Level 3 you can only train your army to 6)

**Side Notes**

* Marksmen get an additional bonus for aimingAccuracy and aimingShake
* Squad Leaders get an additional bonus for courage and commanding
* For a definition of the skills above and all skills governing AI behavior see this article: https://community.bistudio.com/wiki/Arma_3:_AI_Skill 

**Examples**

* Easy difficulty, maxed out soldiers skill: (.6 / 1 + .015 * 20) = .9 (Expert)
* Hard difficulty, maxed out soldier skill: (.6 / 3 + .015 * 20) = .5 (Recruit)
* War level 3 (max training = 6) on Easy: (.6 / 1 + .015 * 6) = .69 (Veteran)
* War level 3 (max training = 6) on Hard: (.6 / 3 + .015 * 6) = .29 (Rookie)

Skill values based on https://community.bistudio.com/wiki/setSkill

* Novice < 0.25
* Rookie >= 0.25 and <= 0.45
* Recruit > 0.45 and <= 0.65
* Veteran > 0.65 and <= 0.85
* Expert > 0.85
