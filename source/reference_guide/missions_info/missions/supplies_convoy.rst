.. _mission_supplies_convoy:


Supplies Convoy
==================

.. rst-class:: sd-mt-0 sd-mb-4 category-p

Category: :ref:`mission_category_convoy`

.. card::
   :class-card: sd-mt-3
   :class-header: header-2

   Description
   ^^^^^^^^^^^

   -  Convoy bringing supplies to a town to attempt to convert it back to occupiers.
   -  Stop the convoy to prohibit this and take the boxer truck to the town yourself for additional support.


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
        - ``-``
        - ``-``
        - +15 / +30 support in nearest town
        - ``-``
        - +10 for 90 minutes
        - 10 / 20
        - 5 / 10

      * - **Failed: Vehicle Destroyed**
        - ``-``
        - ``-``
        - ``-``
        - ``-``
        - +20 for 2 hours
        - ``-``
        - -10 / -20

      * - **Failed: Convoy Arrived**
        - ``-``
        - ``-``
        - +15 / +30 Occupier support in nearest town
        - ``-``
        - -10 for 60 minutes
        - ``-``
        - -10 / -20

      * - **Failed: Captured Vehicle but Timeout or Destroyed**
        - ``-``
        - ``-``
        - -10 / -20 support in nearest town and +5 / +10 Occupier support in nearest town
        - ``-``
        - -10 for 60 minutes
        - ``-``
        - -10 / -20