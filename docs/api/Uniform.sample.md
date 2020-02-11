### [Uniform](Uniform.md).sample (function)


```py

def sample(self, size=None, unit=None, as_quantity=False, wrap_at=None, seed=None, cache_sample=True)

```



Sample from the distribution.

See also:
* [Uniform.pdf](Uniform.pdf.md)
* [Uniform.cdf](Uniform.cdf.md)
* [Uniform.ppf](Uniform.ppf.md)
* [Uniform.plot_sample](Uniform.plot_sample.md)
* [Uniform.plot](Uniform.plot.md)

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
    use for wrapping.  See [Uniform.wrap](Uniform.wrap.md).  If not provided or None,
    will use the value from [Uniform.wrap_at](Uniform.wrap_at.md).  Note: wrapping is
    computed before changing units, so `wrap_at` must be provided
    according to [Uniform.unit](Uniform.unit.md) not `unit`.
* `seed` (int, optional): seed to pass to np.random.seed
    prior to sampling.
* `cache_sample` (bool, optional, default=True): whether to override the
    existing [Uniform.cached_sample](Uniform.cached_sample.md).

Returns
---------
* float or array: float if `size=None`, otherwise a numpy array with
    shape defined by `size`.

