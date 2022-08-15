# Testing

[Pytest](https://docs.pytest.org/) is used for testing. See the [official documentation](https://docs.pytest.org/en/7.1.x/how-to/index.html) for guides.

Pytest can easily run legacy test code, so the transition should be fairly straight forward if you are not using pytest today.

A few plugins are used to enhance pytest these provide the following features.

## pytest-cov

[pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) provides coverage reports of the tested project.

## pytest-sugar

[pytest-sugar](https://github.com/Teemu/pytest-sugar/) prettifies the output of pytest to be more human readable.

## pytest-xdist

[pytest-xdist](https://pytest-xdist.readthedocs.io/en/latest/) runs tests in parallel using multiprocessing.

## pytest-randomly

[pytest-randomly](https://github.com/pytest-dev/pytest-randomly) executes test in random order to ensure that there is no test ordering dependencies.
