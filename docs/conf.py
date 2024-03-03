import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

project = 'Quasar'
copyright = '2024, Khushiyant'
author = 'Khushiyant'
release = '0.1.0'

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.napoleon', 'sphinx.ext.viewcode']

templates_path = ['_templates']
exclude_patterns = ["tests"]


html_theme = 'alabaster'
html_static_path = ['_static']
