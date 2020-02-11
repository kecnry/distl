### [BaseMultivariateDistribution](BaseMultivariateDistribution.md).sample (method)


```py

def sample(self, size=None, dimension=None)

```



Sample from the distribution.

Arguments
-----------
* `size` (int or tuple or None, optional, default=None): size/shape of the
    resulting array.
* `dimension`: (int or list of ints, optional, default=None): dimension(s)
    of the multivariate distribution to sample.  If not provided or
    None, will return all dimensions.

Returns
---------
* float or array: float if `size=None`, otherwise a numpy array with
    shape defined by `size`.

