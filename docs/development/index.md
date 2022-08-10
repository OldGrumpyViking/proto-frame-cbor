# Development

A guide on development on this project.

## Docstrings

For a reference of how to write auto parsed docstrings in the source code see [Napoleon-Extension](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#docstrings).

## Sphinx documentation

Good reference for base syntax is the [Furo library](https://pradyunsg.me/furo/reference/).

Advanced syntax can be found at th [Sphinx-Design library](https://sphinx-design.readthedocs.io/en/furo-theme/get_started.html).

Some useful syntax extensions can be enabled by the [MySt-Parser](https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#).

### PlantUML

PlantUML can be directly made in the documentation.

```{eval-rst}
.. uml::

   Alice -> Bob: Hi!
   Alice <- Bob: How are you?
```