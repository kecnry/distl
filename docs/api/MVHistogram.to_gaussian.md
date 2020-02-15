### [MVHistogram](MVHistogram.md).to_gaussian (function)


```py

def to_gaussian(self, dimension)

```



Convert the [MVHistogram](MVHistogram.md) distribution to a [Gaussian](Gaussian.md) univariate distribution.

Under-the-hood, this calls [MVHistogram.to_histogram](MVHistogram.to_histogram.md) followed by [Histogram.to_gaussian](Histogram.to_gaussian.md).

Arguments
-----------
* `dimension` (int or str): index or label of the dimension to use for
    the univariate distribution.

Returns
----------
* a [Gaussian](Gaussian.md) object

