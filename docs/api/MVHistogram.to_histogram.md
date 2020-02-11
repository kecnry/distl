### [MVHistogram](MVHistogram.md).to_histogram (method)


```py

def to_histogram(self, dimension, wrap_at=None)

```



Convert the [MVHistogram](MVHistogram.md) distribution to a [Histogram](Histogram.md) univariate distribution.

Arguments
-----------
* `dimension` (int or str): index or label of the dimension to use for
    the univariate distribution.
* `wrap_at` (float or None, optional, default=None): value to set for
    `wrap_at` of the returned [Histogram](Histogram.md).  If None or not provided,
    will default to [MVHistogram.wrap_at](MVHistogram.wrap_at.md).

Returns
--------
* a [Histogram](Histogram.md) object

