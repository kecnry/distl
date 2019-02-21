### [Uniform](Uniform.md).wrap_at (property)




Value at which to wrap all sampled values.  If [Uniform.unit](Uniform.unit.md) is not None,
then the value of `wrap_at` is the same as the set units.

If `False`: will not wrap
If `None`: will wrap on range 0-2pi (0-360 deg) if [Uniform.unit](Uniform.unit.md) are angular
    or 0-1 if [Uniform.unit](Uniform.unit.md) are cycles.
If float: will wrap on range 0-`wrap_at`.

See also:

* [Uniform.get_wrap_at](Uniform.get_wrap_at.md)
* [Uniform.wrap](Uniform.wrap.md)

Returns
---------
* (float or None)

