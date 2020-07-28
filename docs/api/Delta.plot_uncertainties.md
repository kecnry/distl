### [Delta](Delta.md).plot_uncertainties (function)


```py

def plot_uncertainties(self, sigma=1, unit=None, show=False, **kwargs)

```



Plot uncertainties as vertical lines and as a latex representation in
the axes title.

See also:

* [Delta.uncertainties](Delta.uncertainties.md)
* [Delta.plot](Delta.plot.md)
* [Delta.plot_sample](Delta.plot_sample.md)
* [Delta.plot_pdf](Delta.plot_pdf.md)
* [Delta.plot_cdf](Delta.plot_cdf.md)
* [Delta.plot_gaussian](Delta.plot_gaussian.md)

Arguments
------------
* `sigma` (int, optional, default=1): sigma to use for uncertainties,
    passed directly to [Delta.uncertainties](Delta.uncertainties.md)
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

