.. _mission_defend_petros:


Defend Petros
================

Category
    :ref:`mission_category_spawned_dynamically`

.. topic:: Description

   The “Defend Petros” mission can be triggered from three different events:

   * **Failing the “Kill the Traitor”** mission specifically by allowing him to flee after an attempt to kill him. If the traitor makes it all the way to an enemy base, the Defend Petros mission will trigger.
   * **If you lose a map marker**, there is a chance Defend Petros will be triggered. Roughly speaking, the chance is greater the higher your War Level and the more players you have on the server.
      * The full formula is whether a random number 1 through 10 is less than: [War Level] + [Difficulty Coefficient, which grows with player count] / 4. 
      * Difficulty Coefficient = [Number of players on your faction] - [Number of players on the enemy faction] / 5. A decimal result will be rounded down no matter what. For example, if you have 5 players or less on the server and all on the same side, the coefficient is 1. If you have 27 and they’re all on the same side, the coefficient would be 5.
   * **Firing mortars or artillery within 300 meters of the HQ**. Every time you fire a mortar within 300 meters of HQ 2 “chance” points are added to a pool and a random number is rolled between 1 and 100. If the random number is less than your chance points, then Defend Petros is triggered.
      * For example, if you fired 10 mortars right next to Petros, you’d have 20 “chance” points so if the RNG gods gave Antistasi a 19 random number, Defend Petros would trigger.



.. topic:: Outcome

   .. list-table:: Outcome
      :header-rows: 1

      * - Result
        - Money
        - HR
        - Town Support
        - Next Attack
        - Enemy Aggression
        - Player Points
        - Commander Points

      * - **Success: Occupier Attacking**
        - 300/300 €
        - ``-``
        - ``-``
        - ``-``
        - Occupier +10 for 60 minutes and Invader +5 for 60 minutes
        - 10
        - ``-``

      * - **Success: Invader Attacking**
        - 300/300 €
        - ``-``
        - ``-``
        - ``-``
        - Occupier +5 for 60 minutes and Invader +10 for 60 minutes
        - 10
        - ``-``

      * - **Failure**
        - :ref:`concept_losingpetrospenalties`
        - ``-``
        - ``-``
        - ``-``
        - ``-``
        - ``-``
        - ``-``
