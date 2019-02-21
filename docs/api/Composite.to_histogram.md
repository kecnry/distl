### [Composite](Composite.md).to_histogram (method)


```py

def to_histogram(self, N=1000, bins=10, range=None)

```



Convert the [Composite](Composite.md) distribution to a [Histogram](Histogram.md) distribution.

Under-the-hood, this calls [Composite.sample](Composite.sample.md) with `size=N` and `wrap_at=False`
and passes the resulting array as well as the requested `bins` and `range`
to [Histogram.from_data](Histogram.from_data.md).

Arguments
-----------
* `N` (int, optional, default=1000): number of samples to use for
    the histogram.
* `bins` (int, optional, default=10): number of bins to use for the
    histogram.
* `range` (tuple or None): range to use for the histogram.

Returns
--------
* a [Histogram](Histogram.md) object

