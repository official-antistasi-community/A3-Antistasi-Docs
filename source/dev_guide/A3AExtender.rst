.. rst-class:: hidden

.. _a3a_extender_guide:

==================================
How to Extend Antistasi?
==================================

.. card::
   :class-card: sd-card-2 sd-mt-3

   An example Code for extending the Antistasi-mod can be found on `Github <https://github.com/HakonRydland/A3AExtender>`_.

Important things to modify
==================================

.. card::
   :class-header: header-2-light

   Important things to modify
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-paragraph

   - Under addons/core/Includes you need to adapt :code:`script_mod.hpp` to have a unique :code:`PREFIX` and :code:`MODFOLDER`.
   - Under all addons **EXCEPT** core you need to update :code:`script_component.hpp` to have updateded path to match the :code:`MODFOLDER` define in :code:`script_mod.hpp`.

   .. rst-class:: code-block-2
   .. code-block:: guess

      #include "\x\${MODFOLDER}\addons\core\Includes\script_mod.hpp"

   .. rst-class:: code-paragraph

   -  | Next you need to update all :code:`$PBOPREFIX$` with the new path :code:`x\${MODFOLDER}\addons\${COMPONENT}`.
      | All ${Something} should be replaced with their corresponding elements.

   .. dropdown:: Example
      :class-title: header-3-light
      :class-container: sd-card-3

      .. rst-class:: code-paragraph

      If MODFOLDER is :code:`A3AE` you would replace all ${MODFOLDER} with A3AE.

      .. rst-class:: code-block-3
      .. code-block:: guess

         #include "\x\A3AE\addons\core\Includes\script_mod.hpp"

Example additions
==================================

.. card::
   :class-header: header-2-light

   Example additions
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. card::
      :class-header: header-3-light
      :class-card: sd-card-3

      Maps
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      .. rst-class:: code-paragraph

      | Antistasi now supports 3rd party map porting.
      | There are two examples added for working with maps. Adding a new map and overwriting/applying additions for an existing map.
      | In this examples there are also demonstrations of mission specific overwrites of :code:`mapInfo` and :code:`navGrid` data as well as global overwrite/addition.
      | You will find all the information regarding this under :code:`A3AE/addons/maps`.
      | Take care to study all the files in the addon to not miss crucial porting steps.

   .. card::
      :class-header: header-3-light
      :class-card: sd-card-3

      Templates
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      .. rst-class:: code-paragraph

      | Antistasi now supports 3rd party template additions/overwrites.
      | To add new templates or overwrite existing ones follow the demonstration given in :code:`A3AE/addons/templates/Templates/Templates.hpp`.
      | Note that while you can add addon vehicle templates to Antistasi at this time, it should be noted that it is still a limited system and you shouldn't expect full functionality from them atm.
      | Again it's important to read through all the files in the :code:`templates` addon to not miss important steps.

Building the mod
==================================

.. card::
   :class-header: header-2-light

   Building the mod
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-paragraph

   | To build the mod you first need to navigate to :code:`Tools\Builder` and edit :code:`buildAddons.ps1`.
   | On line 6 replace :code:`$addonName = "A3AE"` with :code:`$addonName = "${your addons main folder name}"`, so if you name your extension A3A-AltisRemade then the line would be :code:`$addonName = "A3A-AltisRemade"`, save the file and close it.
   | Now all you need to do is run the script and it will build the mod for you (note: it will not sign it for you, this needs to be done manually before publishing with :code:`Arma 3 Tools` -> :code:`DSUtils` & :code:`Publisher`).