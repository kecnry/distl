### [MVSamples](MVSamples.md).plot_uncertainties (function)


```py

def plot_uncertainties(self, sigma=1, unit=None, show=False, **kwargs)

```



Plot uncertainties as vertical lines and as a latex representation in
the axes title.

See also:

* [MVSamples.uncertainties](MVSamples.uncertainties.md)
* [MVSamples.plot](MVSamples.plot.md)
* [MVSamples.plot_sample](MVSamples.plot_sample.md)
* [MVSamples.plot_pdf](MVSamples.plot_pdf.md)
* [MVSamples.plot_cdf](MVSamples.plot_cdf.md)
* [MVSamples.plot_gaussian](MVSamples.plot_gaussian.md)

Arguments
------------
* `sigma` (int, optional, default=1): sigma to use for uncertainties,
    passed directly to [MVSamples.uncertainties](MVSamples.uncertainties.md)
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

