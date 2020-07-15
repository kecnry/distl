### [Histogram](Histogram.md).plot_uncertainties (function)


```py

def plot_uncertainties(self, sigma=1, unit=None, show=False, **kwargs)

```



Plot uncertainties as vertical lines and as a latex representation in
the axes title.

See also:

* [Histogram.uncertainties](Histogram.uncertainties.md)
* [Histogram.plot](Histogram.plot.md)
* [Histogram.plot_sample](Histogram.plot_sample.md)
* [Histogram.plot_pdf](Histogram.plot_pdf.md)
* [Histogram.plot_cdf](Histogram.plot_cdf.md)
* [Histogram.plot_gaussian](Histogram.plot_gaussian.md)

Arguments
------------
* `sigma` (int, optional, default=1): sigma to use for uncertainties,
    passed directly to [Histogram.uncertainties](Histogram.uncertainties.md)
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

