### [MVHistogram](MVHistogram.md).cdf (function)


```py

def cdf(self, x=None, unit=None)

```



Expose the cummulative density function (cdf) at values of `x`.

See [scipy docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.cdf.html)

This method is just a wrapper around the scipy.stats method on
[MVHistogram.dist_constructor_object](MVHistogram.dist_constructor_object.md) after doing any requested unit-conversions.

See also:

* [MVHistogram.logcdf](MVHistogram.logcdf.md)
* [MVHistogram.pdf](MVHistogram.pdf.md)

Arguments
----------
* `x` (float or array, optional, default=None): x-values at which to
    expose the cdf.  If None or not provided, [MVHistogram.cached_sample](MVHistogram.cached_sample.md)
    will be used if available, or raise an error if no cached samples
    are available.
* `unit` (astropy.unit, optional, default=None): unit of the values
    in `x`.  If None or not provided, will assume they're provided in
    [MVHistogram.unit](MVHistogram.unit.md).

Returns
---------
* (float or array) cdf values of the same type/shape as `x`

