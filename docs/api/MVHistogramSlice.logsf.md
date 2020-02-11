### [MVHistogramSlice](MVHistogramSlice.md).logsf (method)


```py

def logsf(self, x, unit=None)

```



Expose the log of the survival function (logsf).

See [scipy docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.logsf.html)

This method is just a wrapper around the scipy.stats method on
[MVHistogramSlice.dist_constructor_object](MVHistogramSlice.dist_constructor_object.md) after doing any requested unit-conversions.

See also:

* [MVHistogramSlice.sf](MVHistogramSlice.sf.md)
* [MVHistogramSlice.cdf](MVHistogramSlice.cdf.md)
* [MVHistogramSlice.isf](MVHistogramSlice.isf.md)

Arguments
----------
* `x` (float or array): x-values at which to expose the logsf
* `unit` (astropy.unit, optional, default=None): unit of the values
    in `x`.  If None or not provided, will assume they're provided in
    [MVHistogramSlice.unit](MVHistogramSlice.unit.md).

Returns
---------
* (float or array) logsf values of the same type/shape as `x`

