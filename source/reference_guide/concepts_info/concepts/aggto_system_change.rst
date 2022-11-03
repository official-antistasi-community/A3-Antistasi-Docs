.. _concept_aggro_system:

Aggro System
============================================

.. card::
   :class-card: sd-mt-3
   :class-header: header-2-light

   Description
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Aggression from kills is now inversely adjusted by balancePlayerScale. This means that aggro should work similarly for low and high player counts. High activity means high aggro, low activity means low aggro.

   There is typically no longer any direct aggro from defeating supports or attacks. Destroying vehicles and killing troops is assumed to be sufficient. This should also be applied to most missions, but wasn't addressed yet to cut down on file changes. Capturing markers still increases aggro, by a flat amount rather than player scaled.

   In the reb vs gov game mode, aggro now affects resource rates directly. In reb vs gov vs inv, aggro doesn't change the total resource rates but affects the quantity that enemies will spend on rebels as against the other enemy faction. Aggro also affects delay times on supports, and the chance of attacks being launched on rebels.