### [distl](distl.md).delta (function)


```py

def delta(value=0.0, unit=None, label=None, wrap_at=None)

```



Create a [Delta](Delta.md) distribution.

Arguments
--------------
* `value` (float or int, default=0.0): the value at which the delta function is True.
* `unit` (astropy.units object, optional): the units of the provided values.
* `label` (string, optional): a label for the distribution.  This is used
    for the x-label while plotting the distribution, as well as a shorthand
    notation when creating a [Composite](Composite.md) distribution.
* `wrap_at` (float or False or None, optional, default=None): value to wrap all
    sampled values.  If None, will default to 0-2pi if `unit` is angular
    (0-360 for degrees), or 0-1 if `unit` is cycles.  If False, will not wrap.
    See [Delta.wrap_at](Delta.wrap_at.md) and [Delta.wrap](Delta.wrap.md) for more details.

Returns
--------
* a [Delta](Delta.md) object

