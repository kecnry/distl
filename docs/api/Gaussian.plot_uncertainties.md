### [Gaussian](Gaussian.md).plot_uncertainties (function)


```py

def plot_uncertainties(self, sigma=1, unit=None, show=False, **kwargs)

```



Plot uncertainties as vertical lines and as a latex representation in
the axes title.

See also:

* [Gaussian.uncertainties](Gaussian.uncertainties.md)
* [Gaussian.plot](Gaussian.plot.md)
* [Gaussian.plot_sample](Gaussian.plot_sample.md)
* [Gaussian.plot_pdf](Gaussian.plot_pdf.md)
* [Gaussian.plot_cdf](Gaussian.plot_cdf.md)
* [Gaussian.plot_gaussian](Gaussian.plot_gaussian.md)

Arguments
------------
* `sigma` (int, optional, default=1): sigma to use for uncertainties,
    passed directly to [Gaussian.uncertainties](Gaussian.uncertainties.md)
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

