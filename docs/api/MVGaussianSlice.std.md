### [MVGaussianSlice](MVGaussianSlice.md).std (function)


```py

def std(self, unit=None, as_quantity=False, wrap_at=None)

```



Expose the standard deviation of the distribution.

See [scipy docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.std.html)

This method is just a wrapper around the scipy.stats method on
[MVGaussianSlice.dist_constructor_object](MVGaussianSlice.dist_constructor_object.md) with unit-conversions, support for
quantity objects, and wrapping done on the returned result.

See also:

* [MVGaussianSlice.median](MVGaussianSlice.median.md)
* [MVGaussianSlice.mean](MVGaussianSlice.mean.md)
* [MVGaussianSlice.var](MVGaussianSlice.var.md)

Arguments
----------
* `unit` (astropy.unit, optional, default=None): unit of the values
    in `x` to expose.  If None or not provided, will assume they're in
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
* (float) standard deviation of the distribution in units `unit`.

