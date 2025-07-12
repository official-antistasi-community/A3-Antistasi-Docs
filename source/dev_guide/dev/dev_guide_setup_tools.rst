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

   | For you to be able to properly work with Antistasi and especially SQF, we have collected tools, IDE extensions and such so you can set up your system to make your development experience easier.
   | It is highly recommended to use VSCode so you can make use of the many Arma-related extensions there, but any text editor will technically work.
   | If you have any questions, feel free to reach out on our Discord.

Arma 3 Developer Mods
============================================================

.. card::
   :class-card: sd-card-2
   :class-header: header-2

   Arma 3 Developer Mods
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   
   | These are some mods that you are recommended to use to make testing easier.
   | It is recommended to make this into a saved modlist along with your local build of the mod so you can always load the right modset.
   .. rst-class:: target-substitude linkname-steam table-mission-info

   .. flat-table::
      :header-rows: 1

      *  - Name
         - Steam URL

      *  - Advanced Developer Tools
         - `Advanced Developer Tools on Steam <https://steamcommunity.com/sharedfiles/filedetails/?id=3499977893>`_

      *  - CBA_A3
         - `CBA_A3 on Steam <http://steamcommunity.com/sharedfiles/filedetails/?id=450814997>`_

      *  - Zeus Enhanced
         - `Zeus Enhanced on Steam <http://steamcommunity.com/sharedfiles/filedetails/?id=1779063631>`_

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

      You can download Visual Studio Code for free on their `Website <https://code.visualstudio.com/download>`_. 
      The following extensions are extremely useful for editing Antistasi and are almost required.

      .. rst-class:: target-substitude table-2-b

      .. flat-table::
         :header-rows: 1

         *  - Name
            - Description

         *  - `Antistasi Development <https://marketplace.visualstudio.com/items?itemName=Giddi.antistasi-development>`_
            - Utilities specifically built for Antistasi development

         *  - `SQF Wiki <https://marketplace.visualstudio.com/items?itemName=EelisLynne.sqf-wiki>`_
            - Hover over command, see explanation

         *  - `Arma 3 - Open Last RPT <https://marketplace.visualstudio.com/items?itemName=bux578.vscode-openlastrpt>`_
            - Quickly open your last RPT to check for errors with Ctrl + Alt + R
            
         *  - `Arma SQF Language <https://marketplace.visualstudio.com/items?itemName=blackfisch.sqf-language>`_
            - Comprehensive command support for SQF

         *  - `SQF Language <https://marketplace.visualstudio.com/items?itemName=blackfisch.sqf-language>`_
            - Adds command and structure highlighting

      |

      | These next extensions can streamline smaller aspects of Antistasi development, but are not at all required.

      |

      .. rst-class:: target-substitude table-2-b

      .. flat-table::
         :header-rows: 1

         *  - Name
            - Description

         *  - `Live Share <https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare>`_
            - Can help other people debug your code if needed

         *  - `GitLens <https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens>`_
            - Extends on the existing VSCode Git support

         *  - `GitHub Pull Requests <https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github>`_
            - Allows the viewing of pull requests from within VSCode

         *  - `Partial Diff <https://marketplace.visualstudio.com/items?itemName=ryu1kn.partial-diff>`_
            - Useful to find differences between files in a pinch

         *  - `XML <https://marketplace.visualstudio.com/items?itemName=redhat.vscode-xml>`_
            - Useful for editing stringtable files


   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      Atom
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      .. card::
         :class-card: sd-card-4-important sd-mt-3

         Atom is no longer supported by Antistasi Dev team. However, it is still possible to use Atom as an editor for Arma. The plugins down below were recommended back then.

      .. rst-class:: target-substitude table-2-b

      .. flat-table::
         :header-rows: 1

         -  * Name
            * Description

         -  * `Arma language support in Atom <https://atom.io/packages/language-arma-atom>`_
            * Syntax highlighting, auto-completions and snippets for sqf and other languages used within the Real Virtuality engine

         -  * `atom-bracket-highlight package <https://atom.io/packages/atom-bracket-highlight>`_
            * Animates bracket highlighting
