### [MVGaussianSlice](MVGaussianSlice.md).ppf (function)


```py

def ppf(self, q)

```



Expose the percent point function (ppf; iverse of cdf - percentiles) at
values of `q`.

See [scipy docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.ppf.html)

This method is just a wrapper around the scipy.stats method on
[MVGaussianSlice.dist_constructor_object](MVGaussianSlice.dist_constructor_object.md) with unit-conversions, support for
quantity objects, and wrapping done on the returned result.

See also:
* [MVGaussianSlice.pdf](MVGaussianSlice.pdf.md)
* [MVGaussianSlice.cdf](MVGaussianSlice.cdf.md)
* [MVGaussianSlice.sample](MVGaussianSlice.sample.md)

Arguments
----------
* `q` (float or array): percentiles at which to expose the ppf
* `unit` (astropy.unit, optional, default=None): unit of the exposed
    values.  If None or not provided, will assume they're provided in
    [MVGaussianSlice.unit](MVGaussianSlice.unit.md).
* `as_quantity` (bool, optional, default=False): whether to return an
    astropy quantity object instead of just the value.  Astropy must
    be installed.
* `wrap_at` (float, None, or False, optional, default=None): value to
    use for wrapping.  See [MVGaussianSlice.wrap](MVGaussianSlice.wrap.md).  If not provided or None,
    will use the value from [MVGaussianSlice.wrap_at](MVGaussianSlice.wrap_at.md).  Note: wrapping is
    computed before changing units, so `wrap_at` must be provided
    according to [MVGaussianSlice.unit](MVGaussianSlice.unit.md) not `unit`.

Returns
---------
* (float or array) ppf values of the same type/shape as `x`

