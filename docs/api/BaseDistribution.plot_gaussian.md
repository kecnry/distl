### [BaseDistribution](BaseDistribution.md).plot_gaussian (method)


```py

def plot_gaussian(self, x=None, unit=None, wrap_at=None, label=None, xlabel=None, show=False, **kwargs)

```



Plot the gaussian distribution that would result from calling
[BaseDistribution.to_gaussian](BaseDistribution.to_gaussian.md) with the same arguments.

Note that for distributions in which [BaseDistribution.to_gaussian](BaseDistribution.to_gaussian.md) calls
[BaseDistribution.to_histogram](BaseDistribution.to_histogram.md) under-the-hood, this could result in slightly
different distributions for each call.

See also:

* [BaseDistribution.plot](BaseDistribution.plot.md)
* [BaseDistribution.plot_sample](BaseDistribution.plot_sample.md)
* [BaseDistribution.plot_pdf](BaseDistribution.plot_pdf.md)
* [BaseDistribution.plot_cdf](BaseDistribution.plot_cdf.md)

Arguments
-----------
* `x` (array, optional, default=None): the numpy array at which to
    sample the value on the x-axis.  If `unit` is not None, the value
    of `x` are assumed to be in the original units [BaseDistribution.unit](BaseDistribution.unit.md),
    not `unit`.  If not provided or None, `x` will be based to cover
    the 99.9% of all distributions (see [BaseDistribution.interval](BaseDistribution.interval.md)) with 1000
    points and 10% padding.
* `unit` (astropy.unit, optional, default=None): units to use along
    the x-axis.  Astropy must be installed.
* `wrap_at` (float, None, or False, optional, default=None): value to
    use for wrapping.  See [BaseDistribution.wrap](BaseDistribution.wrap.md).  If not provided or None,
    will use the value from [BaseDistribution.wrap_at](BaseDistribution.wrap_at.md).  Note: wrapping is
    computed before changing units, so `wrap_at` must be provided
    according to [BaseDistribution.unit](BaseDistribution.unit.md) not `unit`.
* `label` (string, optional, default=None): override the label on the
    x-axis.  If not provided or None, will use [BaseDistribution.label](BaseDistribution.label.md).  Will
    only be used if `show=True`.  Unit will automatically be appended.
    Will be ignored if `xlabel` is provided.
* `xlabel` (string, optional, default=None): override the label on the
    x-axis without appending the unit.  Will override `label`.
* `show` (bool, optional, default=True): whether to show the resulting
    matplotlib figure.
* `**kwargs`: keyword arguments for `sigma`, `N`, `bins`, `range` will
    be passed on to [BaseDistribution.to_gaussian](BaseDistribution.to_gaussian.md) (must be accepted by the
    given distribution type).  All other keyword arguments will be passed
    on to [Gaussian.plot_pdf](Gaussian.plot_pdf.md) on the resulting distribution.

Returns
--------
* the return from plt.plot

Raises
--------
* ImportError: if matplotlib dependency is not met.

