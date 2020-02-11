### [MVGaussianSlice](MVGaussianSlice.md).cdf (method)


```py

def cdf(self, x, unit=None)

```



Expose the cummulative density function (cdf) at values of `x`.

See [scipy docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.cdf.html)

This method is just a wrapper around the scipy.stats method on
[MVGaussianSlice.dist_constructor_object](MVGaussianSlice.dist_constructor_object.md) after doing any requested unit-conversions.

See also:
* [MVGaussianSlice.logcdf](MVGaussianSlice.logcdf.md)
* [MVGaussianSlice.pdf](MVGaussianSlice.pdf.md)

Arguments
----------
* `x` (float or array): x-values at which to expose the cdf
* `unit` (astropy.unit, optional, default=None): unit of the values
    in `x`.  If None or not provided, will assume they're provided in
    [MVGaussianSlice.unit](MVGaussianSlice.unit.md).

Returns
---------
* (float or array) cdf values of the same type/shape as `x`

