### [DistributionCollection](DistributionCollection.md).sample_quantiles (function)


```py

def sample_quantiles(self, quantiles=(0.16, 0.84), samples=None)

```



Return the values at provided quantiles from the samples via np.percentile.

See also:
* [DistributionCollection.sample_uncertainties_formatted](DistributionCollection.sample_uncertainties_formatted.md)

Arguments
-----------
* `quantiles` (tuple, optional, default=(0.16, 0.84)): quantiles
    to expose.
* `samples` (array-type, optional, default=None): samples to use.  If
    not provided, [DistributionCollection.sample](DistributionCollection.sample.md) will be called with `size=1e6`.

Returns
------------
* (list)

