### [BaseDistribution](BaseDistribution.md).plot_gaussian (method)


```py

def plot_gaussian(self, x, unit=None, label=None, show=False, **kwargs)

```



Plot the gaussian distribution that would result from calling
[BaseDistribution.to_gaussian](BaseDistribution.to_gaussian.md) with the same arguments.

Note that for distributions in which [BaseDistribution.to_gaussian](BaseDistribution.to_gaussian.md) calls
[BaseDistribution.to_histogram](BaseDistribution.to_histogram.md) under-the-hood, this could result in slightly
different distributions for each call.

See also:

* [BaseDistribution.plot](BaseDistribution.plot.md)
* [BaseDistribution.plot_sample](BaseDistribution.plot_sample.md)
* [BaseDistribution.plot_dist](BaseDistribution.plot_dist.md)

Arguments
-----------
* `x` (np array): the numpy array at which to sample the value on the
    x-axis.
* `unit` (astropy.unit, optional, default=None): units to use along
    the x-axis.  Astropy must be installed.
* `label` (string, optional, default=None): override the label on the
    x-axis.  If not provided or None, will use [BaseDistribution.label](BaseDistribution.label.md).  Will
    only be used if `show=True`.
* `show` (bool, optional, default=True): whether to show the resulting
    matplotlib figure.
* `**kwargs`: keyword arguments for `sigma`, `N`, `bins`, `range` will
    be passed on to [BaseDistribution.to_gaussian](BaseDistribution.to_gaussian.md) (must be accepted by the
    given distribution type).  All other keyword arguments will be passed
    on to [Gaussian.plot_dist](Gaussian.plot_dist.md) on the resulting distribution.

Returns
--------
* the return from plt.plot

Raises
--------
* ImportError: if matplotlib dependency is not met.

