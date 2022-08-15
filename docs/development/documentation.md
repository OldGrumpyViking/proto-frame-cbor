# Documentation

The documentation is written in markdown with [Sphinx](https://www.sphinx-doc.org/en/master/) with quiet a few extensions.

See the secionts below for references and guide.

## Writing Syntax

The documents can be written in Markdown or reStructured text or a mix of the two.

The [furo](https://pradyunsg.me/furo/reference/) library has a very good page for a reference on how to make simple syntax in both markdown and reStructured text.

Advanced syntax can be found at th [Sphinx-Design library](https://sphinx-design.readthedocs.io/en/furo-theme/get_started.html).

Some useful syntax extensions can be enabled by the [MySt-Parser](https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#).

### Markdown

The markdown follows the [CommonMark](https://spec.commonmark.org/0.30/) syntax and a good cheat sheet can be found at the [MySt library](https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html#commonmark).

### reStructuredText

See [RST-Quickref](https://docutils.sourceforge.io/docs/user/rst/quickref.html) for a cheat-sheet on writin rst
files in addition to the [Sphinx-RST](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html) guide.

### Using Tabs

Tabs can be used with the [Sphinx-Inline-Tabs](https://sphinx-inline-tabs.readthedocs.io/en/latest/usage.html#rich-tab-labels) extension.

:::{tab} Tab 1
Content 1
:::

:::{tab} Tab 2
Content 2
:::

---------
Markdown to get the tabs:
```markdown
:::{tab} Tab 1
Content 1
:::

:::{tab} Tab 2
Content 2
:::
```

### PlantUML

PlantUML can be directly made in the documentation.

::::{tab} Rendered Result
```{eval-rst}
.. uml::

   Alice -> Bob: Hi!
   Alice <- Bob: How are you?
```
::::
::::{tab} Markdown
:::markdown
```{eval-rst}
.. uml::

   Alice -> Bob: Hi!
   Alice <- Bob: How are you?
```
:::
::::
::::{tab} reStructuredText
:::reStructuredText
.. uml::

   Alice -> Bob: Hi!
   Alice <- Bob: How are you?
:::
::::

## Code Documentation

For a reference of how to write auto parsed docstrings in the source code see [Napoleon-Extension](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#docstrings).

For a reference on how to include them in the documentation see the [Sphinx Autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#directives) page.
