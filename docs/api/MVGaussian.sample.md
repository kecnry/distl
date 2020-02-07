### [MVGaussian](MVGaussian.md).sample (function)


```py

def sample(self, size=None, dimension=None)

```



Sample from the distribution.

Arguments
-----------
* `size` (int or tuple or None, optional, default=None): size/shape of the
    resulting array.
* `dimension`: (int, optional): dimension of the multivariate distribution
    to sample.  If not provided or None, will default to [MVGaussian.dimension](MVGaussian.dimension.md).

Returns
---------
* float or array: float if `size=None`, otherwise a numpy array with
    shape defined by `size`.

