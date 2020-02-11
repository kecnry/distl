### [Gaussian](Gaussian.md).to_uniform (function)


```py

def to_uniform(self, sigma=1.0)

```



Convert the [Gaussian](Gaussian.md) distribution to a [Uniform](Uniform.md) distribution by
adopting the lower and upper bounds as a certain value of `sigma`
for the [Gaussian](Gaussian.md) distribution.

Arguments
----------
* `sigma` (float, optional, default=1.0): number of standard deviations
    which should be adopted as the lower and upper bounds of the
    [Uniform](Uniform.md) distribution.

Returns
---------
* a [Uniform](Uniform.md) distribution

