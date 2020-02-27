### [Uniform_Around](Uniform_Around.md).wrap_at (property)




Value at which to wrap all sampled values.  If [Uniform_Around.unit](Uniform_Around.unit.md) is not None,
then the value of `wrap_at` is the same as the set units.

If `False`: will not wrap
If `None`: will wrap on range 0-2pi (0-360 deg) if [Uniform_Around.unit](Uniform_Around.unit.md) are angular
    or 0-1 if [Uniform_Around.unit](Uniform_Around.unit.md) are cycles.
If float: will wrap on range 0-`wrap_at`.

See also:

* [Uniform_Around.get_wrap_at](Uniform_Around.get_wrap_at.md)
* [Uniform_Around.wrap](Uniform_Around.wrap.md)

Returns
---------
* (float or None)

