### [BaseMultivariateSliceDistribution](BaseMultivariateSliceDistribution.md).get_wrap_at (function)


```py

def get_wrap_at(self, wrap_at=None)

```



Get the computed value used for wrapping, given `wrap_at` as an optional
override to the attribute [BaseMultivariateSliceDistribution.wrap_at](BaseMultivariateSliceDistribution.wrap_at.md).

See also:

* [BaseMultivariateSliceDistribution.wrap_at](BaseMultivariateSliceDistribution.wrap_at.md)
* [BaseMultivariateSliceDistribution.wrap](BaseMultivariateSliceDistribution.wrap.md)

Arguments
------------
* `wrap_at` (float or False or None, optional, default=None): override
    the value of [BaseMultivariateSliceDistribution.wrap_at](BaseMultivariateSliceDistribution.wrap_at.md).

Returns
----------
* The computed wrapping value, accounting for [BaseMultivariateSliceDistribution.unit](BaseMultivariateSliceDistribution.unit.md) if `wrap_at`
    is None.

