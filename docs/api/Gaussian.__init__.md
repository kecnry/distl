### [Gaussian](Gaussian.md).__init__ (method)


```py

def __init__(self, loc=0.0, scale=1.0, unit=None, label=None)

```



Create a [Gaussian](Gaussian.md) distribution.

This can also be created from a function at the top-level as:

* [npdists.gaussian](npdists.gaussian.md)

Arguments
--------------
* `loc` (float or int, default=0.0): the central value of the gaussian distribution.
* `scale` (float or int, default=1.0): the scale (sigma) of the gaussian distribution.
* `unit` (astropy.units object, optional): the units of the provided values.
* `label` (string, optional): a label for the distribution.  This is used
    for the x-label while plotting the distribution, as well as a shorthand
    notation when creating a [Composite](Composite.md) distribution.

Returns
--------
* a [Gaussian](Gaussian.md) object

