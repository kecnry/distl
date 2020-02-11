### [Gaussian](Gaussian.md).sample (function)


```py

def sample(self, size=None, unit=None, as_quantity=False, wrap_at=None, seed=None, cache_sample=True)

```



Sample from the distribution.

See also:
* [Gaussian.pdf](Gaussian.pdf.md)
* [Gaussian.cdf](Gaussian.cdf.md)
* [Gaussian.ppf](Gaussian.ppf.md)
* [Gaussian.plot_sample](Gaussian.plot_sample.md)
* [Gaussian.plot](Gaussian.plot.md)

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
    use for wrapping.  See [Gaussian.wrap](Gaussian.wrap.md).  If not provided or None,
    will use the value from [Gaussian.wrap_at](Gaussian.wrap_at.md).  Note: wrapping is
    computed before changing units, so `wrap_at` must be provided
    according to [Gaussian.unit](Gaussian.unit.md) not `unit`.
* `seed` (int, optional): seed to pass to np.random.seed
    prior to sampling.
* `cache_sample` (bool, optional, default=True): whether to override the
    existing [Gaussian.cached_sample](Gaussian.cached_sample.md).

Returns
---------
* float or array: float if `size=None`, otherwise a numpy array with
    shape defined by `size`.

