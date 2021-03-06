### [BaseUnivariateDistribution](BaseUnivariateDistribution.md).cdf (function)


```py

def cdf(self, x=None, unit=None)

```



Expose the cummulative density function (cdf) at values of `x`.

See [scipy docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.cdf.html)

This method is just a wrapper around the scipy.stats method on
[BaseUnivariateDistribution.dist_constructor_object](BaseUnivariateDistribution.dist_constructor_object.md) after doing any requested unit-conversions.

See also:

* [BaseUnivariateDistribution.logcdf](BaseUnivariateDistribution.logcdf.md)
* [BaseUnivariateDistribution.pdf](BaseUnivariateDistribution.pdf.md)

Arguments
----------
* `x` (float or array, optional, default=None): x-values at which to
    expose the cdf.  If None or not provided, [BaseUnivariateDistribution.cached_sample](BaseUnivariateDistribution.cached_sample.md)
    will be used if available, or raise an error if no cached samples
    are available.
* `unit` (astropy.unit, optional, default=None): unit of the values
    in `x`.  If None or not provided, will assume they're provided in
    [BaseUnivariateDistribution.unit](BaseUnivariateDistribution.unit.md).

Returns
---------
* (float or array) cdf values of the same type/shape as `x`

