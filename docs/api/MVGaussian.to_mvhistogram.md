### [MVGaussian](MVGaussian.md).to_mvhistogram (method)


```py

def to_mvhistogram(self, N=1000, bins=10, range=None)

```



Convert the [MVGaussian](MVGaussian.md) distribution to an [MVHistogram](MVHistogram.md) distribution.

Under-the-hood, this calls [MVGaussian.sample](MVGaussian.sample.md) with `size=N` and `wrap_at=False`
and passes the resulting array as well as the requested `bins` and `range`
to [MVHistogram.from_data](MVHistogram.from_data.md).

Arguments
-----------
* `N` (int, optional, default=1000): number of samples to use for
    the histogram.
* `bins` (int, optional, default=10): number of bins to use for the
    histogram.
* `range` (tuple or None): range to use for the histogram.

Returns
--------
* an [MVHistogram](MVHistogram.md) object

