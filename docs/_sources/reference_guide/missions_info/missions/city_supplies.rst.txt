.. _mission_city_supplies:


City Supplies
================

Category
    :ref:`mission_category_support`

.. topic:: Description

  -  Take the supplies to a town and guard it until the timer ends.
  -  Patrols will respond within vicinity of the town.
  -  Enemies coming within the area will reset the timer.
  -  Sit in a nearby house and kill any enemies that come close. The timer should attract nearby gendarme patrols.
  -  This is unconfirmed but often there is an enemy QRF that comes after the mission is completed.

.. topic:: Outcome

  *Note that cells which have two values separated by a / indicate that the reward or penalty depends on if the mission was created with a "difficulty" modifier. The difficulty modifier will make the mission harder but increase the payout. The exact formula is: if a random number 1-10 is lower than your War Level then make the mission harder but with higher payout.*

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
        - -15 / -30 Occupier support in objective town
        - ``-``
        - +10 for 60 minutes
        - 10 / 20
        - 5 / 10

      * - **Failure**
        - ``-``
        - ``-``
        - +5 Occupier support in objective town and -5 support in objective town
        - ``-``
        - ``-``
        - ``-``
        - -10 / -20
