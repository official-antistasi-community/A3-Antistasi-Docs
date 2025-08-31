.. rst-class:: hidden

.. _beginners_guide:

==============================================================================================================================
Beginners Guide for `Antistasi v3.0 <https://steamcommunity.com/sharedfiles/filedetails/?id=2867537125>`_
==============================================================================================================================

.. rst-class:: small-text

   By `Moni <https://www.youtube.com/@daman2911/videos>`_, Meerkat, Bob Murphy, Giddi, DeathTouchWilly, Targetingsnake

Introduction
============

.. card::
   :class-card: sd-mt-3
   :class-header: header-2

   Introduction
   ^^^^^^^^^^^^

   This guide is written exclusively for `Antistasi Community Edition - Version 3.0 <https://steamcommunity.com/sharedfiles/filedetails/?id=2867537125>`_ and following.
   Barbolanis version (the initial mission creator) and other freelance
   versions like Antistasi Plus may or may not be compatible with what I
   say in this guide. That said, I think the tactics and strategies used in
   this guide will likely work in other versions.

   This guide has been scrutinized and vetted by the developers and
   veterans of Antistasi Community Edition.

What is Antistasi?
==================

.. card::
   :class-header: header-2

   What is Antistasi?
   ^^^^^^^^^^^^^^^^^^

   Antistasi is a guerrilla warfare simulator. As a rebel faction, you will
   start severely outnumbered and outgunned. BLUFOR is the main occupying
   force and will start owning most of the land. OPFOR is an invader who
   will start with very little land. The rebels are, well, rebels! As such
   they will start with no land at all.

Supported Modsets & Maps
=============================

.. card::
   :class-header: header-2

   Supported Modsets & Maps
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Antistasi is compatible with different modsets as well as maps and of course there are different playable and AI Factions available with each modset.
   In the past the selection of the Factions was hard coded into the mission, which prevented the player to have any direct option to change who to play against.
   With the release of Antistasi 3.0.0 we have integrated all maps as well as a new Antistasi Setup GUI which at the start of a campaign gives you the option to select from all available Factions to change your enemies and more to your liking.

   Whilst modsets and maps can be combined as you wish, we suggest to only load the mods for the Factions you want to play with and not simply load all mods that are compatible.

   .. rst-class:: nocode

   .. dropdown:: Factions and Modsets
      :class-title: header-3-light
      :class-container: sd-card-3 target-substitude nocode

      .. rst-class:: nocode

      Available Factions with `Vanilla Arma 3 <https://store.steampowered.com/app/107410/Arma_3/>`_ [:download:`Modset </_data/templates_launcher/Arma_3_Preset_Antistasi_Vanilla.html>`]:

      - Rebel - A3 FIA
      - AI - A3 AAF
      - AI - A3 CSAT Arid
      - AI - A3 CSAT Temperate
      - AI - A3 NATO Arid
      - AI - A3 NATO Temperate
      - AI - A3 NATO Tropical

      Added Factions with Arma 3 DLCs [:download:`Modset </_data/templates_launcher/Arma_3_Preset_Antistasi_Vanilla.html>`]:

      - Rebel - A3 SDK (requires `APEX DLC <https://store.steampowered.com/app/395180/Arma_3_Apex/>`_)
      - Rebel - A3 LFF (requires `Contact DLC <https://store.steampowered.com/app/1021790/Arma_3_Contact/>`_)
      - AI - A3 CSAT Apex (requires `APEX DLC <https://store.steampowered.com/app/395180/Arma_3_Apex/>`_)
      - AI - A3 CSAT Enoch (requires `Contact DLC <https://store.steampowered.com/app/1021790/Arma_3_Contact/>`_)
      - AI - A3 ION (requires `APEX DLC <https://store.steampowered.com/app/395180/Arma_3_Apex/>`_ and `Contact DLC <https://store.steampowered.com/app/1021790/Arma_3_Contact/>`_)
      - AI - A3 LDF (requires `Contact DLC <https://store.steampowered.com/app/1021790/Arma_3_Contact/>`_)
      - AI - A3 NATO Apex (requires `APEX DLC <https://store.steampowered.com/app/395180/Arma_3_Apex/>`_)
      - AI - A3 UK/NATO Arid (requires `APEX DLC <https://store.steampowered.com/app/395180/Arma_3_Apex/>`_)
      - AI - A3 UK/NATO Tropical (requires `APEX DLC <https://store.steampowered.com/app/395180/Arma_3_Apex/>`_)

      Added Factions with the `S.O.G. Prairie Fire CDLC <https://store.steampowered.com/app/1227700/Arma_3_Creator_DLC_SOG_Prairie_Fire/>`_ [:download:`Modset </_data/templates_launcher/Arma_3_Preset_Antistasi_SOG.html>`]:

      - Rebel - VN POF
      - AI - VN MACV
      - AI - VN PAVN

      Added Factions with the `Global Mobilisation CDLC <https://store.steampowered.com/app/1042220/Arma_3_Creator_DLC_Global_Mobilization__Cold_War_Germany/>`_ (also requires the `CUP mods <https://steamcommunity.com/sharedfiles/filedetails/?id=2902920186>`_ to be loaded) [:download:`Modset </_data/templates_launcher/Arma_3_Preset_Antistasi_GM_CUP.html>`]:

      - Rebel - GM FIA
      - AI - GM Bundeswehr Arctic
      - AI - GM Bundeswehr Temperate
      - AI - GM Nationale Volksarmee Arctic (National People's Army)
      - AI - GM Nationale Volksarmee Temperate (National People's Army)

      Added Factions with the `Spearhead 1944 CDLC <https://store.steampowered.com/app/1175380/Arma_3_Creator_DLC_Spearhead_1944/>`_ (also requires the `IFA mod and dependencies <https://steamcommunity.com/sharedfiles/filedetails/?id=3010629545>`_ to be loaded) [:download:`Modset </_data/templates_launcher/Arma_3_Preset_Antistasi_SPE_IFA.html>`]:

      - Rebel - SPE_IFA FFF
      - AI - SPE_IFA US
      - AI - SPE_IFA WEH (German Wehrmacht)

      Avaliable Factions with `IFA3 AIO <https://steamcommunity.com/sharedfiles/filedetails/?id=2648308937>`_ [:download:`Modset </_data/templates_launcher/Arma_3_Preset_Antistasi_IFA3.html>`, :download:`Extended Modset </_data/templates_launcher/Arma_3_Preset_Antistasi_IFA3_Extended.html>`]:

      - Rebel - AK
      - Rebel - FFI
      - AI - ALLIES
      - AI - SOVIET ARMY
      - AI - US ARMY
      - AI - UK ARMY
      - AI - WEHRMACHT

      Added Factions with the `Western Sahara CDLC <https://store.steampowered.com/app/1681170/Arma_3_Creator_DLC_Western_Sahara/>`_ [:download:`Modset </_data/templates_launcher/Arma_3_Preset_Antistas_WS.html>`]:

      - Rebel - Tura
      - AI - ION Services
      - AI - SFIA (Sefrawi Freedom and Independence Army)
      - AI - ADF (Arganian Defence Force)
      - AI - CSAT (North African version)
      - AI - NATO (Desert camo)

      Added Factions with `RHS <https://steamcommunity.com/sharedfiles/filedetails/?id=2498438772>`_ [:download:`Modset </_data/templates_launcher/Arma_3_Preset_Antistasi_RHS.html>`]:

      - Rebel - RHS NAPA
      - AI - RHS AFRF Arid
      - AI - RHS AFRF Temperate
      - AI - RHS CDF
      - AI - RHS ChDKZ
      - AI - RHS HIDF
      - AI - RHS TLA
      - AI - RHS SAF
      - AI - RHS US Army Arid
      - AI - RHS US Army Temperate
      - AI - RHS USMC Arid
      - AI - RHS USMC Temperate
      - AI - RHS VDV Arid
      - AI - RHS VDV Temperate

      Added Factions with `3CB Factions <https://steamcommunity.com/sharedfiles/filedetails/?id=2498466977>`_ [:download:`Modset </_data/templates_launcher/Arma_3_Preset_Antistasi_RHS_3CBFaction.html>`]:

      - Rebel - 3CB CCM
      - Rebel - 3CB FIA
      - Rebel - 3CB ION
      - Rebel - 3CB LSM
      - Rebel - 3CB TKM
      - AI - 3CB AAF
      - AI - 3CB AAF Arid
      - AI - 3CB ADA
      - AI - 3CB ANA
      - AI - 3CB Cold War US
      - AI - 3CB Cold War USSR
      - AI - 3CB CSAT BEAR
      - AI - 3CB CSAT GRYPHON
      - AI - 3CB CSAT SCIMITAR
      - AI - 3CB CSAT VIPER
      - AI - 3CB HIDF
      - AI - 3CB ION Arctic
      - AI - 3CB ION Arid
      - AI - 3CB ION Temperate
      - AI - 3CB KRG
      - AI - 3CB LDF
      - AI - 3CB MDF
      - AI - 3CB TKA East
      - AI - 3CB TKA Mix
      - AI - 3CB TKA West

      Added Factions with `3CB BAF <https://steamcommunity.com/sharedfiles/filedetails/?id=2498453852>`_ [:download:`Modset </_data/templates_launcher/Arma_3_Preset_Antistasi_3CBBAF.html>`]:

      - AI - 3CB BAF Arctic
      - AI - 3CB BAF Arid
      - AI - 3CB BAF Temperate
      - AI - 3CB BAF Tropical

      Added Factions with `CUP <https://steamcommunity.com/sharedfiles/filedetails/?id=2902920186>`_ [:download:`Modset </_data/templates_launcher/Arma_3_Preset_Antistasi_CUP.html>`]:

      - Rebel - CUP NAPA
      - Rebel - CUP TKM
      - AI - CUP ACR Arid
      - AI - CUP ACR Temperate
      - AI - CUP AFRF Arctic
      - AI - CUP AFRF Arid
      - AI - CUP AFRF Desert
      - AI - CUP AFRF Temperate
      - AI - CUP BAF Arid
      - AI - CUP BAF Temperate
      - AI - CUP BW Arid
      - AI - CUP BW Temperate
      - AI - CUP CDF Arctic
      - AI - CUP CDF Temperate
      - AI - CUP HIL
      - AI - CUP ION Arctic
      - AI - CUP ION Arid
      - AI - CUP RACS Arid
      - AI - CUP RACS Tropical
      - AI - CUP SLA
      - AI - CUP TKA
      - AI - CUP US Army Arid
      - AI - CUP US Army Temperate
      - AI - CUP USMC Arid
      - AI - CUP USMC Temperate

      Avaliable Factions with `BWMod <https://steamcommunity.com/sharedfiles/filedetails/?id=1200127537>`_ [:download:`Modset </_data/templates_launcher/Arma_3_Preset_Antistasi_BWMod.html>`]:

      - AI - BWA3 BW Arid
      - AI - BWA3 BW Temperate

      Avaliable Factions with `Unsung <https://steamcommunity.com/sharedfiles/filedetails/?id=943001311>`_ [:download:`Modset </_data/templates_launcher/Arma_3_Preset_Antistasi_Unsung.html>`]:

      - Rebel - Unsung VC
      - AI - Unsung PAVN
      - AI - Unsung US

   .. dropdown:: Maps
      :class-title: header-3-light
      :class-container: sd-card-3 target-substitude

      Available Maps with `Vanilla Arma 3 <https://store.steampowered.com/app/107410/Arma_3/>`_:

      - Altis
      - Malden
      - Livonia (requires the `Contact DLC <https://store.steampowered.com/app/1021790/Arma_3_Contact/>`_)
      - Tanoa (requires `APEX DLC <https://store.steampowered.com/app/395180/Arma_3_Apex/>`_)

      Available maps with the `Global Mobilisation CDLC <https://store.steampowered.com/app/1042220/Arma_3_Creator_DLC_Global_Mobilization__Cold_War_Germany/>`_:

      - Weferlingen
      - Weferlingen Winter

      Available maps with the `S.O.G. Prairie Fire CDLC <https://store.steampowered.com/app/1227700/Arma_3_Creator_DLC_SOG_Prairie_Fire/>`_:

      - Cam Lao Nam
      - Khe Sanh

      Available maps with the `Spearhead 1944 CDLC <https://store.steampowered.com/app/1175380/Arma_3_Creator_DLC_Spearhead_1944/>`_:

      - Mortain
      - Normandy

      Available maps with `CUP Terrains - Maps <https://steamcommunity.com/sharedfiles/filedetails/?id=583544987>`_:

      - Chernarus Autumn
      - Chernarus Summer
      - Chernarus Winter
      - Sahrani
      - Takistan

      Available maps with `CUP Terrains - Maps 2.0 <https://steamcommunity.com/sharedfiles/filedetails/?id=1981964169>`_:

      - Chernarus 2020

      Single maps with their own required mods:

      - `Anizay <https://steamcommunity.com/sharedfiles/filedetails/?id=1537973181>`_
      - `Kujari <https://steamcommunity.com/sharedfiles/filedetails/?id=1726494027>`_
      - `Kunduz <https://steamcommunity.com/sharedfiles/filedetails/?id=1188303655>`_
      - `Pulau <https://steamcommunity.com/workshop/filedetails/?id=1423583812>`_
      - `Tembelan Island <https://steamcommunity.com/sharedfiles/filedetails/?id=1252091296>`_
      - `UMB Columbia <https://steamcommunity.com/sharedfiles/filedetails/?id=2266710560>`_
      - `Virolahti <https://steamcommunity.com/sharedfiles/filedetails/?id=1926513010>`_

   .. dropdown:: Additional Mods
      :class-title: header-3-light
      :class-container: sd-card-3 target-substitude

      Antistasi has built in compatibility for the following mods. If loaded (and if applicable) the needed items of the mods will either be available in the arsenal, can be found on AI or in lootboxes. This of course also is depending on which item it is.
      In addition there are parameters which might influence that spawning behaviour so make sure you check them out.

      .. rst-class:: table-additional-mods

      .. flat-table::
         :header-rows: 0
         :widths: 20 80

         *  - `CBA <https://steamcommunity.com/workshop/filedetails/?id=450814997>`_
            - CBA is a framework which adds a range of features Arma in itself does not supply. This mod is a dependency for many other mods and it also adds some additional functionality within Antistasi, for example the ability to modify garage settings and Jeroens Extended Debug Console.

         *  - `ACE <https://steamcommunity.com/workshop/filedetails/?id=463939057>`_
            -  | ACE is a mod that adds a lot of in depth modular systems to Arma like for example a medical system, ballistics and more.
               | Keep in mind that some mods like RHS need their respective `ACE Compatibility Mods <https://steamcommunity.com/id/acemod/myworkshopfiles/?appid=107410>`_ loaded so they work properly. Adjust your modlist accordingly.

         *  - `TFAR (outdated) <https://steamcommunity.com/sharedfiles/filedetails/?id=620019431>`_
            -  | TFAR is a mod which implements a more realistic radio communication by combining Arma 3 and TeamSpeak. It implements SR and LR radios for infantry and vehicles.
               | This version is outdated and superseded by TFAR BETA.

         *  - `TFAR BETA <https://steamcommunity.com/sharedfiles/filedetails/?id=894678801>`_
            - TFAR BETA is the successor of TFAR, adapting the functionality to newer BI functions, fixing bugs and adding new settings and options.

         *  - `ACRE2 <https://steamcommunity.com/sharedfiles/filedetails/?id=751965892>`_
            - ACRE2, like TFAR / TFAR BETA is a mod which combines Arma 3 with TeamSpeak. It is highly customizable, has additional features like taking the terrain of a map into account for the quality of the radio transmission and more. It is more in depth, requires more time to learn, but adds a nice level of realism. For CDLC maps it requires `ACRE2 Compatibility Mods <https://steamcommunity.com/profiles/76561198323575101/myworkshopfiles/?appid=107410>`_.

         *  - `KAT - Advanced Medical REWRITE <https://steamcommunity.com/workshop/filedetails/?id=2020940806>`_
            - KAT - Advanced Medical REWRITE is a mod which adds a very in depth medical system, covering different not only the breathing apperatus and the cardiovascular system but also adds surgery and more to the game.

   .. dropdown:: Additional Vehicle Mods
      :class-title: header-3-light
      :class-container: sd-card-3 target-substitude

      Antistasi has compatibility with the following mods which add to the available civilian vehicle pool if loaded properly and enabled in the Startup GUI.

      - `D3S Cars pack <https://steamcommunity.com/workshop/filedetails/?id=1639607571>`_
      - `Ivory Car Pack [Official] <https://steamcommunity.com/sharedfiles/filedetails/?id=1888644057>`_
      - `RDS Civilian Pack <https://steamcommunity.com/workshop/filedetails/?id=612930542>`_
      - `TCGM_BikeBackpack <https://steamcommunity.com/sharedfiles/filedetails/?id=2096950604>`_

   .. dropdown:: Forbidden Mods
      :class-title: header-3-danger
      :class-container: sd-card-3-danger target-substitude

      There are quite some mods which are **NOT** compatible with Antistasi.
      Following you find a exemplary list of mods which are either completely breaking Antistasi and hence are blacklisted or ones that are known to have a negative impact and should not be loaded to have the best experience.
      AI affecting mods are bad in general as Antistasi includes its own AI system. So any mod interfering with it has the potential to break things.
      Another general category of forbidden mods is anything that automatically transfers groups to headless clients, as that conflicts with Antistasi's headless client system.
      When any of the mods below is loaded, we can't guarantee that Antistasi is working properly and won't be helping you to make it work.
      You have been warned.

      - `LAMBS <https://steamcommunity.com/profiles/76561197962792796/myworkshopfiles/>`_
      - `VCOM <https://steamcommunity.com/sharedfiles/filedetails/?id=721359761>`_
      - `ALiVE <https://steamcommunity.com/workshop/filedetails/?id=620260972>`_
      - `MCC Sandbox 4 <https://steamcommunity.com/sharedfiles/filedetails/?id=338988835>`_
      - `ASR AI3 <https://steamcommunity.com/workshop/filedetails/?id=642457233>`_
      - `Project injury Reaction (PiR) <https://steamcommunity.com/workshop/filedetails/?id=1665585720>`_
      - `Zulu Headless Client (ZHC) <https://steamcommunity.com/sharedfiles/filedetails/?id=2450921295>`_
      - `Werthles' Headless Module <https://steamcommunity.com/sharedfiles/filedetails/?id=510031102>`_
      - `Advanced Rappelling <https://steamcommunity.com/workshop/filedetails/?id=713709341>`_
      - `Advanced Urban Rappelling <https://steamcommunity.com/sharedfiles/filedetails/?id=730310357>`_

How to set up a game
====================

.. card::
   :class-header: header-2

   How to set up a game
   ^^^^^^^^^^^^^^^^^^^^

   Depending on how you want to play Antistasi, there are mainly two options for setting it up:

   .. card::
      :class-header: header-3-light
      :class-card: sd-card-3 code-paragraph

      Single Player / Locally Hosted
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      - Subscribe to the `Antistasi Mod <https://steamcommunity.com/sharedfiles/filedetails/?id=2867537125>`_
      - Load the Antistasi Mod in the Arma 3 Launcher
      - Start Arma 3
      - Go to Server Browser --> Host new Session
      - Select a compatible map and then select the mission called :code:`Antistasi Community [Version number]` in white text.
      - If you play on your own, make sure you pick the :code:`Default Commander` slot as this one has the medic as well as the engineer perk.

      Also please keep in mind the following two things:

      - Only one Antistasi mod should be loaded at a time.
      - All clients must load the same Antistasi mod as the host.

   .. card::
      :class-header: header-3-light
      :class-card: sd-card-3 code-paragraph

      (Dedicated) Server
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      - Install the Antistasi Mod on your server. How you go about this is depending on your server setup. Some servers have the ability to directly subscribe to a Steam Workshop Item. In this case subscribe to the `Antistasi Mod <https://steamcommunity.com/sharedfiles/filedetails/?id=2867537125>`_ via your server. In case your server does not have this functionality, you likely have to upload the files manually to the server. You find the most up to date files `here <https://github.com/official-antistasi-community/A3-Antistasi/releases/latest>`_ . Download the rar, unpack it and upload the content via FTP to your server.
         - You can also upload the client workshop mod from your PC. The latest github release is identical.
         - When using FTP, make sure binary rather than text or auto transfer mode is selected.
      - Make sure you load the Antistasi Mod. This is usually done via commandline. How exactly again is depending on your server setup. Please consult the documentation available for your service or contact their support, if applicable.
         - Only one Antistasi mod should be loaded at a time.
         - The mod should be loaded as a general mod (-mod), not as a server mod (-servermod). Different servers have different names for these.
         - Clients must load the same Antistasi mod as the server.
      - When you now start the server, you should be able to manually select the missions called :code:`Antistasi Community [Version number]`, load it and play.
         - The vast majority of server providers seem to have an empty mission cycle by default, which means you just get a blank loading screen on connection rather than the selection UI.
         - To get to the mission selection UI in this case, you must log in as admin and then use the server command :code:`#missions`.
         - To log in as admin, use the server command :code:`#login adminpassword`. The admin password is in your server config file.
         - Server commands (such as #login or #missions) are entered in the text chat box. The default text chat key is the slash (/) key.
      - Once the mission has been started, log in as admin to see the setup UI. Voted admins do not count.
      - If you want to set the server up to automatically load the Antistasi mission after a restart, that can be done using the mission cycle in the server.cfg like in the following example.

      .. rst-class:: code-block-3
      .. code-block:: cpp

         // MISSIONS CYCLE (see below)
         class Missions {
            class Mission1 {
               template ="Antistasi_mapname.mapname";
               difficulty = "Regular"; //can be Recruit, Regular, Veteran or Custom. Custom needs setting up though.
               class Params {
                  autoLoadLastGame = 60; //Automatically starts the mission 60 seconds after the first player connected to the server and no admin is logged in. {"No automatic load","1min","2min","3min","5min","10min"}
                  LogLevel = 2; //Sets the log level during the setup. {"Error", "Info", "Debug", "Verbose"}
                  A3A_logDebugConsole = 1; //Sets the Log debug console use during setup. {"None", "All non-dev", "All"}
               };
            };
         };

      :code:`Antistasi_mapname.mapname` needs to be replaced with the appropriate mapname based on which map you want to play.
      Here the available ones:

      .. rst-class:: table-2

      .. flat-table::
         :header-rows: 1

         *  - Map
            - Missionname

         *  - Altis
            - :code:`Antistasi_Altis.Altis`

         *  - Anizay
            - :code:`Antistasi_tem_anizay.tem_anizay`

         *  - Cam Lao Nam
            - :code:`Antistasi_cam_lao_nam.cam_lao_nam`

         *  - Chernarus Autumn
            - :code:`Antistasi_chernarus.chernarus`

         *  - Chernarus Summer
            - :code:`Antistasi_chernarus_summer.chernarus_summer`

         *  - Chernarus Winter
            - :code:`Antistasi_chernarus_winter.chernarus_winter`

         *  - Chernarus 2020
            - :code:`Antistasi_cup_chernarus_A3.cup_chernarus_A3`

         *  - Khe Sanh
            - :code:`Antistasi_vn_khe_sanh.vn_khe_sanh`

         *  - Kujari
            - :code:`Antistasi_tem_kujari.tem_kujari`

         *  - Kunduz
            - :code:`Antistasi_Kunduz.Kunduz`

         *  - Livonia
            - :code:`Antistasi_Enoch.Enoch`

         *  - Malden
            - :code:`Antistasi_Malden.Malden`

         *  - Pulau
            - :code:`Antistasi_pulau.pulau`

         *  - Sahrani
            - :code:`Antistasi_sara.sara`

         *  - Mortain
            - :code:`Antistasi_SPE_Mortain.SPE_Mortain`

         *  - Normandy
            - :code:`Antistasi_SPE_Normandy.SPE_Normandy`

         *  - Takistan
            - :code:`Antistasi_Takistan.takistan`

         *  - Tanoa
            - :code:`Antistasi_Tanoa.Tanoa`

         *  - Tembelan Island
            - :code:`Antistasi_Tembelan.Tembelan`

         *  - UMB Colombia
            - :code:`Antistasi_UMB_Colombia.UMB_Colombia`

         *  - Virolahti
            - :code:`Antistasi_vt7.vt7`

         *  - Weferlingen Summer
            - :code:`Antistasi_gm_weferlingen_summer.gm_weferlingen_summer`

         *  - Weferlingen Winter
            - :code:`Antistasi_gm_weferlingen_winter.gm_weferlingen_winter`

Setup UI
===============

.. card::
   :class-header: header-2

   Setup UI
   ^^^^^^^^^^^^^^^

   Antistasi now has a setup UI for choosing factions and parameters, selecting a game to load or creating a new one. On a dedicated server, you need to log in as admin (/ then #login adminpassword) to see the setup UI. There is an (Arma) parameter to automatically load the previous game for unattended restarts, but new games must be created by an admin.

   **Load game tab:**

   This is where you choose which game to load, or to create a new one. All saves from previous Antistasi Community versions and original/Barbolani Antistasi 1.3+ should work. Descriptions of controls:

   - Copy old game: Loads the selected game, but if saved subsequently it will use a new ID & location.
   - Load old params: Retain the parameters (but nothing else) of the selected game when creating a new one.
   - Use new save file: Save data to AntistasiCommunity.vars instead of the global username.vars.arma3profile. Makes it easier to transfer saves between machines or profiles.

   **Factions tab:**

   This is where you select which factions, DLC and addon mods to use for a new game. You can change them later, but the arsenal and garage will not be updated. If you're loading an older save, make sure that the settings are correct. Options will be greyed out (or not shown) if their mods are not loaded on the server.

   **Params tab:**

   This is where you set parameters for a new game or change them for an old game. Some notes:

   - If you're playing with friends, you may want to disable membership (which makes everyone a member) and disable TK punishment.
   - Increasing spawn distance is not recommended due to the impact on performance and enemy behaviour. On more compact maps, reducing spawn distance to ~800m is often a good idea.
   - When players are AFK they're not counted when balancing the mission. When all players are AFK, new resources and attacks are not generated, so if you're playing solo you can effectively pause the campaign by alt-tabbing.
   - If you want to change how much enemies attack or send supports, start by changing "Overall enemy resource balance".
   - Depending on the server skill/precision settings, the AI skill settings here may not change much. Antistasi works well with server precision settings somewhere around 0.5.
   - SAMs and carpet bombing supports are currently the only "unfair" supports.
   - When the number of items required to unlock is set to "No unlocks", friendly AIs will spawn with equipment based on the quantities in the arsenal. Magazines need three times as many items to unlock.

Game modes
==========

.. card::
   :class-header: header-2

   Game modes
   ^^^^^^^^^^

   -  Rebel versus government versus invader - a three-way war. Everyone fights everyone
   -  Rebel versus government - no invaders, just you versus the government
   -  Rebels versus government and invaders - everyone is against you. The invaders and the government are coming for you.

   I recommend playing rebels versus government versus invaders first. It’s
   easier and allows you to fight two different factions.

Map Markers
===========

.. card::
   :class-header: header-2

   Map Markers
   ^^^^^^^^^^^

   Main Article: :ref:`concept_mapmarkers`

   With that out of the way we can get into the mechanics of the mission.
   Map Markers, also known as strategic zones, are areas controlled by BLUFOR, OPFOR, or guerrillas.
   They all have a specific function and are guarded by their occupiers.
   It’s essential to understand how these strategic zones operate to be
   able to prioritize and plan appropriately. Note that garrisons may start
   off weak, but can be strengthened over time.

   -  **Airbases** are the headquarters of the enemy air force and main staging points for BLUFOR and
      OPFOR. You must be war level 3 to capture them. Taking an airbase provides you with an income of airstrike points;
      used for calling in airstrikes on the map.

   -  **Outposts** are fortifications garrisoned by the enemy. They inhibit
      guerrilla operations in the surrounding area and will send patrols
      and the local garrison to counter resistance actions. Outposts sometimes
      have radio towers inside them. Get more information on radio towers here.

   -  **Resources** give passive income to the occupier. Civilians work the resource. If they are killed the resource will be
      destroyed.

   -  **Factories** multiply the income you gain from resources. Civilians work the factory. If 4 of the workers are killed the
      factory will be considered destroyed.

   -  **Seaports** boost the HR you resource each income tick and also discount the cost of vehicles purchased at the HQ.

Towns
=====

.. card::
   :class-header: header-2

   Towns
   ^^^^^

   Main Article: :ref:`concept_gainingandlosingcitysupport`

   -  Towns are where you will find the people and their vehicles to
      “\ *tactically acquire.”*

   -  Taking these towns gives you a small amount of money in the form of
      taxes and a steady income of HR to bolster your army.

   -  Towns are unique because they are not conquered through military
      means.

   -  **The only way to conquer towns is to conquer the hearts and minds of
      the people. This is done through the town support system.**

   -  The town will be guarded by police when the AI factions control it.

   .. card::
      :class-header: header-3
      :class-card: sd-card-3

      Town support system
      ^^^^^^^^^^^^^^^^^^^

      -  The town support system is a simple system. **Having more people
         supporting your side than the occupiers, the town will flip to your
         side and start handing over their men and taxes to fight for
         freedom.**

      -  You can see each town’s support status by going to the map in HQ -
         selecting map info – and clicking on any town to see the population
         of the town and the percentage of people that support you or the
         enemy.

      -  **The town flips to the rebel’s side if more people support you than
         the enemy inside the town.**

Info Bar
========

.. card::
   :class-header: header-2

   Info Bar
   ^^^^^^^^

   At the top middle of your screen, you should see a range of statistics.
   This is what I refer to as your Info Bar.

   -  **HR** - **the number of men ready to volunteer for the good fight.**
      If you have 10 HR, you can recruit 10 men. You gain HR mainly from
      towns and missions

   -  **Personal Money** - money that is gained through completing missions
      and helping the resistance. You can only buy personal items like
      soldiers or a vehicle. This is capable of being transferred to the
      faction funds.

   -  **Faction money** - money only available to the commander. This can
      be used for almost everything including training and HQ command
      squads.

   -  **War level** - the enemy will gradually get better equipment with
      each war level. **War level increases as the resistance takes more
      territory.**

   -  **BLUFOR/OPFOR Aggression** - whenever you take hostile actions
      against a faction or civilians, that faction gains aggression. A
      faction with high aggression will attack more frequently and with
      more assets.

Your Headquarters
=================

.. card::
   :class-header: header-2

   Your Headquarters
   ^^^^^^^^^^^^^^^^^

   HQ is your home. Here you will plan for missions, recruit soldiers,
   stash and retrieve equipment and more. Your HQ has many objects that
   facilitate various functions. We will go over these now.

   .. dropdown:: Petros
      :class-title: header-3-light
      :class-container: sd-card-3

      Petros is the leader of the resistance. Think of him as a banished political figure. He is the leader of the resistance and if he dies you will lose
      a considerable amount of HR and money. Also see: :ref:`concept_losingpetrospenalties`

      **HQ management**

      -  **Grab $100 from pool** - You can take money from the faction and put it in your wallet. Some things can only be bought with personal money so you will need to use this from time to time.
      -  **In game members list** - Displays all server members. Non server members cannot do certain things. Server admins can add members through the commander’s Y menu.
      -  **Manage garrisons** - Allows you to add or remove soldiers from friendly captured locations.
      -  **Move HQ to another zone** - There will be times where your base will be compromised. You will know this when you get a “defend Petros” mission. Note that they never learn about your HQ’s location, if you keep it there after the attack it will not make any difference.
      -  **Train troops** - Your troops suck at the beginning of game. You basically gave a villager a weapon and point them in the general direction of the enemy. You will need to train your men to turn them into soldiers. You do this through copious amounts of money. This is where the majority of money will go in the mid to late game. Also see: :ref:`concept_trainfia`
      -  **Rebuild assets** - In war, things blow up. In the process of taking a factory, you may have killed all the workers. In order to repair assets, hit this button. Clicking the button will take you to the map where you can choose to rebuild the zones you want. Repairing assets costs you 5000 per location.
      -  **Mission select** - Here you can request missions. More information about missions is available below.

   .. dropdown:: The Whiteboard / Map
      :class-title: header-3-light
      :class-container: sd-card-3

      **Game options**

      -  Here you can persistently save, **which I recommend you do every time
         you log off** as not doing so will mean you lose your progress since
         the last autosave.

      -  There are also minor tweaks you can make here like toggling music or
         selecting how many civilians can spawn at a time (list each option).

      **Map info**

      -  Map info is a useful tool for information. It tells you how many
         people support you or the occupiers, and **if you click on icons, it
         will tell you information about that zone.**

      -  Clicking on a town will show you the percentage of support for you
         versus the occupiers. It also tells you how many civilians the
         invaders have killed there.

      -  Clicking on any other zone will tell you its status combined with the
         garrison’s general strength. Consider attacking weakened or
         decimated zones over higher strength garrisons.

   .. dropdown:: The flag
      :class-title: header-3-light
      :class-container: sd-card-3

      -  The flag is where you recruit soldiers into your personal squad.

      -  **Remember that AI will only pick equipment that matches their role
         and is unlocked inside the arsenal.** Buying an automatic rifleman
         will not give you a man with an LMG if you do not have any LMGs
         unlocked.

   .. dropdown:: The Tent
      :class-title: header-3-light
      :class-container: sd-card-3

      **Sleep**

      -  Whenever you want to skip night-time, just press the “sleep 8 hours”
         function. Warning! Missions will auto fail if they exceed their time
         limit.

      **Make things go away**

      -  You can make the rain, the fog, or the nearby forest disappear using
         these options.

   .. dropdown:: The Arsenal
      :class-title: header-3-light
      :class-container: sd-card-3

      -  The arsenal is where all weapons and equipment are stored and
         retrieved from.

      -  You can create, save, and load loadouts from the arsenal for quick
         changes in equipment.

   .. dropdown:: The garage / vehicle arsenal
      :class-title: header-3-light
      :class-container: sd-card-3

      **Open garage**

      -  **Here is where you can ungarage all of your ground vehicles.**

      -  Inside the garage You can mount certain weapons to vehicles. For
         example, if you have a .50 Cal MG you may be able to mount it on the
         back of a truck.
      -  You can also customize your vehicle changing its attachments or painting it a different colour.

      **Heal nearby units**

      -  Hit this button to heal, refill stamina and allow all players and
         ungaraged vehicles to go undercover close to the red box.

      **Buy vehicle**

      -  Here you can buy civilian and military vehicles (vehicles covered in
         a later section).

      **Buy loot box**

      -  Provides you with a small box that can automatically collect loot
         within a small radius.

      -  These boxes can be loaded into the cargo of your truck.

      -  It makes looting much faster, and I highly recommend taking one with
         you everywhere you go.

      -  Loot box will only pick up locked items. If you already have unlocked
         M4 carbines it will not pick these weapons up. You can change this
         parameter in parameters

   .. dropdown:: Sources for the Garage
      :class-title: header-3-light
      :class-container: sd-card-3

      Open the garage and you will see three white squares in the bottom right
      of the screen. These white boxes indicate whether or not you have a
      fuel, ammo, or repair truck.

      -  You need these vehicles to repair, rearm and refuel your vehicles in
         the garage.

      -  For example, if you don’t have a repair vehicle, you will have to
         manually repair damaged vehicles with toolkits.

      -  You can find fuel trucks in towns. Just drive around and you will
         find a tanker.

      -  You can find the ammo truck on ammo convoy or steal and destroy ammo
         truck missions

      -  You can find a repair truck by destroying a radio tower, then waiting
         for a repair the radio tower mission.Alternatively, you can find on
         through a downed helicopter mission.

      *Take these trucks and store them in the garage*. I recommend locking
      them so no one takes them out.

Commander and Member Functionality
========================================

.. card::
   :class-header: header-2

   Commander and Member Functionality
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   **Commander functionality:**

   - Can purchase high command squads & vehicles.
   - Has access to high command UI (ctrl+space).
   - Can use Y->AI management menu with HC squads.
   - Can fast-travel HC squads.
   - Can order mortar strikes with HC squads (shift+Y).
   - Has access to direct garrison recruitment (on Petros).
   - Can create and delete roadblocks & watchposts.
   - Purchases vehicles with faction money.
   - Can manage arsenal guest limits.
   - Persistent save on game options menu is a global save.
   - Can edit ambient civ limit and spawn distance in game options menu.
   - Can override garage locks.
   - Can order airstrikes.
   - Can steal money from the faction.

   **Member functionality:**

   - Can request missions from Petros.
   - Can recruit AI for personal squad.
   - Can take limited(non-unlocked) items from the arsenal.

   .. card::
      :class-header: header-3
      :class-card: sd-card-3

      Guest Commander System
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      There is now a parameter to allow guests to be commander. Guests are marked ineligible for commander by default, but can toggle eligibilty in the usual way (Y->commander->???). Eligible members have priority when selecting the commander, and members can force a re-election (and so remove the guest from the commander role) by making themselves eligible.

      Guest commanders have access to a limited range of commander functionality. They can request missions, spend faction money, use high command and move HQ. They cannot override garage locks, steal money from the faction or modify arsenal limits. They also do not receive member privileges such as the ability to recruit AI to their personal squad or take limited items from the arsenal.

      Guest commanders count as a leash centre for the purposes of the guest leash system, which enables the commander and nearby guests to respond to distant attacks and punishments even when there are no members on the server.

Missions
========

.. card::
   :class-header: header-2

   Missions
   ^^^^^^^^

   Main Article: :ref:`mission_overview`

   There are several categories of missions all which have different tasks and rewards:

   - **Assassination Missions**
      - :ref:`mission_kill_the_officer`
      - :ref:`mission_kill_the_traitor`
      - :ref:`mission_specops`
   - **Conquest Missions**
      - :ref:`mission_resource_acquisition____take_the_outpost`
   - **Convoy Missions**
      - :ref:`mission_ammo_convoy`
      - :ref:`mission_armored_convoy`
      - :ref:`mission_money_convoy`
      - :ref:`mission_prisoner_convoy`
      - :ref:`mission_reinforcements_convoy`
      - :ref:`mission_supplies_convoy`
   - **Destroy missions**
      - :ref:`mission_destroy_radio_tower`
      - :ref:`mission_downed_heli`
      - :ref:`mission_steal_or_destroy_armor`
   - **Logistics Missions**
      - :ref:`mission_bank_mission`
      - :ref:`mission_salvage_supplies`
      - :ref:`mission_steal_or_destroy_ammo_truck`
   - **Rescue Missions**
      - :ref:`mission_pow_rescue`
      - :ref:`mission_refugees_evac`
   - **Spawned Dynamically**
      - :ref:`mission_defend_petros`
      - :ref:`mission_tower_rebuild_disrupt`
   - **Support missions**
      - :ref:`mission_city_supplies`

   **Convoy ambush tips**

   Most convoys are similar so I decided to make a one size fits all guide.

   -  Use mines and IEDs only on isolated roads where civilians will not drive.
   -  Set up entrenchments through the Y menu or using your E tool.
   -  Use roadblocks to slow down or immobilize the enemy.
   -  LMGs, grenade, and rocket launchers will help thin the numbers.
   -  Most convoys will have one or two light vehicles with 50.cal Mgs, and infantry trucks.
   -  Priorities are the 50. Cals, then the infantry trucks.
   -  Try and kill the infantry as they disembark.
   -  You won’t be able to loot soldiers killed inside destroyed vehicles. Better yet, spray them with an MG as they disembark.

Airstrike Points
================

.. card::
   :class-header: header-2

   Airstrike Points
   ^^^^^^^^^^^^^^^^

   Main Article: :ref:`concept_airstrikes`

   -  Once you capture an airbase you will get a passive income of
      airstrike points.

   -  Each airstrike point allows one airstrike to be called in on a
      target.

   -  This is one of the biggest advantages of an airbase. Use airstrikes
      to weaken enemy outposts before launching an attack.

   -  Use cluster bombs for armour and incendiary and HE bombs for
      infantry.

   -  Incendiary bombs can kill crews without destroying the vehicle,
      allowing for recovery.

The Y menu
==========

.. card::
   :class-header: header-2

   The Y menu
   ^^^^^^^^^^

   Press the “y” key to open this menu. You will use this menu for fast
   travel, managing AI, transferring and managing money, recruiting, and
   more.

   - **Fast Travel** - Depending on your parameters setting, you can fast travel to and from different zones provided there are no enemies within 500 meters of you. You can use fast travel to transport High Command squads and vehicles as well.

   - **Player and Money** - Here you can add or remove a player to/from the member list temporarily (until the server is restarted). Non server members do not have access to equipment that is not unlocked. Look at a player and press add server member to give them server membership. You can transfer your personal money to other players or the faction funds.

   - **Undercover On** - Use this setting to go undercoverif you are not being spotted by anyone and are not wearing suspicious equipment.

   - **Construct Here** - A number of objects used for cover and obstacles can be built through this menu. Only bunker options cost money and you must have an engineer in your squad or be an engineer to build bunkers.

   - **Garage vehicle** - Look at a vehicle while in a friendly location and press this button to send it to the garage.

   - **Unlock vehicle** - Allows other groups to use your vehicle.

   .. dropdown:: AI Management Menu
      :class-title: header-3-light
      :class-container: sd-card-3

      How to use: select the squad mate/HC squad you want to command, then
      select the command you want to do. For example, if I want only one of my
      squad mates to loot, I’d select them through the function keys then
      select “Auto Ream/loot.”

      - **Temp AI Control** - This option allows you to take direct control of an AI unit.
      - **Auto Rearm/Loot** - This command will allow your AI to upgrade their equipment from fallen enemies. If you use this command while they are in a vehicle, the AI will load the loot into that vehicle instead.
      - **Auto Heal** - This command allows your AI to heal themselves and others.
      - **Squad Sitrep** - Use for HC squads. They will tell you their combat status, how many of them are still alive, and if they are embarked or disembarked from their vehicle.
      - **Garrison units** - Use this command to add units to a garrison. This is especially useful when you have just taken a strategic zone and you need to defend from an enemy counterattack.
      - **Dismiss units** - Use this to dismiss/delete units. You will gain back the money for the vehicles but not for infantry/crew.
      - **Squad add vehicle** - Give HC squads vehicles they can use. This is especially useful for the INF team that is small enough to serve as a crew for armoured vehicles.
      - **Mount/ Dismount** - Forces HC squad units to mount/dismount their assigned vehicle.

   .. dropdown:: Commander menu
      :class-title: header-3-light
      :class-container: sd-card-3

      **Recruit Inf Squad**

      - **Normal squad** - 8-member with a medic and AT capabilities
      - **Engineer squad** - 8-member with an engineer, medic, and AT capabilities
      - **MG squad** - 8-member squad with a HMG, medic and AT capabilities
      - **Mortar squad** - 8-member squad with mortar, medic and AT capabilities. Also see: :ref:`concept_counterbatteryfire`
      - **Recruit Inf team** - 4 men small cost. Can be used for crewing vehicles
      - **Recruit AT team** - 5 members with 3 of which with AT launchers. Medic capabilities
      - **Recruit AT car** - SPG-9 Technical with 2 members, a gunner and a driver
      - **Recruit AA truck** - 2 members with a ZU-23-2 AA platform mounted on a Ural truck
      - **Recruit MG team** - 2 members with an HMG
      - **Recruit Mortar team** - 2 members with a mortar
      - **Recruit Sniper team** - 2 members. One spotter and one sniper.

      **Air Support**

      - **HE bombs** - High explosive bombs. Effective against infantry
      - **Cluster bombs** - Effective against armoured vehicles
      - **Napalm bombs** - Effective against infantry
      - **Add to air support** - Trades an air vehicle that you are looking at for air support points

      **Build outpost/Roadblock**

      -  Click on a road to place a roadblock. A 5-man roadblock team will
         spawn and drive an armed vehicle to that location to guard the road.
         Click away from a road and you will get a 2-man observation outpost
         who will provide recon and will not fire unless fired upon.


      **Garbage clean**

      -  Cleans up the map of items left over. This will help with performance
         especially after many/large fights.

      **Delete outpost / roadblock**

      -  Deletes observation posts/roadblocks.

      **Resign/Eligible**

      -  Makes you resign as commander OR become eligible/ineligible for being
         given the role.

      **Sell Vehicle**

      -  Sells a vehicle you are looking at for money.

AI management and commanding
============================

.. card::
   :class-header: header-2

   AI management and commanding the AI (micro managing)
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   AI management is essential to winning Antistasi, especially if you are
   alone. Managing AI is only half the battle, I recommend reviewing AI and
   how they work to understand how to fight and command AI effectively.

   .. dropdown:: Personal Squad management
      :class-title: header-3-light
      :class-container: sd-card-3

      -  First, learn the command system. Learning how to more intricately
         command our units allows us to apply our AI in different ways. You
         can learn how to command AI through the ARMA 3 tutorial.

      -  Be the spotter. Your AI will start with terrible spotting skill. The
         person in charge of spotting is the team leader, who has the highest
         spotting skill. But when you are in charge, you are the team leader.
         That is why you must spot for your AI. (\ ` + space while looking at
         target to spot) your AI will track enemies that you spot and fire
         with astonishing accuracy.

      -  AI are adept at crewing weapons regardless of their training. Put
         them on a 50.cal, or a mortar and they will fire with perfect
         accuracy. Use your AI to crew weapons and spot for them. You will be
         surprised at their effectiveness.

      -  Use Auto rearm/loot so your AI can get better gear in the field.

      -  While undercover, place your soldiers in cover and target enemies
         with each friendly soldier. Once their cover is blown, they will
         track and kill that target. This is great for ambushing.

      -  AI takes the attention off of you.

      -  Use the suppressive fire command to keep the AI pinned down. AI that
         are suppressed act irrationally and will be less accurate.

      -  Use AI as a distraction. For example, you can use a squad of AI to
         distract a local outpost while you destroy their radio tower.

   .. dropdown:: HC squad management
      :class-title: header-3-light
      :class-container: sd-card-3

      -  HC squads are primarily controlled through the Y menu and the map.

      -  To select HC squads, use CTRL + SPACE then select which squad you’d
         like to control

      -  On the map, you can only order move/attack orders.

      -  To instruct mortars to conduct a fire mission, have the unit selected
         then select SHIFT + Y.

      -  HC squads cannot be micromanaged to the degree that you can with your
         personal squad.

      -  Every squad will have its own squad leader who will spot for their
         squad mates.

      -  When you mount your squads, make sure that you place a move order on
         the road. AI are terrible at driving offroad.

      -  Disembark your squads away from the fight. The AI are slow to
         disembark even when getting shot at.

Storing equipment
=================

.. card::
   :class-header: header-2

   Storing equipment
   ^^^^^^^^^^^^^^^^^

   I will quickly go over how to store equipment in this game, because
   there are many ways to do it and sometimes you may have trouble storing
   a particular item.

   .. card::
      :class-header: header-3-light
      :class-card: sd-card-3

      Transfer vehicle cargo
      ^^^^^^^^^^^^^^^^^^^^^^

      -  Anything you put inside your vehicle can be quickly and easily
         transferred into the arsenal by using the interaction menu while
         looking at the arsenal.

   .. card::
      :class-header: header-3-light
      :class-card: sd-card-3

      Storing loot boxes and arsenal boxes
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      -  Sometimes you will find an ammo box filled with weapons and equipment
         that you can load onto a truck and take back to base.

      -  Obviously, you need a vehicle with sufficient cargo capacity to load
         the box and then move it back. Just put the vehicle close to the box
         then use the interaction menu to transfer the box to the back of the
         vehicle.

      -  Once you get to the base, the easiest way to transfer to the arsenal
         is unloading the box, opening the Y menu, then selecting “Put vehicle
         in garage.”

      -  Sometimes that might not work. Another way is with the box still
         loaded onto the truck, drive it as close as possible to the arsenal
         with the back of the truck closest to the arsenal as if you are
         unloading the box into the arsenal. Then select on the arsenal
         “transfer vehicle cargo to ammo box” this is buggy so it may take
         multiple tries but it does work.

      -  Lastly you may be able to unload the box, close to the arsenal and
         transfer vehicle cargo to ammo box.

      -  Hopefully with these three ways you will never have trouble storing
         the box. You can use this same method on loot boxes as well.

Looting
=======

.. card::
   :class-header: header-2

   Looting
   ^^^^^^^

   -  Looting is a core part of Antistasi. You need to learn how to
      effectively and safely collect loot.
   -  For starters, always have a loot box. You can obtain loot boxes for
      $10 at the vehicle box.
   -  These loot boxes can be loaded into the back of the truck or inside
      the cargo of any vehicle using ace interact if there is not enough
      cargo capacity.
   -  Loot boxes allow you to collect loot with the press of a button.
   -  Simply look at the box and use the interaction menu to collect
      loot.
   -  The loot box only collects loot that has yet to be unlocked. I.E., it
      will not pick up the M4 if you already unlocked it inside the
      arsenal.
   -  You should only loot when you believe it is safe to do so.
   -  Use your vehicle as cover while looting, it will save your life. I
      like to drive in between unlooted enemies, loading and unloading the
      loot box as needed. This way I can retain the safety of the vehicle.
   -  You can also use the Auto Rearm/loot function AI in a vehicle to
      have them collect and load loot into the vehicle for you.

   .. card::
      :class-header: header-3
      :class-card: sd-card-3

      Managing your loot and arsenal
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      -  In Antistasi you start with limited gear. If you find enemy
         equipment, like an assault rifle for example, you can collect enough
         to eventually “unlock” that equipment.

      -  In order to unlock a weapon, you must have a certain amount of a
         weapon stored in your arsenal. This depends on your parameters. The
         default is 25.

      -  Explosives and Guided AT/AA Launchers cannot be unlocked by default,
         check parameters to change that.

      -  For ammunition, you must have a certain amount to unlock that
         ammunition. You can change this in parameters. The default is 25
         magazines of that weapon.

      -  If you’d like the ammo of a weapon to be automatically unlocked with
         the weapon, there is an option in parameters.

      -  Unlocking equipment allows your AI soldiers to use that equipment.
         For example, after unlocking an assault rifle, new soldiers will
         choose to carry that weapon instead of bolt-actions or SMGs. The
         equipment will also become infinite inside the arsenal.

      -  Obviously, we want ourselves and our soldiers to have the best
         equipment possible. So, we have to attempt to unlock as much
         equipment as possible.

      -  This means always looting the enemies you kill, at least in the early
         to mid-game. As you kill and loot, more equipment becomes unlocked in
         the arsenal and as a result you and your soldiers will become more
         lethal. But there are ways you can speed up this process.

      **There are essentially two schools of thought when it comes to
      equipment.**

      -  The first is to **never take any equipment you want unlocked until it
         is unlocked.** Choose to use worse weapons and equipment so that you
         may unlock that equipment faster. For example, I have 20 M4s **but I choose to use a FAL instead until I get 5 more M4s.**

      -  The second method is to take everything you want **as long as you believe it will make you more likely to come home alive.**

      Both methods have merit. I used to religiously use the first method   and died and failed more often, but when I DID succeed, I kept those weapons no matter what. I think it is more optimal to use what you have if it will make you more effective. Recently I started using equipment that was rare and I found I won more often. It’s really a risk versus reward analysis at the end of the day. Do what you think is optimal.

Loadouts
========

.. card::
   :class-header: header-2

   Loadouts
   ^^^^^^^^

   Please note there are no rules to loadouts, but if you are using the
   ACE mod, you have to account for medical supplies, ammo, weapons, and
   how that equipment will affect your weight. The heavier you are, the
   faster your stamina bar will deplete. This will have an adverse
   effect on your accuracy and speed.

   I assume you are using ACE for this tutorial.

   Here are some suggestions on loadouts you will likely need to pull
   quickly during emergencies. All of these loadouts will have 5 elastic
   bandages, 5 packing bandages, two 500m blood, 2 splints, 2 tourniquets
   and an entrenching tool. For most loadouts, I carry only two grenades and
   two smoke grenades.

   .. dropdown:: Starting loadout
      :class-title: header-3-light
      :class-container: sd-card-3

      -  Starting loadout, I go with a lot of grenades and pistol ammunition,
         I find the WW2 bolt action rifles you get at the start do not do
         enough damage.

      -  I spam grenades and don’t carry a primary to offset the weight of the
         grenades.

   .. dropdown:: AT and AA
      :class-title: header-3-light
      :class-container: sd-card-3

      -  There will be times you will need to grab an AT kit fast.

      -  I usually use an SMG or no primary with heavy AT weapons like the
         javelin or MAAWS because I have to account for the roughly 40-50
         pounds more I will carry.

      -  I carry as many extra rockets as I can carry in my backpack and I
         carry a bigger backpack.

      -  This will make me unbearably heavy so I will have to put some of the
         rockets in my truck to allow me to move around.

   .. dropdown:: MG
      :class-title: header-3-light
      :class-container: sd-card-3

      -  There are times where I want/ need to kill infantry fast. Enemies in
         Antistasi clump up a lot and makes machine gunners drool.

      -  I always put a 4x or higher scope, plenty of ammunition and usually I
         do not carry a secondary.

      -  I put ammo in my vehicle to offset the weight.

Undercover and how to use it
================================

.. card::
   :class-header: header-2

   Undercover and how to use it
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   -  In the early to mid-game, you can dress as a civilian and go
      undercover to recon and ambush enemy positions.

   -  This is an essential tool as it opens up many options for the
      resistance. This is the one advantage your opponent does not
      possess.

   -  In the top part of your screen, it will say (undercover: off/on) on
      coloured in green means you are undercover.

   -  In order to go undercover, you must be in civilian clothes and not
      wearing any military equipment. Being naked does not count either.
      Vests, NVG’s and helmets count as military equipment, but all
      backpacks are safe to wear.

   -  Press Y to open the Y menu and click “undercover on” to go
      undercover.

   -  Jumping into an unreported civilian vehicle will also put you
      undercover even if you are in full military gear.

   -  If you leave the truck near enemies while having military equipment
      on you will be “spotted” and lose your undercover status.

   -  Additionally, going off-road with any vehicle will get you spotted.
      If there are any enemies around Stay to the roads.

   -  Note that passing through checkpoints (the roadblocks you will see
      driving around) sometimes spots you. While this can happen at the
      lower levels of aggression and war level, the higher they become, the
      higher the chance of being spotted.

   -  If you are spotted and jump into a civilian vehicle that vehicle may
      become reported and will render it unable to give you undercover
      status. Try to re-enter your vehicle when no enemies are around.

   -  You can stash your weapons in your backpack and take it out when you
      need it. Understand the second you take out your weapon, even if no
      one sees you, you will be “spotted” and cannot go back undercover.

   -  Use enhanced movement and the E tool to obtain entrenched and
      elevated positions to ambush the enemy. They won’t shoot as long as
      you retain your undercover status

   -  Use your undercover status to recon enemy areas. Find out how many
      men they have, what equipment are they carrying, ETC.

   -  Use undercover to spot for your friendly artillery. You will become
      spotted if the enemy sees you even if you are just “spotting” so use
      cover and spot from a distance.

HQ placement
============

.. card::
   :class-header: header-2

   HQ placement
   ^^^^^^^^^^^^

   -  Placing your HQ correctly is critical to the success of your
      resistance.

   -  You want your HQ to be both concealed and close enough to strategic
      zones for missions.

   -  Always place your HQ on or near the end of a road. You will want all
      of your vehicles to be on a road so you can go undercover. Going off
      road may get you spotted.

   -  Never place your HQ in between towns or other strategic zones. The
      enemy sends patrols in between zones and may spot your HQ.

   -  Place your HQ inside a compound and put Petros inside a building for
      added protection.

   -  Place your HQ within 4km of strategic zones so you can get missions.
      Any area 4km or more from your HQ will not be available for missions
      (distance can be changed through parameters)

Vehicles
========

.. card::
   :class-header: header-2

   Vehicles
   ^^^^^^^^

   -  There are only certain vehicles you can purchase through the red box.
      Civilian vehicles, and military vehicles.

   -  Civilian vehicles are vehicles you can purchase and go undercover
      when you enter them

   -  Military vehicles are vehicles that cannot go undercover and are
      sometimes armed. Weapon statics such as a mortar or HMG’s can also be
      bought.

   -  Off-roads are the backbone of the resistance. These can carry up to 6
      rebels, load supplies, loot, and arsenal boxes. And well, go offroad.
      To boot, they are a cheap 200 bucks! Use these liberally. Honestly,
      this is the only civilian vehicle you need.

   -  SPG-9s and SPG-9 mounted vehicles, this is your best purchasable
      equipment for dealing with enemy armour. The scopes can be
      complicated, but they allow you to fire from longer ranges and is
      very handy once you get the hang of it. The SPG also has HE shells,
      use these to terrorize infantry. Be warned however the SPG is a hit
      or a miss with tanks and IFVs (Infantry Fighting Vehicles).

   -  DSHK and the DSHK mounted vehicles are a great substitute to a M2
      HMMV. use these to out range enemy infantry. (700M or more) throw AI
      on it and target with binoculars for increased effect.

   -  ZU-23-2; your deadliest purchasable weapon and bane of all things air
      and infantry. Place these in your captured zones to annihilate enemy
      air attacks.

Taking a strategic point
========================

.. card::
   :class-header: header-2

   Taking a strategic point
   ^^^^^^^^^^^^^^^^^^^^^^^^

   .. card::
      :class-header: header-3-light
      :class-card: sd-card-3

      What you will need
      ^^^^^^^^^^^^^^^^^^

      -  Taking a strategic point in the early game is no easy challenge.

      -  The enemy’s vehicle arsenal is big and getting bigger every day so
         you will need at least this on hand to take and hold a point.

      -  You will need AT to eliminate Armor threats. NLAWs, MAAWS and JAVELIN
         launchers are the best launchers. The NLAWS and JAVELINS especially
         so because the missile will lock on to the target and should heavily
         damage when it hits.

      -  Armor tends to show up in the mid to late game more often than the
         early game, but you should have some on hand nonetheless.

      -  *You will need anti air when taking a strategic point.* Transport
         helicopters like little birds and chinooks can be taken down with 50.
         Cal MGs but for enemy attack helicopters and jets you will need
         proper AA launchers like the IGLA or STINGER missile launchers.

      -  From personal experience the most likely attack will be 1 or more
         helicopters filled with infantry (in the early game) but you should
         be ready for anything.

      -  You will also need a large amount of infantry on standby. Taking a
         point, you may be able to do alone, *but if you leave the strategic
         zone or more than a single enemy comes inside the strategic zone, the
         zone will flip to the enemy.*

      -  That is something you never want for reasons I'll explain later. That
         is why you will always want friendly infantry nearby to take and hold
         the point.

      -  I usually bring at least double the men the resource has. If they
         have 20, I bring 40. Even if my soldiers have body armour, helmets
         and rifles, they will not have AT launchers, LMGs, or other rare
         equipment and their training will definitely be inferior to the
         enemy. That is why I bring double at least.

   .. card::
      :class-header: header-3-light
      :class-card: sd-card-3

      Scouting your target
      ^^^^^^^^^^^^^^^^^^^^

      -  Go to map info and check to see if the garrison is in a weakened
         state. *If its status is weakened or decimated it will have a
         smaller garrison and easier to attack.*

      -  You should also scout the point you will attack and plan ahead.

      -  Find out how many of them there are and what their equipment looks
         like.

   .. card::
      :class-header: header-3-light
      :class-card: sd-card-3

      Taking the point
      ^^^^^^^^^^^^^^^^

      -  Ok, so you’ve scouted the target, you have double the men outside the
         zone ready to take the point on your command. You have both AA and AT
         assets ready to fight the counterattack. What now? Now you attack.

      -  *The real objective is from the point the fight first starts to
         finish it as fast as possible.*

      -  *The longer you wait, the more likely the enemy will continually send
         unmarked reinforced convoys or transport helicopters to replenish the
         garrison.*

      -  Once you flip the point by interacting with the flag, *you MUST hold
         it.* The enemy will send one counter attack and if you take it down,
         congrats the point is yours. *But, if the enemy takes the point with
         their counterattack, and you flip it back, then you will have to face
         another counter attack AFTER you finish off the previous counter
         attack.* That is often enough to overpower you and force a retreat.

   .. card::
      :class-header: header-3-light
      :class-card: sd-card-3

      After you take the point
      ^^^^^^^^^^^^^^^^^^^^^^^^

      -  Ensure you have a large garrison to protect the point. If you have
         any, you should place static weapons and allow the AI to use them in
         case an attack comes.

      -  In the later stages of the game, I always have a ZU in every other
         zone. That is expensive though.

      -  The enemy WILL attempt to take this point again, make sure you are
         there to keep that point.

Taking an airbase
=================

.. card::
   :class-header: header-2

   Taking an airbase
   ^^^^^^^^^^^^^^^^^

   So, you have a few towns, resources, factories and outposts under your control, a good amount of HR, money, equipment and even some armour assets. What’s the next big step? Taking an airbase of course. Taking an airbase is your gateway to what I call the late game. It allows you to ungarage and use air assets, you have the chance to gain a couple armour and air assets, and you cement your hold on the region. It’s a HUGE power spike.

   But it is not for the faint of heart. This won’t be your usual outpost smash. Air Bases have multiple squads of infantry, MG towers, mortars and even stationary AA Armoured vehicles. There are no armour patrols. Only a stationary AA vehicle which can be anything.

   .. card::
      :class-header: header-3-light
      :class-card: sd-card-3

      What you will need
      ^^^^^^^^^^^^^^^^^^

      -  You can take and hold an airbase in many ways, but three things you
         absolutely must have: AA, AT, and a ton of infantry. Mortars and
         armour helps too. I would not suggest using any air assets as the air
         bases usually have AA sites.

   .. card::
      :class-header: header-3-light
      :class-card: sd-card-3

      Attacking and holding the airbase
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      -  You will want to start with killing the enemy mortar, armour and MG
         towers first.

      -  Javelins make short work of armour

      -  Mortars can do wonders against the infantry, mortars, and MG
         towers.

      -  Once you soften them up, it’s time to send in the infantry. Assist
         the infantry in killing off the remaining infantry and take the
         airbase.

   This is all easier said than done, it might be a process. It once took
   me an hour of dying, and sending waves of infantry to finally take it.
   But the ruthless amount of equipment and manpower it may take is all
   worth the reward. This is part of the victory conditions so either way,
   you need the air base.

Enemy AI behaviour
==================

.. card::
   :class-header: header-2

   Enemy AI behaviour
   ^^^^^^^^^^^^^^^^^^

   Many people who play Arma 3 don’t understand how the AI works. They
   complain of the AI being terminators. They never miss, they don’t see
   foliage, etc. this section will explain how the AI works and how to
   more effectively manipulate and win against them.

   -  *AI responds to suppression.* Enemy AI who are suppressed will react
      irrationally and their accuracy and spotting skill will decrease.
      Keeping steady fire on the enemy will give you an edge in combat.

   -  *AI do see foliage.* Large bushes and foliage that are larger than
      the player’s character hide the player. Bushes smaller than the
      character are inconsistent at concealment however.

   -  *AI can’t see through smoke.* The AI will not be able to see through
      smoke. However, the cloud of smoke must be fully formed to
      conceal.They may also fire through smoke because it was the last
      known position of the player, and they are attempting to suppress.

   -  *The AI does not care about visual camouflage.* It does not matter if
      you wear forested or arid camouflage clothing in a forested
      environment.

   -  *The AI will spot an enemy with a line of sight based on their
      camouflage coefficient number.* A sniper role will have a coefficient
      number of 0.8, making him harder to spot than a basic rifleman that
      has a coefficient number of 1.2. This camouflage coefficient number
      is affected by movement, noise, and stance of the player.

   -  Being prone and crouching will make you less visible to the AI.

   -  The AI will react to audible noises like sprinting close to them or
      firing. Walking slowly to an enemy may allow you to get the jump on
      them.

   -  Suppressed weapons reduce the range at which the AI can hear you
      firing from. They do not prevent the AI from hearing the shot
      altogether.

   -  Continually firing your weapon without pause, even with a suppressor
      will result in the AI looking for the source of the incoming fire and
      identify the source of the fire unless the attacker relocates.

   -  AI can hear you breathing when you are fatigued.

   -  *AI responds to movement.* The faster you move, the more likely it is
      the AI to see you.

   -  *Flashlights will make you more visible to the AI.* especially in low
      light environments.

   -  *AI use offset targeting.* They will become more accurate the longer
      they shoot at a stationary target. Keep moving in combat to avoid
      getting shot.

   -  *AI will attempt to advance and flank the enemy.* Keep moving to
      avoid being flanked by the enemy.

   Credit:

   https://armedassault.fandom.com/wiki/AI_Basics:_Detection

   https://armedassault.fandom.com/wiki/AI_Basics:_Targeting_priority

Support System
==============

.. card::
   :class-header: header-2

   Support System
   ^^^^^^^^^^^^^^

   Enemy squad leaders can call in support in various forms when they
   come under attack from either opposing force. The ability to call in
   supports CAN be transferred from a killed squad leader to the next
   person who controls the group. As the war level increases, more
   options to what the faction can call in opens up. There are more
   factors than just war level to what may be called in.

   Supports:

   -  Quick Reaction Force

   -  Mortars

   -  Generic airstrike

   -  Close Air Support

   -  Air Superiority Fighter

   -  155mm Artillery

   -  Gunship (Vanilla Only)

   -  Carpet Bomber (Unfair Param)

   -  SAM Site (Unfair Param)

   -  Orbital Strike (Futuristic Param)

Victory condition
=================

.. card::
   :class-header: header-2

   Victory condition
   ^^^^^^^^^^^^^^^^^

   Main Article: :ref:`concept_winlossconditions`

   Now it’s time to understand how we win the game. You must own all
   airbases and more than 50% of the population of Altis must support your
   side. You can own all of the map. and still not win. you need to work to
   take airbases and win the hearts and minds of the people to win.

Walkthrough
===========

.. card::
   :class-header: header-2

   Walkthrough
   ^^^^^^^^^^^

   .. card::
      :class-header: header-3-light
      :class-card: sd-card-3

      Early game
      ^^^^^^^^^^

      -  Your first priority is gear. You should not attempt to take and hold
         any zones until you have a rifle, body armour, and helmet unlocked.
         This could take 10-20 hours of your campaign.

      -  Start by killing the patrols scattered around towns and completing
         the easy missions (city supplies and kill the traitor)

      -  Missions should be your bread and butter until the earlier mentioned
         goal is accomplished.

      -  As you accrue better weapons and vehicles, attempt to tackle more
         difficult missions.

      -  Checkpoints are great ways of getting some gear, including a useful
         50.cal mounted vehicle.

      -  Use all available resources to take on greater odds. *Improvise adapt
         overcome.*

      -  Once you obtain placeable explosives like C4, you should work to
         destroy nearby radio towers. Destroying these radio towers will keep
         the enemy from brainwashing the people and allow you to more easily
         convert them.

   .. card::
      :class-header: header-3-light
      :class-card: sd-card-3

      Mid game
      ^^^^^^^^

      -  Once the original goal is completed, it’s time to take a strategic
         zone (refer to taking a strategic zone section), take an outpost with
         a radio tower or a resource first. Garrison 20-30 soldiers for an
         adequate defence.

      -  Now that you have a zone under control expect frequent attacks
         depending on the aggression of the enemy factions. Defend against
         those attacks and scavenge their dead for equipment.

      -  Continue attacking zones only when you have the opportunity to. (You
         will need the vehicles, HR and money)

      -  Fortify your zones with static weapons, soldiers, and cover. This
         will allow you to stay on offense later in the game.

      -  As you gain more advanced AT options, attempt to capture enemy armour
         and turn it against them.

      -  Use roadblocks and observation posts to solidify your hold on an
         area. Observation posts can be used as fast travel points as long as
         they are 500 meters or more from an enemy (must change fast travel
         parameters for this to work).

      -  Use your excess money to train your soldiers. This will make them
         more comparable to the enemy’s hardened infantry.

      -  Once you have a surplus of soldiers, AA and AT assets, and hopefully
         armour it may be enough to take an airbase. Taking an airbase is no
         easy matter. Refer to taking an airbase section for more.

      -  You should attack an airbase only when you feel you’re ready. You
         need to recon the area and plan accordingly to win the day.

      -  Note that attacking an airbase does not have to succeed on the first
         attack. Launch multiple attacks and whittle them down.

   .. card::
      :class-header: header-3-light
      :class-card: sd-card-3

      Late game
      ^^^^^^^^^

      -  Gaining an airbase is your way of knowing “we’re in the end game
         now”

      -  You should have gained armour and air assets, as well as a passive
         income of airstrike points from your airbase. Now it’s time to turn
         from a resistance to an army.

      -  Use your new assets to continue conquering Altis. Make liberal use of
         airstrikes and soldiers to overwhelm the enemy

      -  Use your armour assets carefully. You can be surprised at the
         accuracy of enemy AT. kill the AT assets first and focus on enemy
         armour.

      -  As you take from the government, so will the invaders. This will
         culminate in a power vacuum in between you and the invaders. The
         government will run out of vehicles and unable to counterattack or
         retaliate at all. I call this the collapse of the occupiers. Take
         advantage and take as much from the government as possible. It’s free
         real estate.

      -  Once the government is gone, it’s just you versus the invaders. The
         invaders have a full vehicle arsenal and are not tolerant with the
         local populace. Piss them offand they will destroy cities and kill
         civilians.

      -  Defend every city retaliation. If they kill 1/3\ :sup:`rd` of the
         population of the map you lose the game.

      -  Be prepared for massive attacks because of their full arsenal. Once I
         had to fight 5 jets all at once!

      -  Take airbases and continue to convert as much as possible to win the
         game. You need at least 51% of the population supporting you and all
         air bases to win the game.

      -  This is all a process. You will die. A lot. You will fail attacks.
         The way to win Antistasi is persistence. Keep trying until you win.
         Whittle down the enemy. Sometimes it’s a slog, but I know you can do
         it. Good luck commander!

Translation of Antistasi - How can I help?
=============================================

.. card::
   :class-card: sd-card-2 sd-mt-3
   :class-header: header-2

   Translation of Antistasi - How can I help?
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Our goal is it to translate Antistasi into all languages which are supported by Arma which are the following:

   * Czech
   * French
   * German
   * Italian
   * Japanese
   * Korean
   * Polish
   * Portuguese
   * Russian
   * Simplified Chinese
   * Spanish
   * Turkish

   If you want to help to translate Antistasi in one of the languages mentioned above, the way to get on board and to help is to join our `Discord Server <https://discord.com/invite/TYDwCRKnKX>`_ and to contact Bob Murphy :code:`bob_murphy` by either sending him a DM or by poking him in one of the public channels and stating that you'd like to help with the translation. He will check in with you and onboard you.

   For more detailed information on the translation of Antistasi, check out the `Translation-Localization of Antistasi via Tolgee <https://official-antistasi-community.github.io/A3-Antistasi-Docs/dev_guide/dev/dev_guide_localization.html>`_ entry in the Dev Guide.


Contributors
============

.. card::
   :class-header: header-2

   Contributors
   ^^^^^^^^^^^^

   Thanks to the following contributors for making this guide possible:

   Moni, Meerkat, Bob Murphy, Giddi, DeathTouchWilly, Targetingsnake

   `Moni <https://www.youtube.com/@daman2911/videos>`_ also has some video tutorials on his youtube channel.
