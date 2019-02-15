### [Gaussian](Gaussian.md).plot_sample (method)


```py

def plot_sample(self, size=100000, unit=None, show=False, **kwargs)

```



Plot both a sampled histogram from the distribution.  Requires
matplotlib to be installed.

See also:

* [BaseDistribution.plot](BaseDistribution.plot.md)
* [BaseDistribution.plot_dist](BaseDistribution.plot_dist.md)

Arguments
-----------
* `size` (int, optional, default=100000): number of points to sample for
    the histogram.  See also [BaseDistribution.sample](BaseDistribution.sample.md).
* `unit` (astropy.unit, optional, default=None): units to use along
    the x-axis.  Astropy must be installed.
* `show` (bool, optional, default=True): whether to show the resulting
    matplotlib figure.
* `**kwargs`: all keyword arguments will be passed on to plt.hist.

Returns
--------
* the return from plt.hist

Raises
--------
* ImportError: if matplotlib dependency is not met.

