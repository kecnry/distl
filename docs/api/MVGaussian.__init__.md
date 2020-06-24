### [MVGaussian](MVGaussian.md).__init__ (function)


```py

def __init__(self, mean=0.0, cov=1.0, allow_singular=False, units=None, labels=None, labels_latex=None, wrap_ats=None)

```



A Multivariate Gaussian distribution uses [scipy.stats.multivariate_normal](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.multivariate_normal.html)
to sample values from a multivariate gaussian/normal function.

This can also be created from a function at the top-level as:

* [distl.mvgaussian](distl.mvgaussian.md)

Arguments
--------------
* `mean` (float or int, default=0.0): the central value of the
    multivariate gaussian distribution.
* `cov` (float or int, default=1.0): the covariance matrix of the multivariate
    gaussian distribution.
* `allow_singular` (bool, optional, default=False): passed directly to
    scipy (see link above).
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
* a [MVGaussian](MVGaussian.md) object

