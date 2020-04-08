### [MVHistogramSlice](MVHistogramSlice.md).to_samples (function)


```py

def to_samples(self, N=100000, wrap_at=None)

```



Convert the [MVHistogramSlice](MVHistogramSlice.md) distribution to a [Samples](Samples.md) distribution.

Under-the-hood, this calls [MVHistogramSlice.sample](MVHistogramSlice.sample.md) with `size=N` and `wrap_at=False`
and passes the resulting array to [Samples.__init__](Samples.__init__.md).

Arguments
-----------
* `N` (int, optional, default=100000): number of samples to sample.

* `wrap_at` (float or None, optional, default=None): value to set for
    `wrap_at` of the returned [Histogram](Histogram.md).  If None or not provided,
    will default to [MVHistogramSlice.wrap_at](MVHistogramSlice.wrap_at.md).

Returns
--------
* a [Histogram](Histogram.md) object

