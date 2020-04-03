### [MVSamples](MVSamples.md).get_wrap_at (function)


```py

def get_wrap_at(self, wrap_at=None)

```



Get the computed value used for wrapping, given `wrap_at` as an optional
override to the attribute [MVSamples.wrap_at](MVSamples.wrap_at.md).

See also:

* [MVSamples.wrap_at](MVSamples.wrap_at.md)
* [MVSamples.wrap](MVSamples.wrap.md)

Arguments
------------
* `wrap_at` (float or False or None, optional, default=None): override
    the value of [MVSamples.wrap_at](MVSamples.wrap_at.md).

Returns
----------
* The computed wrapping value, accounting for [MVSamples.unit](MVSamples.unit.md) if `wrap_at`
    is None.

