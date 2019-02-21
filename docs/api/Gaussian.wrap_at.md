### [Gaussian](Gaussian.md).wrap_at (property)




Value at which to wrap all sampled values.  If [Gaussian.unit](Gaussian.unit.md) is not None,
then the value of `wrap_at` is the same as the set units.

If `False`: will not wrap
If `None`: will wrap on range 0-2pi (0-360 deg) if [Gaussian.unit](Gaussian.unit.md) are angular
    or 0-1 if [Gaussian.unit](Gaussian.unit.md) are cycles.
If float: will wrap on range 0-`wrap_at`.

See also:

* [Gaussian.get_wrap_at](Gaussian.get_wrap_at.md)
* [Gaussian.wrap](Gaussian.wrap.md)

Returns
---------
* (float or None)

