### [Histogram](Histogram.md).plot (method)


```py

def plot(self, size=100000, unit=None, plot_sample=True, plot_dist=True, label=None, show=False, **kwargs)

```



Plot both the analytic distribution function as well as a sampled
histogram from the distribution.  Requires matplotlib to be installed.

See also:

* [BaseDistribution.plot_sample](BaseDistribution.plot_sample.md)
* [BaseDistribution.plot_dist](BaseDistribution.plot_dist.md)

Arguments
-----------
* `size` (int, optional, default=100000): number of points to sample for
    the histogram.  See also [BaseDistribution.sample](BaseDistribution.sample.md).
* `unit` (astropy.unit, optional, default=None): units to use along
    the x-axis.  Astropy must be installed.
* `plot_sample` (bool, optional, default=True): whether to plot the
    histogram from sampling.  See also [BaseDistribution.plot_sample](BaseDistribution.plot_sample.md).
* `plot_dist` (bool, optional, default=True): whether to plot the
    analytic form of the underlying distribution, if applicable.
    See also [BaseDistribution.plot_dist](BaseDistribution.plot_dist.md).
* `label` (string, optional, default=None): override the label on the
    x-axis.  If not provided or None, will use [BaseDistribution.label](BaseDistribution.label.md).
* `show` (bool, optional, default=True): whether to show the resulting
    matplotlib figure.
* `**kwargs`: all keyword arguments (except for `bins`) will be passed
    on to [BaseDistribution.plot_dist](BaseDistribution.plot_dist.md) and all keyword arguments will
    be passed on to [BaseDistribution.plot_sample](BaseDistribution.plot_sample.md).

Returns
--------
* tuple: the return values from both [BaseDistribution.plot_sample](BaseDistribution.plot_sample.md) and
    [BaseDistribution.plot_dist](BaseDistribution.plot_dist.md).

Raises
--------
* ImportError: if matplotlib dependency is not met.

