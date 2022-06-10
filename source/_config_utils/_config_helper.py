import os
from pathlib import Path
from functools import cache
from configparser import ConfigParser
from typing import Optional


@cache
def get_groundworks_paths() -> dict[str, Path]:
    import groundwork_sphinx_theme
    base_path = Path(groundwork_sphinx_theme.__file__).resolve().parent
    return {"static": base_path.joinpath("static"), "templates": base_path.joinpath("templates")}


@cache
def get_generate_config() -> ConfigParser:
    config = ConfigParser()
    raw_config_path = os.getenv("_DOC_CREATION_CONFIG_PATH", None)
    if raw_config_path is not None:
        config_path = Path(raw_config_path).resolve()
        config.read(config_path, encoding="utf-8")

    return config
