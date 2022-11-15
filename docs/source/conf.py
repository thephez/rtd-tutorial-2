# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Dash Core'
copyright = '2022, DCG'
author = ''

release = '18.1'
version = '18.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
    'hoverxref.extension',
    # 'sphinx_immaterial',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

hoverxref_roles = [
    'numref',
    'confval',
    'setting',
    'term',
]

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
# html_theme = 'sphinx_immaterial'

# -- Options for EPUB output
epub_show_urls = 'footnote'
