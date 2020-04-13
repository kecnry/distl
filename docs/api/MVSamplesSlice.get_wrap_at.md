### [MVSamplesSlice](MVSamplesSlice.md).get_wrap_at (function)


```py

def get_wrap_at(self, wrap_at=None)

```



Get the computed value used for wrapping, given `wrap_at` as an optional
override to the attribute [MVSamplesSlice.wrap_at](MVSamplesSlice.wrap_at.md).

See also:

* [MVSamplesSlice.wrap_at](MVSamplesSlice.wrap_at.md)
* [MVSamplesSlice.wrap](MVSamplesSlice.wrap.md)

Arguments
------------
* `wrap_at` (float or False or None, optional, default=None): override
    the value of [MVSamplesSlice.wrap_at](MVSamplesSlice.wrap_at.md).

Returns
----------
* The computed wrapping value, accounting for [MVSamplesSlice.unit](MVSamplesSlice.unit.md) if `wrap_at`
    is None.

