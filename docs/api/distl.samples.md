### [distl](distl.md).samples (function)


```py

def samples(samples, weights=None, bw_method=None, unit=None, label=None, label_latex=None, wrap_at=None)

```



Create a [Samples](Samples.md) distribution.

Arguments
--------------
* `samples` (np.array object): an array of samples.  Note that any Nans
    will be removed.
* `weights` (np.array object with length nsamples or None, optional, default=None):
    weights for each entry in `samples`.  NOTE: only supported with
    scipy 1.2+.
* `bw_method` (string, float, or None, optional, default=None): passed
    directly to scipy.stats.gaussian_kde.  Only used for methods that
    rely on the KDE.
* `unit` (astropy.units object, optional): the units of the provided values.
* `label` (string, optional): a label for the distribution.  This is used
    for the x-label while plotting the distribution if `label_latex` is not provided,
    as well as a shorthand notation when creating a [Composite](Composite.md) distribution.
* `label_latex` (string, optional): a latex label for the distribution.  This is used
    for the x-label while plotting.
* `wrap_at` (float, None, or False, optional, default=None): value to
    use for wrapping.  If None and `unit` are angles, will default to
    2*pi (or 360 degrees).  If None and `unit` are cycles, will default
    to 1.0.

Returns
--------
* a [Samples](Samples.md) object

