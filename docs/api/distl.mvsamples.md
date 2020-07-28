### [distl](distl.md).mvsamples (function)


```py

def mvsamples(samples, weights=None, bw_method=None, units=None, labels=None, labels_latex=None, wrap_ats=None)

```



Create a [MVSamples](MVSamples.md) distribution.

Arguments
--------------
* `samples` (np.array object with shape (nsamples, [MVSamples.ndimensions](MVSamples.ndimensions.md))):
    the samples.
* `weights` (np.array object with shape (nsamples) or None, optional, default=None):
    weights for each entry in `samples`.  NOTE: only supported with scipy
    version 1.2+.
* `bw_method` (string, float, or None, optional, default=None): passed
    directly to scipy.stats.gaussian_kde.  Only used for methods that
    rely on the KDE.
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
* an [MVSamples](MVSamples.md) object

