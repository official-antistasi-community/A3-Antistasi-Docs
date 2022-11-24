.. rst-class:: hidden

.. _dev_console_commands:

====================================================================
Debug Console Commands for Devs
====================================================================

.. card::
   :class-card: sd-card-2 sd-mt-3 sd-card-important

   Please note that this part is still heavily work in progress.
   For more dev related information please go to our `Antistasi-Wiki-for-Devs <https://github.com/official-antistasi-community/A3-Antistasi/wiki/Antistasi-Wiki-for-Devs>`_.

.. card::
   :class-card: sd-card-2 sd-mt-3 sd-card-important

   Following is an unsorted collection of debug console commands that usually are not or should not be used by admins and players on live servers.

Nearest Marker
==================================

.. card::
   :class-card: sd-card-2
   :class-header: header-2-light

   Nearest Marker
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Run as local. Prints nearest marker in a hint on screen.

   .. rst-class:: code-block-2
   .. code-block:: guess

      ["Nearest Marker", format ["%1",([markersX, player] call BIS_fnc_nearestPosition)]] call A3A_fnc_customHint;

Display Markernames
==================================

.. card::
   :class-card: sd-card-2
   :class-header: header-2-light

   Display Markernames
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Run as Local. Changes all markernames to their variable names.

   .. rst-class:: code-block-2
   .. code-block:: guess

      {
         _mrk = format ["Dum%1", _x];
         _mrk setMarkerTextLocal _x;
      } forEach (outposts + seaports + airportsX + resourcesX + factories);

Start an attack
==================================

.. card::
   :class-card: sd-card-2
   :class-header: header-2-light

   Start an attack
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   **For versions <= 2.5.5**

   Run as server. Will start the process of selecting a target for an attack and attacking it for the given side (side can be Invaders or Occupants). This might result in the other side counterattack and take something or four smaller attacks instead of one big attack mission.

   .. rst-class:: code-block-2
   .. code-block:: guess

      [side] spawn A3A_fnc_rebelAttack;

   **For Versions >= 3.0.0**

   Run as server. Will start the process of selecting a target for an attack and attacking it for the given side (side can be Invaders or Occupants). Possible attacks include major (waved) attacks, HQ attacks (if the rebel HQ has been detected), punishments and supply convoys.

   .. rst-class:: code-block-2
   .. code-block:: guess

      [side] spawn A3A_fnc_chooseAttack;

Create a support (3.0.0)
==================================

.. rst-class:: code-paragraph

.. card::
   :class-card: sd-card-2
   :class-header: header-2-light

   Create a support (3.0.0)
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Run as server. Create support (or change target of idle support) of a specified type.

   .. rst-class:: code-block-2
   .. code-block:: guess

      [type, side, caller, maxSpend, target, targPos, reveal, delay] spawn A3A_fnc_createSupport;

   - :code:`type`: The type of support to send (eg. "QRFLAND", "MORTAR", "CAS", see initSupports).
   - :code:`side`: The side of the support (Occupants, Invaders).
   - :code:`caller`: Resource pool to use ("attack", "defence").
   - :code:`maxSpend`: Maximum resources to spend, mostly used for sizing QRFs. For a full size QRF use 1000.
   - :code:`target`: The target object of the support. objNull is valid for AREA. false creates with no target (for TARGET).
   - :code:`targPos`: Target position of the support (eg. getPosATL player).
   - :code:`reveal`: Amount of info to reveal to rebels, 0 low, 1 high.
   - :code:`delay`: Optional, setup delay time in seconds, otherwise will calculate based on war tier.

Spawn loot box
==================================

.. card::
   :class-card: sd-card-2
   :class-header: header-2-light

   Spawn loot box
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Run as local. Spawns a loaded, loading enabled, loot box the same way they spawn in outposts.

   .. rst-class:: code-block-2
   .. code-block:: guess

      // Select these factions: A3A_faction_occ, A3A_faction_inv, A3A_faction_reb, A3A_faction_civ
      private _faction = A3A_faction_occ;
      private _boxX = (_faction get "ammobox")createVehicle getPos Player;
      [_boxX] spawn A3A_fnc_fillLootCrate;
      _boxX call A3A_fnc_logistics_addLoadAction;

Force spawn Missions
==================================

.. card::
   :class-card: sd-card-2
   :class-header: header-2-light

   Force spawn Missions
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   | Run local. Spawns a Mission if allowed by current conditions. Marker/Locations is a String, its case-sensitive, use Markertext command or CitiesX to find Names.
   | Missions can be:

   .. rst-class:: code-paragraph

   - :code:`A3A_fnc_LOG_Ammo`: Ammotruck Outposts,
   - :code:`A3A_fnc_LOG_Salvage`: Seaports,
   - :code:`A3A_fnc_LOG_Supplies`: CitiesX,
   - :code:`A3A_fnc_AS_Official`: Airports,
   - :code:`A3A_fnc_AS_Traitor`: Towns,
   - :code:`A3A_fnc_CON_Outpost`: Outpost/Control Markers,
   - :code:`A3A_fnc_DES_Vehicle`: Airports,
   - :code:`A3A_fnc_RES_Prisoners`: Outposts,
   - :code:`A3A_fnc_RES_Refugees`: CitiesX,

   .. rst-class:: code-block-2
   .. code-block:: guess

      [["Marker/Locations"],"Mission"] remoteExec ["A3A_fnc_scheduler",2]

Group Cleaner
==================================

.. card::
   :class-card: sd-card-2
   :class-header: header-2-light

   Group Cleaner
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Run as server. Changes the interval of the group cleaner function.

   .. rst-class:: code-block-2
   .. code-block:: guess

      debug_cleanGroupDelay = 60;

City Data Extraction
==================================

.. card::
   :class-card: sd-card-2
   :class-header: header-2-light

   City Data Extraction
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Run as local. A script that will return the Name, Civilian Count, type, position, and Size (x,y) in that order.

   .. rst-class:: code-block-2
   .. code-block:: guess

      _outputData = [];
      "(getText (_x >> ""type"") in [""NameCityCapital"", ""NameCity"", ""NameVillage"", ""CityCenter""]) &&
      !(getText (_x >> ""Name"") isEqualTo """") &&
      !((configName _x) in [""Lakatoro01"", ""Galili01"",""Sosovu01"", ""Ipota01"", ""Malden_C_Airport"", ""FobNauzad"", ""FobObeh"", ""22"", ""23"", ""toipela"", ""hirvela"", ""Kuusela"", ""Niemela""])"
      configClasses (configfile >> "CfgWorlds" >> worldName >> "Names") apply {

         _nameX = configName _x;
         _sizeX = getNumber (_x >> "radiusA");
         _sizeY = getNumber (_x >> "radiusB");
         _size = [_sizeY, _sizeX] select (_sizeX > _sizeY);
         _pos = getArray (_x >> "position");
         _size = [_size, 400] select (_size < 400);
         _type = getText (_x >> "type");

         _numCiv = if (!isNull server) then {server getVariable _namex};
         if (isNil "_numCiv" || {!(_numCiv isEqualType 0)}) then
         {
            _numCiv = (count (nearestObjects [_pos, ["house"], _size]));
         };

         _outputData pushBack [_namex, _numCiv, _type, _pos, _sizeX, _sizeY];
      };
      _outputData

Get antenna location
==================================

.. card::
   :class-card: sd-card-2
   :class-header: header-2-light

   Get antenna location
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Run as local.

   .. rst-class:: code-block-2
   .. code-block:: guess

      private _antennatypes = ["Land_TTowerBig_1_F", "Land_TTowerBig_2_F", "Land_Communication_F",
      "Land_Vysilac_FM","Land_A_TVTower_base","Land_Telek1", "Land_vn_tower_signal_01"];
      (nearestObjects [[worldSize /2, worldSize/2], _antennatypes, worldsize]) apply {getPos _x};

Show antenna connections
==================================

.. card::
   :class-card: sd-card-2
   :class-header: header-2-light

   Show antenna connections
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Run as local. Visualizes which city/village is influenced by which antenna on the map like visible below.

   .. rst-class:: code-block-2
   .. code-block:: guess

      private _fnc_drawLineMarker = {
          params ["_pos1", "_pos2", "_name"];
          private _mid = _pos1 vectorAdd _pos2 vectorMultiply 0.5;
          deleteMarkerLocal _name;
          private _lineMarker = createMarkerLocal [_name, _mid];
          _lineMarker setMarkerShapeLocal "RECTANGLE";
          _lineMarker setMarkerBrushLocal "SOLID";
          _lineMarker setMarkerColorLocal "ColorBlack";
          _lineMarker setMarkerDirLocal (_pos1 getDir _pos2);
          _lineMarker setMarkerSizeLocal [25, _mid distance2d _pos1];
      };

      {
          private _nearTower = [antennas+antennasDead, markerPos _x] call BIS_fnc_nearestPosition;
          [markerPos _x, getPosATL _nearTower, "CtoR_"+_x] call _fnc_drawLineMarker;
      } forEach citiesX;

   .. figure:: /_images/AltisRadiotowerConnections.jpg