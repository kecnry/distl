### [distl](distl.md).gaussian (function)


```py

def gaussian(loc=0.0, scale=1.0, unit=None, label=None, wrap_at=None)

```



Create a [Gaussian](Gaussian.md) distribution.

Arguments
--------------
* `loc` (float or int, default=0.0): the central value of the gaussian distribution.
* `scale` (float or int, default=1.0): the scale (sigma) of the gaussian distribution.
* `unit` (astropy.units object, optional): the units of the provided values.
* `label` (string, optional): a label for the distribution.  This is used
    for the x-label while plotting the distribution, as well as a shorthand
    notation when creating a [Composite](Composite.md) distribution.
* `wrap_at` (float or False or None, optional, default=None): value to wrap all
    sampled values.  If None, will default to 0-2pi if `unit` is angular
    (0-360 for degrees), or 0-1 if `unit` is cycles.  If False, will not wrap.
    See [Gaussian.wrap_at](Gaussian.wrap_at.md) and [Gaussian.wrap](Gaussian.wrap.md) for more details.

Returns
--------
* a [Gaussian](Gaussian.md) object

