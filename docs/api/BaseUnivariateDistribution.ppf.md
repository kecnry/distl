### [BaseUnivariateDistribution](BaseUnivariateDistribution.md).ppf (function)


```py

def ppf(self, q, unit=None, as_quantity=False, wrap_at=None)

```



Expose the percent point function (ppf; iverse of cdf - percentiles) at
values of `q`.

See [scipy docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.ppf.html)

This method is just a wrapper around the scipy.stats method on
[BaseUnivariateDistribution.dist_constructor_object](BaseUnivariateDistribution.dist_constructor_object.md) with unit-conversions, support for
quantity objects, and wrapping done on the returned result.

See also:

* [BaseUnivariateDistribution.pdf](BaseUnivariateDistribution.pdf.md)
* [BaseUnivariateDistribution.cdf](BaseUnivariateDistribution.cdf.md)
* [BaseUnivariateDistribution.sample](BaseUnivariateDistribution.sample.md)

Arguments
----------
* `q` (float or array): percentiles at which to expose the ppf
* `unit` (astropy.unit, optional, default=None): unit of the exposed
    values.  If None or not provided, will assume they're provided in
    [BaseUnivariateDistribution.unit](BaseUnivariateDistribution.unit.md).
* `as_quantity` (bool, optional, default=False): whether to return an
    astropy quantity object instead of just the value.  Astropy must
    be installed.
* `wrap_at` (float, None, or False, optional, default=None): value to
    use for wrapping.  See [BaseUnivariateDistribution.wrap](BaseUnivariateDistribution.wrap.md).  If not provided or None,
    will use the value from [BaseUnivariateDistribution.wrap_at](BaseUnivariateDistribution.wrap_at.md).  Note: wrapping is
    computed before changing units, so `wrap_at` must be provided
    according to [BaseUnivariateDistribution.unit](BaseUnivariateDistribution.unit.md) not `unit`.

Returns
---------
* (float or array) ppf values of the same type/shape as `x`

