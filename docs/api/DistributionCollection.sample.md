### [DistributionCollection](DistributionCollection.md).sample (function)


```py

def sample(self, *args, **kwargs)

```



Sample from multiple distributions with random seeds automatically determined,
but applied to distributions of the same underlying multivariate distribution
automatically.

For each unique [BaseDistribution.hash](BaseDistribution.hash.md) in the distributions in `dists` a
random seed will be generated and applied to [BaseDistribution.sample](BaseDistribution.sample.md)
for all distributionis in `dists` which share that same hash value.  By doing
so, any [BaseMultivariateDistribution](BaseMultivariateDistribution.md) which samples from the same underlying
multivariate distribution (but for a different
[BaseMultivariateDistribution.dimension](BaseMultivariateDistribution.dimension.md)), will be correctly sampled to account
for the covariance/correlation between parameters, but all other 1-D
[BaseDistribution](BaseDistribution.md) objects will be sampled with their own independent
random seeds.

Arguments
-------------
* `*args`: all positional arguments are sent to [BaseDistribution.sample](BaseDistribution.sample.md)
    for each item in `dists`.
* `**kwargs`: all keyword arguments are sent to [BaseDistribution.sample](BaseDistribution.sample.md)
    for each item in `dists`.  Note: `seed` is forbidden and will raise
    a ValueError.

Returns
-------------
* (list): list of samples, in same order as [DistributionCollection.distributions](DistributionCollection.distributions.md).

Raises
----------
* ValueError: if `seed` is passed.

