### [Uniform](Uniform.md).__init__ (function)


```py

def __init__(self, low=0.0, high=1.0, unit=None, label=None, wrap_at=None)

```



Create a [Uniform](Uniform.md) distribution.

This can also be created from a function at the top-level as:

* [distl.uniform](distl.uniform.md)

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
* `wrap_at` (float, None, or False, optional, default=None): value to
    use for wrapping.  If None and `unit` are angles, will default to
    2*pi (or 360 degrees).  If None and `unit` are cycles, will default
    to 1.0.

Returns
--------
* a [Uniform](Uniform.md) object

