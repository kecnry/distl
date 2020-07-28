### [Function](Function.md).plot_uncertainties (function)


```py

def plot_uncertainties(self, sigma=1, unit=None, show=False, **kwargs)

```



Plot uncertainties as vertical lines and as a latex representation in
the axes title.

See also:

* [Function.uncertainties](Function.uncertainties.md)
* [Function.plot](Function.plot.md)
* [Function.plot_sample](Function.plot_sample.md)
* [Function.plot_pdf](Function.plot_pdf.md)
* [Function.plot_cdf](Function.plot_cdf.md)
* [Function.plot_gaussian](Function.plot_gaussian.md)

Arguments
------------
* `sigma` (int, optional, default=1): sigma to use for uncertainties,
    passed directly to [Function.uncertainties](Function.uncertainties.md)
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

