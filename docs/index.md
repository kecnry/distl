# npdists

**High-Level Wrappers for Probability Density Functions and Distributions using Numpy**

[![badge](https://img.shields.io/badge/github-kecnry%2Fnpdists-blue.svg)](https://github.com/kecnry/npdists)
[![badge](https://img.shields.io/badge/pip-unreleased-lightgray.svg)](https://pypi.org/project/npdists/)
[![badge](https://img.shields.io/badge/license-GPL3-blue.svg)](https://github.com/kecnry/npdists/blob/master/LICENSE)
[![badge](https://travis-ci.org/kecnry/npdists.svg?branch=master)](https://travis-ci.org/kecnry/npdists)
[![badge](https://readthedocs.org/projects/npdists/badge/?version=latest)](https://npdists.readthedocs.io/en/latest/?badge=latest)


**IMPORTANT**: **npdists** is currently still under development, is not yet well-tested, and is subject to significant API changes.  Please check back until an official release is ready.



## Getting Started

### Dependencies

**npdists** requires the following dependencies:

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

## Supported Distribution Types

Creation functions for the following distribution types are currently implemented
and available at the [top-level of npdists](./api/npdists.md):

* [delta](./api/npdists.delta.md)
* [gaussian](./api/npdists.gaussian.md)
* [normal](./api/npdists.normal.md) (shortcut to gaussian)
* [uniform](./api/npdists.uniform.md)
* [boxcar](./api/npdists.boxcar.md) (shortcut to uniform)
* [histogram_from_data](./api/npdists.histogram_from_data.md) or [histogram_from_bins](./api/npdists.histogram_from_bins.md)

## Converting Between Distribution Types

Distributions within npdists allow for converting to other distribution types.
See the [API documention](./api/) for the appropriate distribution type
and look for the `to_` methods to convert along with a description of the options
and limitations.  Below is a summary of all implemented translation methods:

* [Delta](./api/Delta.md)
    * [to_gaussian](./api/Delta.to_gaussian.md)
    * [to_histogram](./api/Delta.to_histogram.md)
    * [to_uniform](./api/Delta.to_uniform.md)
* [Gaussian](./api/Gaussian.md)
    * [to_histogram](./api/Gaussian.to_histogram.md)
    * [to_uniform](./api/Gaussian.to_uniform.md)
* [Uniform](./api/Uniform.md)
    * [to_gaussian](./api/Uniform.to_gaussian.md)
    * [to_histogram](./api/Uniform.to_histogram.md)
* [Composite](./api/Composite.md)
    * [to_gaussian](./api/Composite.to_gaussian.md) (via histogram)
    * [to_histogram](./api/Composite.to_histogram.md)
    * [to_uniform](./api/Composite.to_uniform.md) (via histogram)
* [Function](./api/Function.md)
    * [to_gaussian](./api/Function.to_gaussian.md) (via histogram)
    * [to_histogram](./api/Function.to_histogram.md)
    * [to_uniform](./api/Function.to_uniform.md) (via histogram)
* [Histogram](./api/Histogram.md)
    * [to_gaussian](./api/Histogram.to_gaussian.md)
    * [to_uniform](./api/Histogram.to_uniform.md)


## Sampling

To sample from any distribution, call the [sample](./api/BaseDistribution.sample.md) method,
optionally passing the number of desired samples.

```python
g = npdists.gaussian(10, 2)
g.sample(10)
```

    array([ 8.07893271, 12.51150027,  7.56756268,  7.29151051,  5.55049747,
            8.67495845, 11.61104165, 10.11544651, 11.96864228, 10.54677169])


See [these sampling examples](./examples/sampling.md) for more details.

To ensure consistent results (when needed), set the random seed in numpy
prior to sampling.

```python
g = npdists.gaussian(10, 2)
np.random.seed(1234)
g.sample()
np.random.seed(1234)
g.sample()
```

See [this seeding example](./examples/random_seed.md) for more details.

## Plotting

**NOTE:** matplotlib is required for plotting support.

To plot the distribution, call one of the following:

* [plot](./api/BaseDistribution.plot.md)
* [plot_dist](./api/BaseDistribution.plot_dist.md)
* [plot_sample](./api/BaseDistribution.plot_sample.md)
* [plot_gaussian](./api/BaseDistribution.plot_gaussian.md)

```py
gh = npdists.gaussian(5, 3).to_histogram()
out = gh.plot(200, show=True, plot_gaussian=True)
```

![png](./examples/plotting_files/plotting_19_0.png)

See [these plotting examples](./examples/plotting.md) for more details.


## Math with Distribution Objects

Any (supported) math operator between two Distribution objects, or between a Distribution object and a float or integer, will return another Distribution object.  In most cases, this will return a [Composite Distribution](./api/Composite.md).  In some cases where it is possible to return the same type of Distribution, that will be done instead.  For example, a [Gaussian Distribution](./api/Gaussian.md) multiplied by a float can return another [Gaussian Distribution](./api/Gaussian.md) where that float is interpreted as a [Delta Distribution](./api/Delta.md) with that value.

This means that in the following case `2 * g` is equivalent to `d * g`, but **not** `g + g`:

```py
g = npdists.gaussian(10, 2)
d = npdists.delta(2)
```

Currently supported operators include:

* multiplication, division, addition, subtraction
* np.sin, np.cos, np.tan (but not math.sin, etc)

See [these math examples](./examples/math.md) for more details.


## Support for Units

**NOTE:** astropy is required for units support.

Units can be set for a distribution by setting the [unit](./api/BaseDistribution.unit.md), by passing `unit` to the constructor, or by multiplying the distribution object by an astropy.unit object.

To change units, you can then call [to](./api/BaseDistribution.to.md) to return a new distribution in the requested units.

See [these units examples](./examples/units.md) for more details.

## Wrapping

```py
g = npdists.gaussian(10, 2, wrap_at=12)
out = g.plot(show=True)
```
![png](./examples/wrapping_files/wrapping_2_0.png)

See [these wrapping examples](./examples/wrapping.md) for more details.

## Hard Limits

**COMING SOON**

## API Documentation

See the [API documentation](./api.md) for full details on each type of available distribution.

## Contributors

[Kyle Conroy](https://github.com/kecnry)

Contributions are welcome!  Feel free to file an issue or fork and create a pull-request.
