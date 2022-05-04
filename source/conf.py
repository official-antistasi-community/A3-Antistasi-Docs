

# region [Boilerplate]

import os
import sys
import time

sys.path.insert(0, os.path.abspath('.'))
from _config_helper import get_groundworks_paths
# endregion [Boilerplate]

# region [Project_Info]

project = 'Antistasi Guide'
project_copyright = f'{time.strftime("%Y")!s}, Official Antistasi Community'
author = 'Official Antistasi Community'


antistasi_organization_name = "official-antistasi-community"

antistasi_repo_name = "A3-Antistasi"

html_logo = "_images/antistasi_main_image_small.png"
html_favicon = "_images/antistasi_main_image_tiny.png"

# endregion [Project_Info]

# region [Sphinx_Settings]

extensions = ["myst_parser", 'sphinxcontrib.mermaid', 'sphinxcontrib.images', "sphinxcontrib.fulltoc", "sphinx.ext.githubpages", 'sphinx_copybutton']


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


html_theme = 'groundwork'
html_theme_options = {
    "contribute": True,
    "github_user": antistasi_organization_name,
    "github_fork": f"{antistasi_organization_name}/{antistasi_repo_name}",
    "sidebar_width": "300px"
}


html_last_updated_fmt = "%Y-%m-%d %H:%M:%S"
html_permalinks_icon = ""
html_show_sourcelink = False
html_show_sphinx = False

html_sidebars = {
    '**': ['globaltoc.html',
           'sourcelink.html',
           'searchbox.html',
           'contribute.html']
}
# endregion[HTML_Output_Settings]
