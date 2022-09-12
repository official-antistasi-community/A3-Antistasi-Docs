.. rst-class:: hidden

.. _dev_porting_guide_maps:

==================================
Antistasi Porting Maps
==================================

.. card::
   :class-card: sd-card-2 sd-mt-3 sd-card-important

   Please note that this part is still heavily work in progress.
   For more dev related information please go to our `Antistasi-Wiki-for-Devs <https://github.com/official-antistasi-community/A3-Antistasi/wiki/Antistasi-Wiki-for-Devs>`_.

Map selection
===========================================

.. card::
   :class-card: sd-card-2 sd-mt-3
   :class-header: header-2

   Map selection
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Not every map is fit for the use with Antistasi. Antistasi has some requirements that should be met in order to have a map that is properly playable and working with the systems that are within the mission. Some of the requirements are:

   - a more or less connected road system
   - a decent size from at least 10x10km
   - villages and cities placed on the map with the correct CfgWorld-Name-Types
   - in the optimal case at least one airfield
   - the map should be free of clutter aka post-apocalyptic maps are not the best, especially when it comes to pathfinding

   We have already looked at a ton of maps anc collected the feedback. Here you can find the `Antistasi Map Consideration List <https://docs.google.com/spreadsheets/d/18SQCwXzGA8WoxCz8YBgBHZgEu1-uXQmqTMqCxQpADRQ/edit#gid=0>`_.

Necessary steps to port a map
===========================================

.. card::
   :class-card: sd-card-2 sd-mt-3
   :class-header: header-2

   Necessary steps to port a map
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      Setting up the NavGrid
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      All maps need a custom navigation grid used for spawning vehicles and directing convoys.
      Quick start guide and generation can be found on :ref:`Street Artist Generation <dev_street_artist_editor_guide>`.
      See :ref:`Steet Artist Editor <dev_street_artist_editor_guide>` for A3-Antistasi navGrid Guidelines (and GIFs!).

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      Setting up the mission.sqm
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      Of course not only the navGrid has to be prepared, but also the mission in itself.
      Antistasi utilizes a system of different markers to recognize, where units and assets should be spawned, detected and/or deleted. These markers need to follow certain rules to be able to be recognized properly.

      .. card::
         :class-card: sd-card-4
         :class-header: header-4-light

         Example
         ^^^^^^^^^^^^

         .. rst-class:: code-paragraph-direct

         In the picture below you see the markers that can be used for an airport.
         The main marker is the one called :code:`airport_1`. This marker should cover the whole area of the airport and units will only spawn and man buildings/statics within the marker. Patrols will spawn outside of the marker.
         As visible, all other markers (besides the spawnPoint, which is the starting point for convoys) have the first 4 letters of :code:`airport`, then the matching number and then the purpose identifier following. This way the code knows the purpose as well as the belonging of said marker to the main marker.

         .. image:: /_images/example-marker-airport-map-porting.png

         .. rst-class:: code-paragraph-direct

         The same concept is used for seaports :code:`seap`, outposts :code:`outp`, factories :code:`fact` and resources :code:`reso`.

      [marker explanation missing]

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      Setting up the folder structure and other necessary files
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      [content missing]