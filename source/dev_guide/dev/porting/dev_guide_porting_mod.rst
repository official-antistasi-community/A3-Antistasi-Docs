.. rst-class:: hidden

.. _dev_porting_guide_mods:

==================================
Antistasi Porting Mods
==================================

Logistic System
=====================================

.. rst-class:: code-paragraph

.. card::
   :class-card: sd-card-2 sd-mt-3
   :class-header: header-2

   Logistic System
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Antistasi uses a custom logistics system that allows the loading of cargo and mounting of turrets to vehicles, this system is based on vehicle nodes and cargo data to determine if and how to load/mount cargo to vehicles

   The data for all this is contained within one of the following: :code:`ConfigFile >> A3A`, :code:`ConfigFile >> CfgVehicles >> {Vehicle class}`, or :code:`MissionConfigFile >> A3A`.

   For Data contained on the vehicle/cargo it is simply contained in the class :code:`A3A_Logistics_Nodes`/:code:`A3A_Logistics_Cargo respectivly`.

   For the rest its in the class :code:`A3A_Logistics_Cargo >> {Class name/model}`/:code:`A3A_Logistics_Nodes >> {Class name/model}` respectivly, this is regardless of its the config or mission config file.

   The prioritisation for the nodes/cargo are as follows:

   - MissionConfig
      - Class name based
      - Model based
   - CfgVehicles
   - Config
      - Class name based
      - Model based

   All Antistasi nodes are defined in the config and prefere model based where possible, this gives 3rd party extensions and vehicle makers the abbility to overwrite the default nodes/cargo data.

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      Adding a vehicle
      ^^^^^^^^^^^^^^^^^^^^^^^^^^

      .. dropdown:: The File Structure
         :class-title: header-3-light
         :class-container: sd-card-3

         **Config.cpp**
         This is a boiler plate example of the most basic config.cpp for node definitions that we recomend.

         .. rst-class:: code-block-3
         .. code-block:: guess

            #include "script_component.hpp"

            class CfgPatches {
                class ADDON {
                    name = COMPONENT_NAME;
                    units[] = {};
                    weapons[] = {};
                    requiredVersion = REQUIRED_VERSION;
                    requiredAddons[] = {};
                    author = AUTHOR;
                    authors[] = { AUTHORS };
                    authorUrl = "";
                    VERSION_CONFIG;
                };
            };

            class A3A {
                #include "CfgLogistics.hpp"
            };

         **CfgLogistics.hpp**
         This is the main file to gather all the logistics data in a orderly fasion.

         .. rst-class:: code-block-3
         .. code-block:: C++

            //add a define to cheat the macro for 3rd party development (this is only for external mods)
            #undef TRIPLES(var1,var2,var3)
            #define TRIPLES(var1,var2,var3) A3A_Logistics##_##var2##_##var3

            class A3A_Logistics_Nodes
            {
                class A3A_Logistics_Nodes_Base; //import base class
                #include "Nodes\yourModFile.hpp" //hpp file for your mods vehicle nodes
            };

            class A3A_Logistics_Cargo
            {
                class A3A_Logistics_Cargo_Base //import base class;
                #include "Cargo\yourModFile.hpp" //hpp file for your mods cargo definitions
            };

            //re-define the triples macro (this is only for external mods)
            #undef TRIPLES(var1,var2,var3)
            #define TRIPLES(var1,var2,var3) ##var1##_##var2##_##var3

         this would give you a file structure as follows:

         - Mod folder (Example: A3AE)
            - addons
               - your addon folder (Example: Logistics)
                  - Config.cpp
                  - CfgLogistics.hpp
                  - Nodes
                     - yourModFile.hpp (Example: Vanilla.hpp)
                  - Cargo
                     - yourModFile.hpp (Example: Vanilla.hpp)

      .. dropdown:: Getting the node data
         :class-title: header-3-light
         :class-container: sd-card-3

         To make a vehicle capable to load cargo, use the function "A3A_Logistics_fnc_generateHardPoints" to generate a vehicle hard point array (the nodes may be a bit rough).

         .. rst-class:: code-paragraph-2

         Example: :code:`[cursorTarget, [0,-0.7,-0.7],2.1, true] call A3A_Logistics_fnc_generateHardPoints;`

         where the parameters for the function are:

         | 0. The vehicle your defining the hard points for
         | 1. The start of the cargo plane, relative to model center
         | 2. The length of the cargo plane
         | 3. If the nodes are model based or vehicle (usefull if there many different vehicles use the same model with animations)

         .. figure:: /_images/CommandlineLogisticNodes-1.png

         .. rst-class:: code-paragraph-2

         This will give you a generated class to copy past in to your node hpp file. if you followed the file structure above that would be :code:`{your mod}/addons/{Your addon}/Nodes/{yourModFile}.hpp`

         .. figure:: /_images/CommandlineLogisticNodes-2.png

         Remember to verify the nodes by loading a cargo of both node size 1 and 2 in the vehicle afterwards (assuming it has two or more points). And to check for conflicting animations in the garage

         Finally, you need to add in the seats occupied by each node, to do this:

         #. start the game with the newly added "logistics_vehicleHardpoints" entry
         #. load the vehicle full of size 1 cargo (Example: "Box_IND_Wps_F")

         .. rst-class:: code-block-3
         .. code-block:: guess

            //spawns crate and adds load action to it
            private _object = "Box_IND_Wps_F" createVehicle getPos player;
            [_object] call A3A_logistics_fnc_addLoadAction;

         .. rst-class:: code-paragraph

         #. while looking at the vehicle run this command in debug console. :code:`vic = cursorObject;`
         #. then run this command :code:`moveOut player; player moveInCargo [vic, 0]`

         Increasing the number at the end until your put back in the first seat, and for each increase fill in the seat number into each node where you collide with the cargo (the nodes go from front to back).

         .. figure:: /_images/CommandlineLogisticNodes-3.jfif

         .. figure:: /_images/CommandlineLogisticNodes-4.jfif

         Example from vanilla logistics nodes:

         .. rst-class:: code-block-3
         .. code-block:: guess

            //Offroad node definitions before adding the blocked seats
            class A3_soft_f_Offroad_01_Offroad_01_unarmed_F : TRIPLES(ADDON,Nodes,Base)
            {
                class Nodes
                {
                    class Node1
                    {
                        offset[] = {-0.05,-1.3,-0.683};
                        seats[] = {};
                    };
                    class Node2
                    {
                        offset[] = {-0.05,-2.3,-0.683};
                        seats[] = {};
                    };
                };
            };

         .. rst-class:: code-block-3
         .. code-block:: guess

            //Offroad node definition with the blocked seats added
            class A3_soft_f_Offroad_01_Offroad_01_unarmed_F : TRIPLES(ADDON,Nodes,Base)
            {
                class Nodes
                {
                    class Node1
                    {
                        offset[] = {-0.05,-1.3,-0.683};
                        seats[] = {3,4};
                    };
                    class Node2
                    {
                        offset[] = {-0.05,-2.3,-0.683};
                        seats[] = {1,2};
                    };
                };
            };

         Here we fill in the seat number into the empty array in the nodes.

         Note: if the vehicle is covered or closed, you need to :code:`canLoadWeapon = 0;` to it's class.

         .. rst-class:: code-block-3
         .. code-block:: guess

            class A3_soft_f_Offroad_01_Offroad_01_unarmed_F : TRIPLES(ADDON,Nodes,Base)
            {
                canLoadWeapon = 0;
                class Nodes
                {

   .. card::
      :class-card: sd-card-3
      :class-header: header-3

      Adding a cargo type
      ^^^^^^^^^^^^^^^^^^^^^^^^^^

      Cargo are defined as part of the class :code:`A3A_Logistics_Cargo` as a class named after the model name or classname (note model have :code:`.` replaced with an underscore :code:`_`)

      .. dropdown:: General
         :class-title: header-3-light
         :class-container: sd-card-3

         **Node dimensions**

         A node is considered 1,2m wide and 0,8m long, height is typically not considered but most vehicles are presumed to have 2m clearance

         - W1,2m x L0,8m x H2m

         **Where to put the cargo data**

         - ConfigFile >> A3A >> A3A_Logistics_Cargo
         - MissionConfigFile >> A3A >> A3A_Logistics_Cargo
         - ConfigFile >> CfgVehicles >> Cargo class >> A3A_Logistics_Cargo
            - Note that the data stored in CfgVehicles should be directly in A3A_Logistics_Cargo and not in a subclass like the others.

      .. dropdown:: Class properties
         :class-title: header-3-light
         :class-container: sd-card-3

         **Offset**

         This is the relative offset to the bottom of the cargo you want to load. for the most part its just a bit positive on the Z-axis.

         - Example: {0,0,0.85}

         But some vehicles have there center off from cargo plane center, here you'd need to adjust the X-axis as well

         - Example: {-0.1,0,0.85}

         **Rotation**

         This is model relative rotation between the vehicle and the cargo, simple trial and error works fine here

         - Example: {1,0,0}

         **Size**

         How many vehicle hardpoints this cargo needs, usually sorted into visual size of how big it is from small (1 node), medium (2) to large (6), you can go beyond this as you see fit.

         For more precis definitions you should consider the node dimensions. This would make a cargo of W0,8 x L1 a size 2, but if its rotated it could be considered a size 1.

         - Example: 2

         **Recoil**

         This is only needed when the new cargo is a weapon (static) and defines how hard the weapon should affect the vehicle.

         - Example: 500

      .. dropdown:: Example
         :class-title: header-3-light
         :class-container: sd-card-3

         .. rst-class:: code-block-3
         .. code-block:: guess

            class A3_static_f_Mortar_01_Mortar_01_F : TRIPLES(ADDON,Cargo,Base)
            {
                offset[] = {-0.1,-0.5,0.74};
                rotation[] = {0,1,0};
                size = 2;
                recoil = 2000;
                isWeapon = 1;
                blackList[] = {"\A3\boat_f_gamma\Boat_Civil_01\Boat_Civil_01_F","\A3\boat_f\Boat_Transport_01\Boat_Transport_01_F.p3d","\A3\Boat_F_Exp\Boat_Transport_02\Boat_Transport_02_F.p3d"};
            };

      .. dropdown:: Getting the data
         :class-title: header-3-light
         :class-container: sd-card-3

         Function: A3A_Logistics_fnc_generateCargoOffset Params:

         - Vehicle: A vehicle capable of carrying the cargo (with nodes defined)
         - Cargo: The object you wish to define as a cargo
         - Adjustments
            - Offset: The offset from the node center
            - Rotation: The rotation the cargo is loaded with
            - Size: How many nodes this cargo requires
            - isWeapon: if the cargo is a static weapon
            - Recoil: The amount of recoil to apply to the vehicle when the weapon is fired
         - Model based: True to generate the data with the model to allow all objects sharing the same model to be loaded based on this definition

         Return: The generated class to be copy pasted

         **Example**
         assign the vehicle and cargo to global variables using :code:`Test_vehicle = cursorObject;` and :code:`Test_cargo = cursorObject;` respectivly.

         .. rst-class:: code-block-3
         .. code-block:: guess

            [
                Test_vehicle
                , Test_cargo
                , [
                    [0,0,0]
                    ,[0,0,0]
                    ,2
                    ,false
                    ,0
                ], true
            ] call A3A_Logistics_fnc_generateCargoOffset;

         adjust the offset rotation and size as needed.

         **Notes**

         - The blacklist has to be manually populated
         - Recoil typically should be under 1000 unless the weapon points upwards
         - Boats should not be allowed to carry mortars.
         - Helicopters should not be allowed to carry weapons