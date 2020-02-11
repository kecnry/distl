### [Composite](Composite.md).sample (function)


```py

def sample(self, size=None, unit=None, as_quantity=False, wrap_at=None, seed={}, cache_sample=True)

```



Sample from the distribution.

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
    use for wrapping.  See [Composite.wrap](Composite.wrap.md).  If not provided or None,
    will use the value from [Composite.wrap_at](Composite.wrap_at.md).  Note: wrapping is
    computed before changing units, so `wrap_at` must be provided
    according to [Composite.unit](Composite.unit.md) not `unit`.
* `seed` (dict, optional, default={}): seeds (as hash: seed pairs) to
    pass to underlying distributions.
* `cache_sample` (bool, optional, default=True): whether to override the
    existing [Composite.cached_sample](Composite.cached_sample.md).

Returns
---------
* float or array: float if `size=None`, otherwise a numpy array with
    shape defined by `size`.

