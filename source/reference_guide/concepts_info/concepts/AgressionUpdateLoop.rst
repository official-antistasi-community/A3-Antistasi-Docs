.. _concept_agressionupdateloop:

Agression Update Loop
======================

.. card::
   :class-card: sd-mt-3
   :class-header: header-2-light

   Description
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   This file (basically a 60-second loop) is now responsible for updating all the balance variables, incrementing the four resource pools and launching attacks. Descriptions of balance variables:

   .. rst-class:: code-paragraph

      - :code:`A3A_activePlayerCount` is a count of all active players. Activity is determined by a simple client-side getDir check.
      - :code:`A3A_balancePlayerScale` is the general amount-of-stuff coefficient, normalized to 1 with 6 players at tier 6.
      - :code:`A3A_balanceVehicleCost` is a rough average resource cost of a single attack vehicle + cargo (if any) at the current war tier.
      - :code:`A3A_balanceResourceRate` is the resources of each type typically gained by a faction every 10 minutes, currently just :code:`balancePlayerScale * balanceVehicleCost`. The defence cap is currently at :code:`10 * A3A_balanceResourceRate`.
      - :code:`A3A_enemyBalanceMul` is a parameter (default 10, because params don't do FP) that multiplies :code:`A3A_balancePlayerScale` to make the game generally harder or easier.
      - :code:`A3A_enemyAttackMul` is a parameter that multiplies attack resource rate to make attacks faster or slower.
      - :code:`A3A_invaderBalanceMul` is a parameter that multiplies invader resource gain rates.

   ResourceCheck (the 10-minute loop) still has most of its former responsibilities, although it now runs with any active players (not necessarily a commander), and no longer generates supply convoys against flipped towns (now the responsibility of chooseAttack).