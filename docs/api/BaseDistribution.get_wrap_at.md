### [BaseDistribution](BaseDistribution.md).get_wrap_at (method)


```py

def get_wrap_at(self, wrap_at=None)

```



Get the computed value used for wrapping, given `wrap_at` as an optional
override to the attribute [BaseDistribution.wrap_at](BaseDistribution.wrap_at.md).

See also:

* [BaseDistribution.wrap_at](BaseDistribution.wrap_at.md)
* [BaseDistribution.wrap](BaseDistribution.wrap.md)

Arguments
------------
* `wrap_at` (float or False or None, optional, default=None): override
    the value of [BaseDistribution.wrap_at](BaseDistribution.wrap_at.md).

Returns
----------
* The computed wrapping value, accounting for [BaseDistribution.unit](BaseDistribution.unit.md) if `wrap_at`
    is None.

