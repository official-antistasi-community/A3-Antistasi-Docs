.. _concept_gainingandlosingcitysupport:

.. rst-class:: hidden

=================================
Gaining and Losing City Support
=================================

General Notes
=================================

.. card::
   :class-card: sd-mt-3 code-paragraph
   :class-header: header-2-light

   General Notes
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   * Incidents such as enemy QRF deaths affect the nearest town, but only if they happen within 200m of the town’s radius.
   * Changes to support in a town are scaled by the formula :code:`10 * _change / sqrt _townPop`, unless noted as unscaled. For example a town of 400 population will gain support at half the rate of a town of 100 population.
   * If the nearest radio tower to a town is destroyed, positive support changes are multiplied by 1.5x.
   * If the nearest radio tower to a town is intact and controlled by rebels, positive support changes are multiplied by 2x.
   * If the police station in a town is destroyed, positive support changes are further multiplied by 1.5x.

Enemy-Driven Events
=================================

.. card::
   :class-card: sd-mt-3
   :class-header: header-2-light

   Enemy-Driven Events
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   * +15 or +30 for rebels successfully delivering a supply convoy.
   * -5 if a supply convoy times out or is destroyed.
   * -15 for enemies successfully delivering a supply convoy.
   * Up to +20 (unscaled) to nearby cities for rebels successfully defending a punishment attack, linearly reducing to 0 at 3000m.

Rebel Missions
=================================

.. card::
   :class-card: sd-mt-3
   :class-header: header-2-light

   Rebel Missions
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   * +1-2 for each prisoner rescued. Does not apply unless the outpost was near a town.
   * +20 unscaled for destroying a police station (only as part of mission).
   * +15 for successfully delivering city supplies.
   * -50 unscaled for losing or ignoring a city battle.

Minor Town Missions
=================================

.. card::
   :class-card: sd-mt-3
   :class-header: header-2-light

   Minor Town Missions
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   * -2 if hostage dies (not if mission times out).
   * +10 if hostage is rescued.
   * +5 if corrupt cop is killed.
   * +10 if corrupt cop surrenders.
   * +8 if vehicle recovery is successful.
   * -2 if taxi passenger dies (not if mission times out).
   * +5 if taxi passenger is delivered, +1 extra per 400m distance between towns.

Other Incidents
=================================

.. card::
   :class-card: sd-mt-3
   :class-header: header-2-light

   Other Incidents
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   * +1 for enemy surrender.
   * +1 for enemy kill by rebels.
   * -2 for rebels killing a surrendered enemy.
   * -3 for rebels killing a civilian.
   * -9 for rebels killing a civilian wearing a press vest.
   * -1 per HR for rebel overspend, eg. respawning with 0 HR.
   * -1 for rebels stealing a parked car from a town.
