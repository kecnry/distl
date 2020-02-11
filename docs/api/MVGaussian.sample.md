### [MVGaussian](MVGaussian.md).sample (function)


```py

def sample(self, size=None, dimension=None, cache_sample=True)

```



Sample from the distribution.

Arguments
-----------
* `size` (int or tuple or None, optional, default=None): size/shape of the
    resulting array.
* `dimension`: (int or list of ints, optional, default=None): dimension(s)
    of the multivariate distribution to sample.  If not provided or
    None, will return all dimensions.
* `cache_sample` (bool, optional, default=True): whether to override the
    existing [MVGaussian.cached_sample](MVGaussian.cached_sample.md).

Returns
---------
* float or array: float if `size=None`, otherwise a numpy array with
    shape defined by `size`.

