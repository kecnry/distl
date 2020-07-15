### [MVSamplesSlice](MVSamplesSlice.md).plot_uncertainties (function)


```py

def plot_uncertainties(self, sigma=1, unit=None, show=False, **kwargs)

```



Plot uncertainties as vertical lines and as a latex representation in
the axes title.

See also:

* [MVSamplesSlice.uncertainties](MVSamplesSlice.uncertainties.md)
* [MVSamplesSlice.plot](MVSamplesSlice.plot.md)
* [MVSamplesSlice.plot_sample](MVSamplesSlice.plot_sample.md)
* [MVSamplesSlice.plot_pdf](MVSamplesSlice.plot_pdf.md)
* [MVSamplesSlice.plot_cdf](MVSamplesSlice.plot_cdf.md)
* [MVSamplesSlice.plot_gaussian](MVSamplesSlice.plot_gaussian.md)

Arguments
------------
* `sigma` (int, optional, default=1): sigma to use for uncertainties,
    passed directly to [MVSamplesSlice.uncertainties](MVSamplesSlice.uncertainties.md)
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

