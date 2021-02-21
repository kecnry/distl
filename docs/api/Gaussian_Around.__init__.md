### [Gaussian_Around](Gaussian_Around.md).__init__ (function)


```py

def __init__(self, scale, value=None, unit=None, label=None, label_latex=None, wrap_at=None, uniqueid=None)

```



Create a [Gaussian_Around](Gaussian_Around.md) object which, when called, will resolve
to a [Gaussian](Gaussian.md) object around a given central value.

This can also be created from a function at the top-level as:

* [distl.gaussian_around](distl.gaussian_around.md)

Arguments
--------------
* `scale` (float or int, default=1.0): the scale (sigma) of the gaussian
    distribution.
* `value` (float, optional, default=None): the current face-value.
* `unit` (astropy.units object, optional): the units of the provided values.
* `label` (string, optional): a label for the distribution.  This is used
    for the x-label while plotting the distribution if `label_latex` is not provided,
    as well as a shorthand notation when creating a [Composite](Composite.md) distribution.
* `label_latex` (string, optional): a latex label for the distribution.  This is used
    for the x-label while plotting.
* `wrap_at` (float, None, or False, optional, default=None): value to
    use for wrapping.  If None and `unit` are angles, will default to
    2*pi (or 360 degrees).  If None and `unit` are cycles, will default
    to 1.0.
Returns
--------
* a [Gaussian_Around](Gaussian_Around.md) object

