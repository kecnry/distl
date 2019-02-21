### [Uniform](Uniform.md).plot_gaussian (method)


```py

def plot_gaussian(self, x, unit=None, label=None, show=False, **kwargs)

```



Plot the gaussian distribution that would result from calling
[Uniform.to_gaussian](Uniform.to_gaussian.md) with the same arguments.

Note that for distributions in which [Uniform.to_gaussian](Uniform.to_gaussian.md) calls
[Uniform.to_histogram](Uniform.to_histogram.md) under-the-hood, this could result in slightly
different distributions for each call.

See also:

* [Uniform.plot](Uniform.plot.md)
* [Uniform.plot_sample](Uniform.plot_sample.md)
* [Uniform.plot_dist](Uniform.plot_dist.md)

Arguments
-----------
* `x` (np array): the numpy array at which to sample the value on the
    x-axis.
* `unit` (astropy.unit, optional, default=None): units to use along
    the x-axis.  Astropy must be installed.
* `label` (string, optional, default=None): override the label on the
    x-axis.  If not provided or None, will use [Uniform.label](Uniform.label.md).  Will
    only be used if `show=True`.
* `show` (bool, optional, default=True): whether to show the resulting
    matplotlib figure.
* `**kwargs`: keyword arguments for `sigma`, `N`, `bins`, `range` will
    be passed on to [Uniform.to_gaussian](Uniform.to_gaussian.md) (must be accepted by the
    given distribution type).  All other keyword arguments will be passed
    on to [Gaussian.plot_dist](Gaussian.plot_dist.md) on the resulting distribution.

Returns
--------
* the return from plt.plot

Raises
--------
* ImportError: if matplotlib dependency is not met.

