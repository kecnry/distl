### [MVHistogram](MVHistogram.md).to_mvgaussian (method)


```py

def to_mvgaussian(self, N=100000.0, allow_singular=False)

```



Convert the [MVHistogram](MVHistogram.md) distribution to an [MVGaussian](MVGaussian.md) distribution.

See also:

* [MVHistogram.calculate_means](MVHistogram.calculate_means.md)
* [MVHistogram.calculate_covariances](MVHistogram.calculate_covariances.md)

Arguments
---------
* `N` (int, default=1e5): number of samples to use when calling
    [MVHistogram.calculate_means](MVHistogram.calculate_means.md) and [MVHistogram.calculate_covariances](MVHistogram.calculate_covariances.md).
* `allow_singular` (bool, optional, default=False): value to pass to
    [MVGaussian](MVGaussian.md).

Returns
--------
* an [MVGaussian](MVGaussian.md) object

