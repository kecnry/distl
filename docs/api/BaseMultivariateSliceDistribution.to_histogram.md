### [BaseMultivariateSliceDistribution](BaseMultivariateSliceDistribution.md).to_histogram (function)


```py

def to_histogram(self, N=100000, bins=10, range=None, wrap_at=None)

```



Convert the [BaseMultivariateSliceDistribution](BaseMultivariateSliceDistribution.md) distribution to a [Histogram](Histogram.md) distribution.

Under-the-hood, this calls [BaseMultivariateSliceDistribution.sample](BaseMultivariateSliceDistribution.sample.md) with `size=N` and `wrap_at=False`
and passes the resulting array as well as the requested `bins` and `range`
to [Histogram.from_data](Histogram.from_data.md).

Arguments
-----------
* `N` (int, optional, default=100000): number of samples to use for
    the histogram.
* `bins` (int, optional, default=10): number of bins to use for the
    histogram.
* `range` (tuple or None): range to use for the histogram.
* `wrap_at` (float or None, optional, default=None): value to set for
    `wrap_at` of the returned [Histogram](Histogram.md).  If None or not provided,
    will default to [BaseMultivariateSliceDistribution.wrap_at](BaseMultivariateSliceDistribution.wrap_at.md).

Returns
--------
* a [Histogram](Histogram.md) object

