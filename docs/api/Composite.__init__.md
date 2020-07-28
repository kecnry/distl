### [Composite](Composite.md).__init__ (function)


```py

def __init__(self, math, dists, unit=None, label=None, label_latex=None, wrap_at=None)

```



Create a [Composite](Composite.md) distribution from other distribution(s).

Most likely, users will create Composite objects through math operators
directly.  See examples on the [Composite](Composite.md) overview page.

Arguments
----------
* `math`: operator to be used between the `dists`.  Must
    be a valid and implemented operator.
* `dists` (list of distribution objects): distribution objects
    to apply `math` operator.  Some operators (e.g. sin, cos, tan) only
    take one distribution as an argument, but most require 2 or more.
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
---------
* a [Composite](Composite.md) object.

