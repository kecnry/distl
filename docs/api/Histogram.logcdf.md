### [Histogram](Histogram.md).logcdf (method)


```py

def logcdf(self, x, unit=None)

```



Expose the log-cummulative density function (log of cdf) at values of `x`.

See [scipy docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.logcdf.html)

This method is just a wrapper around the scipy.stats method on
[Histogram.dist_constructor_object](Histogram.dist_constructor_object.md) after doing any requested unit-conversions.

See also:
* [Histogram.cdf](Histogram.cdf.md)
* [Histogram.pdf](Histogram.pdf.md)

Arguments
----------
* `x` (float or array): x-values at which to expose the logcdf
* `unit` (astropy.unit, optional, default=None): unit of the values
    in `x`.  If None or not provided, will assume they're provided in
    [Histogram.unit](Histogram.unit.md).

Returns
---------
* (float or array) logcdf values of the same type/shape as `x`

