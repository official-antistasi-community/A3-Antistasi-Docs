.. _mission_prisoner_convoy:


Prisoner Convoy
==================

.. rst-class:: sd-mt-0 sd-mb-4 category-p

Category: :ref:`mission_category_convoy`

.. card::
   :class-card: sd-mt-3
   :class-header: header-2

   Description
   ^^^^^^^^^^^

   -  A convoy of prisoners is being escorted from one outpost to another.
   -  Kill the driver and the guards and drive the prisoner’s vehicle back to base.


.. card::
   :class-card: sd-mt-3
   :class-header: header-2

   Outcome
   ^^^^^^^

   *Note that cells which have two values separated by a / indicate that the reward or penalty depends on if the mission was created with a "difficulty" modifier. The difficulty modifier will make the mission harder but increase the payout. The exact formula is: if a random number 1-10 is lower than your War Level then make the mission harder but with higher payout.*

   .. rst-class:: table-2
   .. list-table::
      :header-rows: 1

      * - Result
        - Money
        - HR
        - Town Support
        - Next Attack
        - Enemy Aggression
        - Player Points
        - Commander Points

      * - **Success**
        - 300 / 600 per prisoner
        - ``-``
        - +10 / +20 support in nearest town
        - ``-``
        - +10 for 2 hours
        - 1 point per POW
        - 1 point per POW

      * - **Failure**
        - ``-``
        - ``-``
        - ``-``
        - ``-``
        - -10 for 60 minutes
        - ``-``
        - -10 / -20
