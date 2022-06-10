

class ThemeSpecificSettingTemplate:
    theme_name: str = None

    default_html_theme_options = {}
    default_html_sidebars = {'**': ['globaltoc.html',
                                    'searchbox.html']}

    default_pygments_style = "one-dark"

    def __init__(self, global_data: dict[str, object]) -> None:
        self.global_data = global_data.copy()
        self.default_html_context = {"extras_links": ["/extras/glossary", "/extras/links"],
                                     "steam_url": "https://steamcommunity.com/sharedfiles/filedetails/?id=2729074499",
                                     "code_block_color": None,
                                     "use_extra_style": False,
                                     "base_css_name": self.theme_name}

    def apply_html_theme_path(self) -> None:
        if "html_theme_path" not in self.global_data:
            self.global_data["html_theme_path"] = []

    def apply_html_theme_options(self) -> None:
        if "html_theme_options" not in self.global_data:
            self.global_data["html_theme_options"] = self.default_html_theme_options.copy()

    def apply_html_sidebars(self) -> None:
        if "html_sidebars" not in self.global_data:
            self.global_data["html_sidebars"] = self.default_html_sidebars.copy()

    def apply_pygments_style(self) -> None:
        pass

    def apply_html_context(self) -> None:
        if "html_context" not in self.global_data:
            self.global_data["html_context"] = self.default_html_context.copy()

    def apply_other_options(self) -> None:
        pass

    def apply(self) -> dict[str, object]:
        self.apply_html_theme_path()
        self.apply_html_theme_options()
        self.apply_html_sidebars()
        self.apply_pygments_style()
        self.apply_html_context()
        self.apply_other_options()
        return self.global_data


class GroundworkSpecificOptions(ThemeSpecificSettingTemplate):
    theme_name: str = "groundwork"

    def __init__(self, global_data: dict[str, object]) -> None:
        super().__init__(global_data)
        self.antistasi_organization_name = self.global_data["antistasi_organization_name"]
        self.antistasi_repo_name = self.global_data["antistasi_repo_name"]

    def apply_html_sidebars(self) -> None:
        super().apply_html_sidebars()
        self.global_data["html_sidebars"]["**"] += ['contribute.html']

    def apply_html_theme_options(self) -> None:
        super().apply_html_theme_options()
        self.global_data["html_theme_options"] |= {
            "contribute": True,
            "github_user": self.antistasi_organization_name,
            "github_fork": f"{self.antistasi_organization_name}/{self.antistasi_repo_name}",
            "globaltoc_includehidden": True,
            "stickysidebarscrollable": False,
            "stickysidebar": False
        }

    def apply_pygments_style(self) -> None:
        super().apply_pygments_style()
        self.global_data["pygments_style"] = "one-dark"

    def apply_html_context(self) -> None:
        super().apply_html_context()
        self.global_data["html_context"] |= {"use_extra_style": True, "code_block_color": "rgb(79, 76, 103)"}


class ClassicSpecificOptions(ThemeSpecificSettingTemplate):
    theme_name: str = "classic"

    def apply_html_context(self) -> None:
        super().apply_html_context()
        self.global_data["html_context"] |= {"topic_background_color": "rgba(200, 200, 200, 0.5)",
                                             "topic_border_color": "black",
                                             "use_extra_style": True}

    def apply_html_theme_options(self) -> None:
        all_link_color = "#f1d819"

        super().apply_html_theme_options()
        self.global_data["html_theme_options"] |= {"externalrefs": True,
                                                   "bgcolor": "#444444",
                                                   "sidebarbgcolor": "#333333",
                                                   "headbgcolor": "#666666",
                                                   "textcolor": "#181b20",
                                                   "linkcolor": all_link_color,
                                                   "headtextcolor": "#ffffff",
                                                   "headlinkcolor": all_link_color,
                                                   "relbarlinkcolor": all_link_color,
                                                   "sidebarlinkcolor": all_link_color,
                                                   "visitedlinkcolor": all_link_color,
                                                   "relbarbgcolor": "#222222",
                                                   "footerbgcolor": "#222222",
                                                   "codebgcolor": "#111111"}


class BootstrapSpecificOptions(ThemeSpecificSettingTemplate):
    theme_name: str = "bootstrap"

    # def apply_html_theme_path(self) -> None:
    #     super().apply_html_theme_path()
    #     import sphinx_bootstrap_theme
    #     print(sphinx_bootstrap_theme.get_html_theme_path())
    #     self.global_data["html_theme_path"] += sphinx_bootstrap_theme.get_html_theme_path()

    def apply_html_theme_options(self) -> None:
        super().apply_html_theme_options()
        self.global_data["html_theme_options"] |= {"bootswatch_theme": "cosmo"}


def _collect_all_theme_options() -> dict[str, type[ThemeSpecificSettingTemplate]]:

    def _recursive_subclasses(klass: type):
        yield klass
        for _subclass in klass.__subclasses__():
            yield from _recursive_subclasses(_subclass)

    _out = {}

    for subclass in _recursive_subclasses(ThemeSpecificSettingTemplate):
        if subclass.theme_name is not None:
            _out[subclass.theme_name.casefold()] = subclass

    return _out


THEME_SPECIFIC_OPTIONS_CLASSES = _collect_all_theme_options()


def apply_theme_specific_settings(global_data: dict[str, object]) -> dict[str, object]:
    theme_name = global_data["html_theme"]

    specific_option_class = THEME_SPECIFIC_OPTIONS_CLASSES.get(theme_name.casefold(), None)
    if specific_option_class is None:
        return global_data

    return specific_option_class(global_data=global_data).apply()
