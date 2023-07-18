.. rst-class:: hidden

.. _admin_DebugCommands_guide:

====================================================================
Debug Console Commands for Players and Admins
====================================================================

.. card::
   :class-card: sd-card-2 sd-mt-2

   .. rst-class:: mono-space

   | `"Hey Dev, Petros is gone. What should I do?"` and other questions can be answered by the debug commands we collected for you.
   | And we have quite a few! They range from teleporting HQ assets, over adding temporary members to cheating in Money and HR (which we don't recommend - just play it without cheating, you lazy fuck).
   | Nevertheless, we hope the debug commands can solve your issues if you have some.

Basic Commands
=======================

.. card::
   :class-card: sd-card-2 sd-mt-2
   :class-header: header-2

   Basic Commands
   ^^^^^^^^^^^^^^^^^^

   These commands are single liners that do various things, mostly with Antistasi's functions.

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      Teleport HQ Assets
      ^^^^^^^^^^^^^^^^^^^^

      Run as local. Teleports the relevant asset to your position.

      .. rst-class:: code-block-3
      .. code-block:: guess

         petros setPos (getPos player);
         flagX setPos (getPos player);
         mapX setPos (getPos player);
         vehicleBox setPos (getPos player);
         boxX setPos (getPos player);
         fireX setPos (getPos player);

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      Rebuild HQ at player location
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      Run as local. This teleports Petros to your position and then executes the "Build HQ" command.

      .. rst-class:: code-block-3
      .. code-block:: guess

         [getpos player] remoteExec ["A3A_fnc_createPetros", 2];
         [] remoteExec ["A3A_fnc_buildHQ", 2];

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      Force Commander
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      Both run as Local. The first one makes you the commander, the second makes the person you are looking at commander.

      .. rst-class:: code-block-3
      .. code-block:: guess

         [player] remoteExec ["A3A_fnc_makePlayerBossIfEligible", 2];
         [cursorTarget] remoteExec ["A3A_fnc_makePlayerBossIfEligible", 2];

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      Adding Temporary Members
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      Both run as local. First one adds yourself, second adds the person you are looking at.

      .. rst-class:: code-block-3
      .. code-block:: guess

         membersX pushBackUnique (getPlayerUID player); publicVariable "membersX";
         call A3A_fnc_memberAdd;

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      Force commander eligibility
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      Both run as local. First sets yourself eligible, second sets the person you are looking at.

      .. rst-class:: code-block-3
      .. code-block:: guess

         player setVariable ["eligible",true,true];
         cursorTarget setVariable ["eligible",true,true];

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      Resources and money
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      Both run as local. First adds a certain amount to your personal money, Second adds HR and Money to the faction. Replace PM, HR, Money with the value you want to add. Negative numbers will subtract.

      .. rst-class:: table-2-b

      .. flat-table::
         :header-rows: 1

         *  - Variable
            - Values

         *  - PM
            - { x |Element| |GZ| }

         *  - HR
            - { x |Element| |GZ| }

         *  - Money
            - { x |Element| |GZ| }

      .. rst-class:: code-block-3
      .. code-block:: guess

         [PM] call A3A_fnc_resourcesPlayer;

         // [HR,Money]
         [0,0] remoteExec ["A3A_fnc_resourcesFIA",2];

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      Prestige / Aggro
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      Run as local. Adds the specified aggro amount (-100 to 100) to the aggression of the specified side, with falloff over the specified time in minutes. Side must be Occupants or Invaders.

      .. rst-class:: table-2-b

      .. flat-table::
         :header-rows: 1

         *  - Variable
            - Values

         *  - aggroAmount
            - { x |Element| |GZ| `|` -100 |SE| x |SE| 100 }

         *  - aggroTime
            - { x |Element| |NatNum| `|` x > 0 }

         *  - side
            - x |Element| {Occupants, Invaders}

      .. rst-class:: code-block-3
      .. code-block:: guess

         [side, aggroAmount, aggroTime] remoteExec ["A3A_fnc_addAggression",2];

   .. rst-class:: code-paragraph

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      View and adjust enemy resources (3.0.0)
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      Run as server. Defence resources have a maximum of :code:`10*A3A_balanceResourceRate` (depends on player count, aggro, war tier, difficulty), and cannot be used when below zero. Attacks will be launched if attack resources are above zero.

      View all enemy resource counts:

      .. rst-class:: code-block-3
      .. code-block:: guess

         [A3A_resourcesDefenceOcc, A3A_resourcesDefenceInv, A3A_resourcesAttackOcc, A3A_resourcesAttackInv];

      Add 500 to invader attack resources:

      .. rst-class:: code-block-3
      .. code-block:: guess

         A3A_resourcesAttackInv = A3A_resourcesAttackInv + 500;

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      Force update UI
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      Run as local. Forces the UI bar to update.

      .. rst-class:: code-block-3
      .. code-block:: guess

         [] spawn A3A_fnc_statistics;

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      Flip Marker
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      | Run as local. Changes the owner of a marker. Specify the marker to change and what side to give it to.
      | Markername is case-sensitive and needs to be given as a string "outpost_1".
      | Sides are: Teamplayer, Invaders, Occupants

      .. rst-class:: table-2-b

      .. flat-table::
         :header-rows: 1

         *  - Variable
            - Values

         *  - side
            - x |Element| {Teamplayer, Occupants, Invaders}

         *  - markername
            - N/A

      .. rst-class:: code-block-3
      .. code-block:: guess

         [side, markername] remoteExec ["A3A_fnc_markerChange", 2];

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      City Support
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      Run as local. Change the support values of the closest city to you. Values can be negative, both gov and reb must be set to a number from 100 to -100.

      .. rst-class:: table-2-b

      .. flat-table::
         :header-rows: 1

         *  - Variable
            - Values

         *  - gov
            - { x |Element| |GZ| `|` -100 |SE| x |SE| 100 }

         *  - reb
            - { x |Element| |GZ| `|` -100 |SE| x |SE| 100 }

      .. rst-class:: code-block-3
      .. code-block:: guess

         [gov, reb, getPos player, false] remoteExec ["A3A_fnc_citySupportChange", 2];

Advanced Commands
=======================

.. card::
   :class-card: sd-card-2 sd-mt-2
   :class-header: header-2

   Advanced Commands
   ^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      Remove item from arsenal
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      Run as server. Removes the item, specified by classname, from the arsenal.

      .. rst-class:: code-block-3
      .. code-block:: guess

         private _arsenalTab = "rhs_weap_Izh18" call jn_fnc_arsenal_itemType;
         [_arsenalTab,"rhs_weap_Izh18",-1] call jn_fnc_arsenal_removeItem;

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      Remove Array of Items from arsenal
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      Run as server. Removes the item, specified by classname, from the arsenal.

      .. rst-class:: code-block-3
      .. code-block:: guess

         {
            private _tab = _x call  jn_fnc_arsenal_itemType;
            [_tab,_x,-1] call jn_fnc_arsenal_removeItem;
         } forEach someArrayOfTypes;

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      Add initialRebelEquipment
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      **Not recommended to be used after switching between modsets.**

      | For Versions <= 2.5.5
      | Run as server. Adds all initialRebelEquipment again, for cases where mission started without ace, to add missing items.

      .. rst-class:: code-block-3
      .. code-block::

         { [_x] call A3A_fnc_unlockEquipment } forEach initialRebelEquipment

      | For Versions >= 3.0.0
      | Run as server. Adds all unlimited initialRebelEquipment again, for cases where mission started without ace, to add missing items.

      .. rst-class:: code-block-3
      .. code-block::

         {
            if (_x isEqualType "") then { _x call A3A_fnc_unlockEquipment };
         } foreach (A3A_faction_reb get "initialRebelEquipment");

      .. card::
         :class-card: sd-card-3
         :class-header: header-3

         Repair building other than radio-towers
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

         Run as local. Repairs building you are looking at. Do not use for radio towers!

         .. rst-class:: code-block-3
         .. code-block:: guess

            [cursorObject] remoteExec ["A3A_fnc_repairRuinedBuilding", 2];

Other Useful Commands
=======================

.. card::
   :class-card: sd-card-2 sd-mt-2
   :class-header: header-2

   Other Useful Commands
   ^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      Repair Buildings
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      Run as local. Repairs the building that you are looking at.

      .. rst-class:: code-block-3
      .. code-block:: guess

         [cursorObject] remoteExec ["A3A_fnc_repairRuinedBuilding", 2]

      .. rst-class:: .code-paragraph

      Run as server. Repairs all buildings in the area of a marker. Replace :code:`"marker"` with the real name of a marker, e.g :code:`“outpost_1”`

      .. rst-class:: code-block-3
      .. code-block:: guess

         { [_x, true] remoteExec ["A3A_fnc_repairRuinedBuilding", 2] } forEach (destroyedBuildings inAreaArray "marker")

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      Vanilla Revive
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      Run as local. This will revive you and remove any damage.

      .. rst-class:: code-block-3
      .. code-block:: guess

         player setDamage 0;
         player setVariable ["incapacitated",false,true];

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      Vanilla Stamina reset
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      Run as local. This will reset your Stamina

      .. rst-class:: code-block-3
      .. code-block:: guess

         [player, 0] remoteExec ["setFatigue", _0];

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      Ace Revive
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      Run as local. This will fully heal you and revive if you were downed.

      .. rst-class:: code-block-3
      .. code-block:: guess

         [player, player] call ace_medical_treatment_fnc_fullHeal

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      Regain Undercover (Player)
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      Run as local. This allows you to go Undercover if you were reported. Will not allow your Vehicle to go Undercover again.

      .. rst-class:: code-block-3
      .. code-block:: guess

         player setVariable ["compromised", 0, true];

.. |NatNum| unicode:: U+2115
.. |Element| unicode:: U+220A
.. |SE| unicode:: U+2264
.. |GE| unicode:: U+2265
.. |GZ| unicode:: U+2124