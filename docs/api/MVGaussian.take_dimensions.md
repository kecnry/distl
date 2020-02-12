### [MVGaussian](MVGaussian.md).take_dimensions (function)


```py

def take_dimensions(self, dimensions)

```



Take multiple dimensions from the multivariate distribution (and remove
all others), returning another [MVGaussian](MVGaussian.md) object.

See also:

* [MVGaussian.slice](MVGaussian.slice.md)
* [MVGaussian.to_univariate](MVGaussian.to_univariate.md)

Arguments
----------
* `dimension` (list of strings or ints): the labels or indices of the
    dimensions to include in the new distribution.

Returns
----------
* [MVGaussian](MVGaussian.md) object or [Gaussian](Gaussian.md) if only one dimension provided

