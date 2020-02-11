### [MVGaussianSlice](MVGaussianSlice.md).logsf (method)


```py

def logsf(self, x, unit=None)

```



Expose the log of the survival function (logsf).

See [scipy docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.logsf.html)

This method is just a wrapper around the scipy.stats method on
[MVGaussianSlice.dist_constructor_object](MVGaussianSlice.dist_constructor_object.md) after doing any requested unit-conversions.

See also:

* [MVGaussianSlice.sf](MVGaussianSlice.sf.md)
* [MVGaussianSlice.cdf](MVGaussianSlice.cdf.md)
* [MVGaussianSlice.isf](MVGaussianSlice.isf.md)

Arguments
----------
* `x` (float or array): x-values at which to expose the logsf
* `unit` (astropy.unit, optional, default=None): unit of the values
    in `x`.  If None or not provided, will assume they're provided in
    [MVGaussianSlice.unit](MVGaussianSlice.unit.md).

Returns
---------
* (float or array) logsf values of the same type/shape as `x`

