### [MVHistogram](MVHistogram.md).__init__ (function)


```py

def __init__(self, bins, density, units=None, labels=None, labels_latex=None, wrap_ats=None, uniqueid=None)

```



Create an [MVHistogram](MVHistogram.md) distribution from bins and density.

See also:

* [MVHistogram.from_data](MVHistogram.from_data.md)
* [distl.mvhistogram_from_data](distl.mvhistogram_from_data.md)

Arguments
--------------
* `bins` (np.array object): the value of the bin-edges (n-dimensional).
* `density` (np.array object): the value of the bin-densities (n-dimensional).
* `units` (list of astropy.units objects, optional): the units of the provided values.
* `labels` (list of strings, optional): labels for each dimension in the
    distribution.  This is used
    for the x-labels while plotting the distribution when `labels_latex`
    is not provided, as well as a shorthand
    notation when creating a [Composite](Composite.md) distribution.
* `labels_latex` (list of strings, optional):  latex labels for each
    dimension in the distribution.  This is used for plotting the distribution.
* `wrap_ats` (list of floats, None, or False, optional, default=None): values to
    use for wrapping.  If None and `unit` are angles, will default to
    2*pi (or 360 degrees).  If None and `unit` are cycles, will default
    to 1.0.

Returns
--------
* an [MVHistogram](MVHistogram.md) object

