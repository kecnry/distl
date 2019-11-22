### [BaseMultivariateDistribution](BaseMultivariateDistribution.md).plot_gaussian (method)


```py

def plot_gaussian(self, x, unit=None, wrap_at=None, label=None, show=False, **kwargs)

```



Plot the gaussian distribution that would result from calling
[BaseMultivariateDistribution.to_gaussian](BaseMultivariateDistribution.to_gaussian.md) with the same arguments.

Note that for distributions in which [BaseMultivariateDistribution.to_gaussian](BaseMultivariateDistribution.to_gaussian.md) calls
[BaseMultivariateDistribution.to_histogram](BaseMultivariateDistribution.to_histogram.md) under-the-hood, this could result in slightly
different distributions for each call.

See also:

* [BaseMultivariateDistribution.plot](BaseMultivariateDistribution.plot.md)
* [BaseMultivariateDistribution.plot_sample](BaseMultivariateDistribution.plot_sample.md)
* [BaseMultivariateDistribution.plot_dist](BaseMultivariateDistribution.plot_dist.md)

Arguments
-----------
* `x` (np array): the numpy array at which to sample the value on the
    x-axis. If `unit` is not None, the value of `x` are assumed to be
    in the original units [BaseMultivariateDistribution.unit](BaseMultivariateDistribution.unit.md), not `unit`.
* `unit` (astropy.unit, optional, default=None): units to use along
    the x-axis.  Astropy must be installed.
* `wrap_at` (float, None, or False, optional, default=None): value to
    use for wrapping.  See [BaseMultivariateDistribution.wrap](BaseMultivariateDistribution.wrap.md).  If not provided or None,
    will use the value from [BaseMultivariateDistribution.wrap_at](BaseMultivariateDistribution.wrap_at.md).  Note: wrapping is
    computed before changing units, so `wrap_at` must be provided
    according to [BaseMultivariateDistribution.unit](BaseMultivariateDistribution.unit.md) not `unit`.
* `label` (string, optional, default=None): override the label on the
    x-axis.  If not provided or None, will use [BaseMultivariateDistribution.label](BaseMultivariateDistribution.label.md).  Will
    only be used if `show=True`.
* `show` (bool, optional, default=True): whether to show the resulting
    matplotlib figure.
* `**kwargs`: keyword arguments for `sigma`, `N`, `bins`, `range` will
    be passed on to [BaseMultivariateDistribution.to_gaussian](BaseMultivariateDistribution.to_gaussian.md) (must be accepted by the
    given distribution type).  All other keyword arguments will be passed
    on to [Gaussian.plot_dist](Gaussian.plot_dist.md) on the resulting distribution.

Returns
--------
* the return from plt.plot

Raises
--------
* ImportError: if matplotlib dependency is not met.

