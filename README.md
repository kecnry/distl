# distl

**Simple Distributions: math operations, serializing, covariances**

[![badge](https://img.shields.io/badge/github-kecnry%2Fdistl-blue.svg)](https://github.com/kecnry/distl)
[![badge](https://img.shields.io/badge/pip-unreleased-lightgray.svg)](https://pypi.org/project/distl/)
[![badge](https://img.shields.io/badge/license-GPL3-blue.svg)](https://github.com/kecnry/distl/blob/master/LICENSE)
[![badge](https://travis-ci.org/kecnry/distl.svg?branch=master)](https://travis-ci.org/kecnry/distl)
[![badge](https://readthedocs.org/projects/distl/badge/?version=latest)](https://distl.readthedocs.io/en/latest/?badge=latest)

**IMPORTANT**: **distl** is currently still under development, is not yet well-tested, and is subject to significant API changes.  Please keep posted until an official release is ready.

Read the [latest documentation on readthedocs](https://distl.readthedocs.io) or [browse the current documentation](./docs/index.md).

## Getting Started

### Dependencies

**distl** requires the following dependencies:

  - python 2.7+ or 3.6+
  - numpy 1.10+


and the following optional dependencies:

  - matplotlib 2.2+ (required for plotting distributions)
  - astropy 1.0+ (required for units support)
  - dill (required for saving/loading [Function Distributions](./api/Function.md))


You can see the [Travis testing matrix](https://travis-ci.org/kecnry/distl) for
details on what exact versions have been tested and ensured to work.  If you run
into any issues with dependencies, please [submit an issue](https://github.com/kecnry/distl/issues/new).

### Installation

To install locally for a single user:

```sh
python setup.py build
python setup.py install --user
```

Or to install globally:

```sh
python setup.py build
sudo python setup.py install
```

### Import

Now from within python we can import the `distl` package:

```py
import distl
```

and then create, sample from, and plot our first distribution:

```py
g = distl.gaussian(10, 1)
print(g.sample())
print(g.sample(10))
g.plot(show=True)
```

## Documentation and API Docs

Read the [latest documentation on readthedocs](https://distl.readthedocs.io) or [browse the current documentation](./docs/index.md).

## Contributors

[Kyle Conroy](https://github.com/kecnry)

Contributions are welcome!  Feel free to file an issue or fork and create a pull-request.
