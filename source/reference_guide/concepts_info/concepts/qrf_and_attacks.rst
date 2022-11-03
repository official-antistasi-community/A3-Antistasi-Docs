.. _concept_qrf:

QRF and Attack vehicle spawning
============================================

.. card::
   :class-card: sd-mt-3
   :class-header: header-2-light

   Description
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   QRFs, counterattacks (singleAttack), major attacks, punishments and HQ attacks have all been rewritten to use the same code paths for spawning and vehicle/troop behaviour.

   Vehicle choice is based on splitting vehicles into transport (contains cargo units) and support types. Any attack force must contain at least one transport vehicle, typically more than half. Only attack helis are generated as air supports. CAS and ASF must be called separately.

   Land forces are spawned using the vehicle spawn places system, patched up so that it mostly works. Maps without sufficient vehicle spawn places defined will need them added, otherwise land vehicles will be minimal. Air vehicles are restricted to spawning at airfields or the carrier marker.

   Various changes to previous QRF/singleAttack vehicle behaviour:

   - Ground vehicles now have their waypoints culled much more heavily, improving travel speed and preventing some weird cowardly behaviour of unarmed transports.
   - Crew in weapon-less ground transport vehicles now leave with the cargo units.
   - Attack helis are less inclined to give you a free shot on approach, and will not hover once they run out of targets.
   - Paradrop method has been substantially improved. Perf should be better and drop height should be more consistent. Aims further from the target but may miss.
   - combatLanding now lands further away from the target and gets the troops out more reliably, but needs more work (onEachFrame usage, persisting after landing).
