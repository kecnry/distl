### [Delta](Delta.md).__init__ (function)


```py

def __init__(self, loc=0.0, unit=None, label=None, wrap_at=None)

```



Create a [Delta](Delta.md) distribution.

This can also be created from a function at the top-level as:

* [distl.delta](distl.delta.md)

Arguments
--------------
* `loc` (float or int, default=0.0): the loc at which the delta function is True.
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
* a [Delta](Delta.md) object

