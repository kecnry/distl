### [Delta_Around](Delta_Around.md).__init__ (function)


```py

def __init__(self, value=None, unit=None, label=None, label_latex=None, wrap_at=None, unique=None)

```



Create a [Delta_Around](Delta_Around.md) object which, when called, will resolve
to a [Delta](Delta.md) object around a given central value.

This can also be created from a function at the top-level as:

* [distl.delta_around](distl.delta_around.md)

Arguments
--------------
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
* a [Delta](Delta.md) object

