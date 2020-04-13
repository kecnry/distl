### [MVSamples](MVSamples.md).to_samples (function)


```py

def to_samples(self, dimension)

```



Convert the [MVSamples](MVSamples.md) distribution to a [Samples](Samples.md) univariate distribution.

Arguments
-----------
* `dimension` (int or str): index or label of the dimension to use for
    the univariate distribution.
* `wrap_at` (float or None, optional, default=None): value to set for
    `wrap_at` of the returned [Histogram](Histogram.md).  If None or not provided,
    will default to [MVSamples.wrap_at](MVSamples.wrap_at.md).

Returns
--------
* a [Samples](Samples.md) object

