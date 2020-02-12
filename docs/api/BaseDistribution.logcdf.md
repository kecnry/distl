### [BaseDistribution](BaseDistribution.md).logcdf (function)


```py

def logcdf(self, x=None, unit=None)

```



Expose the log-cummulative density function (log of cdf) at values of `x`.

See [scipy docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.logcdf.html)

This method is just a wrapper around the scipy.stats method on
[BaseDistribution.dist_constructor_object](BaseDistribution.dist_constructor_object.md) after doing any requested unit-conversions.

See also:

* [BaseDistribution.cdf](BaseDistribution.cdf.md)
* [BaseDistribution.pdf](BaseDistribution.pdf.md)

Arguments
----------
* `x` (float or array, optional, default=None): x-values at which to
    expose the logcdf.  If None or not provided, [BaseDistribution.cached_sample](BaseDistribution.cached_sample.md)
    will be used if available, or raise an error if no cached samples
    are available.
* `unit` (astropy.unit, optional, default=None): unit of the values
    in `x`.  If None or not provided, will assume they're provided in
    [BaseDistribution.unit](BaseDistribution.unit.md).

Returns
---------
* (float or array) logcdf values of the same type/shape as `x`

