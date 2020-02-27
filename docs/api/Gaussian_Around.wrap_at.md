### [Gaussian_Around](Gaussian_Around.md).wrap_at (property)




Value at which to wrap all sampled values.  If [Gaussian_Around.unit](Gaussian_Around.unit.md) is not None,
then the value of `wrap_at` is the same as the set units.

If `False`: will not wrap
If `None`: will wrap on range 0-2pi (0-360 deg) if [Gaussian_Around.unit](Gaussian_Around.unit.md) are angular
    or 0-1 if [Gaussian_Around.unit](Gaussian_Around.unit.md) are cycles.
If float: will wrap on range 0-`wrap_at`.

See also:

* [Gaussian_Around.get_wrap_at](Gaussian_Around.get_wrap_at.md)
* [Gaussian_Around.wrap](Gaussian_Around.wrap.md)

Returns
---------
* (float or None)

