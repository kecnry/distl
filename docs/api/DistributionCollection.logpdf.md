### [DistributionCollection](DistributionCollection.md).logpdf (function)


```py

def logpdf(self, values=None, unpacked=False)

```



Arguments
------------
* `values` (list, tuple, array or None, optional, default=None): list of
    values in same length and order as [DistributionCollection.distributions](DistributionCollection.distributions.md) or
    [DistributionCollection.distributions_unpacked](DistributionCollection.distributions_unpacked.md) (see `unpacked`).
    If not provided or None, the latest values from [DistributionCollection.sample](DistributionCollection.sample.md)
    will be assumed (respecting the value of `unpacked`).  If no cached
    samples are available, a ValueError will be raised.
* `unpacked` (bool, optional, default=False): whether `values` corresponds
    to the passed distributions ([DistributionCollection.distributions](DistributionCollection.distributions.md))
    or the underlying unpacked distributions ([DistributionCollection.distributions_unpacked](DistributionCollection.distributions_unpacked.md)).
    If the former (`unpacked=False`), the covariances will not be propagated
    through any math or slicing.  If the latter (`unpacked=False`) covariances
    will be respected.

Returns
----------
* float or array of floats

Raises
----------
* ValueError: if `values` is None, but no cached samples are available.

