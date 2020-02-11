### [Uniform](Uniform.md).pdf (method)


```py

def pdf(self, x, unit=None)

```



Expose the probability density function (pdf) at values of `x`.

See [scipy docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.pdf.html)

This method is just a wrapper around the scipy.stats method on
[Uniform.dist_constructor_object](Uniform.dist_constructor_object.md) after doing any requested unit-conversions.

See also:
* [Uniform.logpdf](Uniform.logpdf.md)
* [Uniform.cdf](Uniform.cdf.md)

Arguments
----------
* `x` (float or array): x-values at which to expose the pdf
* `unit` (astropy.unit, optional, default=None): unit of the values
    in `x`.  If None or not provided, will assume they're provided in
    [Uniform.unit](Uniform.unit.md).

Returns
---------
* (float or array) pdf values of the same type/shape as `x`

