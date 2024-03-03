import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

project = 'Quasar Docs'
copyright = '2024, Khushiyant'
author = 'Khushiyant'
release = '0.1.0'


extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'autoapi.extension',
]

templates_path = ['_templates']
exclude_patterns = []


html_theme = 'alabaster'
html_static_path = ['_static']
