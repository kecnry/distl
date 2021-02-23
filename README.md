<p align="center"><a href="http://distl.readthedocs.io"><img src="./docs/images/distl.png" alt="distl logo" width="300px" align="center"/></a></p>

<p align="center" style="text-align:center"><i>simplified and condensed distributions</i></p>

<pre align="center" style="text-align:center; font-family:monospace; margin: 30px">
  pip install distl
</pre>



[![badge](https://img.shields.io/badge/github-kecnry%2Fdistl-blue.svg)](https://github.com/kecnry/distl)
[![badge](https://img.shields.io/badge/pip-distl-lightgray.svg)](https://pypi.org/project/distl/)
![badge](https://img.shields.io/badge/python-2.7+%20%7C%203.6+-blue.svg)
[![badge](https://img.shields.io/badge/license-GPL3-blue.svg)](https://github.com/kecnry/distl/blob/master/LICENSE)
[![badge](https://travis-ci.com/kecnry/distl.svg?branch=master)](https://travis-ci.com/kecnry/distl)
[![badge](https://img.shields.io/codecov/c/github/kecnry/distl)](https://codecov.io/gh/kecnry/distl)
[![badge](https://readthedocs.org/projects/distl/badge/?version=latest)](https://distl.readthedocs.io/en/latest/?badge=latest)


**IMPORTANT**: **distl** is currently still under development, is not yet well-tested, and is subject to significant API changes.  Please keep posted until an official release is ready.

Read the [latest documentation on readthedocs](https://distl.readthedocs.io) or [browse the current documentation](./docs/index.md).

**distl** provides a python object-interface on top of several distribution (random variable) functions in [scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html) and allows for:

  - serialization of distributions (so they can be saved to disk or pickled and sent to processors within MPI)
  - support for units and wrapping
  - conversion between different types of distributions
  - math between distributions, handling covariances from multivariate distributions wherever possible
  - plotting convenience functions

## Getting Started

### Dependencies

**distl** requires the following dependencies:

  - python 2.7+ or 3.6+
  - scipy 1.0+
  - numpy 1.10+


and the following optional dependencies:

  - matplotlib 2.2+ (required for plotting distributions)
  - [corner](https://corner.readthedocs.io) (required for plotting multivariate distributions and distribution collections)
  - astropy 1.0+ (required for units support)
  - dill (required for saving/loading Function distributions)


You can see the [Travis testing matrix](https://travis-ci.com/kecnry/distl) for
details on what exact versions have been tested and ensured to work.  If you run
into any issues with dependencies, please [submit an issue](https://github.com/kecnry/distl/issues/new).

### Installation

To install the latest release via pip:

```sh
pip install distl
```

To install from source locally for a single user:

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
