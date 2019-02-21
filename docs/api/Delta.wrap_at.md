### [Delta](Delta.md).wrap_at (property)




Value at which to wrap all sampled values.  If [Delta.unit](Delta.unit.md) is not None,
then the value of `wrap_at` is the same as the set units.

If `False`: will not wrap
If `None`: will wrap on range 0-2pi (0-360 deg) if [Delta.unit](Delta.unit.md) are angular
    or 0-1 if [Delta.unit](Delta.unit.md) are cycles.
If float: will wrap on range 0-`wrap_at`.

See also:

* [Delta.get_wrap_at](Delta.get_wrap_at.md)
* [Delta.wrap](Delta.wrap.md)

Returns
---------
* (float or None)

