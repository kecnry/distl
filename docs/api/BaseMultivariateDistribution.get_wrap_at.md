### [BaseMultivariateDistribution](BaseMultivariateDistribution.md).get_wrap_at (function)


```py

def get_wrap_at(self, wrap_at=None)

```



Get the computed value used for wrapping, given `wrap_at` as an optional
override to the attribute [BaseMultivariateDistribution.wrap_at](BaseMultivariateDistribution.wrap_at.md).

See also:

* [BaseMultivariateDistribution.wrap_at](BaseMultivariateDistribution.wrap_at.md)
* [BaseMultivariateDistribution.wrap](BaseMultivariateDistribution.wrap.md)

Arguments
------------
* `wrap_at` (float or False or None, optional, default=None): override
    the value of [BaseMultivariateDistribution.wrap_at](BaseMultivariateDistribution.wrap_at.md).

Returns
----------
* The computed wrapping value, accounting for [BaseMultivariateDistribution.unit](BaseMultivariateDistribution.unit.md) if `wrap_at`
    is None.

