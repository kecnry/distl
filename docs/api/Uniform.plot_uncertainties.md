### [Uniform](Uniform.md).plot_uncertainties (function)


```py

def plot_uncertainties(self, sigma=1, unit=None, show=False, **kwargs)

```



Plot uncertainties as vertical lines and as a latex representation in
the axes title.

See also:

* [Uniform.uncertainties](Uniform.uncertainties.md)
* [Uniform.plot](Uniform.plot.md)
* [Uniform.plot_sample](Uniform.plot_sample.md)
* [Uniform.plot_pdf](Uniform.plot_pdf.md)
* [Uniform.plot_cdf](Uniform.plot_cdf.md)
* [Uniform.plot_gaussian](Uniform.plot_gaussian.md)

Arguments
------------
* `sigma` (int, optional, default=1): sigma to use for uncertainties,
    passed directly to [Uniform.uncertainties](Uniform.uncertainties.md)
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

