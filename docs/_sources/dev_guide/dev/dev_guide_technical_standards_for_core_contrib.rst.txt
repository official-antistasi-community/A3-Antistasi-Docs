.. rst-class:: hidden

.. _dev_code_contribution:

====================================================================
Technical Standards for Core Code Contributions
====================================================================

.. card::
   :class-card: sd-card-2 sd-mt-3 sd-card-important

   Please note that this part is still heavily work in progress.
   For more dev related information please go to our `Antistasi-Wiki-for-Devs <https://github.com/official-antistasi-community/A3-Antistasi/wiki/Antistasi-Wiki-for-Devs>`_.

.. card::
   :class-card: sd-card-2 sd-mt-3

   | Contributing new file or updating old ones, please follow the Standardised Header format.
   | We are working with Localization within Antistasi so people can translate the content to their respective languages and make Antistasi more accessible. Please check out and follow Localization Standards.
   | We collected some Standardised Variable Types and put them together with small explanations Standardised Variable Types.
   | Getting started Reviewing Pull Requests.

Standardised Header
============================================================

.. card::
   :class-card: sd-card-2
   :class-header: header-2-light

   Standardised Header
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. rst-class:: code-block-2
   .. code-block::

      /*
      Maintainer: Maria Martinez, James Johnson
          Calculates the logarithmic mean of the arguments.
          Places a marker on the map where Petros is not standing.
          Finally, concludes whether the player will win the next lottery.

      Arguments:
          <STRING> The first argument
          <OBJECT> The second argument
          <SCALAR> Float or number in SQF.
          <INTEGER> If the number cannot have fractional values.
          <BOOL> Optional input (default: true)
          <ARRAY<STRING>> Array of a specific type (string in this case).
          <STRING,ANY> A key-pair as compound type, shorthand by omitting ARRAY.
          <CODE|STRING> Optional input with synonymous types, string compiles into code. (default: {true})
          <STRING> Optional singular String input | <ARRAY> Optional Array input (default: [""])
          <CODE<OBJECT,SCALAR,SCALAR,STRING>> Code that takes arguments of an object, a scalar, a scalar, and returns a string.

      Return Value:
          <BOOL> If the player will win the next lottery.

      Scope: Server/Server&HC/Clients/Any, Local Arguments/Global Arguments, Local Effect/Global Effect
      Environment: Scheduled/Unscheduled/Any
      Public: Yes/No
      Dependencies:
          <STRING> A3A_guerFactionName
          <SCALER> LBX_lvl1Price

      Example:
          ["something", player, 2.718281828, 4, nil, ["Tom","Dick","Harry"], ["UID123Money",0], "hint ""Hello World!"""] call A3A_fnc_standardizedHeader; // false
      */

   .. rst-class:: code-paragraph

   - Maintainer is the person/people who (mostly) knows how the current code works. People who contributed: Localisation; Refactors; Small bug; etcetera; fixes do not go here. The maintainer list is updated when the code has rewritten/overhauled by a new person/people and the previous maintainer(s) will not be able to assist in troubles concerning the current code.
   - Remove unused fields.
   - :code:`Public: Yes` means this function is not tied to a complex system but can be freely called by other code/debug console.
   - It is not necessary to specify exact :ref:`code/array structure <dev_code_contribution_standardVariables>` (just :code:`<CODE>` or :code:`<ARRAY>`). However, a specific structure makes it clear what is expected/returned.
   - It is not normal to have 10 arguments. The majority of humans can only `subitise <https://www.dictionary.com/browse/subitize>`_ ~5 items, use that as a guide.

.. _dev_code_contribution_standardVariables:

Standardised Variable Types
============================================================

.. card::
   :class-card: sd-card-2
   :class-header: header-2-light

   Standardised Variable Types
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Because SQF is a small dynamically typed scripting language, there is no default design in of structures and variable types. I have created this guideline to clear the confusion about how to express variable types for function. The following syntax design is inspired by C# Func<> delegates(Except that name/description is coming after the type).

   .. card::
      :class-card: sd-card-3
      :class-header: header-3-light

      Simple Types
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      .. rst-class:: code-block-3
      .. code-block:: guess

         <ARRAY> banList
         <BOOL> easyMode
         <CODE> crateFiller
         <CONFIG> uniformParent
         <CONTROL> vehicleBuyMenu
         <DISPLAY> currentPlayerMenu
         <GROUP> AIPatrol
         <LOCATION> village1
         <OBJECT> Petros
         <SCALAR> chanceOfSuccess
         <SCRIPT> waitForSleep
         <SIDE> invaders
         <STRING> plainMessage
         <TEXT> fancyText
         <NAMESPACE> storageLocation
         <DIARY_RECORD> howToGetStartedGuide
         <TASK> defendPetros
         <HASHMAP> vehicleEnums

         <NIL> Usually used when a function provides no meaningful return.
         <ANY> Accepts any type, including nil.
         <T> Generic Type
         <T#> Generic Type if multiple are required, substitute # with an integer.

      .. rst-class:: code-paragraph-direct

      These names are based on the return of :code:`typeName` engine command. Variable names/description go after the the . UPPERCASE capitalisation is not strictly required.

   .. card::
      :class-card: sd-card-3
      :class-header: header-3-light

      Variables in Arrays
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      .. rst-class:: code-block-3
      .. code-block::

         <ARRAY<STRING>> badList
         <ARRAY<SCALAR>> weightedSelectionValues

      .. rst-class:: code-paragraph-direct

      Arrays passed to functions are expected contain certain types. Just :code:`<ARRAY>` will not provide enough information.

   .. card::
      :class-card: sd-card-3
      :class-header: header-3-light

      Anonymous Structs
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      .. rst-class:: code-block-3
      .. code-block::

         <SCALAR,SCALAR,SCALAR> A position or vector.
         <ARRAY<SCALAR,SCALAR,SCALAR>> A list of positions or vectors

         <STRING,ANY> A key-value pair.
         <ARRAY<STRING,ANY>> A list of key-value pairs

      .. rst-class:: code-paragraph-direct

      Arrays can be used to pass around structured data. Such as a position, that has to maintain the same order and only 3 values. In this case :code:`<ARRAY<SCALAR>>` will not do.

   .. card::
      :class-card: sd-card-3
      :class-header: header-3-light

      Named Structs
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      Some structs are common enough that almost everyone working with SQF will know what they are. This can provide a great simplification. PascalCase capitalisation is not strictly required.

      .. rst-class:: code-block-3
      .. code-block::

         <Pos3> A 3D position or vector
         <Vec3> A 3D position or vector
         <Poss> A 2D position or vector, such as marker positions.
         <Vec2> A 2D position or vector, such as marker positions.

         <ARRAY<Pos3>> A list of positions or vectors

         <KeyPair> A key-value pair
         <ARRAY<KeyPair>> A list of key-value pairs

      Feel free to add common and strongly defined types here:

      .. rst-class:: code-paragraph

         - :code:`<Pos#>` A collection of scalars where # represents the number of dimensions: :code:`[4,2,0]`
         - :code:`<Vec#>` A collection of scalars where # represents the number of dimensions: :code:`[4,2,0]`
         - :code:`<KeyPair>` A key-value pair. Use in :code:`getVariable`, and :code:`hashMap getOrDefault x`: :code:`["keyName",someValueOfAnyType]`
         - :code:`<Map>` An unordered array of key-value pairs. Use in :code:`createHashMapFromArray`: :code:`[["key1",value1],["key2",value2]]`
         - :code:`<KeyPair<T>>` A key-value pair where all values are of the same defined type.
         - :code:`<Map<T>>` An unordered array of key-value pairs. Values' type are specified: :code:`[["key1",0.5],["key2",0.9]]`
         - :code:`<UnitLoadout>` https://community.bistudio.com/wiki/Unit_Loadout_Array

   .. card::
      :class-card: sd-card-3
      :class-header: header-3-light

      Code Params and Return
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      .. rst-class:: code-paragraph-direct

      Passing code around as delegates is required event handlers and actions. Specifying the parameters and return of code will be useful in it's required in SQF function. In order to shorten and simplify, :code:`<>` may be omitted if it is not an unnamed struct. The following syntax is inspired by C# Func<> delegates as C++ delegates are a mess.

      .. rst-class:: code-block-3
      .. code-block::

         _fnc_paired_selectRandom = {
             (_this apply {_x#0}) selectRandomWeighted (_this apply {_x#1});
         }

      .. rst-class:: code-paragraph-direct

      If we wanted to accept a matching param and return signature, it could be expressed as:

      .. rst-class:: code-block-3
      .. code-block::

         <CODE<ARRAY<STRING,SCALAR>,STRING> A select random weighted function.

   .. card::
      :class-card: sd-card-3
      :class-header: header-3-light

      Generic Functions
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      The above function does not care what type the values are, as they are just selected at random out an array. However, the return type is linked to the the input type. The params are first and return value last. The following is inspired by C# generics.

      .. rst-class:: code-block-3
      .. code-block::

         _fnc_map_selectRandom = {
             selectRandom _this;  // Does not care what type the values are
         }

      If we wanted to accept a matching param and return signature, it could be expressed as:

      .. rst-class:: code-block-3
      .. code-block::

         <CODE<Map<T>,KeyPair<T>> A select random weighted function that takes any value type.

      Sometimes multiple generic types may be required:

      .. rst-class:: code-block-3
      .. code-block::

         _fnc_swap = {
             param ["_var1","_var2"];
             [_var2,_var1];
         }

      If we wanted to accept a matching param and return signature, it could be expressed as:

      .. rst-class:: code-block-3
      .. code-block::

         <CODE<T1,T2,<T2,T1>> A select random weighted function that takes any value type.