### [MVHistogram](MVHistogram.md).to_mvsamples (function)


```py

def to_mvsamples(self, N=1000000.0, range=None)

```



Convert the [MVHistogram](MVHistogram.md) distribution to an [MVSamples](MVSamples.md) distribution.

Under-the-hood, this calls [MVHistogram.sample](MVHistogram.sample.md) with `size=N` and `wrap_at=False`
and passes the resulting array and `bins` to [MVSamples](MVSamples.md).

Arguments
-----------
* `N` (int, optional, default=1e6): number of samples to use for
    the histogram.

Returns
--------
* an [MVSamples](MVSamples.md) object

