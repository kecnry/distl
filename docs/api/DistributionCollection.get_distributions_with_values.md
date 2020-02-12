### [DistributionCollection](DistributionCollection.md).get_distributions_with_values (function)


```py

def get_distributions_with_values(self, values=None, as_univariates=False)

```



Expose the distributions and the values that will be applied when
calling [DistributionCollection.pdf](DistributionCollection.pdf.md), [DistributionCollection.logpdf](DistributionCollection.logpdf.md),
[DistributionCollection.cdf](DistributionCollection.cdf.md), or [DistributionCollection.logcdf](DistributionCollection.logcdf.md)

Arguments
------------
* `values` (list, tuple, array or None, optional, default=None): list of
    values in same length and order as [DistributionCollection.distributions](DistributionCollection.distributions.md) or
    [DistributionCollection.distributions_unpacked](DistributionCollection.distributions_unpacked.md) (see `as_univariates`).
    If not provided or None, the latest values from [DistributionCollection.sample](DistributionCollection.sample.md)
    will be assumed (respecting the value of `as_univariates`).  If no cached
    samples are available, a ValueError will be raised.
* `as_univariates` (bool, optional, default=False): whether `values` corresponds
    to the passed distributions ([DistributionCollection.distributions](DistributionCollection.distributions.md))
    or the underlying unpacked distributions ([DistributionCollection.distributions_unpacked](DistributionCollection.distributions_unpacked.md)).
    If the former (`as_univariates=False`), covariances will be respected
    from any underlying multivariate distributions.  If the latter
    (`as_univariates=True`) covariances will be ignored.

Returns
----------
* dictionary of distribution: value (list or float) pairs

