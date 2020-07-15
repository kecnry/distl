### [MVHistogram](MVHistogram.md).plot_uncertainties (function)


```py

def plot_uncertainties(self, sigma=1, unit=None, show=False, **kwargs)

```



Plot uncertainties as vertical lines and as a latex representation in
the axes title.

See also:

* [MVHistogram.uncertainties](MVHistogram.uncertainties.md)
* [MVHistogram.plot](MVHistogram.plot.md)
* [MVHistogram.plot_sample](MVHistogram.plot_sample.md)
* [MVHistogram.plot_pdf](MVHistogram.plot_pdf.md)
* [MVHistogram.plot_cdf](MVHistogram.plot_cdf.md)
* [MVHistogram.plot_gaussian](MVHistogram.plot_gaussian.md)

Arguments
------------
* `sigma` (int, optional, default=1): sigma to use for uncertainties,
    passed directly to [MVHistogram.uncertainties](MVHistogram.uncertainties.md)
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

