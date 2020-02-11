### [Histogram](Histogram.md).interval (method)


```py

def interval(self, alpha, unit=None, as_quantity=False, wrap_at=None)

```



Expose the range that contains alpha percent of the distribution.

See [scipy docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.interval.html)

This method is just a wrapper around the scipy.stats method on
[Histogram.dist_constructor_object](Histogram.dist_constructor_object.md) with unit-conversions, support for
quantity objects, and wrapping done on the returned result.

Arguments
----------
* `alpha` (float): passed directly to scipy (see link above)
* `unit` (astropy.unit, optional, default=None): unit of the values
    in `x` to expose.  If None or not provided, will assume they're in
    [Histogram.unit](Histogram.unit.md).
* `as_quantity` (bool, optional, default=False): whether to return an
    astropy quantity object instead of just the value.  Astropy must
    be installed.
* `wrap_at` (float, None, or False, optional, default=None): value to
    use for wrapping.  See [Histogram.wrap](Histogram.wrap.md).  If not provided or None,
    will use the value from [Histogram.wrap_at](Histogram.wrap_at.md).  Note: wrapping is
    computed before changing units, so `wrap_at` must be provided
    according to [Histogram.unit](Histogram.unit.md) not `unit`.

Returns
---------
* (array) endpoints in units `unit`.

