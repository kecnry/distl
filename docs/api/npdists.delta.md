### [npdists](npdists.md).delta (function)


```py

def delta(value, unit=None, label=None)

```



Create a [Delta](Delta.md) distribution.

Arguments
--------------
* `value` (float or int): the value at which the delta function is True.
* `unit` (astropy.units object, optional): the units of the provided values.
* `label` (string, optional): a label for the distribution.  This is used
    for the x-label while plotting the distribution, as well as a shorthand
    notation when creating a [Composite](Composite.md) distribution.

Returns
--------
* a [Delta](Delta.md) object

