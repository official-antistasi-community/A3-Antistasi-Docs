.. rst-class:: hidden

.. _dev_functions_folder_lib:

==================================================
Addon Functions & Folders Library
==================================================

General information
========================

.. card::
   :class-card: sd-card-2
   :class-header: header-2-light

   General information
   ^^^^^^^^^^^^^^^^^^^^^^^^

   This function library should help the official development team and anyone who changes Antistasi to his personal mission. It will be filled slowly by the official dev team. If you want to contribute to this wiki, contact us on discord.

   .. card::
      :class-header: header-3
      :class-card: sd-card-3

      Read this library
      ^^^^^^^^^^^^^^^^^^^

      The library will be structured like the original code is. So if you have any file in the code, you can easily find it by navigating the folder structure.

Addons
========================

.. card::
   :class-card: sd-card-2
   :class-header: header-2-light

   Addons
   ^^^^^^^^^^^^^^^^^^^^^^^^

   Addons are a isolated module that could work with Antistasi but might not.

   Top level view of Addons structure

   - `core <https://github.com/official-antistasi-community/A3-Antistasi/tree/master/A3A/addons/core>`_ Core functionality of Antisasti
   - `Events <https://github.com/official-antistasi-community/A3-Antistasi/tree/master/A3A/addons/Events>`_ Antistasi's Event system
   - `Garage <https://github.com/official-antistasi-community/A3-Antistasi/tree/master/A3A/addons/Garage>`_ Antistasi's New Garage system
   - `GUI <https://github.com/official-antistasi-community/A3-Antistasi/tree/master/A3A/addons/JeroenArsenal>`_ Antistasi's New GUIs
   - `JeroenArsenal <https://github.com/official-antistasi-community/A3-Antistasi/tree/master/A3A/addons/JeroenArsenal>`_ Antistasi's Limited Arsenal
   - `Logistics <https://github.com/official-antistasi-community/A3-Antistasi/tree/master/A3A/addons/Logistics>`_ Antistasi's nodes base logtistic system for vehicles
   - `maps <https://github.com/official-antistasi-community/A3-Antistasi/tree/master/A3A/addons/maps>`_ Location for Antistasi's missions for specific terrain

Init
========================

.. card::
   :class-card: sd-card-2
   :class-header: header-2-light

   Init
   ^^^^^^^^^^^^^^^^^^^^^^^^

   Server Init called once on mission start

   - `A3A_fnc_initServer <https://github.com/official-antistasi-community/A3-Antistasi/blob/master/A3A/addons/core/functions/init/fn_initServer.sqf>`_

   Client Init called once on mission start and JIP

   - `A3A_fnc_initClient <https://github.com/official-antistasi-community/A3-Antistasi/blob/master/A3A/addons/core/functions/init/fn_initClient.sqf>`