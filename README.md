# Antistasi Guide

see [Tools Readme](https://github.com/Giddius/Antistasi_Guide/tree/master/tools)

To build the documentation that is in `source`, just run the `make.bat` from the commandline with:

```sh

    make html

```

## General Style-Guide

### File-names

try to make file names adhere to these rules:

- use snake_case (e.g. `this_is_snake_case`;  `this-is-not-snake-case`, `this is also not snake case`, `absolutelyNotSnakeCase`, `IdOnTkNoWwHaTtHiSeVeNiS`)
- only use lower case letters
- no spaces
- no periods (`.`) except for the file-extension of course (`something.png` is allowed, `something.other_thing.png` is not)
- no weird unicode chars or chars that are disallowed on windows (`:`, `*`, `?`, `"`, `<`,`>`,`|`,`#`,`%`,`&`,`{`,`}`,`$`,`!`,`@`,`+`,`=`)

## Repo Setup

Create a virtual environment for Python called venv and then install these libraries:

```pip install sphinx==4.5.0 sphinxcontrib-images==0.9.4 sphinxcontrib-mermaid==0.7.1 myst-parser==0.17.2 groundwork-sphinx-theme==1.1.1 sphinx-copybutton==0.5.0 sphinxcontrib-fulltoc==1.2.0 antistasi_sqf_tools sphinx-design```

then copy the ini file to the root folder of the repo folder

afterwards you can do

```antistasi-sqf-tools docs build -b html```

to build it locally, it will create it in the directory set in the config (default is created/<builder_name>, just add created to the gitignore)