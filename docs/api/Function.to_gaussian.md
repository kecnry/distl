### [Function](Function.md).to_gaussian (function)


```py

def to_gaussian(self, N=1000, bins=10, range=None)

```



Convert the [Function](Function.md) distribution to a [Gaussian](Gaussian.md) distribution via
a [Histogram](Histogram.md) distribution.

Under-the-hood, this calls [Function.to_histogram](Function.to_histogram.md) with the requested
values of `N`, `bins`, and `range` and then calls [Histogram.to_gaussian](Histogram.to_gaussian.md).

Arguments
-----------
* `N` (int, optional, default=1000): number of samples to use for
    the histogram.
* `bins` (int, optional, default=10): number of bins to use for the
    histogram.
* `range` (tuple or None): range to use for the histogram.

Returns
--------
* a [Gaussian](Gaussian.md) object

