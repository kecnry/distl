### [Gaussian](Gaussian.md).logpdf (function)


```py

def logpdf(self, x, unit=None)

```



Expose the log-probability density function (log of pdf) at values of `x`.

See [scipy docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.logpdf.html)

This method is just a wrapper around the scipy.stats method on
[Gaussian.dist_constructor_object](Gaussian.dist_constructor_object.md) after doing any requested unit-conversions.

See also:
* [Gaussian.pdf](Gaussian.pdf.md)
* [Gaussian.cdf](Gaussian.cdf.md)

Arguments
----------
* `x` (float or array): x-values at which to expose the logpdf
* `unit` (astropy.unit, optional, default=None): unit of the values
    in `x`.  If None or not provided, will assume they're provided in
    [Gaussian.unit](Gaussian.unit.md).

Returns
---------
* (float or array) logpdf values of the same type/shape as `x`

