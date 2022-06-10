

# region [Boilerplate]

import os
import sys
import time
from pathlib import Path
from types import ModuleType
import importlib.util


# Needed to also be able to get the config outside of sphinx
def import_module_from_path(module_name: str, module_path: Path) -> ModuleType:
    if module_path.is_dir:
        module_path = module_path.joinpath("__init__.py")
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


sys.path.insert(0, os.path.abspath('.'))


_config_utils = import_module_from_path("_config_utils", Path(__file__).parent.absolute().joinpath("_config_utils"))
from _config_utils._file_preload import files_to_preload
from _config_utils._config_helper import get_groundworks_paths, get_generate_config
from _config_utils._theme_specific_settings import apply_theme_specific_settings, THEME_SPECIFIC_OPTIONS_CLASSES
# endregion [Boilerplate]

# region [Project_Info]

project = 'Antistasi Guide'
project_copyright = f'{time.strftime("%Y")!s}, Official Antistasi Community'
author = 'Official Antistasi Community'


antistasi_organization_name = "official-antistasi-community"

antistasi_repo_name = "A3-Antistasi"
issues_github_path = f"{antistasi_organization_name}/{antistasi_repo_name}"
html_logo = "_images/antistasi_main_logo.png"
html_favicon = "_images/antistasi_main_favicon.png"
github_username = antistasi_organization_name
github_repository = antistasi_repo_name
# endregion [Project_Info]

# region [Sphinx_Settings]

extensions = ["myst_parser",
              'sphinxcontrib.mermaid',
              'sphinxcontrib.images',
              "sphinxcontrib.fulltoc",
              "sphinx.ext.githubpages",
              'sphinx_copybutton',
              "sphinx_design",
              'sphinx.ext.autosectionlabel',
              'sphinx_issues',
              "sphinx_toolbox.shields"
              ]


templates_path = ['_templates', str(get_groundworks_paths()["templates"])]

html_static_path = [str(get_groundworks_paths()["static"]), '_static']


html_css_files = [
    'css/extra_style.css',
]
exclude_patterns = ["available_label.json", "extras/*"]


# get available styles via `pygmentize -L styles`
pygments_style = "one-dark"

# endregion[Sphinx_Settings]

# region [Extension_Settings]

mermaid_params = ['--theme', 'forest', '--width', '2000', '--backgroundColor', 'transparent']
autosectionlabel_prefix_document = True
# endregion[Extension_Settings]

# region [HTML_Output_Settings]


html_theme = 'groundwork'

html_theme_options = {}


html_last_updated_fmt = "%Y/%B/%d"
html_permalinks_icon = ""
html_show_sourcelink = False
html_show_sphinx = False

html_sidebars = {
    '**': [
        'globaltoc.html',
        'searchbox.html',
    ]
}
# endregion[HTML_Output_Settings]

global_data = globals()
global_data |= apply_theme_specific_settings(globals())
