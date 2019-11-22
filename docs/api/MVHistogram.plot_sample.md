### [MVHistogram](MVHistogram.md).plot_sample (method)


```py

def plot_sample(self, size=100000, unit=None, wrap_at=None, seed=None, label=None, show=False, **kwargs)

```



Plot both a sampled histogram from the distribution.  Requires
matplotlib to be installed.

See also:

* [MVHistogram.plot](MVHistogram.plot.md)
* [MVHistogram.plot_dist](MVHistogram.plot_dist.md)
* [MVHistogram.plot_gaussian](MVHistogram.plot_gaussian.md)

Arguments
-----------
* `size` (int, optional, default=100000): number of points to sample for
    the histogram.  See also [MVHistogram.sample](MVHistogram.sample.md).
* `unit` (astropy.unit, optional, default=None): units to use along
    the x-axis.  Astropy must be installed.
* `wrap_at` (float, None, or False, optional, default=None): value to
    use for wrapping.  See [MVHistogram.wrap](MVHistogram.wrap.md).  If not provided or None,
    will use the value from [MVHistogram.wrap_at](MVHistogram.wrap_at.md).  Note: wrapping is
    computed before changing units, so `wrap_at` must be provided
    according to [MVHistogram.unit](MVHistogram.unit.md) not `unit`.
* `seed` (int, optional): seed to use when sampling.  See also
    [MVHistogram.sample](MVHistogram.sample.md).
* `label` (string, optional, default=None): override the label on the
    x-axis.  If not provided or None, will use [MVHistogram.label](MVHistogram.label.md).  Will
    only be used if `show=True`.
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

