### [MVHistogram](MVHistogram.md).get_wrap_at (function)


```py

def get_wrap_at(self, wrap_at=None)

```



Get the computed value used for wrapping, given `wrap_at` as an optional
override to the attribute [MVHistogram.wrap_at](MVHistogram.wrap_at.md).

See also:

* [MVHistogram.wrap_at](MVHistogram.wrap_at.md)
* [MVHistogram.wrap](MVHistogram.wrap.md)

Arguments
------------
* `wrap_at` (float or False or None, optional, default=None): override
    the value of [MVHistogram.wrap_at](MVHistogram.wrap_at.md).

Returns
----------
* The computed wrapping value, accounting for [MVHistogram.unit](MVHistogram.unit.md) if `wrap_at`
    is None.

