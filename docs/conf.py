import os
import sys

sys.path.insert(0, os.path.abspath('..'))

project = 'Quasar Docs'
copyright = '2024, Khushiyant'
author = 'Khushiyant'
release = '0.1.0'


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'tests']


html_theme = 'alabaster'
html_static_path = ['_static']
