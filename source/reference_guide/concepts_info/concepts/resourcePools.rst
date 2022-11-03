.. _concept_resourcepools:

Resource Pools
======================

.. card::
   :class-card: sd-mt-3
   :class-header: header-2-light

   Description
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Enemy resources are split into two types, "attack" and "defence".
   Units generated as part of an attack or support are paid for up-front and have their "A3A_resPool" variable set accordingly.
   If despawned in good condition, they are partially refunded. Mission units have A3A_resPool set to "legacy" and are free
   to spawn (as they're effectively ambient units with no particular task), and paid for equally from both pools on destruction.
   Garrison units are paid for on creation and not refunded on despawn for obvious reasons. Attack and defence resources are saved,
   and updated appropriately on save: Pre-paid units are refunded according to damage level.

   Attack and defence pools are used differently. An attack is launched once an enemy faction hits >0 attack resources,
   typically leaving that faction with a large negative value, which is slowly increased back to zero before the next attack
   can be launched. Defence resources typically have a positive buffer which is used up as reinforcements and supports are generated.
