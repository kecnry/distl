### [Samples](Samples.md).mean (function)


```py

def mean(self, unit=None, as_quantity=False, wrap_at=None)

```



Expose the mean of the [Samples.samples](Samples.samples.md) given the [Samples.weights](Samples.weights.md)

Under-the-hood this uses numpy.average (as numpy.mean does not support weights)

See also:

* [Samples.median](Samples.median.md)
* [Samples.var](Samples.var.md)
* [Samples.std](Samples.std.md)

Arguments
----------
* `unit` (astropy.unit, optional, default=None): unit of the values
    in `x` to expose.  If None or not provided, will assume they're in
    [Samples.unit](Samples.unit.md).
* `as_quantity` (bool, optional, default=False): whether to return an
    astropy quantity object instead of just the value.  Astropy must
    be installed.
* `wrap_at` (float, None, or False, optional, default=None): value to
    use for wrapping.  See [Samples.wrap](Samples.wrap.md).  If not provided or None,
    will use the value from [Samples.wrap_at](Samples.wrap_at.md).  Note: wrapping is
    computed before changing units, so `wrap_at` must be provided
    according to [Samples.unit](Samples.unit.md) not `unit`.

Returns
---------
* (float) mean of the distribution in units `unit`.

