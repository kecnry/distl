### [Delta_Around](Delta_Around.md).wrap_at (property)




Value at which to wrap all sampled values.  If [Delta_Around.unit](Delta_Around.unit.md) is not None,
then the value of `wrap_at` is the same as the set units.

If `False`: will not wrap
If `None`: will wrap on range 0-2pi (0-360 deg) if [Delta_Around.unit](Delta_Around.unit.md) are angular
    or 0-1 if [Delta_Around.unit](Delta_Around.unit.md) are cycles.
If float: will wrap on range 0-`wrap_at`.

See also:

* [Delta_Around.get_wrap_at](Delta_Around.get_wrap_at.md)
* [Delta_Around.wrap](Delta_Around.wrap.md)

Returns
---------
* (float or None)

