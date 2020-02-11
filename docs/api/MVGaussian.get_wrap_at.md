### [MVGaussian](MVGaussian.md).get_wrap_at (method)


```py

def get_wrap_at(self, wrap_at=None)

```



Get the computed value used for wrapping, given `wrap_at` as an optional
override to the attribute [MVGaussian.wrap_at](MVGaussian.wrap_at.md).

See also:

* [MVGaussian.wrap_at](MVGaussian.wrap_at.md)
* [MVGaussian.wrap](MVGaussian.wrap.md)

Arguments
------------
* `wrap_at` (float or False or None, optional, default=None): override
    the value of [MVGaussian.wrap_at](MVGaussian.wrap_at.md).

Returns
----------
* The computed wrapping value, accounting for [MVGaussian.unit](MVGaussian.unit.md) if `wrap_at`
    is None.

