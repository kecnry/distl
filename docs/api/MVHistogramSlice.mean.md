### [MVHistogramSlice](MVHistogramSlice.md).mean (method)


```py

def mean(self, unit=None, as_quantity=False, wrap_at=None)

```



Expose the mean of the distribution.

See [scipy docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.mean.html)

This method is just a wrapper around the scipy.stats method on
[MVHistogramSlice.dist_constructor_object](MVHistogramSlice.dist_constructor_object.md) with unit-conversions, support for
quantity objects, and wrapping done on the returned result.

See also:
* [MVHistogramSlice.median](MVHistogramSlice.median.md)
* [MVHistogramSlice.var](MVHistogramSlice.var.md)
* [MVHistogramSlice.std](MVHistogramSlice.std.md)

Arguments
----------
* `unit` (astropy.unit, optional, default=None): unit of the values
    in `x` to expose.  If None or not provided, will assume they're in
    [MVHistogramSlice.unit](MVHistogramSlice.unit.md).
* `as_quantity` (bool, optional, default=False): whether to return an
    astropy quantity object instead of just the value.  Astropy must
    be installed.
* `wrap_at` (float, None, or False, optional, default=None): value to
    use for wrapping.  See [MVHistogramSlice.wrap](MVHistogramSlice.wrap.md).  If not provided or None,
    will use the value from [MVHistogramSlice.wrap_at](MVHistogramSlice.wrap_at.md).  Note: wrapping is
    computed before changing units, so `wrap_at` must be provided
    according to [MVHistogramSlice.unit](MVHistogramSlice.unit.md) not `unit`.

Returns
---------
* (float) mean of the distribution in units `unit`.

