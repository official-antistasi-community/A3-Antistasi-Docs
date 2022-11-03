.. _concept_supportsystem:

Support System
======================

.. card::
   :class-card: sd-mt-3
   :class-header: header-2-light

   Description
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   This is the call/response system rather than the limited-knowledge system, as I got it mostly working first. Might be replaced in the future as limited-knowledge does have advantages. Key files:

   - initSupports set up various arrays and hashmaps used by the support system, including marker values and static support type data. They're all documented there, so I won't repeat it here.
   - maxDefenceSpend determines how many resources can be spent against a particular target or marker. It takes account of the importance of the location (based on nearby friendly and enemy markers), aggregate threat (based on live friendly garrisons and enemy troops nearby, plus recent casualties taken), available resources, and support resources already spent against that target/area.
   - requestSupport takes dumb support requests against targets (typically from callForSupport or airspaceControl), uses maxDefenceSpend to decide how many resources to spend, and then chooses a support type dependening on base types (area, troops, target) already called nearby. It also uses the SUP_*Available functions to generate weights for each support based on target type and other support-specific factors. There is a similar but simpler function (requestArtillery) used to choose artillery type supports for attacks. requestSupport always uses the defence pool.
   - createSupport is a worker function to force-create a support of a specific type. It will use already-active supports by preference, if they don't currently have a target.

   Each support typically has an availability function (actually returns a weight now, could be renamed), a creation function (intended to be called by createSupport, and so returns fairly quickly), and a persistently spawned routine that manages the support while active. Multi-target supports update the A3A_activeSupports array to indicate readiness and completion.

   All working supports from the previous system have been preserved except for Gunship, which needs now updating to new systems.

   Individual supports have been heavily refactored and in some cases rewritten. Some common trends:

   - Event handlers for damage response have been generalised and moved to AIVehInit.
   - Support marker creation and maintenance is now offloaded to showInterceptedSupportCall.
   - Multitarget supports now only store one target at once. This avoids problems where the support system would overstack a support with targets it was never likely to engage.

   The CAS support had a major overhaul, rewriting the pre-run loop to a semi-proper state engine and converting CASRun to an onEachFrame handler so that it behaves properly under moderate script load.

   callForSupport is now only triggered by damage, not spotting. Unconsciousness triggers have been cleaned up to call AIReactOnKill more consistently with and without ACE. These triggers also add to the recentDamage arrays on the server, to improve the decision making of maxDefenceSpend.

   Marker recapture counterattacks now use maxDefenceSpend to calculate how large a counterattack to send. If the capture was a hard fight with multiple supports called, or the flag was reflipped shortly after a counterattack was cleared, it's likely that nothing further will be sent.