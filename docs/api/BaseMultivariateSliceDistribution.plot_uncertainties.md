### [BaseMultivariateSliceDistribution](BaseMultivariateSliceDistribution.md).plot_uncertainties (function)


```py

def plot_uncertainties(self, sigma=1, unit=None, show=False, **kwargs)

```



Plot uncertainties as vertical lines and as a latex representation in
the axes title.

See also:

* [BaseMultivariateSliceDistribution.uncertainties](BaseMultivariateSliceDistribution.uncertainties.md)
* [BaseMultivariateSliceDistribution.plot](BaseMultivariateSliceDistribution.plot.md)
* [BaseMultivariateSliceDistribution.plot_sample](BaseMultivariateSliceDistribution.plot_sample.md)
* [BaseMultivariateSliceDistribution.plot_pdf](BaseMultivariateSliceDistribution.plot_pdf.md)
* [BaseMultivariateSliceDistribution.plot_cdf](BaseMultivariateSliceDistribution.plot_cdf.md)
* [BaseMultivariateSliceDistribution.plot_gaussian](BaseMultivariateSliceDistribution.plot_gaussian.md)

Arguments
------------
* `sigma` (int, optional, default=1): sigma to use for uncertainties,
    passed directly to [BaseMultivariateSliceDistribution.uncertainties](BaseMultivariateSliceDistribution.uncertainties.md)
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

