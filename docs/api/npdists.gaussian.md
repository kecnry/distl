### [npdists](npdists.md).gaussian (function)


```py

def gaussian(loc, scale, unit=None, label=None)

```



Create a [Gaussian](Gaussian.md) distribution.

Arguments
--------------
* `loc` (float or int): the central value of the gaussian distribution.
* `scale` (float or int): the scale (sigma) of the gaussian distribution.
* `unit` (astropy.units object, optional): the units of the provided values.
* `label` (string, optional): a label for the distribution.  This is used
    for the x-label while plotting the distribution, as well as a shorthand
    notation when creating a [Composite](Composite.md) distribution.

Returns
--------
* a [Gaussian](Gaussian.md) object

