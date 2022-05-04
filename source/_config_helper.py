from pathlib import Path
from functools import cache


@cache
def get_groundworks_paths() -> dict[str, Path]:
    import groundwork_sphinx_theme
    base_path = Path(groundwork_sphinx_theme.__file__).resolve().parent
    return {"static": base_path.joinpath("static"), "templates": base_path.joinpath("templates")}
