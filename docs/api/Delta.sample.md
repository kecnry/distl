### [Delta](Delta.md).sample (method)


```py

def sample(self, size=None, unit=None, as_quantity=False)

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

Returns
---------
* float or array: float if `size=None`, otherwise a numpy array with
    shape defined by `size`.

