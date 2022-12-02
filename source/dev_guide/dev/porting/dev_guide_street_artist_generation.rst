.. rst-class:: hidden

.. _dev_street_artist_generation_guide:

==================================
Street Artist Generation
==================================

.. card::
   :class-card: sd-card-2 sd-mt-3 sd-card-important

   Please note that this part is still heavily work in progress.
   For more dev related information please go to our `Antistasi-Wiki-for-Devs <https://github.com/official-antistasi-community/A3-Antistasi/wiki/Antistasi-Wiki-for-Devs>`_.

Quick Start Guide
=====================================

.. card::
   :class-card: sd-card-2 sd-mt-3
   :class-header: header-2

   Quick Start Guide
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   #. Run Arma 3.
   #. Make an empty mp-mission on any map (community or official) with just one player.
   #. Save and close the editor.
   #. Locate the folder A3-Antistasi\Tools\StreetArtist\.
   #. Copy Everything in this folder (includes: /Collections/; /functions/; /description.ext; /functions.hpp; /NG_importGUI.hpp)
   #. Paste into the folder of the mp mission you created. Usually in C:\Users\User\Documents\Arma 3 - Other Profiles\YOUR_ARMA_NAME\mpmissions\MISSION_NAME.MAP\
   #. Start host LAN multiplayer.
   #. Run and join the mission.
   #. Press Esc on your keyboard to open debug console.
   #. Paste [] spawn A3A_fnc_NG_main into big large debug window.
   #. Click the button Local Exec.
   #. Exit Debug Console, look down, and open map.
   #. Wait for it to start drawing markers.
   #. Open a new file.
   #. Paste into the new file.
   #. Save.

   See `Street Artist Editor <https://github.com/official-antistasi-community/A3-Antistasi/wiki/Street-Artist-Editor>`_ for A3-Antistasi navGrid Guidelines (and GIFs!).

Generate navGridDB & open the Street Artist Editor
==========================================================================

.. card::
   :class-card: sd-card-2 sd-mt-3
   :class-header: header-2

   Generate navGridDB & open the Street Artist Editor
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-paragraph-2

   Executing :code:`[] spawn A3A_fnc_NG_main` will run with default settings.
   Looking down gives the best performance during this process. You can lower render distance if it helps.
   However, you may need to tweak some arguments depending on the simplification level required for the map.

   A3A_fnc_NG_main Arguments:

   #. Max drift is how far the simplified line segment can stray from the road in metres. (Default = 50)
   #. Junctions are only merged if within this distance from each other. (Default = 15)
   #. True to automatically start the StreetArtist Editor. (Default = true)

   .. rst-class:: code-paragraph-2

   | So running with default settings would also look like :code:`this [50,15,true] spawn A3A_fnc_NG_main;`
   | To run with default and not edit use :code:`[nil,nil,false] spawn A3A_fnc_NG_main;`
   | Max drift is not the only thing that affects road simplification: It will only simplify if the nearestTerrainObject from its position will still return one of it's neighbouring roads. This prevents virtual convoys that are trying to spawn vehicles from jumping to another nearby road because that is the closest navGrid node.

Import navGridDB & open the Street Artist Editor
==========================================================================

.. card::
   :class-card: sd-card-2 sd-mt-3
   :class-header: header-2

   Import navGridDB & open the Street Artist Editor
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   If you have already generated a navGridDB before loading the world and you do not want to regenerate it again: you can use the import function to load it into Arma 3 for viewing or editing.

   .. rst-class:: code-paragraph-2

   #. Local exec :code:`[] spawn A3A_fnc_NGSA_main` in the debug console.
   #. Press :code:`Continue` to close debug console. (If you press :code:`Esc`, you will close the import dialogue!)
   #. Switch to real-life and open the navGridDB file and Copy everything.
   #. Switch to Arma 3 and paste it into the editBox and press the the import button.

Further Reading
==========================================================================

.. card::
   :class-card: sd-card-2 sd-mt-3
   :class-header: header-2

   Further Reading
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   | See `Steet Artist Editor <https://github.com/official-antistasi-community/A3-Antistasi/wiki/Street-Artist-Editor>`_ for A3-Antistasi navGrid Guidelines (and GIFs!).
   | You can find further satisfying and accurate documentation on all sorts of things by looking into the headers of files in :code:`./functions/StreetArtist/`.

------

.. figure:: /_images/Street_Artist_generation-1.png