### [MVGaussian](MVGaussian.md).slice (function)


```py

def slice(self, dimension)

```



Take a single dimension from the multivariate distribution while
retaining the covariances.  The returned [MVGaussianSlice](MVGaussianSlice.md) object
keeps the full multivariate distribution while acting somewhat
like a univariate distribution.

See also:

* [MVGaussian.take_dimensions](MVGaussian.take_dimensions.md)
* [MVGaussian.to_histogram](MVGaussian.to_histogram.md)
* [MVGaussian.to_gaussian](MVGaussian.to_gaussian.md)
* [MVGaussianSlice.dimension](MVGaussianSlice.dimension.md)

Arguments
----------
* `dimension` (int or string): the label or index of the dimension to
    take.

Returns
------------
* [MVGaussianSlice](MVGaussianSlice.md) object

