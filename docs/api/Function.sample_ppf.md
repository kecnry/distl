### [Function](Function.md).sample_ppf (method)


```py

def sample_ppf(self, ppf, unit=None, as_quantity=False, wrap_at=None)

```



Sample the distribution by mapping a given percent point function or ppf
(a value between [0, 1)).

Arguments
------------
* `ppf` (float or array of floats): ppf value(s) with values in the range
    [0, 1).
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

Returns
-----------
* float or array: float or array depending on the input of `ppf`.

