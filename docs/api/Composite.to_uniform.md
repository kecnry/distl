### [Composite](Composite.md).to_uniform (method)


```py

def to_uniform(self, sigma=1.0, N=1000, bins=10, range=None)

```



Convert the [Composite](Composite.md) distribution to a [Uniform](Uniform.md) distribution via
a [Histogram](Histogram.md) distribution.

Under-the-hood, this calls [Composite.to_histogram](Composite.to_histogram.md) with the requested
values of `N`, `bins`, and `range` and then calls [Histogram.to_uniform](Histogram.to_uniform.md)
with the requested value of `sigma`.

Arguments
-----------
* `sigma` (float, optional, default=1.0): the number of standard deviations
    to adopt as the lower and upper bounds of the uniform distribution.
* `N` (int, optional, default=1000): number of samples to use for
    the histogram.
* `bins` (int, optional, default=10): number of bins to use for the
    histogram.
* `range` (tuple or None): range to use for the histogram.

Returns
--------
* a [Uniform](Uniform.md) object

