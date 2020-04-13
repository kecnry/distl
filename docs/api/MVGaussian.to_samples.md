### [MVGaussian](MVGaussian.md).to_samples (function)


```py

def to_samples(self, dimension, N=100000, wrap_at=None)

```



Convert the [MVGaussian](MVGaussian.md) distribution to a [Samples](Samples.md) univariate distribution.

Under-the-hood, this calls [MVGaussian.to_gaussian](MVGaussian.to_gaussian.md) and then
[Gaussian.to_samples](Gaussian.to_samples.md).

Arguments
-----------
* `dimension` (int or str): index or label of the dimension to use for
    the univariate distribution.
* `N` (int, optional, default=100000): number of samples to use for
    the histogram.
* `wrap_at` (float or None, optional, default=None): value to set for
    `wrap_at` of the returned [Histogram](Histogram.md).  If None or not provided,
    will default to [MVGaussian.wrap_at](MVGaussian.wrap_at.md).

Returns
--------
* a [Samples](Samples.md) object

