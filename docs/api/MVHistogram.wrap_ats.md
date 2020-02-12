### [MVHistogram](MVHistogram.md).wrap_ats (property)




Value at which to wrap all sampled values.  If [MVHistogram.unit](MVHistogram.unit.md) is not None,
then the value of `wrap_at` is the same as the set units.

If `False`: will not wrap
If `None`: will wrap on range 0-2pi (0-360 deg) if [MVHistogram.unit](MVHistogram.unit.md) are angular
    or 0-1 if [MVHistogram.unit](MVHistogram.unit.md) are cycles.
If float: will wrap on range 0-`wrap_at`.

See also:

* [MVHistogram.all_wrap_ats](MVHistogram.all_wrap_ats.md)
* [MVHistogram.dimensions](MVHistogram.dimensions.md)
* [MVHistogram.get_wrap_at](MVHistogram.get_wrap_at.md)
* [MVHistogram.wrap](MVHistogram.wrap.md)

Returns
---------
* (float or None)

