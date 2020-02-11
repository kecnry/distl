### [BaseMultivariateDistribution](BaseMultivariateDistribution.md).plot_cdf (method)


```py

def plot_cdf(self, x=None, unit=None, wrap_at=None, label=None, xlabel=None, show=False, **kwargs)

```



Plot the pdf function.  Requires matplotlib to be installed.

See also:

* [BaseMultivariateDistribution.plot](BaseMultivariateDistribution.plot.md)
* [BaseMultivariateDistribution.plot_pdf](BaseMultivariateDistribution.plot_pdf.md)
* [BaseMultivariateDistribution.plot_sample](BaseMultivariateDistribution.plot_sample.md)
* [BaseMultivariateDistribution.plot_gaussian](BaseMultivariateDistribution.plot_gaussian.md)

Arguments
-----------
* `x` (array, optional, default=None): the numpy array at which to
    sample the value on the x-axis.  If `unit` is not None, the value
    of `x` are assumed to be in the original units [BaseMultivariateDistribution.unit](BaseMultivariateDistribution.unit.md),
    not `unit`.  If not provided or None, `x` will be based to cover
    the 99.9% of all distributions (see [BaseMultivariateDistribution.interval](BaseMultivariateDistribution.interval.md)) with 1000
    points and 10% padding.
* `unit` (astropy.unit, optional, default=None): units to use along
    the x-axis.  Astropy must be installed.
* `wrap_at` (float, None, or False, optional, default=None): value to
    use for wrapping.  See [BaseMultivariateDistribution.wrap](BaseMultivariateDistribution.wrap.md).  If not provided or None,
    will use the value from [BaseMultivariateDistribution.wrap_at](BaseMultivariateDistribution.wrap_at.md).  Note: wrapping is
    computed before changing units, so `wrap_at` must be provided
    according to [BaseMultivariateDistribution.unit](BaseMultivariateDistribution.unit.md) not `unit`.
* `label` (string, optional, default=None): override the label on the
    x-axis.  If not provided or None, will use [BaseMultivariateDistribution.label](BaseMultivariateDistribution.label.md).  Will
    only be used if `show=True`.  Unit will automatically be appended.
    Will be ignored if `xlabel` is provided.
* `xlabel` (string, optional, default=None): override the label on the
    x-axis without appending the unit.  Will override `label`.
* `show` (bool, optional, default=True): whether to show the resulting
    matplotlib figure.
* `**kwargs`: all keyword arguments will be passed on to plt.plot.  Note:
    if wrapping is enabled, either via `wrap_at` or [BaseMultivariateDistribution.wrap_at](BaseMultivariateDistribution.wrap_at.md),
    the resulting line will break when wrapping, resulting in using multiple
    colors.  Sending `color` as a keyword argument will prevent this
    matplotlib behavior.  Calling this through [BaseMultivariateDistribution.plot](BaseMultivariateDistribution.plot.md) with
    `plot_gaussian=True` defaults to sending `color='blue'` through
    the `plot_gaussian_kwargs` argument.

Returns
--------
* the return from plt.plot

Raises
--------
* ImportError: if matplotlib dependency is not met.

