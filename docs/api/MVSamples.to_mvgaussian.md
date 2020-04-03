### [MVSamples](MVSamples.md).to_mvgaussian (function)


```py

def to_mvgaussian(self, allow_singular=False)

```



Convert the [MVSamples](MVSamples.md) distribution to an [MVGaussian](MVGaussian.md) distribution.

See also:

* [MVSamples.calculate_means](MVSamples.calculate_means.md)
* [MVSamples.calculate_covariances](MVSamples.calculate_covariances.md)

Arguments
---------
* `allow_singular` (bool, optional, default=False): value to pass to
    [MVGaussian](MVGaussian.md).

Returns
--------
* an [MVGaussian](MVGaussian.md) object

