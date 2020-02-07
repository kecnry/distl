### [Gaussian](Gaussian.md).plot (function)


```py

def plot(self, size=100000.0, unit=None, wrap_at=None, seed=None, plot_sample=True, plot_sample_kwargs={'color': 'gray'}, plot_pdf=True, plot_pdf_kwargs={'color': 'red'}, plot_cdf=False, plot_cdf_kwargs={'color': 'green'}, plot_gaussian=False, plot_gaussian_kwargs={'color': 'blue'}, label=None, show=False, **kwargs)

```



Plot both the analytic distribution function as well as a sampled
histogram from the distribution.  Requires matplotlib to be installed.

See also:

* [Gaussian.plot_sample](Gaussian.plot_sample.md)
* [Gaussian.plot_pdf](Gaussian.plot_pdf.md)
* [Gaussian.plot_cdf](Gaussian.plot_cdf.md)
* [Gaussian.plot_gaussian](Gaussian.plot_gaussian.md)

Arguments
-----------
* `size` (int, optional, default=1e5): number of points to sample for
    the histogram.  See also [Gaussian.sample](Gaussian.sample.md).
* `unit` (astropy.unit, optional, default=None): units to use along
    the x-axis.  Astropy must be installed.
* `wrap_at` (float, None, or False, optional, default=None): value to
    use for wrapping.  See [Gaussian.wrap](Gaussian.wrap.md).  If not provided or None,
    will use the value from [Gaussian.wrap_at](Gaussian.wrap_at.md).  Note: wrapping is
    computed before changing units, so `wrap_at` must be provided
    according to [Gaussian.unit](Gaussian.unit.md) not `unit`.
* `seed` (int, optional): seed to use when sampling.  See also
    [Gaussian.sample](Gaussian.sample.md).
* `plot_sample` (bool, optional, default=True): whether to plot the
    histogram from sampling.  See also [Gaussian.plot_sample](Gaussian.plot_sample.md).
* `plot_sample_kwargs` (dict, optional, default={'color': 'gray'}):
    keyword arguments to send to [Gaussian.plot_sample](Gaussian.plot_sample.md).
* `plot_pdf` (bool, optional, default=True): whether to plot the
    analytic form of the underlying distribution, if applicable.
    See also [Gaussian.plot_pdf](Gaussian.plot_pdf.md).
* `plot_pdf_kwargs` (dict, optional, default={'color': 'red'}):
    keyword arguments to send to [Gaussian.plot_pdf](Gaussian.plot_pdf.md).
* `plot_cdf` (bool, optional, default=True): whether to plot the
    analytic form of the cdf, if applicable.
    See also [Gaussian.plot_cdf](Gaussian.plot_cdf.md).
* `plot_cdf_kwargs` (dict, optional, default={'color': 'green'}):
    keyword arguments to send to [Gaussian.plot_cdf](Gaussian.plot_cdf.md).
* `plot_gaussian` (bool, optional, default=False): whether to plot
    a guassian distribution fit to the sample.  Only supported for
    distributions that have [Gaussian.to_gaussian](Gaussian.to_gaussian.md) methods.
* `plot_gaussian_kwargs` (dict, optional, default={'color': 'blue'}):
    keyword arguments to send to [Gaussian.plot_gaussian](Gaussian.plot_gaussian.md).
* `label` (string, optional, default=None): override the label on the
    x-axis.  If not provided or None, will use [Gaussian.label](Gaussian.label.md).  Will
    only be used if `show=True`.
* `show` (bool, optional, default=True): whether to show the resulting
    matplotlib figure.
* `**kwargs`: all keyword arguments (except for `bins`) will be passed
    on to [Gaussian.plot_pdf](Gaussian.plot_pdf.md) and [Gaussian.plot_gaussian](Gaussian.plot_gaussian.md) and all
    keyword arguments will be passed on to [Gaussian.plot_sample](Gaussian.plot_sample.md).
    Keyword arguments defined in `plot_sample_kwargs`,
    `plot_pdf_kwargs`, and `plot_gaussian_kwargs`
    will override the values sent in `kwargs`.

Returns
--------
* tuple: the return values from [Gaussian.plot_sample](Gaussian.plot_sample.md) (or None if
    `plot_sample=False`), [Gaussian.plot_pdf](Gaussian.plot_pdf.md) (or None if `plot_pdf=False`),
    [Gaussian.plot_cdf](Gaussian.plot_cdf.md) (or None if `plot_cdf=False`),
    and [Gaussian.plot_pdf](Gaussian.plot_pdf.md) (or None if `plot_gaussian=False`).

Raises
--------
* ImportError: if matplotlib dependency is not met.

