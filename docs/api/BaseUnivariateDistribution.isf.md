### [BaseUnivariateDistribution](BaseUnivariateDistribution.md).isf (method)


```py

def isf(self, x, unit=None)

```



Expose the inverse of the survival function (isf).

See [scipy docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.isf.html)

This method is just a wrapper around the scipy.stats method on
[BaseUnivariateDistribution.dist_constructor_object](BaseUnivariateDistribution.dist_constructor_object.md) after doing any requested unit-conversions.

See also:

* [BaseUnivariateDistribution.sf](BaseUnivariateDistribution.sf.md)
* [BaseUnivariateDistribution.cdf](BaseUnivariateDistribution.cdf.md)
* [BaseUnivariateDistribution.logsf](BaseUnivariateDistribution.logsf.md)

Arguments
----------
* `x` (float or array): x-values at which to expose the osf
* `unit` (astropy.unit, optional, default=None): unit of the values
    in `x`.  If None or not provided, will assume they're provided in
    [BaseUnivariateDistribution.unit](BaseUnivariateDistribution.unit.md).

Returns
---------
* (float or array) osf values of the same type/shape as `x`

