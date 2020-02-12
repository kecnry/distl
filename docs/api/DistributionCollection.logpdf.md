### [DistributionCollection](DistributionCollection.md).logpdf (function)


```py

def logpdf(self, values=None, as_univariates=False)

```



Compute the logpdf of drawing `values` from the stored distributions.

See also:

* [DistributionCollection.pdf](DistributionCollection.pdf.md)
* [DistributionCollection.cdf](DistributionCollection.cdf.md)
* [DistributionCollection.logcdf](DistributionCollection.logcdf.md)
* [DistributionCollection.get_distributions_with_values](DistributionCollection.get_distributions_with_values.md)

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
* float or array of floats

Raises
----------
* ValueError: if `values` is None, but no cached samples are available.

