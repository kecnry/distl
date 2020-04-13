### [Samples](Samples.md).sample (function)


```py

def sample(self, size=None, unit=None, as_quantity=False, wrap_at=None, seed=None, cache_sample=True)

```



Sample from the samples [Samples.samples](Samples.samples.md) given [Samples.weights](Samples.weights.md).

Under-the-hood this calls numpy.random.choice with `replace=True`.

See also:

* [Samples.pdf](Samples.pdf.md)
* [Samples.cdf](Samples.cdf.md)
* [Samples.ppf](Samples.ppf.md)
* [Samples.plot_sample](Samples.plot_sample.md)
* [Samples.plot](Samples.plot.md)

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
    use for wrapping.  See [Samples.wrap](Samples.wrap.md).  If not provided or None,
    will use the value from [Samples.wrap_at](Samples.wrap_at.md).  Note: wrapping is
    computed before changing units, so `wrap_at` must be provided
    according to [Samples.unit](Samples.unit.md) not `unit`.
* `seed` (int, optional): seed to pass to np.random.seed
    prior to sampling.
* `cache_sample` (bool, optional, default=True): whether to override the
    existing [Samples.cached_sample](Samples.cached_sample.md).

Returns
---------
* float or array: float if `size=None`, otherwise a numpy array with
    shape defined by `size`.

