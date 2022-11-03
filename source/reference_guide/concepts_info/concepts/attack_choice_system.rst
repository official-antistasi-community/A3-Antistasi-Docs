.. _concept_attack_choice_system:

Attack choice system
============================================

.. card::
   :class-card: sd-mt-3
   :class-header: header-2-light

   Description
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Once a faction has positive attack resources, it will call chooseAttack to launch an attack. Target selection is handled with findAttackTargets, which weights potential attacks depending on target value and threat. Main differences:

   - Lower-rated attacks can be chosen, using the weight as a probability.
   - Attacks against rebel targets outside mission distance are now permitted, although chance is reduced.
   - Danger of flying over other enemy locations is taken into account.
   - Threat of other nearby locations is taken into account, not just the target.
   - Distance has no effect (other than the hard air distance cap), but nearby land bases are beneficial.
   - Supply convoys are now used instead of occupant city attacks.
   - HQ attacks are now generated with the same system
