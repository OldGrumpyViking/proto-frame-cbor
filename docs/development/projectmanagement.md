# Project Management

Vanilla usage of [`pip`](https://pip.pypa.io/en/stable/) and [`venv`](https://docs.python.org/3/library/venv.html) is supported but using [`hatch`](https://hatch.pypa.io/latest/) is recommended as it automates a lot of mundaine tasks.

As the usage of [`hatch`](https://hatch.pypa.io/latest/) is a new tool for most developers and the vanilla ways are well known, this documentation will focus on explaining how to manage the project using Hatch.

## Vanilla
The project can be installed using pip and can also be installed en ["editable"](https://pip.pypa.io/en/stable/topics/local-project-installs/#editable-installs) mode for development on the project.

It is recommended to use [`venv`](https://docs.python.org/3/library/venv.html) to setup a virtual environment for you project to isolate its environment from other projects.

Here is an example workflow:

:::{tab} Windows
```powershell
$ python -m venv .venv  # Creates a virtual environment in the .venv dir in the current folder.
$ .\.venv\bin\Activate.ps1  # Activates the virtual environment
$ pip install -e .[dev]  # Installs the project in editable mode with all its dependencies.
```
:::
:::{tab} Linux
```bash
$ python -m venv .venv  # Creates a virtual environment in the .venv dir in the current folder.
$ source .venv/bin/activate  # Activates the virtual environment
$ pip install -e .[dev]  # Installs the project in editable mode with all its dependencies.
```
:::
:::{tab} Conda
```bash
$ conda create -n proj_venv -c conda-forge --no-channel-priority -y python=3.10  # Create a virtual env with python3.10
$ conda activate proj_venv  # Activates the virtual environment
$ pip install -e .[dev]  # Installs the project in editable mode with all its dependencies.
```
:::

## Hatch
Hatch is used for pacakage management as it is highly flexible and extendable and conforms to [PyPA](https://www.pypa.io/en/latest/). Hatch mainly helps controlling the virtual environments and making shortcuts to common commands. Hatch is also used in the CI/CD pipeline to build and release a python package.

To use hatch it must be installed in your "default" python installation. To utilize container and conda environment backends two plugins are needed aswell.
```console
$ pip install hatch hatch-conda hatch-containers
```

### Virtual Environments

Hatch will run all commans inside a virtual environment with the python version the project calls for and the projects dependencies.
```console
$ hatch run <command>  # Run any command inside the projects default virtual environment.
```

## Managing different python versions

To be able to easily switch between python versions it is recommended to use either `pyenv` or `Conda/Mamba`. Note that `pyenv` can also create `Conda/Mamba` environments so it is the stronger option for advanced users.

Installing the different python versions manually and setting up the `Path` environment variable and executables to be named accordin to their version is also possible.

### Pyenv
Pyenv is available for windows and linux and supports the defined use cases.

Installation guide can be found at:

:::{tab} Windows
https://github.com/pyenv-win/pyenv-win#power-shell
:::
:::{tab} Linux
https://github.com/pyenv/pyenv-installer#pyenv-installer
:::

#### Usage

To install a new python version:
```console
$ pyenv install 3.10.6
```

To use multiple python versions simultaniously:
```console
$ pyenv global 3.10.6 3.9.13 3.8.13
$ python -V
Python 3.10.6
$ python3.9 -V
Python 3.9.13
$ python3.8 -V
Python 3.8.13
```

When all the different python versions are available in `PATH` simply using `hatch run` will create the correct virtual python environment to run your project in using the python `venv` backend.

### Conda

It is recommended to install [Mamba](https://github.com/mamba-org/mamba) which is a faster dropin for [Conda])(https://docs.conda.io/en/latest/) with exacly the same syntax. It is also prefered to install the `mini` versions to avoid bloating the system.

The environment needs to be specified to be a conda environment using the `type = "conda"` setting in the `[tool.hatch.envs.<envname>]` section.
If using mamba also add the `command = "mamba"` to the section.

Then Hatch will automatically create a conda environment with the correct python version and run your project inside that environment whenever using `hatch run`.

A conda environment is defined in this project so using `hatch run cnda:<command>` will execute any command in a conda virtual environment fitting the project.

### Containers

Hatch supports using containers for virtual environments using the `hatch-containers` plugin.

The environment needs to be specified to be a container environment using the `type = "container"` setting in the `[tool.hatch.envs.<envname>]` section.

A container environment is defined in this project so using `hatch run cont:<command>` will execute any command in a container virtual environment fitting the project.

## Developing on multiple projects

When developing on e.g. library and application simultaniously it can be useful to have them both open in "editable" mode so local changes in both projects are present in the running environment.

Insert your project as a local dependency into the `codev` environment:

```toml
[tool.hatch.envs.codev]
pre-install-commands = [  # Changes to this line requires re-creation of the environment "hatch env remove codev".
  "pip install -e ../<dir-with-other-project>"  # Used for developing on two projects in editable mode simultaniously
]
```

Then using the environment in hatch commands can be executed in this environment using:
```console
$ hatch run codev:<command>
```

## Testing with multiple python versions

To run e.g. tests with all supported python versions the `mrun` environment is defined.
If not all python versions are available in `PATH` you need to enable either the conda or containers plugin features:

```toml
[tool.hatch.envs.mrun]  # Used to run a command in multiple python environments
# type = "container"  # Needs the "hatch-containers" plugin
# type = "conda"  # Needs the "hatch-conda" plugin

[[tool.hatch.envs.mrun.matrix]]
python = ["38", "39", "310"]
```

This can be used with:
```console
$ hatch run mrun:test
```
