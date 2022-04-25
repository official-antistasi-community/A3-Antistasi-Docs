# Tools

## Files

- __example_generate_config.ini__

    ⚙️ **__usage__**:

    ```
    copy into root folder of this repo and rename to `generate_config.ini`.
    ```

    > 💭 *generate_config.ini of the root folder is ignored by git via gitignore.*

    This ini file handles the meta-build process and is used by the wrapper around the Sphinx-library.
    <br>
- __python_setup.ps1__
    > ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️
    > 🛑 ____THIS IS ONLY NECESSARY UNTIL GIDDI HAS FINISHED THE BASIC SPHINX_WRAPPER____ 🛑
    > ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️ - ⚠️

    > *Afterwards an independent executable can be provided and used without installing python*
    >
    > So you only need to do this if you want to build the html yourself until then.

    If python 3.10 is not installed, this script downloads it and installs it.
    It also installs [pipx](https://pypa.github.io/pipx/) and afterward installs sphinx and some extensions into this isolated pipx-environment

    <br>

    🚨 **__warning__** 🚨:
    The script installs python for all users, if this is not wanted, change `InstallAllUsers=1` to `InstallAllUsers=0`

---

## Useful links

- [reStructuredText](https://docutils.sourceforge.io/rst.html)

  - [Syntax](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html)

<br>

- [Sphinx](https://www.sphinx-doc.org/en/master/)

  - Themes

    - [Built-in themes](https://www.sphinx-doc.org/en/master/usage/theming.html#builtin-themes)

    - [Third-Party theme gallery](https://sphinx-themes.org/)

  - Extensions

    - [Built-in extensions](https://www.sphinx-doc.org/en/master/usage/extensions/index.html)

    - [Third-Party extensions project](https://github.com/sphinx-contrib/)

    - [Awesome Sphinx](https://github.com/yoloseem/awesome-sphinxdoc)

  - Helper

    - [CheatSheet](https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html)
