# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import importlib.metadata
import os
import sys

sys.path.insert(0, os.path.abspath("../../../llambda"))  # lets sphinx find llambda code

project = "LLaMBDA"
copyright = "2024, Dylan Bouchard"
author = "Dylan Bouchard"
version = importlib.metadata.version("llambda")
release = ".".join(version.rsplit(".")[:-1])

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinxcontrib.bibtex",
]

bibtex_bibfiles = ["refs.bib"]

autodoc_mock_imports = ["sentence_transformers", "transformers"]

autosummary_generate = True

templates_path = ["_templates"]

html_static_path = ["_static"]

exclude_patterns = []

html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "github_url": "https://github.com/cvs-health/llambda",
    "navbar_align": "left",
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "logo": {
        "image_light": "_static/images/llambda-logo.png",
        "image_dark": "_static/images/llambda-logo2.png",
    },
}

html_favicon = "_static/images/llambda-logo-only.png"