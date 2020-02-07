### [Histogram](Histogram.md).__init__ (function)


```py

def __init__(self, bins, density, unit=None, label=None, wrap_at=None)

```



Create a [Histogram](Histogram.md) distribution from bins and density.

This can also be created from a function at the top-level as:

* [distl.histogram_from_bins](distl.histogram_from_bins.md)

See also:

* [Histogram.from_data](Histogram.from_data.md)
* [distl.histogram_from_data](distl.histogram_from_data.md)

Arguments
--------------
* `bins` (np.array object): the value of the bin-edges.  Must have one more
    entry than `density`.
* `density` (np.array object): the value of the bin-densities.  Must have one
    less entry than `bins`.
* `unit` (astropy.units object, optional): the units of the provided values.
* `label` (string, optional): a label for the distribution.  This is used
    for the x-label while plotting the distribution, as well as a shorthand
    notation when creating a [Composite](Composite.md) distribution.
* `wrap_at` (float, None, or False, optional, default=None): value to
    use for wrapping.  If None and `unit` are angles, will default to
    2*pi (or 360 degrees).  If None and `unit` are cycles, will default
    to 1.0.

Returns
--------
* a [Histogram](Histogram.md) object

