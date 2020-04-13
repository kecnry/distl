### [MVGaussian](MVGaussian.md).to_mvsamples (function)


```py

def to_mvsamples(self, N=1000000.0)

```



Convert the [MVGaussian](MVGaussian.md) distribution to an [MVSamples](MVSamples.md) distribution.

Under-the-hood, this calls [MVGaussian.sample](MVGaussian.sample.md) with `size=N` and `wrap_at=False`
and passes the resulting array and `bins` to [MVSamples](MVSamples.md).

Arguments
-----------
* `N` (int, optional, default=1e6): number of samples to use for
    the histogram.
* `bins` (int, optional, default=15): number of bins to use for the
    histogram.

Returns
--------
* an [MVSamples](MVSamples.md) object

