### [Uniform](Uniform.md).get_wrap_at (function)


```py

def get_wrap_at(self, wrap_at=None)

```



Get the computed value used for wrapping, given `wrap_at` as an optional
override to the attribute [Uniform.wrap_at](Uniform.wrap_at.md).

See also:

* [Uniform.wrap_at](Uniform.wrap_at.md)
* [Uniform.wrap](Uniform.wrap.md)

Arguments
------------
* `wrap_at` (float or False or None, optional, default=None): override
    the value of [Uniform.wrap_at](Uniform.wrap_at.md).

Returns
----------
* The computed wrapping value, accounting for [Uniform.unit](Uniform.unit.md) if `wrap_at`
    is None.

