### [BaseMultivariateDistribution](BaseMultivariateDistribution.md).plot_uncertainties (function)


```py

def plot_uncertainties(self, sigma=1, unit=None, show=False, **kwargs)

```



Plot uncertainties as vertical lines and as a latex representation in
the axes title.

See also:

* [BaseMultivariateDistribution.uncertainties](BaseMultivariateDistribution.uncertainties.md)
* [BaseMultivariateDistribution.plot](BaseMultivariateDistribution.plot.md)
* [BaseMultivariateDistribution.plot_sample](BaseMultivariateDistribution.plot_sample.md)
* [BaseMultivariateDistribution.plot_pdf](BaseMultivariateDistribution.plot_pdf.md)
* [BaseMultivariateDistribution.plot_cdf](BaseMultivariateDistribution.plot_cdf.md)
* [BaseMultivariateDistribution.plot_gaussian](BaseMultivariateDistribution.plot_gaussian.md)

Arguments
------------
* `sigma` (int, optional, default=1): sigma to use for uncertainties,
    passed directly to [BaseMultivariateDistribution.uncertainties](BaseMultivariateDistribution.uncertainties.md)
* `unit` (astropy.unit, optional, default=None): units to use along
    the x-axis.  Astropy must be installed.
* `show` (bool, optional, default=True): whether to show the resulting
    matplotlib figure.
* `**kwargs`: keyword arguments for will be passed on to plt.axvline.

Returns
--------
* the return from the plt.axvline calls.

Raises
--------
* ImportError: if matplotlib dependency is not met.

