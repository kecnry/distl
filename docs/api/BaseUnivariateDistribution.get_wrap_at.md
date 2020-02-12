### [BaseUnivariateDistribution](BaseUnivariateDistribution.md).get_wrap_at (function)


```py

def get_wrap_at(self, wrap_at=None)

```



Get the computed value used for wrapping, given `wrap_at` as an optional
override to the attribute [BaseUnivariateDistribution.wrap_at](BaseUnivariateDistribution.wrap_at.md).

See also:

* [BaseUnivariateDistribution.wrap_at](BaseUnivariateDistribution.wrap_at.md)
* [BaseUnivariateDistribution.wrap](BaseUnivariateDistribution.wrap.md)

Arguments
------------
* `wrap_at` (float or False or None, optional, default=None): override
    the value of [BaseUnivariateDistribution.wrap_at](BaseUnivariateDistribution.wrap_at.md).

Returns
----------
* The computed wrapping value, accounting for [BaseUnivariateDistribution.unit](BaseUnivariateDistribution.unit.md) if `wrap_at`
    is None.

