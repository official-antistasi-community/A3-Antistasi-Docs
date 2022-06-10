.. _dev_guide_ace_settings:

.. rst-class:: hidden

==============
ACE-SETTINGS
==============

.. rst-class:: sd-mt-0 sd-mb-4 category-p

FILE: :download:`ace_settings.txt </_data/ace_settings.txt>`

Antistasi
==============

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   Antistasi
   ^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      HR_GRG_dLock                                                                =     false
      force HR_GRG_PoolBase                                                       =     10
      force HR_GRG_PoolIncr                                                       =     2
      force HR_GRG_Pylons_Enabled                                                 =     true
      force HR_GRG_ServiceDisabled_Rearm                                          =     false
      force HR_GRG_ServiceDisabled_Refuel                                         =     false
      force HR_GRG_ServiceDisabled_Repair                                         =     false

ACE Map
=========

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Map
   ^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force force ace_map_BFT_Enabled                                             =     false
      force force ace_map_BFT_HideAiGroups                                        =     false
      force force ace_map_BFT_Interval                                            =     1
      force force ace_map_BFT_ShowPlayerNames                                     =     false
      force force ace_map_DefaultChannel                                          =     1
      force force ace_map_mapGlow                                                 =     true
      force force ace_map_mapIllumination                                         =     true
      force force ace_map_mapLimitZoom                                            =     false
      force force ace_map_mapShake                                                =     true
      force force ace_map_mapShowCursorCoordinates                                =     false
      force force ace_markers_moveRestriction                                     =     0
      ace_markers_timestampEnabled                                                =     true
      ace_markers_timestampFormat                                                 =     "HH:MM"
      ace_markers_timestampHourFormat                                             =     24

ACE Fire
==========

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Fire
   ^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force ace_fire_dropWeapon                                                   =     1
      force ace_fire_enabled                                                      =     true
      force ace_fire_enableFlare                                                  =     false
      ace_fire_enableScreams                                                      =     true

ACE Zeus
==========

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Zeus
   ^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force force ace_zeus_autoAddObjects                                         =     true
      force force ace_zeus_canCreateZeus                                          =     0
      force force ace_zeus_radioOrdnance                                          =     false
      force force ace_zeus_remoteWind                                             =     false
      force force ace_zeus_revealMines                                            =     0
      force force ace_zeus_zeusAscension                                          =     false
      force force ace_zeus_zeusBird                                               =     false

ACE Common
============

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Common
   ^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force force ace_common_allowFadeMusic                                       =     true
      force force ace_common_checkPBOsAction                                      =     0
      force force ace_common_checkPBOsCheckAll                                    =     false
      force force ace_common_checkPBOsWhitelist                                   =     "[]"
      ace_common_displayTextColor                                                 =     [0,0,0,0.1]
      ace_common_displayTextFontColor                                             =     [1,1,1,1]
      ace_common_epilepsyFriendlyMode                                             =     false
      ace_common_progressBarInfo                                                  =     2
      ace_common_settingFeedbackIcons                                             =     1
      ace_common_settingProgressBarLocation                                       =     0
      force force ace_noradio_enabled                                             =     true

ACE Pylons
============

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Pylons
   ^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force force ace_pylons_enabledForZeus                                       =     true
      force force ace_pylons_enabledFromAmmoTrucks                                =     true
      force force ace_pylons_rearmNewPylons                                       =     true
      force force ace_pylons_requireEngineer                                      =     false
      force force ace_pylons_requireToolkit                                       =     true
      force force ace_pylons_searchDistance                                       =     20
      force force ace_pylons_timePerPylon                                         =     10

ACE Scopes
============

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Scopes
   ^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force force ace_scopes_correctZeroing                                       =     true
      force force ace_scopes_deduceBarometricPressureFromTerrainAltitude          =     true
      force force ace_scopes_defaultZeroRange                                     =     100
      force force ace_scopes_enabled                                              =     true
      force force ace_scopes_forceUseOfAdjustmentTurrets                          =     true
      force force ace_scopes_overwriteZeroRange                                   =     true
      force force ace_scopes_simplifiedZeroing                                    =     false
      force force ace_scopes_useLegacyUI                                          =     false
      force force ace_scopes_zeroReferenceBarometricPressure                      =     1013.25
      force force ace_scopes_zeroReferenceHumidity                                =     0
      force force ace_scopes_zeroReferenceTemperature                             =     15

ACE Volume
============

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Volume
   ^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      acex_volume_enabled                                                         =     false
      acex_volume_fadeDelay                                                       =     1
      acex_volume_lowerInVehicles                                                 =     false
      acex_volume_reduction                                                       =     5
      acex_volume_remindIfLowered                                                 =     false
      acex_volume_showNotification                                                =     true



ACE Arsenal
=============

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Arsenal
   ^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force ace_arsenal_allowDefaultLoadouts                                      =     false
      force ace_arsenal_allowSharedLoadouts                                       =     true
      ace_arsenal_camInverted                                                     =     false
      force ace_arsenal_enableIdentityTabs                                        =     true
      ace_arsenal_enableModIcons                                                  =     true
      ace_arsenal_EnableRPTLog                                                    =     true
      ace_arsenal_fontHeight                                                      =     5.5

ACE Fortify
=============

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Fortify
   ^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force ace_fortify_markObjectsOnMap                                          =     1
      force ace_fortify_timeCostCoefficient                                       =     1
      force ace_fortify_timeMin                                                   =     1.5
      acex_fortify_settingHint                                                    =     2



ACE Goggles
=============

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Goggles
   ^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      ace_goggles_effects                                                         =     2
      force force ace_goggles_showClearGlasses                                    =     false
      force force ace_goggles_showInThirdPerson                                   =     false

ACE Hearing
=============

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Hearing
   ^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force force ace_hearing_autoAddEarplugsToUnits                              =     false
      ace_hearing_disableEarRinging                                               =     true
      force force ace_hearing_earplugsVolume                                      =     0.5
      force force ace_hearing_enableCombatDeafness                                =     true
      force force ace_hearing_enabledForZeusUnits                                 =     false
      force force ace_hearing_unconsciousnessVolume                               =     0.4

ACE Medical
=============

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Medical
   ^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force force ace_medical_ai_enabledFor                                       =     2
      force force ace_medical_AIDamageThreshold                                   =     0.1
      force force ace_medical_bleedingCoefficient                                 =     0.3
      force force ace_medical_blood_bloodLifetime                                 =     300
      force force ace_medical_blood_enabledFor                                    =     2
      force force ace_medical_blood_maxBloodObjects                               =     500
      force ace_medical_deathChance                                               =     1
      force ace_medical_enableVehicleCrashes                                      =     true
      force force ace_medical_fatalDamageSource                                   =     2
      ace_medical_feedback_bloodVolumeEffectType                                  =     0
      ace_medical_feedback_enableHUDIndicators                                    =     true
      ace_medical_feedback_painEffectType                                         =     2
      force ace_medical_fractureChance                                            =     0.1
      force force ace_medical_fractures                                           =     2
      ace_medical_gui_bloodLossColor_0                                            =     [1,1,1,1]
      ace_medical_gui_bloodLossColor_1                                            =     [1,0.95,0.64,1]
      ace_medical_gui_bloodLossColor_2                                            =     [1,0.87,0.46,1]
      ace_medical_gui_bloodLossColor_3                                            =     [1,0.8,0.33,1]
      ace_medical_gui_bloodLossColor_4                                            =     [1,0.72,0.24,1]
      ace_medical_gui_bloodLossColor_5                                            =     [1,0.63,0.15,1]
      ace_medical_gui_bloodLossColor_6                                            =     [1,0.54,0.08,1]
      ace_medical_gui_bloodLossColor_7                                            =     [1,0.43,0.02,1]
      ace_medical_gui_bloodLossColor_8                                            =     [1,0.3,0,1]
      ace_medical_gui_bloodLossColor_9                                            =     [1,0,0,1]
      ace_medical_gui_damageColor_0                                               =     [1,1,1,1]
      ace_medical_gui_damageColor_1                                               =     [0.75,0.95,1,1]
      ace_medical_gui_damageColor_2                                               =     [0.62,0.86,1,1]
      ace_medical_gui_damageColor_3                                               =     [0.54,0.77,1,1]
      ace_medical_gui_damageColor_4                                               =     [0.48,0.67,1,1]
      ace_medical_gui_damageColor_5                                               =     [0.42,0.57,1,1]
      ace_medical_gui_damageColor_6                                               =     [0.37,0.47,1,1]
      ace_medical_gui_damageColor_7                                               =     [0.31,0.36,1,1]
      ace_medical_gui_damageColor_8                                               =     [0.22,0.23,1,1]
      ace_medical_gui_damageColor_9                                               =     [0,0,1,1]
      ace_medical_gui_enableActions                                               =     0
      force force ace_medical_gui_enableMedicalMenu                               =     1
      force force ace_medical_gui_enableSelfActions                               =     true
      ace_medical_gui_interactionMenuShowTriage                                   =     1
      force force ace_medical_gui_maxDistance                                     =     4
      force force ace_medical_gui_openAfterTreatment                              =     true
      force force ace_medical_ivFlowRate                                          =     1.5
      force force ace_medical_limping                                             =     0
      force force ace_medical_painCoefficient                                     =     0.4
      force ace_medical_painUnconsciousChance                                     =     0.1
      force force ace_medical_playerDamageThreshold                               =     1.6
      force force ace_medical_spontaneousWakeUpChance                             =     0.7
      force force ace_medical_spontaneousWakeUpEpinephrineBoost                   =     2.45
      force force ace_medical_statemachine_AIUnconsciousness                      =     true
      force ace_medical_statemachine_cardiacArrestBleedoutEnabled                 =     true
      force force ace_medical_statemachine_cardiacArrestTime                      =     900
      force force ace_medical_statemachine_fatalInjuriesAI                        =     0
      force force ace_medical_statemachine_fatalInjuriesPlayer                    =     2
      force force ace_medical_treatment_advancedBandages                          =     2
      force force ace_medical_treatment_advancedDiagnose                          =     2
      force force ace_medical_treatment_advancedMedication                        =     true
      force ace_medical_treatment_allowBodyBagUnconscious                         =     false
      force force ace_medical_treatment_allowLitterCreation                       =     true
      force force ace_medical_treatment_allowSelfIV                               =     1
      force ace_medical_treatment_allowSelfPAK                                    =     0
      force force ace_medical_treatment_allowSelfStitch                           =     0
      force force ace_medical_treatment_allowSharedEquipment                      =     0
      force ace_medical_treatment_clearTrauma                                     =     1
      force force ace_medical_treatment_consumePAK                                =     1
      force force ace_medical_treatment_consumeSurgicalKit                        =     0
      force force ace_medical_treatment_convertItems                              =     0
      force ace_medical_treatment_cprSuccessChanceMax                             =     0.65
      force ace_medical_treatment_cprSuccessChanceMin                             =     0.4
      force force ace_medical_treatment_holsterRequired                           =     0
      force force ace_medical_treatment_litterCleanupDelay                        =     150
      force force ace_medical_treatment_locationEpinephrine                       =     0
      force ace_medical_treatment_locationIV                                      =     0
      force force ace_medical_treatment_locationPAK                               =     0
      force force ace_medical_treatment_locationsBoostTraining                    =     true
      force force ace_medical_treatment_locationSurgicalKit                       =     0
      force force ace_medical_treatment_maxLitterObjects                          =     50
      force force ace_medical_treatment_medicEpinephrine                          =     0
      force ace_medical_treatment_medicIV                                         =     1
      force force ace_medical_treatment_medicPAK                                  =     1
      force force ace_medical_treatment_medicSurgicalKit                          =     1
      force force ace_medical_treatment_timeCoefficientPAK                        =     1
      force ace_medical_treatment_treatmentTimeAutoinjector                       =     5
      force ace_medical_treatment_treatmentTimeBodyBag                            =     15
      force ace_medical_treatment_treatmentTimeCPR                                =     15
      force ace_medical_treatment_treatmentTimeIV                                 =     12
      force ace_medical_treatment_treatmentTimeSplint                             =     7
      force ace_medical_treatment_treatmentTimeTourniquet                         =     7
      force ace_medical_treatment_woundReopenChance                               =     1
      force ace_medical_treatment_woundStitchTime                                 =     5

ACE Respawn
=============

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Respawn
   ^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force force ace_respawn_removeDeadBodiesDisconnected                        =     true
      force force ace_respawn_savePreDeathGear                                    =     false

ACE Sitting
=============

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Sitting
   ^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force acex_sitting_enable                                                   =     true

ACE Weapons
=============

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Weapons
   ^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force force ace_common_persistentLaserEnabled                               =     true
      force force ace_laserpointer_enabled                                        =     true
      force force ace_reload_displayText                                          =     true
      ace_reload_showCheckAmmoSelf                                                =     true
      force force ace_weaponselect_displayText                                    =     true

ACE Weather
=============

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Weather
   ^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force force ace_weather_enabled                                             =     true
      ace_weather_showCheckAirTemperature                                         =     true
      force force ace_weather_updateInterval                                      =     60
      force force ace_weather_windSimulation                                      =     true

ACE Captives
==============

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Captives
   ^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force force ace_captives_allowHandcuffOwnSide                               =     false
      force force ace_captives_allowSurrender                                     =     true
      force force ace_captives_requireSurrender                                   =     2
      force force ace_captives_requireSurrenderAi                                 =     true

ACE Cook off
==============

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Cook off
   ^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force force ace_cookoff_ammoCookoffDuration                                 =     0.5
      force force ace_cookoff_enable                                              =     2
      force force ace_cookoff_enableAmmobox                                       =     true
      force force ace_cookoff_enableAmmoCookoff                                   =     true
      force ace_cookoff_enableFire                                                =     true
      force force ace_cookoff_probabilityCoef                                     =     1

ACE Dragging
==============

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Dragging
   ^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      ace_dragging_dragAndFire                                                    =     true



ACE G-Forces
==============

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE G-Forces
   ^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force ace_gforces_coef                                                      =     0.8
      force force ace_gforces_enabledFor                                          =     1

ACE Grenades
==============

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Grenades
   ^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force ace_grenades_convertExplosives                                        =     false

ACE Headless
==============

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Headless
   ^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force acex_headless_delay                                                   =     15
      force acex_headless_enabled                                                 =     false
      force acex_headless_endMission                                              =     0
      force acex_headless_log                                                     =     false
      force acex_headless_transferLoadout                                         =     0

ACE Pointing
==============

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Pointing
   ^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force force ace_finger_enabled                                              =     true
      ace_finger_indicatorColor                                                   =     [1,0.503034,0,1]
      force force ace_finger_indicatorForSelf                                     =     true
      force force ace_finger_maxRange                                             =     5.01867

ACE Trenches
==============

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Trenches
   ^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force ace_trenches_bigEnvelopeDigDuration                                   =     25
      force ace_trenches_bigEnvelopeRemoveDuration                                =     15
      force ace_trenches_smallEnvelopeDigDuration                                 =     20
      force ace_trenches_smallEnvelopeRemoveDuration                              =     12

ACE Vehicles
==============

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Vehicles
   ^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      ace_vehicles_hideEjectAction                                                =     true
      force ace_vehicles_keepEngineRunning                                        =     false
      ace_vehicles_speedLimiterStep                                               =     5

ACE Artillery
===============

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Artillery
   ^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force ace_artillerytables_advancedCorrections                               =     false
      force ace_artillerytables_disableArtilleryComputer                          =     false
      force force ace_mk6mortar_airResistanceEnabled                              =     false
      force force ace_mk6mortar_allowCompass                                      =     true
      force force ace_mk6mortar_allowComputerRangefinder                          =     true
      force force ace_mk6mortar_useAmmoHandling                                   =     false

ACE Logistics
===============

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Logistics
   ^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force force ace_cargo_enable                                                =     true
      ace_cargo_enableRename                                                      =     true
      force force ace_cargo_loadTimeCoefficient                                   =     3.46515
      ace_cargo_openAfterUnload                                                   =     0
      force force ace_cargo_paradropTimeCoefficent                                =     2.5
      force force ace_rearm_distance                                              =     20
      force force ace_rearm_level                                                 =     1
      force force ace_rearm_supply                                                =     0
      force force ace_refuel_hoseLength                                           =     12
      force force ace_refuel_rate                                                 =     1
      force force ace_repair_addSpareParts                                        =     true
      force force ace_repair_autoShutOffEngineWhenStartingRepair                  =     true
      force force ace_repair_consumeItem_toolKit                                  =     0
      force force ace_repair_displayTextOnRepair                                  =     true
      force force ace_repair_engineerSetting_fullRepair                           =     1
      force force ace_repair_engineerSetting_repair                               =     1
      force force ace_repair_engineerSetting_wheel                                =     0
      force force ace_repair_fullRepairLocation                                   =     3
      force force ace_repair_fullRepairRequiredItems                              =     ["ace_repair_anyToolKit"]
      force ace_repair_locationsBoostTraining                                     =     false
      force force ace_repair_miscRepairRequiredItems                              =     ["ace_repair_anyToolKit"]
      force force ace_repair_repairDamageThreshold                                =     0.6
      force force ace_repair_repairDamageThreshold_engineer                       =     0.4
      force force ace_repair_wheelRepairRequiredItems                             =     []

ACE Map Tools
===============

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Map Tools
   ^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      ace_maptools_drawStraightLines                                              =     true
      ace_maptools_rotateModifierKey                                              =     1

ACE Name Tags
===============

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Name Tags
   ^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force ace_nametags_ambientBrightnessAffectViewDist                          =     1
      ace_nametags_defaultNametagColor                                            =     [0.77,0.51,0.08,1]
      ace_nametags_nametagColorBlue                                               =     [0.67,0.67,1,1]
      ace_nametags_nametagColorGreen                                              =     [0.67,1,0.67,1]
      ace_nametags_nametagColorMain                                               =     [1,1,1,1]
      ace_nametags_nametagColorRed                                                =     [1,0.67,0.67,1]
      ace_nametags_nametagColorYellow                                             =     [1,1,0.67,1]
      force ace_nametags_playerNamesMaxAlpha                                      =     0.8
      force ace_nametags_playerNamesViewDistance                                  =     5
      force ace_nametags_showCursorTagForVehicles                                 =     false
      ace_nametags_showNamesForAI                                                 =     false
      ace_nametags_showPlayerNames                                                =     1
      ace_nametags_showPlayerRanks                                                =     false
      ace_nametags_showSoundWaves                                                 =     1
      ace_nametags_showVehicleCrewInfo                                            =     true
      ace_nametags_tagSize                                                        =     2

ACE Spectator
===============

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Spectator
   ^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force ace_spectator_enableAI                                                =     false
      ace_spectator_maxFollowDistance                                             =     5
      force ace_spectator_restrictModes                                           =     0
      force ace_spectator_restrictVisions                                         =     0

ACE Explosives
================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Explosives
   ^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      ace_explosives_customTimerDefault                                           =     30
      force ace_explosives_customTimerMax                                         =     900
      force ace_explosives_customTimerMin                                         =     5
      force force ace_explosives_explodeOnDefuse                                  =     true
      force force ace_explosives_punishNonSpecialists                             =     true
      force force ace_explosives_requireSpecialist                                =     false

ACE Interaction
=================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Interaction
   ^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force force ace_interaction_disableNegativeRating                           =     false
      force ace_interaction_enableGroupRenaming                                   =     true
      force force ace_interaction_enableMagazinePassing                           =     true
      force force ace_interaction_enableTeamManagement                            =     true
      ace_interaction_enableWeaponAttachments                                     =     true
      force ace_interaction_interactWithTerrainObjects                            =     false

ACE Nightvision
=================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Nightvision
   ^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force force ace_nightvision_aimDownSightsBlur                               =     0.14061
      force force ace_nightvision_disableNVGsWithSights                           =     false
      force force ace_nightvision_effectScaling                                   =     0.284091
      force force ace_nightvision_fogScaling                                      =     0.241047
      force force ace_nightvision_noiseScaling                                    =     0.241047
      force force ace_nightvision_shutterEffects                                  =     false

ACE Overheating
=================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Overheating
   ^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force ace_overheating_cookoffCoef                                           =     2.50373
      force ace_overheating_coolingCoef                                           =     1
      force force ace_overheating_displayTextOnJam                                =     true
      force force ace_overheating_enabled                                         =     true
      force ace_overheating_heatCoef                                              =     0.75
      force ace_overheating_jamChanceCoef                                         =     0.8
      force force ace_overheating_overheatingDispersion                           =     true
      force ace_overheating_overheatingRateOfFire                                 =     true
      ace_overheating_particleEffectsAndDispersionDistance                        =     3000
      ace_overheating_showParticleEffects                                         =     true
      ace_overheating_showParticleEffectsForEveryone                              =     false
      force ace_overheating_suppressorCoef                                        =     1
      force force ace_overheating_unJamFailChance                                 =     0.5
      force force ace_overheating_unJamOnreload                                   =     false
      force ace_overheating_unJamOnSwapBarrel                                     =     false

ACE Quick Mount
=================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Quick Mount
   ^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force force ace_quickmount_distance                                         =     3
      force force ace_quickmount_enabled                                          =     true
      force force ace_quickmount_enableMenu                                       =     3
      ace_quickmount_priority                                                     =     0
      force force ace_quickmount_speed                                            =     15

ACE Map Gestures
==================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Map Gestures
   ^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      ace_map_gestures_allowCurator                                               =     true
      ace_map_gestures_allowSpectator                                             =     true
      ace_map_gestures_briefingMode                                               =     0
      force ace_map_gestures_defaultColor                                         =     [1,0.88,0,0.7]
      force ace_map_gestures_defaultLeadColor                                     =     [1,0,0,0.95]
      force ace_map_gestures_enabled                                              =     true
      force ace_map_gestures_interval                                             =     0.03
      force ace_map_gestures_maxRange                                             =     7
      force ace_map_gestures_maxRangeCamera                                       =     14
      ace_map_gestures_nameTextColor                                              =     [0.2,0.2,0.2,0.3]
      force ace_map_gestures_onlyShowFriendlys                                    =     false

ACE Switch Units
==================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Switch Units
   ^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force ace_switchunits_enableSafeZone                                        =     false
      force ace_switchunits_enableSwitchUnits                                     =     false
      force ace_switchunits_safeZoneRadius                                        =     100
      force ace_switchunits_switchToCivilian                                      =     false
      force ace_switchunits_switchToEast                                          =     false
      force ace_switchunits_switchToIndependent                                   =     false
      force ace_switchunits_switchToWest                                          =     false

ACE Vehicle Lock
==================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Vehicle Lock
   ^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force force ace_vehiclelock_defaultLockpickStrength                         =     10
      force force ace_vehiclelock_lockVehicleInventory                            =     false
      force force ace_vehiclelock_vehicleStartingLockState                        =     -1

ACE Field Rations
===================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Field Rations
   ^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force acex_field_rations_affectAdvancedFatigue                              =     true
      force acex_field_rations_enabled                                            =     false
      acex_field_rations_hudShowLevel                                             =     0
      acex_field_rations_hudTransparency                                          =     -1
      acex_field_rations_hudType                                                  =     0
      force acex_field_rations_hungerSatiated                                     =     1
      force acex_field_rations_terrainObjectActions                               =     true
      force acex_field_rations_thirstQuenched                                     =     1
      force acex_field_rations_timeWithoutFood                                    =     2
      force acex_field_rations_timeWithoutWater                                   =     2
      force acex_field_rations_waterSourceActions                                 =     2

ACE Uncategorized
===================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Uncategorized
   ^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force force ace_fastroping_requireRopeItems                                 =     false
      force ace_gunbag_swapGunbagEnabled                                          =     true
      force force ace_hitreactions_minDamageToTrigger                             =     0.122781
      ace_inventory_inventoryDisplaySize                                          =     1
      force force ace_laser_dispersionCount                                       =     2
      force force ace_microdagr_mapDataAvailable                                  =     2
      force force ace_microdagr_waypointPrecision                                 =     3
      ace_optionsmenu_showNewsOnMainMenu                                          =     false
      force force ace_overpressure_distanceCoefficient                            =     1
      force ace_parachute_failureChance                                           =     0
      force force ace_parachute_hideAltimeter                                     =     true
      ace_tagging_quickTag                                                        =     0

ACE User Interface
====================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE User Interface
   ^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force force ace_ui_allowSelectiveUI                                         =     false
      force force ace_ui_ammoCount                                                =     false
      force force ace_ui_ammoType                                                 =     false
      force force ace_ui_commandMenu                                              =     true
      force ace_ui_enableSpeedIndicator                                           =     true
      force force ace_ui_firingMode                                               =     true
      force force ace_ui_groupBar                                                 =     true
      force force ace_ui_gunnerAmmoCount                                          =     true
      force force ace_ui_gunnerAmmoType                                           =     true
      force force ace_ui_gunnerFiringMode                                         =     true
      force force ace_ui_gunnerLaunchableCount                                    =     true
      force force ace_ui_gunnerLaunchableName                                     =     true
      force force ace_ui_gunnerMagCount                                           =     true
      force force ace_ui_gunnerWeaponLowerInfoBackground                          =     true
      force force ace_ui_gunnerWeaponName                                         =     true
      force force ace_ui_gunnerWeaponNameBackground                               =     true
      force force ace_ui_gunnerZeroing                                            =     true
      force force ace_ui_magCount                                                 =     true
      force force ace_ui_soldierVehicleWeaponInfo                                 =     true
      force force ace_ui_staminaBar                                               =     true
      force force ace_ui_stance                                                   =     true
      force force ace_ui_throwableCount                                           =     false
      force force ace_ui_throwableName                                            =     true
      force force ace_ui_vehicleAltitude                                          =     true
      force force ace_ui_vehicleCompass                                           =     true
      force force ace_ui_vehicleDamage                                            =     true
      force force ace_ui_vehicleFuelBar                                           =     true
      force force ace_ui_vehicleInfoBackground                                    =     true
      force force ace_ui_vehicleName                                              =     true
      force force ace_ui_vehicleNameBackground                                    =     true
      force force ace_ui_vehicleRadar                                             =     true
      force force ace_ui_vehicleSpeed                                             =     true
      force force ace_ui_weaponLowerInfoBackground                                =     true
      force force ace_ui_weaponName                                               =     true
      force force ace_ui_weaponNameBackground                                     =     true
      force force ace_ui_zeroing                                                  =     true

ACE Magazine Repack
=====================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Magazine Repack
   ^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      ace_magazinerepack_repackLoadedMagazines                                    =     true
      force force ace_magazinerepack_timePerAmmo                                  =     1.5
      force force ace_magazinerepack_timePerBeltLink                              =     8
      force force ace_magazinerepack_timePerMagazine                              =     2

ACE Wind Deflection
=====================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Wind Deflection
   ^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force force ace_winddeflection_enabled                                      =     true
      force force ace_winddeflection_simulationInterval                           =     0.05
      force force ace_winddeflection_vehicleEnabled                               =     true

ACE Advanced Fatigue
======================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Advanced Fatigue
   ^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force ace_advanced_fatigue_enabled                                          =     true
      force ace_advanced_fatigue_enableStaminaBar                                 =     true
      ace_advanced_fatigue_fadeStaminaBar                                         =     true
      force ace_advanced_fatigue_loadFactor                                       =     1
      force ace_advanced_fatigue_performanceFactor                                =     1
      force ace_advanced_fatigue_recoveryFactor                                   =     3
      force ace_advanced_fatigue_swayFactor                                       =     1
      force ace_advanced_fatigue_terrainGradientFactor                            =     1

ACE Interaction Menu
======================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Interaction Menu
   ^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      ace_gestures_showOnInteractionMenu                                          =     2
      ace_interact_menu_actionOnKeyRelease                                        =     true
      ace_interact_menu_addBuildingActions                                        =     false
      ace_interact_menu_alwaysUseCursorInteraction                                =     true
      ace_interact_menu_alwaysUseCursorSelfInteraction                            =     true
      ace_interact_menu_colorShadowMax                                            =     [0,0,0,1]
      ace_interact_menu_colorShadowMin                                            =     [0,0,0,0.25]
      ace_interact_menu_colorTextMax                                              =     [1,1,1,1]
      ace_interact_menu_colorTextMin                                              =     [1,1,1,0.25]
      ace_interact_menu_consolidateSingleChild                                    =     false
      ace_interact_menu_cursorKeepCentered                                        =     false
      ace_interact_menu_cursorKeepCenteredSelfInteraction                         =     false
      force force ace_interact_menu_menuAnimationSpeed                            =     0
      ace_interact_menu_menuBackground                                            =     0
      ace_interact_menu_menuBackgroundSelf                                        =     0
      ace_interact_menu_selectorColor                                             =     [1,0,0]
      ace_interact_menu_shadowSetting                                             =     2
      ace_interact_menu_textSize                                                  =     2
      ace_interact_menu_useListMenu                                               =     true
      ace_interact_menu_useListMenuSelf                                           =     true

ACE View Restriction
======================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE View Restriction
   ^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force acex_viewrestriction_mode                                             =     0
      force acex_viewrestriction_modeSelectiveAir                                 =     0
      force acex_viewrestriction_modeSelectiveFoot                                =     0
      force acex_viewrestriction_modeSelectiveLand                                =     0
      force acex_viewrestriction_modeSelectiveSea                                 =     0
      acex_viewrestriction_preserveView                                           =     false

ACE Advanced Throwing
=======================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Advanced Throwing
   ^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force force ace_advanced_throwing_enabled                                   =     true
      force force ace_advanced_throwing_enablePickUp                              =     true
      force force ace_advanced_throwing_enablePickUpAttached                      =     true
      force force ace_advanced_throwing_showMouseControls                         =     true
      force force ace_advanced_throwing_showThrowArc                              =     true

ACE Advanced Ballistics
=========================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Advanced Ballistics
   ^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force force ace_advanced_ballistics_ammoTemperatureEnabled                  =     true
      force force ace_advanced_ballistics_barrelLengthInfluenceEnabled            =     true
      force force ace_advanced_ballistics_bulletTraceEnabled                      =     true
      force force ace_advanced_ballistics_enabled                                 =     true
      force force ace_advanced_ballistics_muzzleVelocityVariationEnabled          =     true
      force force ace_advanced_ballistics_simulationInterval                      =     0.05

ACE Crew Served Weapons
=========================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Crew Served Weapons
   ^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force force ace_csw_ammoHandling                                            =     1
      force force ace_csw_defaultAssemblyMode                                     =     false
      force force ace_csw_dragAfterDeploy                                         =     false
      force force ace_csw_handleExtraMagazines                                    =     false
      force force ace_csw_progressBarTimeCoefficent                               =     1

ACE View Distance Limiter
===========================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE View Distance Limiter
   ^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force force ace_viewdistance_enabled                                        =     true
      force force ace_viewdistance_limitViewDistance                              =     8000
      ace_viewdistance_objectViewDistanceCoeff                                    =     0
      ace_viewdistance_viewDistanceAirVehicle                                     =     8
      ace_viewdistance_viewDistanceLandVehicle                                    =     4
      ace_viewdistance_viewDistanceOnFoot                                         =     4

ACE Advanced Vehicle Damage
=============================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Advanced Vehicle Damage
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force ace_vehicle_damage_enableCarDamage                                    =     false
      force ace_vehicle_damage_enabled                                            =     false
      force ace_vehicle_damage_removeAmmoDuringCookoff                            =     true

ACE Fragmentation Simulation
==============================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Fragmentation Simulation
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force force ace_frag_enabled                                                =     false
      force force ace_frag_maxTrack                                               =     0
      force force ace_frag_maxTrackPerFrame                                       =     0
      force force ace_frag_reflectionsEnabled                                     =     false
      force force ace_frag_spallEnabled                                           =     false

ACE Interaction Menu (Self) - More
====================================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Interaction Menu (Self) - More
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      ace_interact_menu_more__ACE_CheckAirTemperature                             =     false
      ace_interact_menu_more__ace_csw_deploy                                      =     false
      ace_interact_menu_more__ACE_Equipment                                       =     false
      ace_interact_menu_more__ACE_Explosives                                      =     false
      ace_interact_menu_more__ace_field_rations                                   =     false
      ace_interact_menu_more__ace_fortify                                         =     false
      ace_interact_menu_more__ace_gestures                                        =     false
      ace_interact_menu_more__ace_intelitems                                      =     false
      ace_interact_menu_more__ACE_MapFlashlight                                   =     false
      ace_interact_menu_more__ACE_MapGpsHide                                      =     false
      ace_interact_menu_more__ACE_MapGpsShow                                      =     false
      ace_interact_menu_more__ACE_MapTools                                        =     false
      ace_interact_menu_more__ACE_Medical                                         =     false
      ace_interact_menu_more__ACE_Medical_Menu                                    =     false
      ace_interact_menu_more__ACE_MoveRallypoint                                  =     false
      ace_interact_menu_more__ACE_RepackMagazines                                 =     false
      ace_interact_menu_more__ace_sandbag_place                                   =     false
      ace_interact_menu_more__ACE_StartSurrenderingSelf                           =     false
      ace_interact_menu_more__ACE_StopEscortingSelf                               =     false
      ace_interact_menu_more__ACE_StopSurrenderingSelf                            =     false
      ace_interact_menu_more__ACE_Tags                                            =     false
      ace_interact_menu_more__ACE_TeamManagement                                  =     false
      ace_interact_menu_more__ace_zeus_create                                     =     false
      ace_interact_menu_more__ace_zeus_delete                                     =     false
      ace_interact_menu_more__acex_sitting_Stand                                  =     false
      ace_interact_menu_more__TFAR_Radio                                          =     false
      ace_interact_menu_more__UPSL_aime_change_ammo_ammo_class                    =     false
      ace_interact_menu_more__UPSL_aime_inventory_assemble_action                 =     false
      ace_interact_menu_more__UPSL_aime_uav_terminal_uav_action                   =     false
      ace_interact_menu_more__UPSL_aime_vehicle_controls_user_actions             =     false
      ace_interact_menu_more__UPSL_aime_vehicle_seats_change_action               =     false
      ace_interact_menu_more__UPSL_aime_vehicle_seats_eject_action                =     false
      ace_interact_menu_more__UPSL_aime_vehicle_seats_getout_action               =     false
      ace_interact_menu_more__UPSL_aime_vehicle_seats_turnin_action               =     false

ACE Interaction Menu (Self) - Move to Root
============================================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   ACE Interaction Menu (Self) - Move to Root
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      ace_interact_menu_moveToRoot__ACE_Equipment__ace_atragmx_open               =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_attach_Attach              =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_attach_Detach              =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ACE_CheckDogtags               =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ACE_Chemlights                 =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_dagr_menu                  =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_dagr_menu__ace_dagr_toggle =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_goggles_wipeGlasses        =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_gunbag_actions             =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_gunbag_actions__ace_gunbag_status =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_gunbag_actions__ace_gunbag_weaponOff =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_gunbag_actions__ace_gunbag_weaponSwap =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_gunbag_actions__ace_gunbag_weaponTo =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_huntir_open                =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_interaction_weaponAttachments =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_kestrel4500_open           =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_kestrel4500_open__ace_kestrel4500_hide =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_kestrel4500_open__ace_kestrel4500_show =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_microdagr_configure        =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_microdagr_configure__ace_microdagr_close =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_microdagr_configure__ace_microdagr_show =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_minedetector_metalDetector =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_minedetector_metalDetector__ace_minedetector_activate =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_minedetector_metalDetector__ace_minedetector_connectHeadphones =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_minedetector_metalDetector__ace_minedetector_deactivate =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_minedetector_metalDetector__ace_minedetector_disconnectHeadphones =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_mk6mortar_rangetable       =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_overheating_CheckTemperature =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_overheating_CheckTemperatureSpareBarrels =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_overheating_CoolWeaponWithItem =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_overheating_SwapBarrel     =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_overheating_UnJam          =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ACE_PutInEarplugs              =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_rangecard_open             =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_rangecard_open__ace_rangecard_makeCopy =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_rangecard_open__ace_rangecard_openCopy =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_reload_checkAmmo           =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ACE_RemoveEarplugs             =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_scopes_adjustZero          =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_scopes_resetZero           =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_spottingscope_place        =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ACE_TacticalLadders            =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_trenches                   =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_trenches__ace_trenches_digEnvelopeBig =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_trenches__ace_trenches_digEnvelopeSmall =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_trenches__grad_trenches_digEnvelopeGiant =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_trenches__grad_trenches_digEnvelopeLongNameEmplacment =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_trenches__grad_trenches_digEnvelopeShort =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_trenches__grad_trenches_digEnvelopeVehicle =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__ace_tripod_place               =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__UPSL_aime_uav_terminal_gps_action =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__UPSL_aime_uav_terminal_term_action =     false
      ace_interact_menu_moveToRoot__ACE_Equipment__UPSL_aime_uav_terminal_uav_action =     false
      ace_interact_menu_moveToRoot__ACE_Explosives__ACE_Cellphone                 =     false
      ace_interact_menu_moveToRoot__ACE_Explosives__ACE_Place                     =     false
      ace_interact_menu_moveToRoot__ace_gestures__ace_gestures_Advance            =     false
      ace_interact_menu_moveToRoot__ace_gestures__ace_gestures_CeaseFire          =     false
      ace_interact_menu_moveToRoot__ace_gestures__ace_gestures_Cover              =     false
      ace_interact_menu_moveToRoot__ace_gestures__ace_gestures_Engage             =     false
      ace_interact_menu_moveToRoot__ace_gestures__ace_gestures_Follow             =     false
      ace_interact_menu_moveToRoot__ace_gestures__ace_gestures_Forward            =     false
      ace_interact_menu_moveToRoot__ace_gestures__ace_gestures_Freeze             =     false
      ace_interact_menu_moveToRoot__ace_gestures__ace_gestures_Go                 =     false
      ace_interact_menu_moveToRoot__ace_gestures__ace_gestures_Hold               =     false
      ace_interact_menu_moveToRoot__ace_gestures__ace_gestures_Point              =     false
      ace_interact_menu_moveToRoot__ace_gestures__ace_gestures_Regroup            =     false
      ace_interact_menu_moveToRoot__ace_gestures__ace_gestures_Stop               =     false
      ace_interact_menu_moveToRoot__ace_gestures__ace_gestures_Up                 =     false
      ace_interact_menu_moveToRoot__ace_gestures__ace_gestures_Warning            =     false
      ace_interact_menu_moveToRoot__ACE_MapTools__ACE_MapToolsAlignCompass        =     false
      ace_interact_menu_moveToRoot__ACE_MapTools__ACE_MapToolsAlignNorth          =     false
      ace_interact_menu_moveToRoot__ACE_MapTools__ACE_MapToolsHide                =     false
      ace_interact_menu_moveToRoot__ACE_MapTools__ACE_MapToolsShowNormal          =     false
      ace_interact_menu_moveToRoot__ACE_MapTools__ACE_MapToolsShowSmall           =     false
      ace_interact_menu_moveToRoot__ACE_Medical__ACE_ArmLeft                      =     false
      ace_interact_menu_moveToRoot__ACE_Medical__ACE_ArmRight                     =     false
      ace_interact_menu_moveToRoot__ACE_Medical__ACE_Head                         =     false
      ace_interact_menu_moveToRoot__ACE_Medical__ACE_LegLeft                      =     false
      ace_interact_menu_moveToRoot__ACE_Medical__ACE_LegRight                     =     false
      ace_interact_menu_moveToRoot__ACE_Medical__ACE_Torso                        =     false
      ace_interact_menu_moveToRoot__ACE_Medical__ACE_Torso__TriageCard            =     false
      ace_interact_menu_moveToRoot__ACE_TeamManagement__ACE_BecomeLeader          =     false
      ace_interact_menu_moveToRoot__ACE_TeamManagement__ACE_JoinTeamBlue          =     false
      ace_interact_menu_moveToRoot__ACE_TeamManagement__ACE_JoinTeamGreen         =     false
      ace_interact_menu_moveToRoot__ACE_TeamManagement__ACE_JoinTeamRed           =     false
      ace_interact_menu_moveToRoot__ACE_TeamManagement__ACE_JoinTeamYellow        =     false
      ace_interact_menu_moveToRoot__ACE_TeamManagement__ACE_LeaveGroup            =     false
      ace_interact_menu_moveToRoot__ACE_TeamManagement__ACE_LeaveTeam             =     false
      ace_interact_menu_moveToRoot__ACE_TeamManagement__ACE_RenameGroup           =     false
      ace_interact_menu_moveToRoot__ACE_TeamManagement__diwako_dui_buddy_buddy_action_team_remove =     false
      ace_interact_menu_moveToRoot__ACE_TeamManagement__UPSL_aime_group_drop_leader_action =     false
      ace_interact_menu_moveToRoot__UPSL_aime_vehicle_seats_change_action__UPSL_aime_vehicle_seats_turnout_action =     false
      ace_interact_menu_moveToRoot__UPSL_aime_vehicle_seats_eject_action__UPSL_aime_vehicle_seats_eject_confirm_action =     false
      ace_interact_menu_moveToRoot__UPSL_aime_vehicle_seats_getout_action__UPSL_aime_vehicle_seats_eject_action =     false

AIME General
==============

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   AIME General
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      UPSL_aime_setting_hide                                                      =     true

GRAD Trenches
===============

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   GRAD Trenches
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force force grad_trenches_functions_allowBigEnvelope                        =     true
      force force grad_trenches_functions_allowCamouflage                         =     true
      force force grad_trenches_functions_allowDigging                            =     true
      force grad_trenches_functions_allowEffects                                  =     true
      force force grad_trenches_functions_allowGiantEnvelope                      =     true
      force grad_trenches_functions_allowHitDecay                                 =     true
      force force grad_trenches_functions_allowLongEnvelope                       =     true
      force force grad_trenches_functions_allowShortEnvelope                      =     true
      force force grad_trenches_functions_allowSmallEnvelope                      =     true
      force force grad_trenches_functions_allowTrenchDecay                        =     true
      force force grad_trenches_functions_allowVehicleEnvelope                    =     true
      force grad_trenches_functions_bigEnvelopeDamageMultiplier                   =     2
      force force grad_trenches_functions_bigEnvelopeDigTime                      =     60
      force grad_trenches_functions_bigEnvelopeRemovalTime                        =     30
      force force grad_trenches_functions_buildFatigueFactor                      =     0
      force force grad_trenches_functions_camouflageRequireEntrenchmentTool       =     true
      force grad_trenches_functions_createTrenchMarker                            =     false
      force force grad_trenches_functions_decayTime                               =     1800
      force grad_trenches_functions_giantEnvelopeDamageMultiplier                 =     1
      force force grad_trenches_functions_giantEnvelopeDigTime                    =     180
      force grad_trenches_functions_giantEnvelopeRemovalTime                      =     90
      force grad_trenches_functions_hitDecayMultiplier                            =     1
      force force grad_trenches_functions_LongEnvelopeDigTime                     =     100
      force grad_trenches_functions_LongEnvelopeRemovalTime                       =     50
      force grad_trenches_functions_shortEnvelopeDamageMultiplier                 =     2
      force force grad_trenches_functions_shortEnvelopeDigTime                    =     30
      force grad_trenches_functions_shortEnvelopeRemovalTime                      =     15
      force grad_trenches_functions_smallEnvelopeDamageMultiplier                 =     3
      force force grad_trenches_functions_smallEnvelopeDigTime                    =     40
      force grad_trenches_functions_smallEnvelopeRemovalTime                      =     20
      force force grad_trenches_functions_stopBuildingAtFatigueMax                =     true
      force force grad_trenches_functions_timeoutToDecay                          =     3600
      force grad_trenches_functions_vehicleEnvelopeDamageMultiplier               =     1
      force force grad_trenches_functions_vehicleEnvelopeDigTime                  =     180
      force grad_trenches_functions_vehicleEnvelopeRemovalTime                    =     90

Zeus Enhanced
===============

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   Zeus Enhanced
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      zen_camera_adaptiveSpeed                                                    =     true
      zen_camera_defaultSpeedCoef                                                 =     1
      zen_camera_fastSpeedCoef                                                    =     1
      zen_camera_followTerrain                                                    =     true
      force zen_common_ascensionMessages                                          =     false
      force zen_common_autoAddObjects                                             =     true
      force zen_common_cameraBird                                                 =     false
      zen_common_darkMode                                                         =     false
      zen_common_disableGearAnim                                                  =     true
      zen_common_preferredArsenal                                                 =     1
      zen_compat_ace_hideModules                                                  =     true
      zen_context_menu_enabled                                                    =     2
      zen_context_menu_overrideWaypoints                                          =     false
      zen_editor_addGroupIcons                                                    =     false
      zen_editor_declutterEmptyTree                                               =     true
      zen_editor_disableLiveSearch                                                =     false
      zen_editor_moveDisplayToEdge                                                =     true
      force zen_editor_parachuteSounds                                            =     true
      zen_editor_previews_enabled                                                 =     true
      zen_editor_randomizeCopyPaste                                               =     false
      zen_editor_removeWatermark                                                  =     true
      zen_editor_unitRadioMessages                                                =     0
      zen_placement_enabled                                                       =     true
      zen_remote_control_cameraExitPosition                                       =     2
      zen_visibility_enabled                                                      =     true
      zen_vision_enableBlackHot                                                   =     false
      zen_vision_enableBlackHotGreenCold                                          =     false
      zen_vision_enableBlackHotRedCold                                            =     false
      zen_vision_enableGreenHotCold                                               =     false
      zen_vision_enableNVG                                                        =     true
      zen_vision_enableRedGreenThermal                                            =     false
      zen_vision_enableRedHotCold                                                 =     false
      zen_vision_enableWhiteHot                                                   =     true
      zen_vision_enableWhiteHotRedCold                                            =     false

AIME Inventory
================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   AIME Inventory
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      UPSL_aime_inventory_setting_assemble_action                                 =     true
      UPSL_aime_inventory_setting_backpack_action                                 =     true
      UPSL_aime_inventory_setting_holder_action                                   =     true
      UPSL_aime_inventory_setting_open_action                                     =     true

VET_Unflipping
================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   VET_Unflipping
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force vet_unflipping_require_serviceVehicle                                 =     false
      force vet_unflipping_require_toolkit                                        =     false
      force vet_unflipping_time                                                   =     20
      force vet_unflipping_unit_man_limit                                         =     7
      force vet_unflipping_unit_mass_limit                                        =     3000
      force vet_unflipping_vehicle_mass_limit                                     =     100000

AIME Vehicle Seats
====================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   AIME Vehicle Seats
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      UPSL_aime_vehicle_seats_setting_change_action                               =     true
      UPSL_aime_vehicle_seats_setting_force_eject                                 =     false
      UPSL_aime_vehicle_seats_setting_getin_action                                =     true
      UPSL_aime_vehicle_seats_setting_getout_action                               =     true
      UPSL_aime_vehicle_seats_setting_turnout_action                              =     true

AIME Ammo Type Menu
=====================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   AIME Ammo Type Menu
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      UPSL_aime_change_ammo_setting_ammo_class                                    =     true
      UPSL_aime_change_ammo_setting_vehicle_ammo_class                            =     true

AIME Group Management
=======================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   AIME Group Management
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      UPSL_aime_group_setting_drop_leader_action                                  =     true

AIME Vehicle Controls
=======================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   AIME Vehicle Controls
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      UPSL_aime_vehicle_controls_setting_arty_computer_action                     =     true
      UPSL_aime_vehicle_controls_setting_collision_action                         =     true
      UPSL_aime_vehicle_controls_setting_engine_action                            =     true
      UPSL_aime_vehicle_controls_setting_flaps_action                             =     true
      UPSL_aime_vehicle_controls_setting_gear_action                              =     true
      UPSL_aime_vehicle_controls_setting_hover_action                             =     true
      UPSL_aime_vehicle_controls_setting_lights_action                            =     true
      UPSL_aime_vehicle_controls_setting_manual_action                            =     true
      UPSL_aime_vehicle_controls_setting_user_actions                             =     true

Community Base Addons
=======================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   Community Base Addons
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      cba_diagnostic_ConsoleIndentType                                            =     -1
      cba_disposable_dropUsedLauncher                                             =     2
      force cba_disposable_replaceDisposableLauncher                              =     true
      cba_events_repetitionMode                                                   =     1
      force cba_network_loadoutValidation                                         =     0
      cba_optics_usePipOptics                                                     =     true
      cba_ui_notifyLifetime                                                       =     4
      cba_ui_StorePasswords                                                       =     1

TFAR - Global settings
========================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   TFAR - Global settings
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force force TFAR_AICanHearPlayer                                            =     true
      force force TFAR_AICanHearSpeaker                                           =     true
      force force TFAR_allowDebugging                                             =     false
      force force tfar_core_noTSNotConnectedHint                                  =     false
      force force TFAR_defaultIntercomSlot                                        =     0
      force force TFAR_disableAutoMute                                            =     false
      force force TFAR_enableIntercom                                             =     true
      force force TFAR_experimentalVehicleIsolation                               =     false
      force force TFAR_fullDuplex                                                 =     true
      force force TFAR_giveLongRangeRadioToGroupLeaders                           =     false
      force force TFAR_giveMicroDagrToSoldier                                     =     false
      force force TFAR_givePersonalRadioToRegularSoldier                          =     false
      force force TFAR_globalRadioRangeCoef                                       =     1
      force force TFAR_instantiate_instantiateAtBriefing                          =     false
      force force TFAR_objectInterceptionEnabled                                  =     false
      force force TFAR_objectInterceptionStrength                                 =     400
      force force tfar_radiocode_east                                             =     "_opfor"
      force force tfar_radiocode_independent                                      =     "_independent"
      force force tfar_radiocode_west                                             =     "_bluefor"
      force force tfar_radioCodesDisabled                                         =     true
      force force TFAR_SameLRFrequenciesForSide                                   =     true
      force force TFAR_SameSRFrequenciesForSide                                   =     true
      force force TFAR_setting_defaultFrequencies_lr_east                         =     "77"
      force force TFAR_setting_defaultFrequencies_lr_independent                  =     "77"
      force force TFAR_setting_defaultFrequencies_lr_west                         =     "77"
      force force TFAR_setting_defaultFrequencies_sr_east                         =     "31.1,120,130,140,150,160,170,77"
      force force TFAR_setting_defaultFrequencies_sr_independent                  =     "31.1,120,130,140,150,160,170,77"
      force force TFAR_setting_defaultFrequencies_sr_west                         =     "31.1,120,130,140,150,160,170,77"
      force force TFAR_setting_DefaultRadio_Airborne_east                         =     ""
      force force TFAR_setting_DefaultRadio_Airborne_Independent                  =     ""
      force force TFAR_setting_DefaultRadio_Airborne_West                         =     ""
      force force TFAR_setting_DefaultRadio_Backpack_east                         =     ""
      force force TFAR_setting_DefaultRadio_Backpack_Independent                  =     ""
      force force TFAR_setting_DefaultRadio_Backpack_west                         =     ""
      force force TFAR_setting_DefaultRadio_Personal_east                         =     ""
      force force TFAR_setting_DefaultRadio_Personal_Independent                  =     "TFAR_anprc148jem"
      force force TFAR_setting_DefaultRadio_Personal_West                         =     ""
      force force TFAR_setting_DefaultRadio_Rifleman_East                         =     ""
      force force TFAR_setting_DefaultRadio_Rifleman_Independent                  =     "TFAR_anprc148jem"
      force force TFAR_setting_DefaultRadio_Rifleman_West                         =     ""
      force TFAR_spectatorCanHearEnemyUnits                                       =     true
      force TFAR_spectatorCanHearFriendlies                                       =     true
      force force TFAR_takingRadio                                                =     2
      force TFAR_Teamspeak_Channel_Name                                           =     ""
      force TFAR_Teamspeak_Channel_Password                                       =     ""
      force force tfar_terrain_interception_coefficient                           =     7
      force force TFAR_voiceCone                                                  =     true

DUI - Squad Radar - Main
==========================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   DUI - Squad Radar - Main
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      diwako_dui_ace_hide_interaction                                             =     true
      diwako_dui_colors                                                           =     "standard"
      diwako_dui_font                                                             =     "RobotoCondensed"
      diwako_dui_icon_style                                                       =     "standard"
      diwako_dui_main_hide_dialog                                                 =     true
      diwako_dui_main_hide_ui_by_default                                          =     false
      diwako_dui_main_squadBlue                                                   =     [0,0,1,1]
      diwako_dui_main_squadGreen                                                  =     [0,1,0,1]
      diwako_dui_main_squadMain                                                   =     [1,1,1,1]
      diwako_dui_main_squadRed                                                    =     [1,0,0,1]
      diwako_dui_main_squadYellow                                                 =     [1,1,0,1]
      diwako_dui_main_trackingColor                                               =     [0.93,0.26,0.93,1]
      diwako_dui_reset_ui_pos                                                     =     false

AIME GPS and UAV Terminal
===========================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   AIME GPS and UAV Terminal
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      UPSL_aime_uav_terminal_setting_gps_action                                   =     true
      UPSL_aime_uav_terminal_setting_term_action                                  =     true
      UPSL_aime_uav_terminal_setting_uav_action                                   =     true

DUI - Squad Radar - Radar
===========================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   DUI - Squad Radar - Radar
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      diwako_dui_compass_hide_alone_group                                         =     false
      diwako_dui_compass_hide_blip_alone_group                                    =     false
      diwako_dui_compass_icon_scale                                               =     1
      diwako_dui_compass_opacity                                                  =     1
      diwako_dui_compass_style                                                    =     ["\z\diwako_dui\addons\radar\UI\compass_styles\standard\compass_limited.paa","\z\diwako_dui\addons\radar\UI\compass_styles\standard\compass.paa"]
      diwako_dui_compassRange                                                     =     35
      diwako_dui_compassRefreshrate                                               =     0
      diwako_dui_dir_showMildot                                                   =     false
      diwako_dui_dir_size                                                         =     1.25
      diwako_dui_distanceWarning                                                  =     3
      diwako_dui_enable_compass                                                   =     true
      diwako_dui_enable_compass_dir                                               =     1
      diwako_dui_enable_occlusion                                                 =     false
      diwako_dui_enable_occlusion_cone                                            =     360
      diwako_dui_hudScaling                                                       =     1
      diwako_dui_namelist                                                         =     true
      diwako_dui_namelist_bg                                                      =     0
      diwako_dui_namelist_only_buddy_icon                                         =     false
      diwako_dui_namelist_size                                                    =     1
      diwako_dui_namelist_text_shadow                                             =     2
      diwako_dui_namelist_width                                                   =     215
      diwako_dui_radar_ace_finger                                                 =     true
      force diwako_dui_radar_ace_medic                                            =     true
      diwako_dui_radar_compassRangeCrew                                           =     500
      diwako_dui_radar_dir_padding                                                =     25
      diwako_dui_radar_dir_shadow                                                 =     2
      diwako_dui_radar_group_by_vehicle                                           =     false
      diwako_dui_radar_icon_opacity                                               =     1
      diwako_dui_radar_icon_opacity_no_player                                     =     true
      force diwako_dui_radar_icon_priority_setting                                =     1
      diwako_dui_radar_icon_scale_crew                                            =     6
      diwako_dui_radar_leadingZeroes                                              =     false
      diwako_dui_radar_namelist_hideWhenLeader                                    =     false
      diwako_dui_radar_namelist_vertical_spacing                                  =     1
      diwako_dui_radar_occlusion_fade_in_time                                     =     1
      diwako_dui_radar_occlusion_fade_time                                        =     10
      diwako_dui_radar_pointer_color                                              =     [1,0.5,0,1]
      diwako_dui_radar_pointer_style                                              =     "standard"
      diwako_dui_radar_show_cardinal_points                                       =     true
      diwako_dui_radar_showSpeaking                                               =     true
      diwako_dui_radar_showSpeaking_radioOnly                                     =     false
      diwako_dui_radar_showSpeaking_replaceIcon                                   =     true
      force diwako_dui_radar_sortType                                             =     "none"
      force diwako_dui_radar_sqlFirst                                             =     false
      force diwako_dui_radar_syncGroup                                            =     false
      force diwako_dui_radar_vehicleCompassEnabled                                =     false
      diwako_dui_use_layout_editor                                                =     false

TFAR - Clientside settings
============================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   TFAR - Clientside settings
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      TFAR_curatorCamEars                                                         =     false
      TFAR_default_radioVolume                                                    =     6
      TFAR_intercomDucking                                                        =     0.2
      TFAR_intercomVolume                                                         =     0.1
      TFAR_moveWhileTabbedOut                                                     =     false
      TFAR_noAutomoveSpectator                                                    =     false
      TFAR_oldVolumeHint                                                          =     false
      TFAR_pluginTimeout                                                          =     4
      TFAR_PosUpdateMode                                                          =     0.1
      TFAR_showChannelChangedHint                                                 =     true
      TFAR_ShowDiaryRecord                                                        =     true
      TFAR_showTransmittingHint                                                   =     true
      TFAR_ShowVolumeHUD                                                          =     false
      TFAR_tangentReleaseDelay                                                    =     0
      TFAR_VolumeHudTransparency                                                  =     0
      TFAR_volumeModifier_forceSpeech                                             =     false

DUI - Squad Radar - Nametags
==============================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   DUI - Squad Radar - Nametags
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      diwako_dui_nametags_customRankStyle                                         =     "[[""PRIVATE"",""CORPORAL"",""SERGEANT"",""LIEUTENANT"",""CAPTAIN"",""MAJOR"",""COLONEL""],[""Pvt."",""Cpl."",""Sgt."",""Lt."",""Capt."",""Maj."",""Col.""]]"
      diwako_dui_nametags_deadColor                                               =     [0.2,0.2,0.2,1]
      diwako_dui_nametags_deadRenderDistance                                      =     3.5
      diwako_dui_nametags_drawRank                                                =     true
      diwako_dui_nametags_enabled                                                 =     true
      diwako_dui_nametags_enableFOVBoost                                          =     true
      diwako_dui_nametags_enableOcclusion                                         =     true
      diwako_dui_nametags_fadeInTime                                              =     0.05
      diwako_dui_nametags_fadeOutTime                                             =     0.5
      diwako_dui_nametags_fontGroup                                               =     "RobotoCondensedLight"
      diwako_dui_nametags_fontGroupNameSize                                       =     8
      diwako_dui_nametags_fontName                                                =     "RobotoCondensedBold"
      diwako_dui_nametags_fontNameSize                                            =     10
      diwako_dui_nametags_groupColor                                              =     [1,1,1,1]
      diwako_dui_nametags_groupFontShadow                                         =     1
      diwako_dui_nametags_groupNameOtherGroupColor                                =     [0.6,0.85,0.6,1]
      diwako_dui_nametags_nameFontShadow                                          =     1
      diwako_dui_nametags_nameOtherGroupColor                                     =     [0.2,1,0,1]
      diwako_dui_nametags_rankNameStyle                                           =     "default"
      diwako_dui_nametags_renderDistance                                          =     40
      diwako_dui_nametags_showUnconAsDead                                         =     true
      diwako_dui_nametags_useLIS                                                  =     true
      diwako_dui_nametags_useSideIsFriendly                                       =     true

DUI - Squad Radar - Indicators
================================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   DUI - Squad Radar - Indicators
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      force diwako_dui_indicators_crew_range_enabled                              =     false
      diwako_dui_indicators_fov_scale                                             =     false
      diwako_dui_indicators_icon_buddy                                            =     true
      diwako_dui_indicators_icon_leader                                           =     true
      diwako_dui_indicators_icon_medic                                            =     true
      diwako_dui_indicators_range                                                 =     20
      diwako_dui_indicators_range_crew                                            =     300
      diwako_dui_indicators_range_scale                                           =     false
      diwako_dui_indicators_show                                                  =     true
      diwako_dui_indicators_size                                                  =     1
      diwako_dui_indicators_style                                                 =     "standard"
      diwako_dui_indicators_useACENametagsRange                                   =     true

Zeus Enhanced - Faction Filter
================================

.. card::
   :class-header: header-2-light
   :class-card: sd-card-2

   Zeus Enhanced - Faction Filter
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block:: toml

      zen_faction_filter_0_OPF_F                                                  =     true
      zen_faction_filter_0_OPF_G_F                                                =     true
      zen_faction_filter_0_OPF_GEN_F                                              =     true
      zen_faction_filter_0_OPF_R_F                                                =     true
      zen_faction_filter_0_OPF_T_F                                                =     true
      zen_faction_filter_0_rhs_faction_msv                                        =     true
      zen_faction_filter_0_rhs_faction_rva                                        =     true
      zen_faction_filter_0_rhs_faction_tv                                         =     true
      zen_faction_filter_0_rhs_faction_vdv                                        =     true
      zen_faction_filter_0_rhs_faction_vmf                                        =     true
      zen_faction_filter_0_rhs_faction_vpvo                                       =     true
      zen_faction_filter_0_rhs_faction_vv                                         =     true
      zen_faction_filter_0_rhs_faction_vvs                                        =     true
      zen_faction_filter_0_rhs_faction_vvs_c                                      =     true
      zen_faction_filter_0_rhsgref_faction_chdkz                                  =     true
      zen_faction_filter_0_rhsgref_faction_chdkz_groups                           =     true
      zen_faction_filter_0_rhsgref_faction_tla                                    =     true
      zen_faction_filter_0_UK3CB_AAF_O                                            =     true
      zen_faction_filter_0_UK3CB_ADA_O                                            =     true
      zen_faction_filter_0_UK3CB_ADC_O                                            =     true
      zen_faction_filter_0_UK3CB_ADE_O                                            =     true
      zen_faction_filter_0_UK3CB_ADG_O                                            =     true
      zen_faction_filter_0_UK3CB_ADM_O                                            =     true
      zen_faction_filter_0_UK3CB_ADP_O                                            =     true
      zen_faction_filter_0_UK3CB_ADR_O                                            =     true
      zen_faction_filter_0_UK3CB_ARD_O                                            =     true
      zen_faction_filter_0_UK3CB_CCM_O                                            =     true
      zen_faction_filter_0_UK3CB_CHC_O                                            =     true
      zen_faction_filter_0_UK3CB_CHD_O                                            =     true
      zen_faction_filter_0_UK3CB_CHD_O_groups                                     =     true
      zen_faction_filter_0_UK3CB_CHD_W_O                                          =     true
      zen_faction_filter_0_UK3CB_CHD_W_O_groups                                   =     true
      zen_faction_filter_0_UK3CB_CPD_O                                            =     true
      zen_faction_filter_0_UK3CB_CW_SOV_O_EARLY                                   =     true
      zen_faction_filter_0_UK3CB_CW_SOV_O_LATE                                    =     true
      zen_faction_filter_0_UK3CB_KDF_O                                            =     true
      zen_faction_filter_0_UK3CB_MDF_O                                            =     true
      zen_faction_filter_0_UK3CB_NAP_O                                            =     true
      zen_faction_filter_0_UK3CB_NAP_O_groups                                     =     true
      zen_faction_filter_0_UK3CB_NFA_O                                            =     true
      zen_faction_filter_0_UK3CB_NFA_O_groups                                     =     true
      zen_faction_filter_0_UK3CB_NPD_O                                            =     true
      zen_faction_filter_0_UK3CB_TKA_O                                            =     true
      zen_faction_filter_0_UK3CB_TKC_O                                            =     true
      zen_faction_filter_0_UK3CB_TKM_O                                            =     true
      zen_faction_filter_0_UK3CB_TKP_O                                            =     true
      zen_faction_filter_1_BLU_CTRG_F                                             =     true
      zen_faction_filter_1_BLU_F                                                  =     true
      zen_faction_filter_1_BLU_G_F                                                =     true
      zen_faction_filter_1_BLU_GEN_F                                              =     true
      zen_faction_filter_1_BLU_T_F                                                =     true
      zen_faction_filter_1_BLU_W_F                                                =     true
      zen_faction_filter_1_rhs_faction_socom                                      =     true
      zen_faction_filter_1_rhs_faction_usaf                                       =     true
      zen_faction_filter_1_rhs_faction_usarmy_d                                   =     true
      zen_faction_filter_1_rhs_faction_usarmy_wd                                  =     true
      zen_faction_filter_1_rhs_faction_usmc_d                                     =     true
      zen_faction_filter_1_rhs_faction_usmc_wd                                    =     true
      zen_faction_filter_1_rhs_faction_usn                                        =     true
      zen_faction_filter_1_rhsgref_faction_cdf_air_b                              =     true
      zen_faction_filter_1_rhsgref_faction_cdf_ground_b                           =     true
      zen_faction_filter_1_rhsgref_faction_cdf_ground_b_groups                    =     true
      zen_faction_filter_1_rhsgref_faction_cdf_ng_b                               =     true
      zen_faction_filter_1_rhsgref_faction_hidf                                   =     true
      zen_faction_filter_1_UK3CB_AAF_B                                            =     true
      zen_faction_filter_1_UK3CB_ADA_B                                            =     true
      zen_faction_filter_1_UK3CB_ADC_B                                            =     true
      zen_faction_filter_1_UK3CB_ADG_B                                            =     true
      zen_faction_filter_1_UK3CB_ADM_B                                            =     true
      zen_faction_filter_1_UK3CB_ADP_B                                            =     true
      zen_faction_filter_1_UK3CB_ADR_B                                            =     true
      zen_faction_filter_1_UK3CB_ANA_B                                            =     true
      zen_faction_filter_1_UK3CB_ANP_B                                            =     true
      zen_faction_filter_1_UK3CB_ARD_B                                            =     true
      zen_faction_filter_1_UK3CB_CCM_B                                            =     true
      zen_faction_filter_1_UK3CB_CHC_B                                            =     true
      zen_faction_filter_1_UK3CB_CHD_B                                            =     true
      zen_faction_filter_1_UK3CB_CHD_B_groups                                     =     true
      zen_faction_filter_1_UK3CB_CHD_W_B                                          =     true
      zen_faction_filter_1_UK3CB_CHD_W_B_groups                                   =     true
      zen_faction_filter_1_UK3CB_CPD_B                                            =     true
      zen_faction_filter_1_UK3CB_CW_US_B_EARLY                                    =     true
      zen_faction_filter_1_UK3CB_CW_US_B_LATE                                     =     true
      zen_faction_filter_1_UK3CB_KDF_B                                            =     true
      zen_faction_filter_1_UK3CB_MDF_B                                            =     true
      zen_faction_filter_1_UK3CB_NAP_B                                            =     true
      zen_faction_filter_1_UK3CB_NAP_B_groups                                     =     true
      zen_faction_filter_1_UK3CB_NFA_B                                            =     true
      zen_faction_filter_1_UK3CB_NFA_B_groups                                     =     true
      zen_faction_filter_1_UK3CB_NPD_B                                            =     true
      zen_faction_filter_1_UK3CB_TKA_B                                            =     true
      zen_faction_filter_1_UK3CB_TKC_B                                            =     true
      zen_faction_filter_1_UK3CB_TKM_B                                            =     true
      zen_faction_filter_1_UK3CB_TKP_B                                            =     true
      zen_faction_filter_1_UK3CB_UN_B                                             =     true
      zen_faction_filter_2_IND_C_F                                                =     true
      zen_faction_filter_2_IND_E_F                                                =     true
      zen_faction_filter_2_IND_F                                                  =     true
      zen_faction_filter_2_IND_G_F                                                =     true
      zen_faction_filter_2_IND_L_F                                                =     true
      zen_faction_filter_2_rhsgref_faction_cdf_air                                =     true
      zen_faction_filter_2_rhsgref_faction_cdf_ground                             =     true
      zen_faction_filter_2_rhsgref_faction_cdf_ground_groups                      =     true
      zen_faction_filter_2_rhsgref_faction_cdf_ng                                 =     true
      zen_faction_filter_2_rhsgref_faction_cdf_ng_groups                          =     true
      zen_faction_filter_2_rhsgref_faction_chdkz_g                                =     true
      zen_faction_filter_2_rhsgref_faction_chdkz_g_groups                         =     true
      zen_faction_filter_2_rhsgref_faction_nationalist                            =     true
      zen_faction_filter_2_rhsgref_faction_nationalist_groups                     =     true
      zen_faction_filter_2_rhsgref_faction_tla_g                                  =     true
      zen_faction_filter_2_rhsgref_faction_un                                     =     true
      zen_faction_filter_2_UK3CB_AAF_I                                            =     true
      zen_faction_filter_2_UK3CB_ADA_I                                            =     true
      zen_faction_filter_2_UK3CB_ADC_I                                            =     true
      zen_faction_filter_2_UK3CB_ADE_I                                            =     true
      zen_faction_filter_2_UK3CB_ADG_I                                            =     true
      zen_faction_filter_2_UK3CB_ADM_I                                            =     true
      zen_faction_filter_2_UK3CB_ADP_I                                            =     true
      zen_faction_filter_2_UK3CB_ADR_I                                            =     true
      zen_faction_filter_2_UK3CB_ARD_I                                            =     true
      zen_faction_filter_2_UK3CB_CCM_I                                            =     true
      zen_faction_filter_2_UK3CB_CHC_I                                            =     true
      zen_faction_filter_2_UK3CB_CHD_I                                            =     true
      zen_faction_filter_2_UK3CB_CHD_I_groups                                     =     true
      zen_faction_filter_2_UK3CB_CHD_W_I                                          =     true
      zen_faction_filter_2_UK3CB_CHD_W_I_groups                                   =     true
      zen_faction_filter_2_UK3CB_CPD_I                                            =     true
      zen_faction_filter_2_UK3CB_KDF_I                                            =     true
      zen_faction_filter_2_UK3CB_MDF_I                                            =     true
      zen_faction_filter_2_UK3CB_NAP_I                                            =     true
      zen_faction_filter_2_UK3CB_NAP_I_groups                                     =     true
      zen_faction_filter_2_UK3CB_NFA_I                                            =     true
      zen_faction_filter_2_UK3CB_NFA_I_groups                                     =     true
      zen_faction_filter_2_UK3CB_NPD_I                                            =     true
      zen_faction_filter_2_UK3CB_TKA_I                                            =     true
      zen_faction_filter_2_UK3CB_TKC_I                                            =     true
      zen_faction_filter_2_UK3CB_TKM_I                                            =     true
      zen_faction_filter_2_UK3CB_TKP_I                                            =     true
      zen_faction_filter_2_UK3CB_UN_I                                             =     true
      zen_faction_filter_3_CIV_F                                                  =     true
      zen_faction_filter_3_CIV_IDAP_F                                             =     true
      zen_faction_filter_3_IND_L_F                                                =     true
      zen_faction_filter_3_UK3CB_ADC_C                                            =     true
      zen_faction_filter_3_UK3CB_CHC_C                                            =     true
      zen_faction_filter_3_UK3CB_TKC_C                                            =     true