.. rst-class:: hidden

.. _dev_how_build_guide:

==================================
How to build Antistasi
==================================

.. card::
   :class-card: sd-card-2 sd-mt-3

   | Antistasi, of course, can't simply be run as a loose collection of files slapped together in a folder - it needs to be built first.
   | There are a few different ways listed here for how to do that, ordered by preference: try the first method, then the second and so on if they dont work.
   | At the end of this documentation is a guide on how to load your files as a mod into the game.
   | The guide below is only for Version 2.6.0 and onwards. If you want to build an older version, look :ref:`here <dev_how_build_mission_guide>`.
   | If none of the methods on this page work on your computer or you want to optimize your workflow further, see the advanced build methods :ref:`here <dev_how_build_advanced_guide>`.

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
        For example: :code:`-a3ToolsDir="H:/SteamLibrary/steamapps/common/Arma 3 Tools"`
        Make sure that the path is in quotes.
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
   - It is recommended to use this mod for testing alongside the mods in the :ref:`Dev Tools Setup page <dev_setup_tools_guide>`.
