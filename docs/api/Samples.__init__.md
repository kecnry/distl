### [Samples](Samples.md).__init__ (function)


```py

def __init__(self, samples, bins=20, unit=None, label=None, wrap_at=None)

```



Create a [Samples](Samples.md) distribution from samples.

This can also be created from a function at the top-level as:

* [distl.samples](distl.samples.md)

Arguments
--------------
* `samples` (np.array object): an array of samples.
* `bins` (int, optional, default=20): number of bins
    to use when binning into a histogram for [Samples.pdf](Samples.pdf.md), etc.
    [Samples.sample](Samples.sample.md), [Samples.mean](Samples.mean.md), [Samples.median](Samples.median.md), [Samples.var](Samples.var.md),
    [Samples.std](Samples.std.md) do not require binning and act directly on the passed
    array of `samples` ([Samples.samples](Samples.samples.md)).
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
* a [Samples](Samples.md) object

