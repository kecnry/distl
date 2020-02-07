### [Composite](Composite.md).__init__ (function)


```py

def __init__(self, math, dist1, dist2=None, unit=None, label=None, wrap_at=None)

```



Create a [Composite](Composite.md) distribution from two other distributions.

Most likely, users will create Composite objects through math operators
directly.  See examples on the [Composite](Composite.md) overview page.

Arguments
----------
* `math`: operator to be used between the two distributions.  Must
    be a valid and implemented operator.
* `dist1` ([BaseDistribution](BaseDistribution.md))
* `dist2` ([BaseDistribution](BaseDistribution.md), optional, default=None): the second
    distribution is required for most operators.  Some operators
    (e.g. sin, cos, tan) only take one distribution as an argument.
* `unit` (astropy.units object, optional): the units of the provided values.
* `label` (string, optional): a label for the distribution.  This is used
    for the x-label while plotting the distribution, as well as a shorthand
    notation when creating a [Composite](Composite.md) distribution.
* `wrap_at` (float, None, or False, optional, default=None): value to
    use for wrapping.  If None and `unit` are angles, will default to
    2*pi (or 360 degrees).  If None and `unit` are cycles, will default
    to 1.0.

Returns
---------
* a [Composite](Composite.md) object.

