### [Function](Function.md).sample (function)


```py

def sample(self, size=None, unit=None, as_quantity=False, wrap_at=None, seed={}, cache_sample=True)

```



Sample from the [Function](Function.md) distribution.

Note: if some combinations of [Function.args](Function.args.md) and [Function.kwargs](Function.kwargs.md) raises
an error in [Function.func](Function.func.md), set [Function.vectorized](Function.vectorized.md) to False and those
individual failures will be re-drawn (careful!  this can be slow or
even take forever if the function always fails)

See also:

* [Function.sample_args_kwargs](Function.sample_args_kwargs.md)

Arguments
-----------
* `size` (int or tuple or None, optional, default=None): size/shape of the
    resulting array.
* `unit` (astropy.unit, optional, default=None): unit to convert the
    resulting sample(s).  Astropy must be installed in order to convert
    units.
* `as_quantity` (bool, optional, default=False): whether to return an
    astropy quantity object instead of just the value.  Astropy must
    be installed.
* `wrap_at` (float, None, or False, optional, default=None): value to
    use for wrapping.  See [Function.wrap](Function.wrap.md).  If not provided or None,
    will use the value from [Function.wrap_at](Function.wrap_at.md).  Note: wrapping is
    computed before changing units, so `wrap_at` must be provided
    according to [Function.unit](Function.unit.md) not `unit`.
* `seed` (dict, optional, default={}): seeds (as uniqueid: seed pairs) to
    pass to underlying distributions.
* `cache_sample` (bool, optional, default=True): whether to override the
    existing [Function.cached_sample](Function.cached_sample.md).

Returns
---------
* float or array: float if `size=None`, otherwise a numpy array with
    shape defined by `size`.

