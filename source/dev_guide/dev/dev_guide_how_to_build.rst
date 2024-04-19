.. rst-class:: hidden

.. _dev_how_build_guide:

==================================
How to build Antistasi
==================================

.. card::
   :class-card: sd-card-2 sd-mt-3 sd-card-important

   Please note that this part is still heavily work in progress.
   For more dev related information please go to our `Antistasi-Wiki-for-Devs <https://github.com/official-antistasi-community/A3-Antistasi/wiki/Antistasi-Wiki-for-Devs>`_.

.. card::
   :class-card: sd-card-2 sd-mt-3

   | Antistasi of course can't simply be run as a loose collection of files slapped together in a folder - it needs to be build first.
   | There are different ways how that can be accomplished. Be it from within VS Code, with the Arma 3 Tools or our own AntistasiBuilder.
   | The guide below is only for Version 2.6.0 and onwards. If you want to build older version look :ref:`here <dev_how_build_mission_guide>`.

Common setup
=============================

.. card::
   :class-card: sd-card-2 sd-mt-3
   :class-header: header-2

   Common setup
   ^^^^^^^^^^^^^^^^^^

   Install Arma 3 Tools in the same steam library that Arma 3 is installed.

With AntistasiBuilder
================================

.. card::
   :class-card: sd-card-2 sd-mt-3
   :class-header: header-2

   With AntistasiBuilder
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      First time
      ^^^^^^^^^^^^^^^^^^^^^^^^^^

      .. rst-class:: code-paragraph

      - AntistasiBuilder can be found under :code:`Tools/Builder/`
      - run the program once, this will generate a config file called :code:`AntistasiBuilder.cfg`
      - open the config file and add the path to the arma 3 tools direcotry under :code:`-a3ToolsDir="PATH"`.
        For example: :code:`-a3ToolsDir="H:\SteamLibrary\steamapps\common\Arma 3 Tools"`
      - save the config file, close it.

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      Building the mod
      ^^^^^^^^^^^^^^^^^^^^^^^^^^

      To build the mod run antistasiBuilder. The mod will have been built under the build folder in the repository root.

With VS code Arma Dev Extension
===================================

.. card::
   :class-card: sd-card-2 sd-mt-3
   :class-header: header-2

   With VS code Arma Dev Extension
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-paragraph

   - Install extension from `marketplace <https://marketplace.visualstudio.com/items?itemName=ole1986.arma-dev>`_
   - configure the extension from the Antistasi workspace by opening the command pallet :code:`Ctrl`/ :code:`⌘` + :code:`Shift` + :code:`P` and running the :code:`Arma 3: configure` command
   - fill in the configuration :code:`.json` file something like this

   .. rst-class:: code-block-3
   .. code-block:: json

      {
         "title": "A3 Antistasi",
         "name": "A3A",
         "author": "Official Antistasi dev team",
         "website": "https://antistasi.de/",
         "version": "2.5.4",
         "buildPath": "build",
         "privateKey": "", //add the path to a private bikey for signing when building
         "serverDirs": [],
         "serverUse32bit": false,
         "clientDirs": [ //should list all addons the mod provides
      		"A3A/addons/config_fixes",
      		"A3A/addons/core",
      		"A3A/addons/Events",
      		"A3A/addons/Garage",
      		"A3A/addons/gear",
      		"A3A/addons/GUI",
      		"A3A/addons/jeroen_arsenal",
      		"A3A/addons/Logistics",
      		"A3A/addons/maps",
      		"A3A/addons/patcom"
           ],
         "clientMods": [
            // Example:
      		// "!Workshop/@CBA_A3",
      		// "!Workshop/@ace",
      		// "!Workshop/@User Input Menus",
      		// "!Workshop/@Extended Function Viewer",
      		// "!Workshop/@Debug Console",
      		// "!Workshop/@Zeus Enhanced",
      		// "!Workshop/@Zeus Enhanced - ACE3 Compatibility",
      		// "!Workshop/@Enhanced Movement",
      		// "!Workshop/@DUI - Squad Radar"
         ],
         "ftpConnection": {},
         "steamPath": "H:\\SteamLibrary" //arma 3 install steam library, arma 3 tools should be in the same folder
      }

   .. rst-class:: code-paragraph

   - Run the command :code:`Extensions: Open Extension Folder` and navigate to :code:`ole1986.arma-dev-0.0.20 -> out -> helpers -> runArma.js -> ln 54` and add :code:`-debug` to the list

   .. rst-class:: code-block-3
   .. code-block:: js

      let args = [
             '2', '1', '0', '-exe', 'arma3_x64.exe',
             '-mod=' + clientMods.join(';'),
             '-nosplash',
             '-world empty',
             '-skipIntro',
             '-debug'
         ];

   .. rst-class:: code-paragraph

   - now run the :code:`Arma 3: Build` command, this will output into your build folder with packed addons (and signed if you have a key designated)
   - run the :code:`Arma 3: Toggle code live` command this will create symlinked folders in your arma directory for filepatching, allowing "live editing" of code, by editing the source files (dosnt include anything processed by the config.cpp)
   - run the :code:`Arma 3: Run client` or :code:`Arma 3: Run client (with logging)` command arma should start with everything ready for you, (the logging alternate will open the rpt thats created on arma launch)

With Arma 3 Tools
===================================

.. card::
   :class-card: sd-card-2 sd-mt-3
   :class-header: header-2

   With Arma 3 Tools
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      Packing
      ^^^^^^^^

      .. rst-class:: code-paragraph

      - open :code:`Addon Builder` from :code:`Arma 3 Tools`
      - click options
         - add to :code:`List of files to copy directly` this line :code:`*.p3d;*.paa;*.hpp;*.sqf`
         - click the tree dots next to :code:`Path to project folder` and navigate to the repository's A3A folder
         - add the prefix in the format :code:`x\A3A\{folder to build}`
         - optionally add a path to a :code:`.biprivatekey` for signing, this allows you to leave key verification on for dedicated server testing
      - back in the main window, add a source directory, this will be in turn each addon folder in :code:`repository -> A3A -> addons -> {folder to build}`
      - add a destination folder, this would be for example: :code:`repository -> build -> @A3A -> addons`
      - ensure for testing that it dosnt binarize the files
      - now to simply press build and repeat for each folder in the :code:`A3A -> addons`

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      Running
      ^^^^^^^^

      .. rst-class:: code-paragraph

      - copy the folder in your build directory to your arma 3 directory (or symbolic link it, recommended)
      - in the arma 3 launcher, under the :code:`Mods` tab, click :code:`... More` -> :code:`Add watched folder...` -> :code:`Add 'Arma 3' folder`. This will automatically add local mods in your arma directory to your mods list for easy loading.

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      Live editing
      ^^^^^^^^^^^^^^

      .. rst-class:: code-paragraph

      - For live editing you need to create this folder structure in your arma 3 directory :code:`x\A3A\addons`, and the create symbolic links from each folder in your repositorys :code:`A3A\addons` folder to the one in your arma directory.
      - Next you need to go in your ArmA 3 launchers :code:`Parameters` tab and under :code:`All Parameters` section :code:`Advanced` tick of the parameter :code:`Enable File-Pathcing`, then under the section :code:`Author` tick of the parameter :code:`Debug Mode`. I recommend favoriting these two for ease of use later on.
      - Now when you start with the build loaded under the :code:`Mods` tab, it will start in Dev mode and allow for recompilation of functions on the go either by reloading the missing or by calling the function :code:`A3A_fnc_prepFunctions`.
