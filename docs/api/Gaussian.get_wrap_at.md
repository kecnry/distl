### [Gaussian](Gaussian.md).get_wrap_at (method)


```py

def get_wrap_at(self, wrap_at=None)

```



Get the computed value used for wrapping, given `wrap_at` as an optional
override to the attribute [Gaussian.wrap_at](Gaussian.wrap_at.md).

See also:

* [Gaussian.wrap_at](Gaussian.wrap_at.md)
* [Gaussian.wrap](Gaussian.wrap.md)

Arguments
------------
* `wrap_at` (float or False or None, optional, default=None): override
    the value of [Gaussian.wrap_at](Gaussian.wrap_at.md).

Returns
----------
* The computed wrapping value, accounting for [Gaussian.unit](Gaussian.unit.md) if `wrap_at`
    is None.

