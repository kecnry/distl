# npdists

**High-level wrappers for Probability Density Functions and Distributions using Numpy**

**IMPORTANT**: npdists is currently still under development, is not yet well-tested, and is subject to significant API changes.  Please keep posted until an official release is ready.

Read the [latest documentation on readthedocs](https://npdists.readthedocs.io) or [browse the current documentation](./api/index.md).

## Getting Started

### Dependencies

npdists requires the following dependencies:

  - python 2.7+ or 3.6+
  - numpy 1.10+


and the following optional dependencies:

  - matplotlib 2.2+ (required for plotting distributions)
  - astropy 1.0+ (required for units support)
  - dill (required for saving/loading [Function Distributions](./api/Function.md))


You can see the [Travis testing matrix](https://travis-ci.org/kecnry/npdists) for
details on what exact versions have been tested and ensured to work.  If you run
into any issues with dependencies, please [submit an issue](https://github.com/kecnry/npdists/issues/new).

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

Now from within python we can import the `npdists` package:

```py
import npdists
```

and then create, sample from, and plot our first distribution:

```py
g = npdists.gaussian(10, 1)
print(g.sample())
print(g.sample(10))
g.plot(show=True)
```

## Documentation and API Docs

Read the [latest documentation on readthedocs](https://npdists.readthedocs.io) or [browse the current documentation](./api/index.md).
