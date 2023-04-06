.. _concept_warlevel:

.. rst-class:: hidden

=================
War Level
=================

General Information
==================================

.. card::
   :class-card: sd-mt-3
   :class-header: header-2-light

   General Information
   ^^^^^^^^^^^^^^^^^^^^

   In general, War Level is a reflection of the level of escalation in arms and manpower the enemy is
   committing to fight you. The higher the War Level, the heavier the weaponry and the stronger the
   force you can expect to combat. For example, at low War Level a supply convoy is normally made up
   of some trucks of infantry and perhaps a vehicle with a mounted heavy machine gun. At higher war
   levels, these same convoys may consist of APCs and tanks.

Calculating War Level
==================================

.. card::
   :class-card: sd-mt-3
   :class-header: header-2-light

   Calculating War Level
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   War Level is calculated by the number of map markers you hold when a resource check takes place.
   Each map marker under your control is worth a certain number of points and each War Level is tied
   to a threshold of map marker points. The threshold is based on what percentage of the total map
   marker points on the map you currently control.

   .. card::
      :class-header: header-3-light
      :class-card: sd-card-3

      Point Value of each Map Marker
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      .. rst-class:: table-2

      .. flat-table::
         :header-rows: 1

         *  - Marker
            - Point Value

         *  - Airport
            - 8

         *  - Seaport
            - 4

         *  - Outpost
            - 2

         *  - Factories
            - 2

         *  - Resources
            - 2

         *  - Cities
            - 1

   .. card::
      :class-header: header-3-light
      :class-card: sd-card-3

      War Level Threshold
      ^^^^^^^^^^^^^^^^^^^^

      .. rst-class:: table-2

      .. flat-table::
         :header-rows: 1

         *  - War level
            - Threshold in Percent

         *  - Tier 2
            - 0.8%

         *  - Tier 3
            - 3.3%

         *  - Tier 4
            - 7.6%

         *  - Tier 5
            - 13.5%

         *  - Tier 6
            - 21.2%

         *  - Tier 7
            - 30.6%

         *  - Tier 8
            - 41.8%

         *  - Tier 9
            - 54.7%

         *  - Tier 10
            - 69.3%

      .. figure:: /_images/war-level-graph.png

   This may sound confusing. Here is a simple example:

   - There are 100 map marker points on the map.
   - You control two airports, two factories, and five cities.
   - This would mean 16 points for airports, 4 points for factories, and 5 points for cities. This is a total of 25 points
   - Given 100 map marker points, this means you control 25% of the map marker points available.
   - Based on the War Level threshold this would put you above the 21.2% for level 6 - so you would be at War Level 6.

War Level’s Impact
==================================

.. card::
   :class-card: sd-mt-3
   :class-header: header-2-light

   War Level’s Impact
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   War Level has a wide ranging impact on the scenario. The enemy’s attacks and responses to you will
   change significantly as the War Level escalates. In addition, the player is prevented from doing
   certain things until reaching a sufficiently high War Level for balance purposes.

   .. dropdown:: Enemy capabilities impacted by War Level
      :class-title: header-3-light
      :class-container: sd-card-3

      - Enemy factions get more resources to spend on their attacks and QRFs
      - With higher war tier, enemies will use more high-quality vehicles such as tanks, APCs and attack helis
      - Composition of enemy forces will become harder in things like convoy missions
      - At higher war tiers, garrisons are less likely to consist of militia troops and spawn more patrols
      - The number of civilians that you will see in cities will decrease with War Level
      - Enemy AI have slightly higher skill
      - In Reb vs Gov vs Inv, attacks are more likely to be launched against you rather than the other enemy faction
      - Invader attacks are more likely to be Punishment missions, Gov attacks are less likely to be Supply Convoy missions
      - Artillery is more likely to be used instead of mortars
      - Carpet bombs are more likely to be used instead of airstrikes
      - The chance of intel in Outpost being booby trapped private increases with War Level

   .. dropdown:: Player capabilities impacted by War Level
      :class-title: header-3-light
      :class-container: sd-card-3

      - Mission difficulty roll (most missions have an easy and hard version which it will silently choose
        as the mission is created). Higher War Level increases the chance you will receive the more difficult version of the mission.
      - Upgrading the skill of the AI in your army is limited by War Level
      - The number of vehicles you can garage is limited by War Level
      - You cannot capture airports before War Level 3
      - Chance of intercepting enemy comms increases as War Level increases
      - The chance of being detected at a roadblock or non-airport garrison increases with war level.