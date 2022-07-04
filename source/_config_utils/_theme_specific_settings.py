from antistasi_sqf_tools.doc_creating.utils.theme_options_handling import theme_specific_option, apply_theme_specific_option

groundwork_specific_options = theme_specific_option("groundwork",
                                                    html_sidebars={"**": ['contribute.html']},
                                                    pygments_style="one-dark",
                                                    html_context={"use_extra_style": True, "code_block_color": "rgb(79, 76, 103)"},
                                                    html_theme_options={
                                                        "contribute": True,
                                                        "github_user": "official-antistasi-community",
                                                        "github_fork": "official-antistasi-community/A3-Antistasi",
                                                        "globaltoc_includehidden": True,
                                                        "stickysidebarscrollable": False,
                                                        "stickysidebar": False
                                                    })
