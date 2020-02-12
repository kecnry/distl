### [Delta](Delta.md).get_wrap_at (function)


```py

def get_wrap_at(self, wrap_at=None)

```



Get the computed value used for wrapping, given `wrap_at` as an optional
override to the attribute [Delta.wrap_at](Delta.wrap_at.md).

See also:

* [Delta.wrap_at](Delta.wrap_at.md)
* [Delta.wrap](Delta.wrap.md)

Arguments
------------
* `wrap_at` (float or False or None, optional, default=None): override
    the value of [Delta.wrap_at](Delta.wrap_at.md).

Returns
----------
* The computed wrapping value, accounting for [Delta.unit](Delta.unit.md) if `wrap_at`
    is None.

