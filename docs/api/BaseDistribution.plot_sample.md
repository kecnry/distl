### [BaseDistribution](BaseDistribution.md).plot_sample (method)


```py

def plot_sample(self, size=100000, unit=None, wrap_at=None, label=None, show=False, **kwargs)

```



Plot both a sampled histogram from the distribution.  Requires
matplotlib to be installed.

See also:

* [BaseDistribution.plot](BaseDistribution.plot.md)
* [BaseDistribution.plot_dist](BaseDistribution.plot_dist.md)
* [BaseDistribution.plot_gaussian](BaseDistribution.plot_gaussian.md)

Arguments
-----------
* `size` (int, optional, default=100000): number of points to sample for
    the histogram.  See also [BaseDistribution.sample](BaseDistribution.sample.md).
* `unit` (astropy.unit, optional, default=None): units to use along
    the x-axis.  Astropy must be installed.
* `wrap_at` (float, None, or False, optional, default=None): value to
    use for wrapping.  See [BaseDistribution.wrap](BaseDistribution.wrap.md).  If not provided or None,
    will use the value from [BaseDistribution.wrap_at](BaseDistribution.wrap_at.md).  Note: wrapping is
    computed before changing units, so `wrap_at` must be provided
    according to [BaseDistribution.unit](BaseDistribution.unit.md) not `unit`.
* `label` (string, optional, default=None): override the label on the
    x-axis.  If not provided or None, will use [BaseDistribution.label](BaseDistribution.label.md).  Will
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

