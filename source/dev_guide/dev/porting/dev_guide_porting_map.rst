.. rst-class:: hidden

.. _dev_porting_guide_maps:

==================================
Antistasi Porting Maps
==================================

Intro
===========================================

.. card::
   :class-card: sd-card-2 sd-mt-3
   :class-header: header-2

   Intro
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   To be able to play Antistasi on a certain map, this map needs to be ported aka it needs to be implemented into the Antistasi code. This may sound fairly simple but it can be quite the opposite.
   This document has the purpose to give a rough overview over the map porting process. Nevertheless it has to be said that no map port is the same and there are always adjustments that need to be made as well as exceptions.

Map selection
===========================================

.. card::
   :class-card: sd-card-2 sd-mt-3
   :class-header: header-2

   Map selection
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   The first part of porting a map is to check if the map in question is reasonably close to the best-practice requirements. These requirements, which are a rule-of-thumb and based on experience, are as follows:

   - The map should be at least approx. 10x10km or have a landmass of approx. 80 - 100km²
   - The map should have a more or less connected road system – important for pathfinding
   - The map needs to have villages and cities, as having a civilian population is necessary for Antistasi
   - The markers of villages and cities needs to be configured correctly in CfgWorld-Name-Types
   - The map should ideally have at least one airfield
   - The map should be clutter-free aka post-apocalyptic maps are not desirable

   .. rst-class:: target-substitude linkname-here

   | Over the time we have looked at and evaluated a lot of maps. The list together with a feasibility evaluation and comments can be found `here-1 <https://docs.google.com/spreadsheets/d/18SQCwXzGA8WoxCz8YBgBHZgEu1-uXQmqTMqCxQpADRQ/edit?usp=sharing>`_.
   | If you find a map which is not on the list but you think would be fitting for Antistasi, please let us know on our Discord.



First steps
===========================================

.. card::
   :class-card: sd-card-2 sd-mt-3
   :class-header: header-2

   First steps
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-paragraph target-substitude linkname-here

   | One of the first steps and still partially part of the evaluation process is setting up the navGrid. The navGrid is a a hashmap which contains the coordinated of different road pieces as well as information about other road pieces that are connected to it. This hashmap is used to calculate waypoints for convoys and such. During the creation process, which is documented :ref:`here-2 <dev_street_artist_generation_guide>`, the data is visualized on the ingame map and points and connections can be manually adapted, added and removed.
   | This tool does not only create the hashmaps but the visualization gives direct visual feedback on the quality of the road system of a map. Whilst a good road system for example usually has one connected grid, maps with bad road systems can have a lot of disconnected parts, as can be seen below in the bad and the examples. If left unchanged, this makes it impossible for convoys to drive from one grid into another and therefore blocks land-vehicle-based options.
   | When the map does satisfy the requirements and the navGrid is fine, it makes sense to directly save the navGrid in a file called :code:`navGrid.sqf`.

   .. figure:: /_images/MapPorting-1.png

      Figure 1: Bad example

   .. figure:: /_images/MapPorting-2.png

      Figure 2: Good example

   .. rst-class:: code-paragraph

   | Now that we have a decision for a map and the first file, we have to start setting up the folder for it.
   | For that purpose, it’s easiest to copy an already existing folder and rename it. The foldername has to be :code:`Antistasi_mapname.mapname`. The mapname has to be exactly what the map is called when saved from the editor like for example `chernarus_summer` for Chernarus Summer, `vt7` for Virolahti or `vn_khe_sanh` for Khe Sanh of the S.O.G. Prairie Fire CDLC. If the name is not exact, it won’t be recognized by the code. Below you for example can see the folder name as well as the files for Altis.

   .. figure:: /_images/MapPorting-3.png

   .. dropdown:: pic.jpg
      :class-title: header-3-light
      :class-container: sd-card-3

      This is the cover picture which also is visible when the campaign is loading. Should be 1080p.

   .. dropdown:: whiteboard.jpg
      :class-title: header-3-light
      :class-container: sd-card-3

      This is the texture for the whiteboard. Needs to be 2048x2048px. Best is to take a different whiteboard.jpg and overlay the map part.

   .. dropdown:: cba_settings.sqf
      :class-title: header-3-light
      :class-container: sd-card-3

      This file is needed for the system, no adjustments needed to be made.

   .. dropdown::  description.ext
      :class-title: header-3-light
      :class-container: sd-card-3

      | This file contains references to the stringtable entries as well as debriefing texts.
      | The four stringtable references need to be adjusted with the new mapname and new string entries have to be created in the `stringtable.xml` in the main folder of the maps addon.
      | The debriefing texts need to be adapted with the mapname

   .. dropdown:: initPlayerLocal.sqf
      :class-title: header-3-light
      :class-container: sd-card-3

      This file is needed for the system, no adjustments needed to be made.

   .. dropdown:: initServer.sqf
      :class-title: header-3-light
      :class-container: sd-card-3

      This file is needed for the system, no adjustments needed to be made.

   .. dropdown:: mapInfo.hpp
      :class-title: header-3-light
      :class-container: sd-card-3

      The map info needs to be updated with the necessary data, once the mission.sqm has been completed. More info on that further below.

   .. dropdown:: missions.sqm
      :class-title: header-3-light
      :class-container: sd-card-3

      The mission.sqm is the file that contains all the necessary markers as well as unit and asset placements from the Arma 3 Editor. More info on that further below.

   .. dropdown:: navGrid.sqf
      :class-title: header-3-light
      :class-container: sd-card-3

      This file needs to contain the exported information from the Street Artist Tool.

   .. dropdown:: onPlayerRespawn.sqf
      :class-title: header-3-light
      :class-container: sd-card-3

      This file is needed for the system, no adjustments needed to be made.

Setting up the mission.sqm
==================================

.. card::
   :class-card: sd-card-2
   :class-header: header-2

   Setting up the mission.sqm
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-paragraph target-substitude linkname-here

   | To start the work on the map itself it is easiest to use something that already contains all the necessary markers, modules and assets rather than starting new. For this purpose, I have created a custom composition which is available `here-3 <https://drive.google.com/drive/folders/1haydzz1IHlt77Q924yv1P_tD_-vooE2j?usp=sharing>`_.
   | Download the rar, go to your :code:`C:\Users\[Username]\Documents\Arma 3 - Other Profiles\[playername]\compositions` folder or wherever your profile is saved and unpack it.
   | After you have done that, the custom composition is available in the Arma 3 Editor and can be placed.
   | Once the custom composition is placed within an empty mission, you have the following content:

   - all necessary modules to run Antistasi including game logic, headless clients and the gamemaster module
   - all necessary HQ assets like the arsenal, the vehicle box, the tent and more
   - Petros as well as all payable units
   - marker for the support corridors
   - 6 sets of airport markers
   - 20 sets of outpost markers
   - 10 sets of seaport markers
   - 10 sets of factory markers
   - 20 sets of resource markers
   - additional markers like detectPlayer, control, seaAttackSpawn, seapatrol and seaSpawn

   Usually, these assets are more than enough to populate a full map. When more markers are needed, orient yourself on the naming conventions of the already existing markers. Getting the naming right is crucial, as the markers otherwise are not recognized by the code which in the best case simply doesn’t work and in the worst case crashes the complete mission.

   When placing the markers for airports, outposts, seaports, factories and resources make sure that the main markers are large enough to cover the whole area you want to assign to them. For the vehicle and mortar markers, they are usually placed within the area of the main marker. The hangar as well as the helipad marker are only necessary, when there is a helipad or hangar outside of the main marker area and you still want to use it for said main marker. When not needed after completing the map port, the unused markers can simply be deleted.

   There are no set rules on how markers should be placed but here a few rules-of-thumb based on experience which create to a somewhat balanced map.

   - Have at least 3 airport. If there are not enough airfields, build custom ones with for example helipads and such. Make sure that the airfields are somewhat equally spread over the map.
   - Use logical and organic bottlenecks as well as advantageous positions to place outposts like near major road crossings, elevated positions, near larger cities or somewhat close to factories.
   - Have resources and factories spread more or less equally over the whole map. Ideally you want to use a 1-4 to 1-7 ratio of factories to resources as factories are multipliers to the income of resource points.
   - Don’t fill the whole map to the brim but leave gaps for the rebels to place the HQ. Players prefer dead ends or somewhat protected areas to place their HQs.
   - Don’t cluster too many markers on a too close space. This can lead to areas with too much AI which decreases FPS whilst also creating a situation in which the players can be completely overrun by AI for a prolonged time aka certainly less fun.

   Once the mission is completed in the editor, save the mission, do not binarize the file and copy the mission.sqm over into the map folder.

Setting up the mapInfo.hpp
==================================

.. card::
   :class-card: sd-card-2
   :class-header: header-2

   Setting up the mapInfo.hpp
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: target-substitude linkname-here

   | Once the mission is completed, now you have input the map relevant information into the MapInfo.hpp. Currently there are nine things that need to be adjusted.
   | Debug commands to get the necessary information can be found :ref:`here-4 <dev_console_commands>`.
   | In all of the cases check how the information is set up in already ported maps.

   .. dropdown:: class
      :class-title: header-3-light
      :class-container: sd-card-3

      In the first line, enter the mapname before the opening bracket.

   .. dropdown:: population
      :class-title: header-3-light
      :class-container: sd-card-3

      .. rst-class:: code-paragraph

      Enter the config names of cities and villages with the population like :code:`{"configname",amount}` separated by commas.

   .. dropdown:: disabledTowns
      :class-title: header-3-light
      :class-container: sd-card-3

      .. rst-class:: code-paragraph

      Enter config names of cities and villages that should be disabled. For example when there are is a city marker in the middle of an airfield like :code:`{ "city1", “city 2”}`.

   .. dropdown:: antennas
      :class-title: header-3-light
      :class-container: sd-card-3

      Here enter the coordinates from all antennas on the map.

   .. dropdown:: antennasBlacklistIndex
      :class-title: header-3-light
      :class-container: sd-card-3

      Here enter the incides of antennas in the array that should not be active. Array starts at 0.

   .. dropdown:: banks
      :class-title: header-3-light
      :class-container: sd-card-3

      Enter the coordinates from all available bank buildings.

   .. dropdown:: garrison
      :class-title: header-3-light
      :class-container: sd-card-3

      Enter the named of the markers that should be hold by the invaders. The second bracket contains all markers whilst the fourth bracket only contains the control markers.

   .. dropdown:: fuelStationTypes
      :class-title: header-3-light
      :class-container: sd-card-3

      Enter the active fuel station types based on the assets being used on the map. Best way here is to copy the fuel stations from a map using the same buildings.

   .. dropdown:: climate
      :class-title: header-3-light
      :class-container: sd-card-3

      .. rst-class:: code-paragraph

      Enter the climate of the map from the selection :code:`arid, temperate, tropical, arctic`.

Integration into the system
==================================

.. card::
   :class-card: sd-card-2
   :class-header: header-2

   Integration into the system
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   | To get Antistasi to recognize the new map, references need to be added in a few points.
   | In the main folder of the maps addon add the appropriate references in the following files:

   - config.cpp
   - mapInfo.hpp
   - NavGrid.hpp

   Once that is done, you made no mistakes and you built and loaded Antistasi properly with the mods necessary to run the map you ported, the mission should appear in the list.

   | And just to have it said again, yes, this is only a rough guide but as mentioned before, every map is different and hence a more in depth guide would not make sense as you have to adapt either way and the information could be incorrect for whichever map you choose.
   | If you have further questions, please join our discord and ask your specific questions there.
   | And now, have fun porting!
