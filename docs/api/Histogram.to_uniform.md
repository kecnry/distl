### [Histogram](Histogram.md).to_uniform (method)


```py

def to_uniform(self, sigma=1.0)

```



Convert the [Histogram](Histogram.md) distribution to a [Uniform](Uniform.md) distribution via
a [Gaussian](Gaussian.md) distribution.

Under-the-hood, this calls [Histogram.to_gaussian](Histogram.to_gaussian.md) and then calls
[Gaussian.to_uniform](Gaussian.to_uniform.md) with the requested value of `sigma`.

Arguments
-----------
* `sigma` (float, optional, default=1.0): the number of standard deviations
    to adopt as the lower and upper bounds of the uniform distribution.

Returns
--------
* a [Uniform](Uniform.md) object

