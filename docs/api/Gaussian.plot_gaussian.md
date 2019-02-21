### [Gaussian](Gaussian.md).plot_gaussian (method)


```py

def plot_gaussian(self, x, unit=None, label=None, show=False, **kwargs)

```



Plot the gaussian distribution that would result from calling
[Gaussian.to_gaussian](Gaussian.to_gaussian.md) with the same arguments.

Note that for distributions in which [Gaussian.to_gaussian](Gaussian.to_gaussian.md) calls
[Gaussian.to_histogram](Gaussian.to_histogram.md) under-the-hood, this could result in slightly
different distributions for each call.

See also:

* [Gaussian.plot](Gaussian.plot.md)
* [Gaussian.plot_sample](Gaussian.plot_sample.md)
* [Gaussian.plot_dist](Gaussian.plot_dist.md)

Arguments
-----------
* `x` (np array): the numpy array at which to sample the value on the
    x-axis.
* `unit` (astropy.unit, optional, default=None): units to use along
    the x-axis.  Astropy must be installed.
* `label` (string, optional, default=None): override the label on the
    x-axis.  If not provided or None, will use [Gaussian.label](Gaussian.label.md).  Will
    only be used if `show=True`.
* `show` (bool, optional, default=True): whether to show the resulting
    matplotlib figure.
* `**kwargs`: keyword arguments for `sigma`, `N`, `bins`, `range` will
    be passed on to [Gaussian.to_gaussian](Gaussian.to_gaussian.md) (must be accepted by the
    given distribution type).  All other keyword arguments will be passed
    on to [Gaussian.plot_dist](Gaussian.plot_dist.md) on the resulting distribution.

Returns
--------
* the return from plt.plot

Raises
--------
* ImportError: if matplotlib dependency is not met.

