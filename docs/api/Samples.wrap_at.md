### [Samples](Samples.md).wrap_at (property)




Value at which to wrap all sampled values.  If [Samples.unit](Samples.unit.md) is not None,
then the value of `wrap_at` is the same as the set units.

If `False`: will not wrap
If `None`: will wrap on range 0-2pi (0-360 deg) if [Samples.unit](Samples.unit.md) are angular
    or 0-1 if [Samples.unit](Samples.unit.md) are cycles.
If float: will wrap on range 0-`wrap_at`.

See also:

* [Samples.get_wrap_at](Samples.get_wrap_at.md)
* [Samples.wrap](Samples.wrap.md)

Returns
---------
* (float or None)

