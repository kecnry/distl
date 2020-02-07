### [BaseUnivariateDistribution](BaseUnivariateDistribution.md).wrap_at (property)




Value at which to wrap all sampled values.  If [BaseUnivariateDistribution.unit](BaseUnivariateDistribution.unit.md) is not None,
then the value of `wrap_at` is the same as the set units.

If `False`: will not wrap
If `None`: will wrap on range 0-2pi (0-360 deg) if [BaseUnivariateDistribution.unit](BaseUnivariateDistribution.unit.md) are angular
    or 0-1 if [BaseUnivariateDistribution.unit](BaseUnivariateDistribution.unit.md) are cycles.
If float: will wrap on range 0-`wrap_at`.

See also:

* [BaseUnivariateDistribution.get_wrap_at](BaseUnivariateDistribution.get_wrap_at.md)
* [BaseUnivariateDistribution.wrap](BaseUnivariateDistribution.wrap.md)

Returns
---------
* (float or None)

