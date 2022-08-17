# proto-frame

**CI/CD**:
[![CI - Test](https://github.com/OldGrumpyViking/proto-frame/actions/workflows/test.yml/badge.svg)](https://github.com/OldGrumpyViking/proto-frame/actions/workflows/test.yml)
[![CD - Build](https://github.com/OldGrumpyViking/proto-frame/actions/workflows/build.yml/badge.svg)](https://github.com/OldGrumpyViking/proto-frame/actions/workflows/build.yml)
[![Docs](https://readthedocs.org/projects/proto-frame/badge/?version=latest)](https://proto-frame.readthedocs.io/en/latest/?badge=latest)

**Pakcage**:
[![PyPI - Version](https://img.shields.io/pypi/v/proto-frame.svg?logo=pypi&label=PyPI&logoColor=gold)](https://pypi.org/project/proto-frame/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/proto-frame.svg?logo=python&label=Python&logoColor=gold)](https://pypi.org/project/proto-frame/)

**Quality**:
[![Coverage](https://coveralls.io/repos/github/OldGrumpyViking/proto-frame/badge.svg?branch=main)](https://coveralls.io/github/OldGrumpyViking/proto-frame?branch=main)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)
[![code style - black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![types - Mypy](https://img.shields.io/badge/types-Mypy-blue.svg)](https://github.com/ambv/black)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![imports - isort](https://img.shields.io/badge/imports-isort-ef8336.svg)](https://github.com/pycqa/isort)

**Meta**:
[![License - MIT](https://img.shields.io/badge/license-MIT-9400d3.svg)](https://spdx.org/licenses/)

-----

<!-- start overview include -->

A Protocol Frame parser framework.

<!-- end overview include -->

# Documentation

The documentation can be found at: xxxx

<!-- start quickstart include -->

# Quickstart

This package only uses tools backed by [PyPa](https://www.pypa.io/en/latest/) and [PyCQA](https://meta.pycqa.org/).

## Installation
The package can be installed with:

```console
$ pip install proto-frame
```

## Develop - Pip

Pip can be used to install and develop on the package.

```console
$ pip install -e .[dev]
```

See available commands in `pyproject.toml` under the `[tool.hatch.envs.default.scripts]` section.

## Develop - Hatch

It is recommended to use hatch for development as it helps with setting up venv's and running predefined commands.

Here are some base usage examples:
```console
$ pip install hatch
$ hatch run test  # for testing
$ hatcn run fmt  # Auto format code according to code style
$ hatch run lint  # Lint code
$ hatch run doc  # Build the documentation
$ hatch run doc-live  # Live updated http server for doc writing.
$ hatch run locked:lock  # Create a locked requirements file.
$ hatch run locked:check  # Check if lock file is valid.
$ hatch run locked:update  # Update locked deps.
```

<!-- end quickstart include -->
