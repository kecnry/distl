### [BaseDistribution](BaseDistribution.md).wrap_at (property)




Value at which to wrap all sampled values.  If [BaseDistribution.unit](BaseDistribution.unit.md) is not None,
then the value of `wrap_at` is the same as the set units.

If `False`: will not wrap
If `None`: will wrap on range 0-2pi (0-360 deg) if [BaseDistribution.unit](BaseDistribution.unit.md) are angular
    or 0-1 if [BaseDistribution.unit](BaseDistribution.unit.md) are cycles.
If float: will wrap on range 0-`wrap_at`.

See also:

* [BaseDistribution.get_wrap_at](BaseDistribution.get_wrap_at.md)
* [BaseDistribution.wrap](BaseDistribution.wrap.md)

Returns
---------
* (float or None)

