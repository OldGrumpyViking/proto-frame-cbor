# Linters

The used linters are from the [PyCQA](https://meta.pycqa.org/).

Some of the linters are automatic and automatically change the source code while other linters look for more complicated errors that need to be fixed by the developer.

## mypy

[mypy](https://mypy.readthedocs.io/en/stable/index.html) is a static type checker for python. It checks if type annotations are valid to avoid errors or wrong type annotations. It ignores source code that is not type annoted, so starting to use mypy is easy.

## isort

[isort](https://pycqa.github.io/isort/) sorts the import statements of the source code according to the style guide. isort automatically sorts imports and does not need manual work.

## black

[black](https://black.readthedocs.io/en/stable/) is an automatic style formatter for python and formats the source code according to the style.

## bandit

[bandit](https://bandit.readthedocs.io/en/latest/) is a security checker for python code and will highlight any known common security issues in python source code.

## pyupgrade

[pyupgrade](https://github.com/asottile/pyupgrade) is an automatic formatter that will upgrade the source code to use newer python syntax according to the lowest supported python version.

## pydocstringformatter

[pydocstringformatter](https://github.com/DanielNoord/pydocstringformatter) will automatically format docstrings to follow the style guide.

## pylint

[pylint](https://pylint.pycqa.org/en/latest/) performs linting on the source code checking for many common errors using advanced inspection.
