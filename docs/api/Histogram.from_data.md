### [Histogram](Histogram.md).from_data (method)


```py

def from_data(cls, data, bins=10, range=None, weights=None, label=None, unit=None, wrap_at=None)

```



Create a [Histogram](Histogram.md) distribution from data.  Note that under-the-hood
a linear interpolator is used between the bins for the pdf, cdf, and ppf
functions (and for sampling).

This can also be created from a function at the top-level as:

* [distl.histogram_from_data](distl.histogram_from_data.md)

See also:

* [Histogram.__init__](Histogram.__init__.md)
* [distl.histogram_from_bins](distl.histogram_from_bins.md)

Arguments
--------------
* `data` (np.array object): 1D array of values.
* `bins` (int or array, optional, default=10): number of bins or value
    of bin edges.  Passed to np.histogram.
* `range` (tuple, optional, default=None): passed to np.histogram.
* `weights` (array, optional, default=None): passed to np.histogram.
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

