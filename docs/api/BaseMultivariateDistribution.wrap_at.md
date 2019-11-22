### [BaseMultivariateDistribution](BaseMultivariateDistribution.md).wrap_at (property)




Value at which to wrap all sampled values.  If [BaseMultivariateDistribution.unit](BaseMultivariateDistribution.unit.md) is not None,
then the value of `wrap_at` is the same as the set units.

If `False`: will not wrap
If `None`: will wrap on range 0-2pi (0-360 deg) if [BaseMultivariateDistribution.unit](BaseMultivariateDistribution.unit.md) are angular
    or 0-1 if [BaseMultivariateDistribution.unit](BaseMultivariateDistribution.unit.md) are cycles.
If float: will wrap on range 0-`wrap_at`.

See also:

* [BaseMultivariateDistribution.get_wrap_at](BaseMultivariateDistribution.get_wrap_at.md)
* [BaseMultivariateDistribution.wrap](BaseMultivariateDistribution.wrap.md)

Returns
---------
* (float or None)

