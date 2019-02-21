### [Composite](Composite.md).wrap_at (property)




Value at which to wrap all sampled values.  If [Composite.unit](Composite.unit.md) is not None,
then the value of `wrap_at` is the same as the set units.

If `False`: will not wrap
If `None`: will wrap on range 0-2pi (0-360 deg) if [Composite.unit](Composite.unit.md) are angular
    or 0-1 if [Composite.unit](Composite.unit.md) are cycles.
If float: will wrap on range 0-`wrap_at`.

See also:

* [Composite.get_wrap_at](Composite.get_wrap_at.md)
* [Composite.wrap](Composite.wrap.md)

Returns
---------
* (float or None)

