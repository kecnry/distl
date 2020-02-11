### [MVHistogramSlice](MVHistogramSlice.md).sf (method)


```py

def sf(self, x, unit=None)

```



Expose the survival function (sf; also defined as 1 - cdf, but sf is
sometimes more accurate)

See [scipy docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.sf.html)

This method is just a wrapper around the scipy.stats method on
[MVHistogramSlice.dist_constructor_object](MVHistogramSlice.dist_constructor_object.md) after doing any requested unit-conversions.

See also:

* [MVHistogramSlice.cdf](MVHistogramSlice.cdf.md)
* [MVHistogramSlice.logsf](MVHistogramSlice.logsf.md)
* [MVHistogramSlice.isf](MVHistogramSlice.isf.md)

Arguments
----------
* `x` (float or array): x-values at which to expose the sf
* `unit` (astropy.unit, optional, default=None): unit of the values
    in `x`.  If None or not provided, will assume they're provided in
    [MVHistogramSlice.unit](MVHistogramSlice.unit.md).

Returns
---------
* (float or array) sf values of the same type/shape as `x`

