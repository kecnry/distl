### [MVGaussian](MVGaussian.md).to_histogram (method)


```py

def to_histogram(self, dimension, N=100000, bins=10, range=None, wrap_at=None)

```



Convert the [MVGaussian](MVGaussian.md) distribution to a [Histogram](Histogram.md) univariate distribution.

Under-the-hood, this calls [MVGaussian.to_gaussian](MVGaussian.to_gaussian.md) and then
[Gaussian.to_histogram](Gaussian.to_histogram.md).

Arguments
-----------
* `dimension` (int or str): index or label of the dimension to use for
    the univariate distribution.
* `N` (int, optional, default=100000): number of samples to use for
    the histogram.
* `bins` (int, optional, default=10): number of bins to use for the
    histogram.
* `range` (tuple or None): range to use for the histogram.
* `wrap_at` (float or None, optional, default=None): value to set for
    `wrap_at` of the returned [Histogram](Histogram.md).  If None or not provided,
    will default to [MVGaussian.wrap_at](MVGaussian.wrap_at.md).

Returns
--------
* a [Histogram](Histogram.md) object

