### [Function](Function.md).plot (method)


```py

def plot(self, size=100000, unit=None, wrap_at=None, plot_sample=True, plot_sample_kwargs={'color': 'gray'}, plot_dist=True, plot_dist_kwargs={'color': 'red'}, plot_gaussian=False, plot_gaussian_kwargs={'color': 'blue'}, label=None, show=False, **kwargs)

```



Plot both the analytic distribution function as well as a sampled
histogram from the distribution.  Requires matplotlib to be installed.

See also:

* [Function.plot_sample](Function.plot_sample.md)
* [Function.plot_dist](Function.plot_dist.md)
* [Function.plot_gaussian](Function.plot_gaussian.md)

Arguments
-----------
* `size` (int, optional, default=100000): number of points to sample for
    the histogram.  See also [Function.sample](Function.sample.md).
* `unit` (astropy.unit, optional, default=None): units to use along
    the x-axis.  Astropy must be installed.
* `wrap_at` (float, None, or False, optional, default=None): value to
    use for wrapping.  See [Function.wrap](Function.wrap.md).  If not provided or None,
    will use the value from [Function.wrap_at](Function.wrap_at.md).  Note: wrapping is
    computed before changing units, so `wrap_at` must be provided
    according to [Function.unit](Function.unit.md) not `unit`.
* `plot_sample` (bool, optional, default=True): whether to plot the
    histogram from sampling.  See also [Function.plot_sample](Function.plot_sample.md).
* `plot_sample_kwargs` (dict, optional, default={'color': 'gray'}):
    keyword arguments to send to [Function.plot_sample](Function.plot_sample.md).
* `plot_dist` (bool, optional, default=True): whether to plot the
    analytic form of the underlying distribution, if applicable.
    See also [Function.plot_dist](Function.plot_dist.md).
* `plot_dist_kwargs` (dict, optional, default={'color': 'red'}):
    keyword arguments to send to [Function.plot_dist](Function.plot_dist.md).
* `plot_gaussian` (bool, optional, default=False): whether to plot
    a guassian distribution fit to the sample.  Only supported for
    distributions that have [Function.to_gaussian](Function.to_gaussian.md) methods.
* `plot_gaussian_kwargs` (dict, optional, default={'color': 'blue'}):
    keyword arguments to send to [Function.plot_gaussian](Function.plot_gaussian.md).
* `label` (string, optional, default=None): override the label on the
    x-axis.  If not provided or None, will use [Function.label](Function.label.md).  Will
    only be used if `show=True`.
* `show` (bool, optional, default=True): whether to show the resulting
    matplotlib figure.
* `**kwargs`: all keyword arguments (except for `bins`) will be passed
    on to [Function.plot_dist](Function.plot_dist.md) and [Function.plot_gaussian](Function.plot_gaussian.md) and all
    keyword arguments will be passed on to [Function.plot_sample](Function.plot_sample.md).
    Keyword arguments defined in `plot_sample_kwargs`,
    `plot_dist_kwargs`, and `plot_gaussian_kwargs`
    will override the values sent in `kwargs`.

Returns
--------
* tuple: the return values from [Function.plot_sample](Function.plot_sample.md) (or None if
    `plot_sample=False`), [Function.plot_dist](Function.plot_dist.md) (or None if `plot_dist=False`),
    and [Gaussian.plot_dist](Gaussian.plot_dist.md) (or None if `plot_gaussian=False`).

Raises
--------
* ImportError: if matplotlib dependency is not met.

