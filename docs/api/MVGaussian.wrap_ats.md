### [MVGaussian](MVGaussian.md).wrap_ats (property)




Value at which to wrap all sampled values.  If [MVGaussian.unit](MVGaussian.unit.md) is not None,
then the value of `wrap_at` is the same as the set units.

If `False`: will not wrap
If `None`: will wrap on range 0-2pi (0-360 deg) if [MVGaussian.unit](MVGaussian.unit.md) are angular
    or 0-1 if [MVGaussian.unit](MVGaussian.unit.md) are cycles.
If float: will wrap on range 0-`wrap_at`.

See also:

* [MVGaussian.all_wrap_ats](MVGaussian.all_wrap_ats.md)
* [MVGaussian.dimensions](MVGaussian.dimensions.md)
* [MVGaussian.get_wrap_at](MVGaussian.get_wrap_at.md)
* [MVGaussian.wrap](MVGaussian.wrap.md)

Returns
---------
* (float or None)

