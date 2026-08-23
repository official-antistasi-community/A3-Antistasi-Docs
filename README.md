# Tools

## Python

### Requirements

- at least Python `3.9` has to be installed. Preferably Python `3.10`
  - installer for Python 3.10 [Windows 64bit](https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe)
  - other installers at [python.org](https://www.python.org/downloads/)

- ⚠️**Python has to be on your `Path`, this can be set in the installer via checkbox**⚠️

### Workspace Setup (*Venv*)

- run `setup_python_venv.ps1` inside this Folder (`tools/setup_python_venv.ps1`)
  - this will create a Python-Venv with the name `.venv` inside the root folder
  - it will also install all `dependencies` and `dev-dependencies` (formatter, linter,...) into this virtual-environment(`Venv`)

----

### Building locally

#### Via Vscode-tasks

- a task named `Generate LOCAL HTML` is already definded via vscode-workspace-tasks (`.vscode/tasks.json`)

  > This will take the `source` folder as input and build the docs as `HTML` inside the folder `created/html`

#### Via Command-Line

- make sure that the venv is activated

- use the command `antistasi-sqf-tools docs build -b html`

  >   This will take the `source` folder as input and build the docs as `HTML` inside the folder `created/html`

----

----

## Extensions Usage

[see extensions_readme.md](/tools/extensions_readme.md)

----

----

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
