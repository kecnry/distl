### [MVHistogram](MVHistogram.md).slice (method)


```py

def slice(self, dimension)

```



Take a single dimension from the multivariate distribution while
retaining the covariances.  The returned [MVHistogramSlice](MVHistogramSlice.md) object
keeps the full multivariate distribution while acting somewhat
like a univariate distribution.

See also:
* [MVHistogram.to_histogram](MVHistogram.to_histogram.md)
* [MVHistogram.to_gaussian](MVHistogram.to_gaussian.md)
* [MVHistorgramSlice.dimension](MVHistorgramSlice.dimension.md)

Arguments
----------
* `dimension` (int or string): the label or index of the dimension to
    take.

Returns
------------
* [MVHistogramSlice](MVHistogramSlice.md) object

