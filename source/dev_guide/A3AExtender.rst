.. rst-class:: hidden

.. _a3a_extender_guide:

==================================
How to Extend Antistasi?
==================================

.. card::
   :class-card: sd-card-2 sd-mt-3

   An example Code for extending the Antistasi-mod can be found on `Github <https://github.com/official-antistasi-community/A3AExtender>`_.

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

Event-System
==================================

.. card::
   :class-header: header-2-light

   Mod integrated event system
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Antistasi’s functionality is extendable by 3rd party mods through the events system, where you can subscribe to events whitin antistasi like for example vehicle initilisation.

   .. rst-class:: code-paragraph-2

   A record of the events and their arguments can be found in the config under :code:`A3A >> Events` where the class name is the event name and the sub class params contains a list of the arguments in order of argument index, each element of this list contains a :code:`discription`, a list of valid :code:`types` (array, string, number, `…`) and a flag for if it is :code:`optional` (not guarented to be passed along). In addition to this class of arguments is a flag for the execution location of the event (:code:`isLocal`, 1 = local, 0 = global)

   .. dropdown:: Subscribe to an Event
      :class-container: sd-card-3
      :class-title: header-3-light

      .. rst-class:: code-paragraph

      To subscribe to an event you use the :code:`A3A_Events_fnc_addEventListener`.

      .. rst-class:: code-block-3
      .. code-block:: guess

         /**
         Description:
             Add a listener to an event, allowing you to trigger functions when that event occurs

         Arguments:
         0. <String> Event identifier, as registered in configFile >> A3A >> Events
         1. <String> Unique identifier of listener
         2. <String|Code> Code block or name of function to excecute on event occurance

         Return Value:
         <Array<Event, ID>> data needed to remove listener

         Scope: Any
         Environment: unscheduled
         Public: Yes
         Dependencies:

         Example:
         */

         ["AIVehInit", "A3A_Events_example", "someFuncName"] call A3A_Events_fnc_addEventListener;
         ["AIVehInit", "A3A_Events_example", {systemChat "Example event listener triggered!"}] call A3A_Events_fnc_addEventListener;
         ["AIVehInit", "A3A_Events_example", someFunc] call A3A_Events_fnc_addEventListener;

   .. dropdown:: Unsubscribe an Event
      :class-container: sd-card-3
      :class-title: header-3-light

      .. rst-class:: code-paragraph

      To remove an event listener use the :code:`A3A_Events_fnc_removeEventListener` function.

      .. rst-class:: code-block-3
      .. code-block:: guess

         /**
         Description:
             Removes a event listener

         Arguments:
         0. <String> Event the listener is subscribed to
         1. <String> The event listeners unique identifier

         Return Value:
         <Nil|Array> Nil if failed, deleted event listener otherwise

         Scope: Any
         Environment: unscheduled
         Public: Yes
         Dependencies:
         */

         Example: ["AIVehInit", "A3A_Events_example"] call A3A_Events_fnc_removeEventListener;

   .. dropdown:: Unsubscribe all Events
      :class-container: sd-card-3
      :class-title: header-3-light

      .. rst-class:: code-paragraph

      To remove all event listener of a type use the :code:`A3A_events_fnc_removeAllEventListeners` function.

      .. rst-class:: code-block-3
      .. code-block:: guess

         /**
         Description:
             Removes all event listeners subscribed to a particular event

         Arguments:
         0. <String> Event to remove listeners from

         Return Value: <Nil|Array> Nil if failed, the removed listeners otherwise

         Scope: Any
         Environment: unscheduled
         Public: Yes
         Dependencies:
         */

         Example: ["AIVehInit"] call A3A_Events_fnc_removeAllEventListeners;

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