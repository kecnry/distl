### [Histogram](Histogram.md).plot (function)


```py

def plot(self, size=100000.0, unit=None, wrap_at=None, seed=None, samples=None, plot_sample=True, plot_sample_kwargs={'color': 'gray'}, plot_pdf=True, plot_pdf_kwargs={'color': 'red'}, plot_cdf=False, plot_cdf_kwargs={'color': 'green'}, plot_gaussian=False, plot_gaussian_kwargs={'color': 'blue'}, label=None, xlabel=None, show=False, **kwargs)

```



Plot both the analytic distribution function as well as a sampled
histogram from the distribution.  Requires matplotlib to be installed.

See also:

* [Histogram.plot_sample](Histogram.plot_sample.md)
* [Histogram.plot_pdf](Histogram.plot_pdf.md)
* [Histogram.plot_cdf](Histogram.plot_cdf.md)
* [Histogram.plot_gaussian](Histogram.plot_gaussian.md)

Arguments
-----------
* `size` (int, optional, default=1e5): number of points to sample for
    the histogram.  See also [Histogram.sample](Histogram.sample.md).  Will be ignored
    if `samples` is provided.
* `unit` (astropy.unit, optional, default=None): units to use along
    the x-axis.  Astropy must be installed.  If `samples` is provided,
    the passed values will be assumed to be in the correct units.
* `wrap_at` (float, None, or False, optional, default=None): value to
    use for wrapping.  See [Histogram.wrap](Histogram.wrap.md).  If not provided or None,
    will use the value from [Histogram.wrap_at](Histogram.wrap_at.md).  Note: wrapping is
    computed before changing units, so `wrap_at` must be provided
    according to [Histogram.unit](Histogram.unit.md) not `unit`.  Will be ignored if
    `samples` is provided.
* `seed` (int, optional): seed to use when sampling.  See also
    [Histogram.sample](Histogram.sample.md).  Will be ignored if `samples` is provided.
* `samples` (array, optional, default=None): plot specific sampled
    values instead of calling [Histogram.sample](Histogram.sample.md) internally.  Will override
    `size`.
* `plot_sample` (bool, optional, default=True): whether to plot the
    histogram from sampling.  See also [Histogram.plot_sample](Histogram.plot_sample.md).
* `plot_sample_kwargs` (dict, optional, default={'color': 'gray'}):
    keyword arguments to send to [Histogram.plot_sample](Histogram.plot_sample.md).
* `plot_pdf` (bool, optional, default=True): whether to plot the
    analytic form of the underlying distribution, if applicable.
    See also [Histogram.plot_pdf](Histogram.plot_pdf.md).
* `plot_pdf_kwargs` (dict, optional, default={'color': 'red'}):
    keyword arguments to send to [Histogram.plot_pdf](Histogram.plot_pdf.md).
* `plot_cdf` (bool, optional, default=True): whether to plot the
    analytic form of the cdf, if applicable.
    See also [Histogram.plot_cdf](Histogram.plot_cdf.md).
* `plot_cdf_kwargs` (dict, optional, default={'color': 'green'}):
    keyword arguments to send to [Histogram.plot_cdf](Histogram.plot_cdf.md).
* `plot_gaussian` (bool, optional, default=False): whether to plot
    a guassian distribution fit to the sample.  Only supported for
    distributions that have [Histogram.to_gaussian](Histogram.to_gaussian.md) methods.
* `plot_gaussian_kwargs` (dict, optional, default={'color': 'blue'}):
    keyword arguments to send to [Histogram.plot_gaussian](Histogram.plot_gaussian.md).
* `label` (string, optional, default=None): override the label on the
    x-axis.  If not provided or None, will use [Histogram.label](Histogram.label.md).  Will
    only be used if `show=True`.  Unit will automatically be appended.
    Will be ignored if `xlabel` is provided.
* `xlabel` (string, optional, default=None): override the label on the
    x-axis without appending the unit.  Will override `label`.
* `show` (bool, optional, default=True): whether to show the resulting
    matplotlib figure.
* `**kwargs`: all keyword arguments (except for `bins`) will be passed
    on to [Histogram.plot_pdf](Histogram.plot_pdf.md) and [Histogram.plot_gaussian](Histogram.plot_gaussian.md) and all
    keyword arguments will be passed on to [Histogram.plot_sample](Histogram.plot_sample.md).
    Keyword arguments defined in `plot_sample_kwargs`,
    `plot_pdf_kwargs`, and `plot_gaussian_kwargs`
    will override the values sent in `kwargs`.

Returns
--------
* tuple: the return values from [Histogram.plot_sample](Histogram.plot_sample.md) (or None if
    `plot_sample=False`), [Histogram.plot_pdf](Histogram.plot_pdf.md) (or None if `plot_pdf=False`),
    [Histogram.plot_cdf](Histogram.plot_cdf.md) (or None if `plot_cdf=False`),
    and [Gaussian.plot_pdf](Gaussian.plot_pdf.md) (or None if `plot_gaussian=False`).

Raises
--------
* ImportError: if matplotlib dependency is not met.

