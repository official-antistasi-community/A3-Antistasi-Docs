

# region [Boilerplate]

import os
import sys
import time

sys.path.insert(0, os.path.abspath('.'))
from _config_helper import get_groundworks_paths
from _theme_specific_settings import apply_theme_specific_settings, THEME_SPECIFIC_OPTIONS_CLASSES
# endregion [Boilerplate]

# region [Project_Info]

project = 'Antistasi Guide'
project_copyright = f'{time.strftime("%Y")!s}, Official Antistasi Community'
author = 'Official Antistasi Community'


antistasi_organization_name = "official-antistasi-community"

antistasi_repo_name = "A3-Antistasi"

html_logo = "_images/antistasi_main_logo.png"
html_favicon = "_images/antistasi_main_favicon.png"

# endregion [Project_Info]

# region [Sphinx_Settings]

extensions = ["myst_parser", 'sphinxcontrib.mermaid', 'sphinxcontrib.images', "sphinxcontrib.fulltoc", "sphinx.ext.githubpages", 'sphinx_copybutton', "sphinx_design"]


templates_path = ['_templates', str(get_groundworks_paths()["templates"])]

html_static_path = [str(get_groundworks_paths()["static"]), '_static']


html_css_files = [
    'css/extra_style.css',
]
exclude_patterns = []


# get available styles via `pygmentize -L styles`
pygments_style = "one-dark"

# endregion[Sphinx_Settings]

# region [Extension_Settings]

mermaid_params = ['--theme', 'forest', '--width', '2000', '--backgroundColor', 'transparent']

# endregion[Extension_Settings]

# region [HTML_Output_Settings]


html_theme = 'classic'

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
