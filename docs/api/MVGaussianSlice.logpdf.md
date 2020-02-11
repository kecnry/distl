### [MVGaussianSlice](MVGaussianSlice.md).logpdf (function)


```py

def logpdf(self, x=None, unit=None)

```



Expose the log-probability density function (log of pdf) at values of `x`.

See [scipy docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.logpdf.html)

This method is just a wrapper around the scipy.stats method on
[MVGaussianSlice.dist_constructor_object](MVGaussianSlice.dist_constructor_object.md) after doing any requested unit-conversions.

See also:
* [MVGaussianSlice.pdf](MVGaussianSlice.pdf.md)
* [MVGaussianSlice.cdf](MVGaussianSlice.cdf.md)

Arguments
----------
* `x` (float or array, optional, default=None): x-values at which to
    expose the logpdf.  If None or not provided, [MVGaussianSlice.cached_sample](MVGaussianSlice.cached_sample.md)
    will be used if available, or raise an error if no cached samples
    are available.
* `unit` (astropy.unit, optional, default=None): unit of the values
    in `x`.  If None or not provided, will assume they're provided in
    [MVGaussianSlice.unit](MVGaussianSlice.unit.md).

Returns
---------
* (float or array) logpdf values of the same type/shape as `x`

