### [MVGaussianSlice](MVGaussianSlice.md).plot_uncertainties (function)


```py

def plot_uncertainties(self, sigma=1, unit=None, show=False, **kwargs)

```



Plot uncertainties as vertical lines and as a latex representation in
the axes title.

See also:

* [MVGaussianSlice.uncertainties](MVGaussianSlice.uncertainties.md)
* [MVGaussianSlice.plot](MVGaussianSlice.plot.md)
* [MVGaussianSlice.plot_sample](MVGaussianSlice.plot_sample.md)
* [MVGaussianSlice.plot_pdf](MVGaussianSlice.plot_pdf.md)
* [MVGaussianSlice.plot_cdf](MVGaussianSlice.plot_cdf.md)
* [MVGaussianSlice.plot_gaussian](MVGaussianSlice.plot_gaussian.md)

Arguments
------------
* `sigma` (int, optional, default=1): sigma to use for uncertainties,
    passed directly to [MVGaussianSlice.uncertainties](MVGaussianSlice.uncertainties.md)
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

