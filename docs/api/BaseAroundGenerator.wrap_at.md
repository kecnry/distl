### [BaseAroundGenerator](BaseAroundGenerator.md).wrap_at (property)




Value at which to wrap all sampled values.  If [BaseAroundGenerator.unit](BaseAroundGenerator.unit.md) is not None,
then the value of `wrap_at` is the same as the set units.

If `False`: will not wrap
If `None`: will wrap on range 0-2pi (0-360 deg) if [BaseAroundGenerator.unit](BaseAroundGenerator.unit.md) are angular
    or 0-1 if [BaseAroundGenerator.unit](BaseAroundGenerator.unit.md) are cycles.
If float: will wrap on range 0-`wrap_at`.

See also:

* [BaseAroundGenerator.get_wrap_at](BaseAroundGenerator.get_wrap_at.md)
* [BaseAroundGenerator.wrap](BaseAroundGenerator.wrap.md)

Returns
---------
* (float or None)

