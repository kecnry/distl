### [Uniform](Uniform.md).isf (function)


```py

def isf(self, x, unit=None)

```



Expose the inverse of the survival function (isf).

See [scipy docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.isf.html)

This method is just a wrapper around the scipy.stats method on
[Uniform.dist_constructor_object](Uniform.dist_constructor_object.md) after doing any requested unit-conversions.

See also:

* [Uniform.sf](Uniform.sf.md)
* [Uniform.cdf](Uniform.cdf.md)
* [Uniform.logsf](Uniform.logsf.md)

Arguments
----------
* `x` (float or array): x-values at which to expose the osf
* `unit` (astropy.unit, optional, default=None): unit of the values
    in `x`.  If None or not provided, will assume they're provided in
    [Uniform.unit](Uniform.unit.md).

Returns
---------
* (float or array) osf values of the same type/shape as `x`

