### [BaseUnivariateDistribution](BaseUnivariateDistribution.md).sf (function)


```py

def sf(self, x=None, unit=None)

```



Expose the survival function (sf; also defined as 1 - cdf, but sf is
sometimes more accurate)

See [scipy docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.sf.html)

This method is just a wrapper around the scipy.stats method on
[BaseUnivariateDistribution.dist_constructor_object](BaseUnivariateDistribution.dist_constructor_object.md) after doing any requested unit-conversions.

See also:

* [BaseUnivariateDistribution.cdf](BaseUnivariateDistribution.cdf.md)
* [BaseUnivariateDistribution.logsf](BaseUnivariateDistribution.logsf.md)
* [BaseUnivariateDistribution.isf](BaseUnivariateDistribution.isf.md)

Arguments
----------
* `x` (float or array, optional, default=None): x-values at which to
    expose the sf.  If None or not provided, [BaseUnivariateDistribution.cached_sample](BaseUnivariateDistribution.cached_sample.md)
    will be used if available, or raise an error if no cached samples
    are available.
* `unit` (astropy.unit, optional, default=None): unit of the values
    in `x`.  If None or not provided, will assume they're provided in
    [BaseUnivariateDistribution.unit](BaseUnivariateDistribution.unit.md).

Returns
---------
* (float or array) sf values of the same type/shape as `x`

