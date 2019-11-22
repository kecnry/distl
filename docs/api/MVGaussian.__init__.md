### [MVGaussian](MVGaussian.md).__init__ (method)


```py

def __init__(self, locs=0.0, cov=1.0, unit=None, label=None, wrap_at=None)

```



Create a [MVGaussian](MVGaussian.md) distribution.

This can also be created from a function at the top-level as:

* [npdists.mvgaussian](npdists.mvgaussian.md)

Arguments
--------------
* `locs` (float or int, default=0.0): the central value of the gaussian distribution.
* `cov` (float or int, default=1.0): the scale (sigma) of the gaussian distribution.
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
* a [MVGaussian](MVGaussian.md) object
