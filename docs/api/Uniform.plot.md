### [Uniform](Uniform.md).plot (method)


```py

def plot(self, size=100000, unit=None, plot_sample=True, plot_dist=True, plot_gaussian=False, plot_gaussian_kwargs={}, label=None, show=False, **kwargs)

```



Plot both the analytic distribution function as well as a sampled
histogram from the distribution.  Requires matplotlib to be installed.

See also:

* [Uniform.plot_sample](Uniform.plot_sample.md)
* [Uniform.plot_dist](Uniform.plot_dist.md)
* [Uniform.plot_gaussian](Uniform.plot_gaussian.md)

Arguments
-----------
* `size` (int, optional, default=100000): number of points to sample for
    the histogram.  See also [Uniform.sample](Uniform.sample.md).
* `unit` (astropy.unit, optional, default=None): units to use along
    the x-axis.  Astropy must be installed.
* `plot_sample` (bool, optional, default=True): whether to plot the
    histogram from sampling.  See also [Uniform.plot_sample](Uniform.plot_sample.md).
* `plot_dist` (bool, optional, default=True): whether to plot the
    analytic form of the underlying distribution, if applicable.
    See also [Uniform.plot_dist](Uniform.plot_dist.md).
* `plot_gaussian` (bool, optional, default=False): whether to plot
    a guassian distribution fit to the sample.  Only supported for
    distributions that have [Uniform.to_gaussian](Uniform.to_gaussian.md) methods.
* `plot_gaussian_kwargs` (dict, optional, default={}): keyword arguments
    to send to [Uniform.plot_gaussian](Uniform.plot_gaussian.md).
* `label` (string, optional, default=None): override the label on the
    x-axis.  If not provided or None, will use [Uniform.label](Uniform.label.md).  Will
    only be used if `show=True`.
* `show` (bool, optional, default=True): whether to show the resulting
    matplotlib figure.
* `**kwargs`: all keyword arguments (except for `bins`) will be passed
    on to [Uniform.plot_dist](Uniform.plot_dist.md) and all keyword arguments will
    be passed on to [Uniform.plot_sample](Uniform.plot_sample.md).

Returns
--------
* tuple: the return values from [Uniform.plot_sample](Uniform.plot_sample.md) (or None if
    `plot_sample=False`), [Uniform.plot_dist](Uniform.plot_dist.md) (or None if `plot_dist=False`),
    and [Gaussian.plot_dist](Gaussian.plot_dist.md) (or None if `plot_gaussian=False`).

Raises
--------
* ImportError: if matplotlib dependency is not met.

