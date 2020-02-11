### [MVHistogramSlice](MVHistogramSlice.md).get_wrap_at (function)


```py

def get_wrap_at(self, wrap_at=None)

```



Get the computed value used for wrapping, given `wrap_at` as an optional
override to the attribute [MVHistogramSlice.wrap_at](MVHistogramSlice.wrap_at.md).

See also:

* [MVHistogramSlice.wrap_at](MVHistogramSlice.wrap_at.md)
* [MVHistogramSlice.wrap](MVHistogramSlice.wrap.md)

Arguments
------------
* `wrap_at` (float or False or None, optional, default=None): override
    the value of [MVHistogramSlice.wrap_at](MVHistogramSlice.wrap_at.md).

Returns
----------
* The computed wrapping value, accounting for [MVHistogramSlice.unit](MVHistogramSlice.unit.md) if `wrap_at`
    is None.

