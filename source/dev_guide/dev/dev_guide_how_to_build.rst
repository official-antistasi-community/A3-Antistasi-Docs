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

   | Antistasi, of course, can't simply be run as a loose collection of files slapped together in a folder - it needs to be built first.
   | There are a few different ways listed here for how to do that, ordered by preference: try the first method, then the second and so on if they dont work.
   | At the end of this documentation is a guide on how to load your files as a mod into the game.
   | The guide below is only for Version 2.6.0 and onwards. If you want to build an older version, look :ref:`here <dev_how_build_mission_guide>`.

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

      First time setup
      ^^^^^^^^^^^^^^^^^^^^^^^^^^

      .. rst-class:: code-paragraph

      - The :code:`Arma 3 Tools` program needs to be installed for this. It can be found on Steam under the Tools section of your games.
      - AntistasiBuilder can be found in the main installation folder, where the :code:`A3A` and :code:`Tools` folders are located.
      - To set the program up the first time, run the executable once. This will generate a config file called :code:`AntistasiBuilder.cfg` in the same folder.
      - Open that config file and add the path to the Arma 3 Tools directory under :code:`-a3ToolsDir="PATH"`.
        | For example: :code:`-a3ToolsDir="H:/SteamLibrary/steamapps/common/Arma 3 Tools"`
        | Make sure that the path is in quotes.
      - Save the config file and close it.

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      Building the mod
      ^^^^^^^^^^^^^^^^^^^^^^^^^^

      To build the mod, run the AntistasiBuilder.exe file. It should generate the build files to the :code:`/build/A3A` folder.
   .. card::
      :class-card: sd-card-2 sd-mt-3 sd-card-important

      :code:`AntistasiBuilder.exe` has a bug in which file paths with spaces in them will break the program.
      If this happens, you will see an error relating to an invalid number of parameters. Try moving your Antistasi folder to a path without spaces. 
      If your username has spaces and you can't move it higher, you can try one of the following methods.

With PowerShell
================================

.. card::
   :class-card: sd-card-2 sd-mt-3
   :class-header: header-2

   With PowerShell
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-paragraph

   - Navigate to your main Antistasi folder, then :code:`/Tools/Builder`
   - Right click on the :code:`buildAddons.ps1` and select "Run with Powershell"
   - This will build the mod and put it in the same :code:`/build/A3A` folder
   - If this is your first time interacting with PowerShell scripts, you might need to setup the execution policy on your computer. Open a PowerShell window as an administrator and run :code:`Set-ExecutionPolicy -ExecutionPolicy Unrestricted` to allow foreign scripts to run.



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
         - add the prefix in the format :code:`x/A3A/{folder to build}`
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


Adding build files to main mod
================================

.. card::
   :class-card: sd-card-2 sd-mt-3
   :class-header: header-2

   Adding build files to main mod
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-paragraph

   - With most methods, your build files will be in :code:`/build/A3A`. The PBOs will then be in :code:`/addons`.
   - In your Arma 3 Launcher, go to the "Mods" page and click on the "Local Mod" button at the top.
   - Open the :code:`/build/A3A` folder, where you can see the :code:`addons` folder.
   - This will add a mod to your launcher, which you can then load as a mod. Do not load this mod with the normal Antistasi mod.
   - It is recommended to use this mod for testing alongside the mods in the Dev Tools Setup page.
