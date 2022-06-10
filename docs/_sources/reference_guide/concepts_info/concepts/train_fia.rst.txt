.. _concept_trainfia:

Train FIA
=================

.. card::
   :class-card: sd-mt-3
   :class-header: header-2-light

   Description
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   The calculation for your army’s skill is:

   .. card::
      :class-header: header-3-light
      :class-card: sd-card-3

      Algorithm
      ^^^^^^^^^

      Friendly AI Skill = (0.6 / [Skill Multiplier] + 0.015 * [Army Training Level]);

   .. card::
      :class-header: header-3-light
      :class-card: sd-card-3

      Skill Multiplier Values
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^

      * Easy 1
      * Normal 2
      * Hard 3

   .. card::
      :class-header: header-3-light
      :class-card: sd-card-3

      Rules on Max Army Training
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^

      * Hard Cap = 20 (Only available at War Level 10)
      * Dynamic Cap = [War Level] * 2 (Ex: At War Level 3 you can only train your army to 6)

   .. card::
      :class-header: header-3-light
      :class-card: sd-card-3

      Side Notes
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^

      * Marksmen get an additional bonus for aimingAccuracy and aimingShake
      * Squad Leaders get an additional bonus for courage and commanding
      * For a definition of the skills above and all skills governing AI behavior see this article: https://community.bistudio.com/wiki/Arma_3:_AI_Skill

   .. dropdown:: Example
      :class-title: header-3-light
      :class-container: sd-card-3

      * Easy difficulty, maxed out soldiers skill: (.6 / 1 + .015 * 20) = .9 (Expert)
      * Hard difficulty, maxed out soldier skill: (.6 / 3 + .015 * 20) = .5 (Recruit)
      * War level 3 (max training = 6) on Easy: (.6 / 1 + .015 * 6) = .69 (Veteran)
      * War level 3 (max training = 6) on Hard: (.6 / 3 + .015 * 6) = .29 (Rookie)

   .. card::
      :class-header: header-3-light
      :class-card: sd-card-3

      Skill value meanings
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^

      * Novice < 0.25
      * Rookie >= 0.25 and <= 0.45
      * Recruit > 0.45 and <= 0.65
      * Veteran > 0.65 and <= 0.85
      * Expert > 0.85

      Values above are based on https://community.bistudio.com/wiki/setSkill .