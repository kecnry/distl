### [Function](Function.md).get_wrap_at (function)


```py

def get_wrap_at(self, wrap_at=None)

```



Get the computed value used for wrapping, given `wrap_at` as an optional
override to the attribute [Function.wrap_at](Function.wrap_at.md).

See also:

* [Function.wrap_at](Function.wrap_at.md)
* [Function.wrap](Function.wrap.md)

Arguments
------------
* `wrap_at` (float or False or None, optional, default=None): override
    the value of [Function.wrap_at](Function.wrap_at.md).

Returns
----------
* The computed wrapping value, accounting for [Function.unit](Function.unit.md) if `wrap_at`
    is None.

