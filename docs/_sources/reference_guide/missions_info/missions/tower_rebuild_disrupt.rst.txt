.. _mission_tower_rebuild_disrupt:


Tower Rebuild Disrupt
==========================

Category
    :ref:`mission_category_spawned_dynamically`

.. topic:: Description


  -  After you destroy a radio tower the government will attempt to repair the tower with a repair vehicle.
  -  Try to steal it to gain a new source vehicle to repair other vehicles and entrenchments.
  -  If all else fails, simply blow it up with a rocket launcher or mortar.


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
        - ``-``
        - 20 minute delay
        - +15 for 90 minutes (Occupier) and +5 for 60 minutes (Invader)
        - 10
        - ``-``

      * - **Failure**
        - ``-``
        - ``-``
        - ``-``
        - 10 minutes sooner
        - ``-``
        - ``-``
        - -10
