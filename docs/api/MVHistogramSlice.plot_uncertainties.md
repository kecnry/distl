### [MVHistogramSlice](MVHistogramSlice.md).plot_uncertainties (function)


```py

def plot_uncertainties(self, sigma=1, unit=None, show=False, **kwargs)

```



Plot uncertainties as vertical lines and as a latex representation in
the axes title.

See also:

* [MVHistogramSlice.uncertainties](MVHistogramSlice.uncertainties.md)
* [MVHistogramSlice.plot](MVHistogramSlice.plot.md)
* [MVHistogramSlice.plot_sample](MVHistogramSlice.plot_sample.md)
* [MVHistogramSlice.plot_pdf](MVHistogramSlice.plot_pdf.md)
* [MVHistogramSlice.plot_cdf](MVHistogramSlice.plot_cdf.md)
* [MVHistogramSlice.plot_gaussian](MVHistogramSlice.plot_gaussian.md)

Arguments
------------
* `sigma` (int, optional, default=1): sigma to use for uncertainties,
    passed directly to [MVHistogramSlice.uncertainties](MVHistogramSlice.uncertainties.md)
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

