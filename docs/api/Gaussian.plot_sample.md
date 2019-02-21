### [Gaussian](Gaussian.md).plot_sample (method)


```py

def plot_sample(self, size=100000, unit=None, wrap_at=None, label=None, show=False, **kwargs)

```



Plot both a sampled histogram from the distribution.  Requires
matplotlib to be installed.

See also:

* [Gaussian.plot](Gaussian.plot.md)
* [Gaussian.plot_dist](Gaussian.plot_dist.md)
* [Gaussian.plot_gaussian](Gaussian.plot_gaussian.md)

Arguments
-----------
* `size` (int, optional, default=100000): number of points to sample for
    the histogram.  See also [Gaussian.sample](Gaussian.sample.md).
* `unit` (astropy.unit, optional, default=None): units to use along
    the x-axis.  Astropy must be installed.
* `wrap_at` (float, None, or False, optional, default=None): value to
    use for wrapping.  See [Gaussian.wrap](Gaussian.wrap.md).  If not provided or None,
    will use the value from [Gaussian.wrap_at](Gaussian.wrap_at.md).  Note: wrapping is
    computed before changing units, so `wrap_at` must be provided
    according to [Gaussian.unit](Gaussian.unit.md) not `unit`.
* `label` (string, optional, default=None): override the label on the
    x-axis.  If not provided or None, will use [Gaussian.label](Gaussian.label.md).  Will
    only be used if `show=True`.
* `show` (bool, optional, default=True): whether to show the resulting
    matplotlib figure.
* `**kwargs`: all keyword arguments will be passed on to plt.hist.  If
    not provided, `bins` will default to the stored bins for [Histogram](Histogram.md)
    distributions, otherwise will default to 25.

Returns
--------
* the return from plt.hist

Raises
--------
* ImportError: if matplotlib dependency is not met.

