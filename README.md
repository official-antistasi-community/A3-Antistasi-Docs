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
