### [BaseMultivariateDistribution](BaseMultivariateDistribution.md).plot_sample (function)


```py

def plot_sample(self, **kwargs)

```



Plot both a sampled histogram from the distribution.  Requires
matplotlib to be installed.

See also:

* [BaseMultivariateDistribution.plot](BaseMultivariateDistribution.plot.md)
* [BaseMultivariateDistribution.plot_pdf](BaseMultivariateDistribution.plot_pdf.md)
* [BaseMultivariateDistribution.plot_cdf](BaseMultivariateDistribution.plot_cdf.md)
* [BaseMultivariateDistribution.plot_gaussian](BaseMultivariateDistribution.plot_gaussian.md)

Arguments
-----------
* `size` (int, optional, default=1e5): number of points to sample for
    the histogram.  See also [BaseMultivariateDistribution.sample](BaseMultivariateDistribution.sample.md).  Will be ignored
    if `samples` is provided.
* `unit` (astropy.unit, optional, default=None): units to use along
    the x-axis.  Astropy must be installed.  If `samples` is provided,
    the passed values will be assumed to be in the correct units.
* `wrap_at` (float, None, or False, optional, default=None): value to
    use for wrapping.  See [BaseMultivariateDistribution.wrap](BaseMultivariateDistribution.wrap.md).  If not provided or None,
    will use the value from [BaseMultivariateDistribution.wrap_at](BaseMultivariateDistribution.wrap_at.md).  Note: wrapping is
    computed before changing units, so `wrap_at` must be provided
    according to [BaseMultivariateDistribution.unit](BaseMultivariateDistribution.unit.md) not `unit`.  Will be ignored
    if `samples` is provided.
* `seed` (int, optional): seed to use when sampling.  See also
    [BaseMultivariateDistribution.sample](BaseMultivariateDistribution.sample.md).  Will be ignored if `samples` is provided.
* `samples` (array, optional, default=None): plot specific sampled
    values instead of calling [BaseMultivariateDistribution.sample](BaseMultivariateDistribution.sample.md) internally.  Will override
    `size`.
* `label` (string, optional, default=None): override the label on the
    x-axis.  If not provided or None, will use [BaseMultivariateDistribution.label](BaseMultivariateDistribution.label.md).  Will
    only be used if `show=True`.  Unit will automatically be appended.
    Will be ignored if `xlabel` is provided.
* `xlabel` (string, optional, default=None): override the label on the
    x-axis without appending the unit.  Will override `label`.
* `show` (bool, optional, default=True): whether to show the resulting
    matplotlib figure.
* `**kwargs`: all keyword arguments will be passed on to plt.hist.  If
    not provided, `bins` will default to the stored bins for [Histogram](Histogram.md)
    distributions, otherwise will default to 25.

Returns
--------
* the return from plt.hist

Raises
--------
* ImportError: if matplotlib dependency is not met.

