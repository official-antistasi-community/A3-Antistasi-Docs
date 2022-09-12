.. rst-class:: hidden

.. _dev_setup_tools_guide:

==================================
Dev Tools Starter Setup
==================================

.. card::
   :class-card: sd-card-2 sd-mt-3 sd-card-important

   Please note that this part is still heavily work in progress.
   For more dev related information please go to our `Antistasi-Wiki-for-Devs <https://github.com/official-antistasi-community/A3-Antistasi/wiki/Antistasi-Wiki-for-Devs>`_.

.. card::
   :class-card: sd-card-2 sd-mt-3

   | For you to be able to properly work with Antistasi and especially SQF, we have collected tools, IDE extensions and such so you can set up your system before starting to work on anything.
   | We recommend using VS Code but lowest minimal standard you should use it Notepad++ with SQF Syntax Highlighting.
   | Setting up dev tools and extensions or add-ons can be a pain. Here is a summery of links and copy-paste solutions.
   | If you have any questions please get in contact with a member of the Dev-Team

Arma 3 Dev Extensions
============================================================

.. card::
   :class-card: sd-card-2
   :class-header: header-2

   Arma 3 Dev Extensions
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   .. rst-class:: target-substitude linkname-steam table-mission-info

   .. flat-table::
      :header-rows: 1

      *  - Name
         - Steam URL

      *  - 3den Enhanced
         - `3den Enhanced on Steam <http://steamcommunity.com/sharedfiles/filedetails/?id=623475643>`_

      *  - CBA_A3
         - `CBA_A3 on Steam <http://steamcommunity.com/sharedfiles/filedetails/?id=450814997>`_

      *  - Debug Console
         - `Debug Console on Steam <http://steamcommunity.com/sharedfiles/filedetails/?id=1231625987>`_

      *  - Enhanced Movement
         - `Enhanced Movement on Steam <http://steamcommunity.com/sharedfiles/filedetails/?id=333310405>`_

      *  - Extended Function Viewer
         - `Extended Function Viewer on Steam <http://steamcommunity.com/sharedfiles/filedetails/?id=1678581937>`_

      *  - User Input Menus
         - `User Input Menus on Steam <http://steamcommunity.com/sharedfiles/filedetails/?id=1673595418>`_

      *  - Zeus Enhanced
         - `Zeus Enhanced on Steam <http://steamcommunity.com/sharedfiles/filedetails/?id=1779063631>`_

   .. card::
      :class-card: sd-card-3 sd-mt-3 sd-card-important

      Do not use the following to join servers with Battleye enabled!

   .. rst-class:: target-substitude linkname-steam table-mission-info

   .. flat-table::
      :header-rows: 1

      *  - Name
         - Steam URL

      *  - Intercept Minimal Dev
         - `Intercept Minimal Dev on Steam <http://steamcommunity.com/sharedfiles/filedetails/?id=1645973522>`_

      *  - ArmaZeusCache
         - `ArmaZeusCache on Steam <http://steamcommunity.com/sharedfiles/filedetails/?id=1908099028>`_

      *  - Arma Debug Engine
         - `Arma Debug Engine on Steam <https://steamcommunity.com/sharedfiles/filedetails/?id=1585582292>`_ (could have issues, check out steam workshop description and comment)

      *  - Arma Script Profiler
         - `Arma Script Profiler on Steam <https://steamcommunity.com/sharedfiles/filedetails/?id=1652506957>`_ (could have issues, check out steam workshop description and comment)

Code Editor Extensions
============================================================

.. card::
   :class-card: sd-card-2
   :class-header: header-2

   Code Editor Extensions
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      Visual Studio Code
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      You can download Visual Studio Code for free on their `Website <https://code.visualstudio.com/download>`_. The following extensions are recommended.

      .. rst-class:: target-substitude table-2-b

      .. flat-table::
         :header-rows: 1

         *  - Name
            - Description

         *  - `SQF Language <https://marketplace.visualstudio.com/items?itemName=Armitxes.sqf>`_
            - Provides language for SQF extensions and highlighting.

         *  - `SQF Wiki <https://marketplace.visualstudio.com/items?itemName=EelisLynne.sqf-wiki>`_
            - Hover over command, see explanation.

         *  - `Arma 3 CfgFunctions <https://marketplace.visualstudio.com/items?itemName=HkonRRydland.a3cfgfunctions>`_
            - Lets you have Auto completion, function peeking, and header preview for mission functions

         *  - `Github Pull Requests and issues <https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github>`_
            - Review and manage your GitHub pull requests and issues directly in VS Code

         *  - `GitLens <https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens>`_
            - Supercharge the Git capabilities built into Visual Studio Code

         *  - `Live Share <https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare>`_
            - Real-time collaborative development from the comfort of your favorite tools.

         *  - `File Header Comment <https://marketplace.visualstudio.com/items?itemName=doi.fileheadercomment>`_
            - Insert File Header Comment such as date, time

         *  - `SQFLint <https://marketplace.visualstudio.com/items?itemName=skacekachna.sqflint>`_
            - Under lines some errors, quite a few false positives, so take it with a pinch of salt. Do not wait for it to finish Indexing as it will struggle since there is no description.ext in src folder.

         *  - `Arma 3 - Open Last RPT <https://marketplace.visualstudio.com/items?itemName=bux578.vscode-openlastrpt>`_
            - Ctrl+Shift+P -> Open Last -> [enter]: will open the last RPT.

         *  - `Save and Run <https://marketplace.visualstudio.com/items?itemName=wk-j.save-and-run>`_
            - Requires some config, see bellow.

      .. card::
         :class-card: sd-card-4
         :class-header: header-4-light

         Save and Run
         ^^^^^^^^^^^^^^^^^^

         .. rst-class:: code-paragraph-direct target-substitude

         Allows running a specified script or program when a keybind is pressed, or a specific filetype is saved. The extension does provide documentation, but here is an example that I use with this repository. Edit the WORKSPACE settings. It's already in .gitIgnore :code:`...\A3-Antistasi\.vscode\settings.json`. You can Download an `Example <https://gist.github.com/CalebSerafin/d91c15bfbbf913d13c56e9494abc05ab>`_

      .. card::
         :class-card: sd-card-4
         :class-header: header-4-light

         Antistasi-Dev-Deploy-Configurator
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

         .. rst-class:: target-substitude

         It is recommended using the configurator to set up map-template filter for Antistasi-Dev-Deploy.exe So that every save does not update 16+ templates. You can fin this tool and a guide `here <https://github.com/CalebSerafin/Antistasi-Dev-Deploy/wiki/Antistasi-Dev-Deploy-Configurator>`_.

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      Atom
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      .. card::
         :class-card: sd-card-4-important sd-mt-3

         Atom is no longer supported by antistasi dev team. However it is still possible to use Atom as an editor for arma. The plugins down below where recommended back then.

      .. rst-class:: target-substitude table-2-b

      .. flat-table::
         :header-rows: 1

         -  * Name
            * Description

         -  * `Arma language support in Atom <https://atom.io/packages/language-arma-atom>`_
            * Syntax highlighting, auto-completions and snippets for sqf and other languages used within the Real Virtuality engine

         -  * `atom-bracket-highlight package <https://atom.io/packages/atom-bracket-highlight>`_
            * Animates bracket highlighting

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      Notepad++
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      .. rst-class:: target-substitude table-2-b

      .. flat-table::
         :header-rows: 1

         -  * Name
            * Description

         -  * `Notepad++ SQF Syntax Highlighting and Auto Completion <https://github.com/Barrow/npp-sqf>`_
            * If you don't have an IDE and no clue how to work with one, this is basically the minimum requirement to work with it.