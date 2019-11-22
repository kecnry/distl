### [MVHistogram](MVHistogram.md).to_mvgaussian (method)


```py

def to_mvgaussian(self, N=100000.0)

```



Convert the [MVHistogram](MVHistogram.md) distribution to an [MVGaussian](MVGaussian.md) distribution.

See also:

* [MVHistogram.means](MVHistogram.means.md)
* [MVHistogram.get_covariances](MVHistogram.get_covariances.md)

Arguments
---------
* `N` (int, default=1e5): number of samples to use when calling
    [MVHistogram.get_covariances](MVHistogram.get_covariances.md).

Returns
--------
* an [MVGaussian](MVGaussian.md) object

