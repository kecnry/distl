### [Gaussian](Gaussian.md).__init__ (function)


```py

def __init__(self, loc=0.0, scale=1.0, unit=None, label=None, label_latex=None, wrap_at=None, uniqueid=None)

```



Create a [Gaussian](Gaussian.md) distribution.

This can also be created from a function at the top-level as:

* [distl.gaussian](distl.gaussian.md)

Arguments
--------------
* `loc` (float or int, default=0.0): the central value (mean) of the
    gaussian distribution.
* `scale` (float or int, default=1.0): the scale (sigma) of the gaussian
    distribution.
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
* a [Gaussian](Gaussian.md) object

