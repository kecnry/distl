### [Composite](Composite.md).plot_gaussian (function)


```py

def plot_gaussian(self, x=None, unit=None, wrap_at=None, label=None, show=False, **kwargs)

```



Plot the gaussian distribution that would result from calling
[Composite.to_gaussian](Composite.to_gaussian.md) with the same arguments.

Note that for distributions in which [Composite.to_gaussian](Composite.to_gaussian.md) calls
[Composite.to_histogram](Composite.to_histogram.md) under-the-hood, this could result in slightly
different distributions for each call.

See also:

* [Composite.plot](Composite.plot.md)
* [Composite.plot_sample](Composite.plot_sample.md)
* [Composite.plot_pdf](Composite.plot_pdf.md)
* [Composite.plot_cdf](Composite.plot_cdf.md)

Arguments
-----------
* `x` (array, optional, default=None): the numpy array at which to
    sample the value on the x-axis.  If `unit` is not None, the value
    of `x` are assumed to be in the original units [Composite.unit](Composite.unit.md),
    not `unit`.  If not provided or None, `x` will be based to cover
    the 99.9% of all distributions (see [Composite.interval](Composite.interval.md)) with 1000
    points and 10% padding.
* `unit` (astropy.unit, optional, default=None): units to use along
    the x-axis.  Astropy must be installed.
* `wrap_at` (float, None, or False, optional, default=None): value to
    use for wrapping.  See [Composite.wrap](Composite.wrap.md).  If not provided or None,
    will use the value from [Composite.wrap_at](Composite.wrap_at.md).  Note: wrapping is
    computed before changing units, so `wrap_at` must be provided
    according to [Composite.unit](Composite.unit.md) not `unit`.
* `label` (string, optional, default=None): override the label on the
    x-axis.  If not provided or None, will use [Composite.label](Composite.label.md).  Will
    only be used if `show=True`.
* `show` (bool, optional, default=True): whether to show the resulting
    matplotlib figure.
* `**kwargs`: keyword arguments for `sigma`, `N`, `bins`, `range` will
    be passed on to [Composite.to_gaussian](Composite.to_gaussian.md) (must be accepted by the
    given distribution type).  All other keyword arguments will be passed
    on to [Gaussian.plot_pdf](Gaussian.plot_pdf.md) on the resulting distribution.

Returns
--------
* the return from plt.plot

Raises
--------
* ImportError: if matplotlib dependency is not met.

