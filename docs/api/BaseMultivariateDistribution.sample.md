### [BaseMultivariateDistribution](BaseMultivariateDistribution.md).sample (function)


```py

def sample(self, size=None, dimension=None, seed=None, cache_sample=True)

```



Sample from the distribution.

Arguments
-----------
* `size` (int or tuple or None, optional, default=None): size/shape of the
    resulting array.
* `dimension`: (int or list of ints, optional, default=None): dimension(s)
    of the multivariate distribution to sample.  If not provided or
    None, will return all dimensions.
* `seed` (int, optional): seed to pass to np.random.seed
    prior to sampling.
* `cache_sample` (bool, optional, default=True): whether to override the
    existing [BaseMultivariateDistribution.cached_sample](BaseMultivariateDistribution.cached_sample.md).

Returns
---------
* float or array: float if `size=None`, otherwise a numpy array with
    shape defined by `size`.

