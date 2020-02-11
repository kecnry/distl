### [Histogram](Histogram.md).isf (method)


```py

def isf(self, x, unit=None)

```



Expose the inverse of the survival function (isf).

See [scipy docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.isf.html)

This method is just a wrapper around the scipy.stats method on
[Histogram.dist_constructor_object](Histogram.dist_constructor_object.md) after doing any requested unit-conversions.

See also:

* [Histogram.sf](Histogram.sf.md)
* [Histogram.cdf](Histogram.cdf.md)
* [Histogram.logsf](Histogram.logsf.md)

Arguments
----------
* `x` (float or array): x-values at which to expose the osf
* `unit` (astropy.unit, optional, default=None): unit of the values
    in `x`.  If None or not provided, will assume they're provided in
    [Histogram.unit](Histogram.unit.md).

Returns
---------
* (float or array) osf values of the same type/shape as `x`

