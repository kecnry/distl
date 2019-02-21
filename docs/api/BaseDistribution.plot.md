### [BaseDistribution](BaseDistribution.md).plot (method)


```py

def plot(self, size=100000, unit=None, plot_sample=True, plot_dist=True, plot_gaussian=False, plot_gaussian_kwargs={}, label=None, show=False, **kwargs)

```



Plot both the analytic distribution function as well as a sampled
histogram from the distribution.  Requires matplotlib to be installed.

See also:

* [BaseDistribution.plot_sample](BaseDistribution.plot_sample.md)
* [BaseDistribution.plot_dist](BaseDistribution.plot_dist.md)
* [BaseDistribution.plot_gaussian](BaseDistribution.plot_gaussian.md)

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
* `plot_gaussian` (bool, optional, default=False): whether to plot
    a guassian distribution fit to the sample.  Only supported for
    distributions that have [BaseDistribution.to_gaussian](BaseDistribution.to_gaussian.md) methods.
* `plot_gaussian_kwargs` (dict, optional, default={}): keyword arguments
    to send to [BaseDistribution.plot_gaussian](BaseDistribution.plot_gaussian.md).
* `label` (string, optional, default=None): override the label on the
    x-axis.  If not provided or None, will use [BaseDistribution.label](BaseDistribution.label.md).  Will
    only be used if `show=True`.
* `show` (bool, optional, default=True): whether to show the resulting
    matplotlib figure.
* `**kwargs`: all keyword arguments (except for `bins`) will be passed
    on to [BaseDistribution.plot_dist](BaseDistribution.plot_dist.md) and all keyword arguments will
    be passed on to [BaseDistribution.plot_sample](BaseDistribution.plot_sample.md).

Returns
--------
* tuple: the return values from [BaseDistribution.plot_sample](BaseDistribution.plot_sample.md) (or None if
    `plot_sample=False`), [BaseDistribution.plot_dist](BaseDistribution.plot_dist.md) (or None if `plot_dist=False`),
    and [Gaussian.plot_dist](Gaussian.plot_dist.md) (or None if `plot_gaussian=False`).

Raises
--------
* ImportError: if matplotlib dependency is not met.

