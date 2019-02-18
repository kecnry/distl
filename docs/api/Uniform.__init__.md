### [Uniform](Uniform.md).__init__ (method)


```py

def __init__(self, low=0.0, high=1.0, unit=None, label=None)

```



Create a [Uniform](Uniform.md) distribution.

This can also be created from a function at the top-level as:

* [npdists.uniform](npdists.uniform.md)

Arguments
--------------
* `low` (float or int, default=0.0): the lower limit of the uniform distribution.
* `high` (float or int, default=1.0): the upper limits of the uniform distribution.
* `unit` (astropy.units object, optional): the units of the provided values.
* `label` (string, optional): a label for the distribution.  This is used
    for the x-label while plotting the distribution, as well as a shorthand
    notation when creating a [Composite](Composite.md) distribution.

Returns
--------
* a [Uniform](Uniform.md) object

