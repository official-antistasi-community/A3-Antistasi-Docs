.. rst-class:: hidden

.. _dev_street_artist_editor_guide:

==================================
Street Artist Editor
==================================

.. card::
   :class-card: sd-card-2 sd-mt-3

   See :ref:`dev_street_artist_generation_guide` for starting up the editor.

   *Help for the Editor's functions is provided in-game.*
   *However, there are guidelines for creating A3-Antistasi navGrids.*

Important Guidelines
=====================================

.. card::
   :class-card: sd-card-2 sd-mt-3
   :class-header: header-2

   Important Guidelines
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   1. | **Along a road section, the closest node must be one at the end.**
      | The Street Artist Generation takes this into account when simplifying the navGrid. However, there is no checking when the user connects nodes or adds new ones. Ensure that new nodes will not become the closest to any other nearby roads.


   2. | **Ground supplied outposts should have a node within 300m.**
      | You can create a path to outposts and airports to allow ground convoys access. You will need to take a screenshot or memorise A3-Antistasi outpost locations as they are not available in the Editor.

Automated Actions
=====================================

.. card::
   :class-card: sd-card-2 sd-mt-3
   :class-header: header-2

   Automated Actions
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   The Street Artist Editor helps the user avoid common problems.
   There is no way to bypass these systems.

   -  | **If there's no road path between two nodes, then one of the nodes should be off-road.**
      | Every time the user connects two road nodes, it will a employ quick pathfinding check to determine whether there is a valid direct connection. If not, it will add a middle node automatically.

   -  | **Nodes cannot share the same road.**
      | The minimum distance between two nodes is currently 16cm. This also means an off-road node needs to be at least 16cm from any road.

   -  | **Nodes must be on top of bridges.**
      | All added nodes in the Editor are placed on top of the highest surface. The height above ground is displayed next to the cursor. Take this into account for routes going under tunnels or overhangs. To avoid any issues: Place off-road nodes on both ends of the tunnel and hope the AI path safely between them. Nodes snapped to roads will inherit the roads' height, therefore no intervention is required.

GIFs
=====================================

.. card::
   :class-card: sd-card-2 sd-mt-3
   :class-header: header-2

   GIFs
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. figure:: /_images/StreetArtistSetRoadType.gif

      Street Artist- Set Road Types

   .. figure:: /_images/StreetArtistConnectionAndCreationBasics.gif

      Street Artist- Connection & Creation Basics

   .. figure:: /_images/StreetArtistCreateIsland.gif

      Street Artist- Create Island

   .. figure:: /_images/StreetArtistDeletionBrush.gif

      Street Artist- Deletion brush

   .. figure:: /_images/StreetArtistReRoute.gif

      Street Artist- Re Route Roads

   .. figure:: /_images/StreetArtistChangeColor.gif

      Street Artist- Change Colour Division Mode