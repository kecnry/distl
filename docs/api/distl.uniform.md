### [distl](distl.md).uniform (function)


```py

def uniform(low=0.0, high=1.0, unit=None, label=None, wrap_at=None)

```



Create a [Uniform](Uniform.md) distribution.

Arguments
--------------
* `low` (float or int, default=0.0): the lower limit of the uniform distribution.
* `high` (float or int, default=1.0): the upper limits of the uniform distribution.
    Must be higher than `low` unless `wrap_at` is provided or `unit`
    is provided as angular (rad, deg, cycles).
* `unit` (astropy.units object, optional): the units of the provided values.
* `label` (string, optional): a label for the distribution.  This is used
    for the x-label while plotting the distribution, as well as a shorthand
    notation when creating a [Composite](Composite.md) distribution.
* `wrap_at` (float or False or None, optional, default=None): value to wrap all
    sampled values.  If None, will default to 0-2pi if `unit` is angular
    (0-360 for degrees), or 0-1 if `unit` is cycles.  If False, will not wrap.
    See [Uniform.wrap_at](Uniform.wrap_at.md) and [Uniform.wrap](Uniform.wrap.md) for more details.

Returns
--------
* a [Uniform](Uniform.md) object

