# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import importlib.metadata
import time
from typing import List

project = "proto-frame"
auth_mail = importlib.metadata.metadata(project)["Author-email"]
author = auth_mail[: auth_mail.find("<")].rstrip()
copyright = f"{time.localtime().tm_year}, {author}"
release = importlib.metadata.version(project)

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "myst_parser",
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx_autodoc_typehints",
    "sphinxcontrib.plantuml",  # Requires a "plantuml" command on the system
    "sphinx_design",
    "sphinx_inline_tabs",
    "sphinx_copybutton",
]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}

typehints_use_rtype = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]
html_favicon = "_static/favicon.ico"
html_title = f"{project}\n{release}"
html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
]
html_theme_options = {
    "navigation_with_keys": True,
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/OldGrumpyViking/proto-frame",
            "html": "",
            "class": "fa-brands fa-github fa-2x",
        },
    ],
    "source_repository": "https://github.com/OldGrumpyViking/proto-frame",
    "source_branch": "main",
    "source_directory": "docs/",
}

autodoc_member_order = "bysource"

nitpicky = True
nitpick_ignore: List[str] = []

myst_enable_extensions = [
    "replacements",
    "colon_fence",
    "deflist",
    "linkify",
]
myst_heading_anchors = 3

copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True
