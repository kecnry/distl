### [npdists](npdists.md).uniform (function)


```py

def uniform(low, high, unit=None, label=None)

```



Create a [Uniform](Uniform.md) distribution.

Arguments
--------------
* `low` (float or int): the lower limit of the uniform distribution.
* `high` (float or int): the upper limits of the uniform distribution.
* `unit` (astropy.units object, optional): the units of the provided values.
* `label` (string, optional): a label for the distribution.  This is used
    for the x-label while plotting the distribution, as well as a shorthand
    notation when creating a [Composite](Composite.md) distribution.

Returns
--------
* a [Uniform](Uniform.md) object

