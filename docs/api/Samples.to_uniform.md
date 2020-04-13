### [Samples](Samples.md).to_uniform (function)


```py

def to_uniform(self, sigma=1.0)

```



Convert the [Samples](Samples.md) distribution to a [Uniform](Uniform.md) distribution via
a [Gaussian](Gaussian.md) distribution.

Under-the-hood, this calls [Samples.to_gaussian](Samples.to_gaussian.md) and then calls
[Gaussian.to_uniform](Gaussian.to_uniform.md) with the requested value of `sigma`.

Arguments
-----------
* `sigma` (float, optional, default=1.0): the number of standard deviations
    to adopt as the lower and upper bounds of the uniform distribution.

Returns
--------
* a [Uniform](Uniform.md) object

