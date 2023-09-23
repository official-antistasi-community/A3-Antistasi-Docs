.. rst-class:: hidden

.. _dev_localization_guide:

=================================================
Translation-Localization of Antistasi via Tolgee
=================================================


What is Tolgee and how can I help translating Antistasi?
============================================================

.. card::
   :class-card: sd-card-2 sd-mt-3
   :class-header: header-2

   What is Tolgee and how can I help translating Antistasi?
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Tolgee is an open-source localization platform which we have decided to use as the tool-to-go for the localization of Antistasi. As it can be seen below, it provides a web-interface which can simply be used by people to translate stringtables into different languages. It provides the option to have multiple sub-projects with independent stringtables, allows to add basically an unlimited amount of people and has the option to give those people different access to the projects and sub-projects.
   Utilizing this system, we now finally have a platform we can use to have the community help with the translation of Antistasi in hopefully all languages which are supported by Arma 3 so that more people can enjoy it in their native language.


   The languages supported by Arma 3 and which we aim to cover are the following ones besides English:

   * Czech
   * French
   * German
   * Italian
   * Japanese
   * Korean
   * Polish
   * Portuguese
   * Russian
   * Simplified Chinese
   * Spanish
   * Turkish

   Due to the technical limitations of Arma 3 we unfortunately can't and won't translate to any other languages.


   If you want to translate Antistasi in one of the languages mentioned above, the way to get on board and to help is to join our `Discord Server <https://discord.com/invite/TYDwCRKnKX>`_ and to contact Bob Murphy :code:`bob_murphy` by either sending him a DM or by poking him in one of the public channels and stating that you'd like to help with the translation. He will check in with you and onboard you.


   To be able to help with the translation, all you need is to be able to properly read and write in one of those languages and to have a valid email address. The email address is only necessary for creating a user account for the Tolgee interface, nothing else.


How to work with Tolgee?
============================================================

.. card::
   :class-card: sd-card-2 sd-mt-3
   :class-header: header-2

   How to work with Tolgee?
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   As visible below, the first time you see after gaining access to your Tolgee account and after the permissions are set properly are all the different projects for the different addons/pbos within Antistasi.
   The defree of completion in this overview is the overall view of all languages for this project as well as the amount of keys within it and the available languages.

   .. figure:: /_images/tolgee-1.png
      :width: 500px
      :align: center
      :class: tolgee-image



   When you select one of those projects, you then get into the project-view where you see the completion regarding the different languages within this project.
   You also see the last changes submitted to this project and some more info on the top.
   Grey in the progress bar means not translated, yellow means translated and green means confirmed.
   The goal is to, in the most optimal case, get every key for every language translated by one person and then reviewed by another one to not have any typos or errors in translation.
   As there are currently not so many translators, it's acceptable to translate and review the keys by yourself.

   .. figure:: /_images/tolgee-2.png
      :width: 500px
      :align: center
      :class: tolgee-image




   For adding translations or for reviewing already existing ones, you click on the language you want to work on.
   One of the most useful thing in Tolgee are the shortcuts. You can literally translate and review hundreds of keys without the need to use the mouse but you can keep your hands on your keyboard the whole time.
   When in the ``Translations`` view you see the available shortcuts in the bottom right corner.
   You can:

   * switch between the strings using the arrow keys
   * select a string by pressing :kbd:`Enter`
   * abort working on a string by pressing :kbd:`Esc`
   * switch between the ``Translated`` and the ``Reviewed`` status of a key by pressing :kbd:`Ctrl+E`
   * when having the edit window open, save your edits and jump to the next edit window by pressing :kbd:`Ctrl+Enter`
   * when having the edit window open, copy in the Original/English text by pressing :kbd:`Ctrl+Ins`


   .. figure:: /_images/tolgee-3.png
      :width: 500px
      :align: center
      :class: tolgee-image



   The only time you have to use the mouse is when you have either the ability to select a translation from the Translation Memory or the Machine Translation.

   * :Translation Memory: The translation memory checks all available stringtables for (somewhat) matching translations which already exist. This can be the case when different stringtables contain the same keys like for example ones for things like "Yes", "No", "Garrisons", "Battle Options" or such.
   * :Machine Translation: Tolgee can be hooked up with different translation services via API. Nevertheless, as those cost money and we don't see that using our limited funds would add sufficient value, we don't use those.


Automation / Updates
============================================================

.. card::
   :class-card: sd-card-2 sd-mt-3
   :class-header: header-2

   Automation / Updates
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   | The exchange of information between GitHub as well as Tolgee is automated via a GitHub action which utilizes some magical scripts by Giddi which interact with Tolgee directly via the API, check for differences, sort the keys, containers etc alphabetically and submit a PR to the :code:`unstable` branch containing the appropriate changes.
   | This GitHub Action only is to be activated by Dev Team Leads and based on the :code:`unstable` branch.


Localization within the Antistasi Code
============================================================

.. card::
   :class-card: sd-card-2 sd-mt-3
   :class-header: header-2

   Localization within the Antistasi Code
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   | Localization of strings within the Antistasi code is done via the Stringtable.xml which exists within each addon/pbo of the project.
   | When setting up a new string it's important to only set the :code:`<Original>` language within the stringtable.
   | The only other time when the stringtable should be manually changed via the code is either when the key is being changed, there is a change of the English original string or the whole key gets deleted.
   | Do NOT ever touch any language entry within the xml which is not :code:`<Original>`. Every translation is only to be handled via Tolgee.

