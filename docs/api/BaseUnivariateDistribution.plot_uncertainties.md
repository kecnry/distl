### [BaseUnivariateDistribution](BaseUnivariateDistribution.md).plot_uncertainties (function)


```py

def plot_uncertainties(self, sigma=1, unit=None, show=False, **kwargs)

```



Plot uncertainties as vertical lines and as a latex representation in
the axes title.

See also:

* [BaseUnivariateDistribution.uncertainties](BaseUnivariateDistribution.uncertainties.md)
* [BaseUnivariateDistribution.plot](BaseUnivariateDistribution.plot.md)
* [BaseUnivariateDistribution.plot_sample](BaseUnivariateDistribution.plot_sample.md)
* [BaseUnivariateDistribution.plot_pdf](BaseUnivariateDistribution.plot_pdf.md)
* [BaseUnivariateDistribution.plot_cdf](BaseUnivariateDistribution.plot_cdf.md)
* [BaseUnivariateDistribution.plot_gaussian](BaseUnivariateDistribution.plot_gaussian.md)

Arguments
------------
* `sigma` (int, optional, default=1): sigma to use for uncertainties,
    passed directly to [BaseUnivariateDistribution.uncertainties](BaseUnivariateDistribution.uncertainties.md)
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

