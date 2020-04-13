### [MVSamples](MVSamples.md).slice (function)


```py

def slice(self, dimension)

```



Take a single dimension from the multivariate distribution while
retaining the covariances.  The returned [MVSamplesSlice](MVSamplesSlice.md) object
keeps the full multivariate distribution while acting somewhat
like a univariate distribution.

See also:

* [MVSamples.to_histogram](MVSamples.to_histogram.md)
* [MVSamples.to_gaussian](MVSamples.to_gaussian.md)
* [MVSamplesSlice.dimension](MVSamplesSlice.dimension.md)

Arguments
----------
* `dimension` (int or string): the label or index of the dimension to
    take.

Returns
------------
* [MVSamplesSlice](MVSamplesSlice.md) object

