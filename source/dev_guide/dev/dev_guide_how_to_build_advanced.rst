.. rst-class:: hidden

.. _dev_how_build_advanced_guide:

==================================
Advanced build methods
==================================

.. card::
   :class-card: sd-card-2 sd-mt-3

   | This page lists a few more advanced methods for building the mod if you're looking for true workflow optimization, or if none of the previous methods worked for you.


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


With batch scripting
===================================

.. card::
   :class-card: sd-card-2 sd-mt-3
   :class-header: header-2

   With batch scripting
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-paragraph

   - This method allows you to "somewhat" easily sign your mod with a private key if you want to run your mod on a dedicated server with signature verification.
   - To use the following batch script, copy it into a text file and rename the extension to .bat
   - Make sure to change all of the marked paths to the relevant absolute paths.
   - You can remove the portions about filepatching, private key signing, and public key signing if those parts are not needed.

   .. rst-class:: code-block-3
   .. code-block:: bat

      @echo off
      setlocal

      rem *******Edit these three to match local config*********
      set builderpath="C:\Program Files (x86)\Steam\steamapps\common\Arma 3 Tools\AddonBuilder\AddonBuilder.exe"
      set armapath="G:\SteamLibrary\steamapps\common\Arma 3"
      set keypath="C:\Projects\BISkeys\Antistasi__NAME__.biprivatekey"

      set sourcedir="%CD%\A3A\addons"
      set builddir="%CD%\build\@A3A\addons"
      set extraparams=-packonly -sign=%keypath%

      del /Q %builddir%\*.*
      for /F %%x in ('dir /A:D /B /D %sourcedir%') do (
         %builderpath% %sourcedir%\%%x %builddir% %extraparams% -prefix=x\A3A\addons\%%x
      )

      rem *******Create links to mod and file patching data*******
      rmdir %armapath%\@A3ALocal
      mklink /J %armapath%\@A3ALocal "%CD%\build\@A3A"
      rmdir %armapath%\x\A3A
      mklink /J %armapath%\x\A3A "%CD%\A3A"

      endlocal