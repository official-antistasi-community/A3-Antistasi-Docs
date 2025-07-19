.. rst-class:: hidden

.. _dev_guide_police_station:

============================================
Antistasi Police Station Documentation
============================================

Selection of Police Stations
==========================================================================

.. card::
   :class-card: sd-card-2 sd-mt-3
   :class-header: header-2

   Selection of Police Stations
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   First, browse through the mid-size and larger towns in the editor (100 population is the current margin). Identify suitable buildings within 100-150m
   of the center to use as police stations, and make notes of their classnames. Buildings need interiors, which ideally shouldn't be too large or too small.
   Not every town with 100 population needs to have a police station, but most of them should.

   .. rst-class:: code-paragraph-2

   Add the chosen classnames to the map's :code:`policeStationTypes[]` array in :code:`mapInfo.hpp`. Note that this doesn't use inheritance,
   so you may need to add multiple similar buildings here.

Furnishing
===============

.. card::
   :class-card: sd-card-2 sd-mt-3
   :class-header: header-2

   Furnishing
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-paragraph-2

   Create a new editor scenario in the VR map. Place one of your selected buildings down in this (you can use :code:`class Land_whatever` in the search bar to find it,
   if necessary). Add banners, an old office table, a NATO weapons crate and whatever else you want. Avoid placing objects near building positions (mostly near
   windows) or blocking routes through the house.

   In some cases, similar buildings will have a common parent class. If so, you only need to define the furniture for that class.

   Special case classnames:

   .. rst-class:: code-paragraph

   - :code:`Banner_01_F`: Will be textured with the faction flag. Make sure it has the correct orientation and distance from wall.
   - :code:`OfficeTable_01_old_F`: Will have intel placed on top of it.
   - :code:`Land_Document_01_F`: Can be used instead of the office table as a direct intel position on other furniture. However, check that the furniture supports the document.
     None of the CUP tables seem to. Note that definition order doesn't matter, as the intel is placed afterwards.
   - :code:`Box_NATO_Wps_F`: Replaced with faction-defined surrender crate.

   Once the objects are placed, place a player unit, start the mission, look at the house and run the following code to get the relative object positions:

   .. rst-class:: code-block-3
   .. code-block:: guess

      _house = cursorObject;
      _objects = ((8 allObjects 0) + (8 allObjects 1)) select { typeof _x != "CBA_NamespaceDummy" };

      _output = [];
      {
         _pos = _house worldToModel ASLToAGL getPosASL _x;
         _dir = getDir _x - getDir _house;
         _output pushBack [typeof _x, _pos, _dir];
      } forEach _objects;

      _output

   .. rst-class:: code-paragraph-2

   Convert these to config. See a :code:`houses.hpp` file as an example. Make sure you use the correct inheritance for the building.

Testing
===============

.. card::
   :class-card: sd-card-2 sd-mt-3 code-paragraph-2
   :class-header: header-2

   Testing
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Restart Arma (it's config so it needs it). Start up an Antistasi campaign on the map and then search for :code:`initPoliceStations` in the RPT.
   Cases where a valid police station building wasn't found within 150m are reported. Check if these are reasonable. You may need to add additional buildings.

   In some cases you may need to move town centers to more reasonable locations. See :code:`config_fixes/CUPMapsCore/CfgWorlds.hpp` for an example.
   Positions may be copied to the clipboard with a right-click action in the editor.