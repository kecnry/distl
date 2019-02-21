### [Histogram](Histogram.md).plot_gaussian (method)


```py

def plot_gaussian(self, x, unit=None, label=None, show=False, **kwargs)

```



Plot the gaussian distribution that would result from calling
[Histogram.to_gaussian](Histogram.to_gaussian.md) with the same arguments.

Note that for distributions in which [Histogram.to_gaussian](Histogram.to_gaussian.md) calls
[Histogram.to_histogram](Histogram.to_histogram.md) under-the-hood, this could result in slightly
different distributions for each call.

See also:

* [Histogram.plot](Histogram.plot.md)
* [Histogram.plot_sample](Histogram.plot_sample.md)
* [Histogram.plot_dist](Histogram.plot_dist.md)

Arguments
-----------
* `x` (np array): the numpy array at which to sample the value on the
    x-axis.
* `unit` (astropy.unit, optional, default=None): units to use along
    the x-axis.  Astropy must be installed.
* `label` (string, optional, default=None): override the label on the
    x-axis.  If not provided or None, will use [Histogram.label](Histogram.label.md).  Will
    only be used if `show=True`.
* `show` (bool, optional, default=True): whether to show the resulting
    matplotlib figure.
* `**kwargs`: keyword arguments for `sigma`, `N`, `bins`, `range` will
    be passed on to [Histogram.to_gaussian](Histogram.to_gaussian.md) (must be accepted by the
    given distribution type).  All other keyword arguments will be passed
    on to [Gaussian.plot_dist](Gaussian.plot_dist.md) on the resulting distribution.

Returns
--------
* the return from plt.plot

Raises
--------
* ImportError: if matplotlib dependency is not met.

