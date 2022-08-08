# proto-frame
Protocol Frame parser.

| | |
| --- | --- |
| CI/CD | [![CI - Test](https://github.com/OldGrumpyViking/proto-frame/actions/workflows/test.yml/badge.svg)](https://github.com/OldGrumpyViking/proto-frame/actions/workflows/test.yml) Coverage [![CD - Build](https://github.com/OldGrumpyViking/proto-frame/actions/workflows/build.yml/badge.svg)](https://github.com/OldGrumpyViking/proto-frame/actions/workflows/build.yml) Docs |
| Package | [![PyPI - Version](https://img.shields.io/pypi/v/proto-frame.svg?logo=pypi&label=PyPI&logoColor=gold)](https://pypi.org/project/proto-frame/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/proto-frame.svg?logo=python&label=Python&logoColor=gold)](https://pypi.org/project/proto-frame/) |
| Meta | [![code style - black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![types - Mypy](https://img.shields.io/badge/types-Mypy-blue.svg)](https://github.com/ambv/black) [![imports - isort](https://img.shields.io/badge/imports-isort-ef8336.svg)](https://github.com/pycqa/isort) [![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit) [![License - MIT](https://img.shields.io/badge/license-MIT-9400d3.svg)](https://spdx.org/licenses/) |

-----

## Installation
```shell
pip install proto-frame
```

## Development
This package only uses tools backed by [PyPa](https://www.pypa.io/en/latest/) and [PyCQA](https://meta.pycqa.org/).

### Using Pip
Pip can be used to install and develop on the package.
```shell
pip install -e .[dev]
```

See available commands in `pyproject.toml` under the `[tool.hatch.envs.default.scripts]` section.

### Using Hatch
It is recommended to use hatch for development as it helps with setting up venv's and running predefined commands.

```shell
pip install hatch
hatch run test  # for testing
hatch run mtest:test  # Run tests for all supported python versions
hatch run typing  # Verify static type annotations
hatcn run fmt  # Auto format code according to code style
hatch run lint  # Lint code
hatch run lock  # Create a locked requirements file.
```
