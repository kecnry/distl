### [Uniform](Uniform.md).to_gaussian (function)


```py

def to_gaussian(self, sigma=1.0)

```



Convert the [Uniform](Uniform.md) distribution to a [Gaussian](Gaussian.md) distribution by
adopting a certain `sigma`: number of standard deviations which should
be adopted as the lower and upper bounds of the [Uniform](Uniform.md) distribution.

Arguments
----------
* `sigma` (float, optional, default=1.0): number of standard deviations
    which should be adopted as the lower and upper bounds of the
    [Uniform](Uniform.md) distribution.

Returns
---------
* a [Gaussian](Gaussian.md) distribution

