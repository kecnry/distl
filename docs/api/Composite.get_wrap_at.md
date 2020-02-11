### [Composite](Composite.md).get_wrap_at (method)


```py

def get_wrap_at(self, wrap_at=None)

```



Get the computed value used for wrapping, given `wrap_at` as an optional
override to the attribute [Composite.wrap_at](Composite.wrap_at.md).

See also:

* [Composite.wrap_at](Composite.wrap_at.md)
* [Composite.wrap](Composite.wrap.md)

Arguments
------------
* `wrap_at` (float or False or None, optional, default=None): override
    the value of [Composite.wrap_at](Composite.wrap_at.md).

Returns
----------
* The computed wrapping value, accounting for [Composite.unit](Composite.unit.md) if `wrap_at`
    is None.

