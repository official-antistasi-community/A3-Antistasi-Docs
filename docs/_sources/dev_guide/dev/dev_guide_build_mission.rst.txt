.. rst-class:: hidden

.. _dev_how_build_mission_guide:

==================================
How to build Antistasi (Mission)
==================================

.. card::
   :class-card: sd-card-2 sd-mt-3 sd-card-important

   Be aware that this guide only is for Antistasi Version 2.5.x and earlier.

Build with Antistasi Dev Deploy
===================================

.. card::
   :class-card: sd-card-2 sd-mt-3
   :class-header: header-2

   Build with Antistasi Dev Deploy
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   The Antistasi Dev Deploy Configurator binaries can be found at `Github-Repository <https://github.com/CalebSerafin/Arma-3-Dev-Deploy/releases/tag/v4>`_.
   You can find a guide on getting started in the wiki `here <https://github.com/CalebSerafin/Arma-3-Dev-Deploy/wiki/Antistasi-Dev-Deploy>`_.
   Further you can find an information about Configurator over `there <https://github.com/CalebSerafin/Arma-3-Dev-Deploy/wiki/Antistasi-Dev-Deploy-Configurator>`_.

Build with Powershell
===================================

.. card::
   :class-card: sd-card-2 sd-mt-3
   :class-header: header-2

   Build with Powershell
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-paragraph

   1. Download ZIP file from GitHub
   2. Extract ZIP
   3. Right click on :code:`PrepareMissionsForPacking.ps` and select 'Open with PowerShell'
   4. The script will create a new folder called :code:`PreparedMissions/`
   5. Inside this folder you will find multiple subfolders, labeled :code:`Antistasi-VersionNumber.MapName`
   6. Use a PBO Packager to pack the any of these mission folders