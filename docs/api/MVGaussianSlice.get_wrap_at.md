### [MVGaussianSlice](MVGaussianSlice.md).get_wrap_at (function)


```py

def get_wrap_at(self, wrap_at=None)

```



Get the computed value used for wrapping, given `wrap_at` as an optional
override to the attribute [MVGaussianSlice.wrap_at](MVGaussianSlice.wrap_at.md).

See also:

* [MVGaussianSlice.wrap_at](MVGaussianSlice.wrap_at.md)
* [MVGaussianSlice.wrap](MVGaussianSlice.wrap.md)

Arguments
------------
* `wrap_at` (float or False or None, optional, default=None): override
    the value of [MVGaussianSlice.wrap_at](MVGaussianSlice.wrap_at.md).

Returns
----------
* The computed wrapping value, accounting for [MVGaussianSlice.unit](MVGaussianSlice.unit.md) if `wrap_at`
    is None.

