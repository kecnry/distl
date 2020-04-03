### [MVSamples](MVSamples.md).wrap_ats (property)




Value at which to wrap all sampled values.  If [MVSamples.unit](MVSamples.unit.md) is not None,
then the value of `wrap_at` is the same as the set units.

If `False`: will not wrap
If `None`: will wrap on range 0-2pi (0-360 deg) if [MVSamples.unit](MVSamples.unit.md) are angular
    or 0-1 if [MVSamples.unit](MVSamples.unit.md) are cycles.
If float: will wrap on range 0-`wrap_at`.

See also:

* [MVSamples.all_wrap_ats](MVSamples.all_wrap_ats.md)
* [MVSamples.dimensions](MVSamples.dimensions.md)
* [MVSamples.get_wrap_at](MVSamples.get_wrap_at.md)
* [MVSamples.wrap](MVSamples.wrap.md)

Returns
---------
* (float or None)

