### [Composite](Composite.md).to_samples (function)


```py

def to_samples(self, N=100000, wrap_at=None)

```



Convert the [Composite](Composite.md) distribution to a [Samples](Samples.md) distribution.

Under-the-hood, this calls [Composite.sample](Composite.sample.md) with `size=N` and `wrap_at=False`
and passes the resulting array to [Samples.__init__](Samples.__init__.md).

Arguments
-----------
* `N` (int, optional, default=100000): number of samples to sample.
* `wrap_at` (float or None, optional, default=None): value to set for
    `wrap_at` of the returned [Histogram](Histogram.md).  If None or not provided,
    will default to [Composite.wrap_at](Composite.wrap_at.md).

Returns
--------
* a [Histogram](Histogram.md) object

