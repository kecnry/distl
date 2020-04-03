### [MVSamples](MVSamples.md).to_histogram (function)


```py

def to_histogram(self, dimension)

```



Convert the [MVSamples](MVSamples.md) distribution to a [Histogram](Histogram.md) univariate distribution.

Under-the-hood, this calls [MVSamples.to_samples](MVSamples.to_samples.md) followed by [Samples.to_histogram](Samples.to_histogram.md).

Arguments
-----------
* `dimension` (int or str): index or label of the dimension to use for
    the univariate distribution.

Returns
--------
* a [Histogram](Histogram.md) object

