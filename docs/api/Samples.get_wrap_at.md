### [Samples](Samples.md).get_wrap_at (function)


```py

def get_wrap_at(self, wrap_at=None)

```



Get the computed value used for wrapping, given `wrap_at` as an optional
override to the attribute [Samples.wrap_at](Samples.wrap_at.md).

See also:

* [Samples.wrap_at](Samples.wrap_at.md)
* [Samples.wrap](Samples.wrap.md)

Arguments
------------
* `wrap_at` (float or False or None, optional, default=None): override
    the value of [Samples.wrap_at](Samples.wrap_at.md).

Returns
----------
* The computed wrapping value, accounting for [Samples.unit](Samples.unit.md) if `wrap_at`
    is None.

