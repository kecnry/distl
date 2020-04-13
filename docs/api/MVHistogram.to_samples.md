### [MVHistogram](MVHistogram.md).to_samples (function)


```py

def to_samples(self, dimension, N=100000, wrap_at=None)

```



Convert the [MVHistogram](MVHistogram.md) distribution to a [Samples](Samples.md) univariate distribution.

Under-the-hood, this calls [MVHistogram.to_histogram](MVHistogram.to_histogram.md) followed by [Histogram.to_samples](Histogram.to_samples.md).

Arguments
-----------
* `dimension` (int or str): index or label of the dimension to use for
    the univariate distribution.
* `N` (int, optional, default=1e5): number of samples to draw and store
    in the [Samples](Samples.md) distribution.  See [Histogram.to_samples](Histogram.to_samples.md).
* `wrap_at` (float or None, optional, default=None): value to set for
    `wrap_at` of the returned [Histogram](Histogram.md).  If None or not provided,
    will default to [MVHistogram.wrap_at](MVHistogram.wrap_at.md).

Returns
--------
* a [Histogram](Histogram.md) object

