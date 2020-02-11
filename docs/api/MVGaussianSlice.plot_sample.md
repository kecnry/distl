### [MVGaussianSlice](MVGaussianSlice.md).plot_sample (function)


```py

def plot_sample(self, *args, **kwargs)

```



Plot both a sampled histogram from the distribution.  Requires
matplotlib to be installed.

See also:

* [MVGaussianSlice.plot](MVGaussianSlice.plot.md)
* [MVGaussianSlice.plot_pdf](MVGaussianSlice.plot_pdf.md)
* [MVGaussianSlice.plot_cdf](MVGaussianSlice.plot_cdf.md)
* [MVGaussianSlice.plot_gaussian](MVGaussianSlice.plot_gaussian.md)

Arguments
-----------
* `size` (int, optional, default=1e5): number of points to sample for
    the histogram.  See also [MVGaussianSlice.sample](MVGaussianSlice.sample.md).  Will be ignored
    if `samples` is provided.
* `unit` (astropy.unit, optional, default=None): units to use along
    the x-axis.  Astropy must be installed.  If `samples` is provided,
    the passed values will be assumed to be in the correct units.
* `wrap_at` (float, None, or False, optional, default=None): value to
    use for wrapping.  See [MVGaussianSlice.wrap](MVGaussianSlice.wrap.md).  If not provided or None,
    will use the value from [MVGaussianSlice.wrap_at](MVGaussianSlice.wrap_at.md).  Note: wrapping is
    computed before changing units, so `wrap_at` must be provided
    according to [MVGaussianSlice.unit](MVGaussianSlice.unit.md) not `unit`.  Will be ignored
    if `samples` is provided.
* `seed` (int, optional): seed to use when sampling.  See also
    [MVGaussianSlice.sample](MVGaussianSlice.sample.md).  Will be ignored if `samples` is provided.
* `samples` (array, optional, default=None): plot specific sampled
    values instead of calling [MVGaussianSlice.sample](MVGaussianSlice.sample.md) internally.  Will override
    `size`.
* `label` (string, optional, default=None): override the label on the
    x-axis.  If not provided or None, will use [MVGaussianSlice.label](MVGaussianSlice.label.md).  Will
    only be used if `show=True`.  Unit will automatically be appended.
    Will be ignored if `xlabel` is provided.
* `xlabel` (string, optional, default=None): override the label on the
    x-axis without appending the unit.  Will override `label`.
* `show` (bool, optional, default=True): whether to show the resulting
    matplotlib figure.
* `**kwargs`: all keyword arguments will be passed on to plt.hist.  If
    not provided, `bins` will default to the stored bins for [Histogram](Histogram.md)
    distributions, otherwise will default to 25.

Returns
--------
* the return from plt.hist

Raises
--------
* ImportError: if matplotlib dependency is not met.

