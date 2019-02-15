### [Histogram](Histogram.md).from_data (method)


```py

def from_data(cls, data, bins=10, range=None, weights=None, label=None, unit=None)

```



Create a [Histogram](Histogram.md) distribution from data.

This can also be created from a function at the top-level as:

* [npdists.histogram_from_data](npdists.histogram_from_data.md)

See also:

* [Histogram.__init__](Histogram.__init__.md)
* [npdists.histogram_from_bins](npdists.histogram_from_bins.md)

Arguments
--------------
* `data` (np.array object): 1D array of values.
* `unit` (astropy.units object, optional): the units of the provided values.
* `label` (string, optional): a label for the distribution.  This is used
    for the x-label while plotting the distribution, as well as a shorthand
    notation when creating a [Composite](Composite.md) distribution.

Returns
--------
* a [Histogram](Histogram.md) object

