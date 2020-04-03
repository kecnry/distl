### [MVSamples](MVSamples.md).__init__ (function)


```py

def __init__(self, samples, bins=20, units=None, labels=None, wrap_ats=None)

```



Create an [MVSamples](MVSamples.md) distribution from samples (eg. chains from MCMC).

See also:

* [distl.mvsamples](distl.mvsamples.md)

Arguments
--------------
* `samples` (np.array object with shape (nsamples, [MVSamples.ndimensions](MVSamples.ndimensions.md))):
    the samples.
* `bins` (int, optional, default=20): number of bins to use when binning
    into a histogram.
* `units` (list of astropy.units objects, optional): the units of the provided values.
* `labels` (list of strings, optional): labels for each dimension in the
    distribution.  This is used
    for the x-labels while plotting the distribution, as well as a shorthand
    notation when creating a [Composite](Composite.md) distribution.
* `wrap_ats` (list of floats, None, or False, optional, default=None): values to
    use for wrapping.  If None and `unit` are angles, will default to
    2*pi (or 360 degrees).  If None and `unit` are cycles, will default
    to 1.0.

Returns
--------
* an [MVSamples](MVSamples.md) object

