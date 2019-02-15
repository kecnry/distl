### [npdists](npdists.md).histogram_from_data (function)


```py

def histogram_from_data(data, bins=10, range=None, weights=None, unit=None, label=None)

```



Create a [Histogram](Histogram.md) distribution from data.

See also:

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

