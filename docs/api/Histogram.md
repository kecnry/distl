## Histogram (class)


A Histogram distribution stores a discrete PDF and allows sampling from
that binned density distribution.

To create a Histogram distribution from already binned data, see
[distl.histogram_from_bins](distl.histogram_from_bins.md) or [Histogram.__init__](Histogram.__init__.md).  To create a
Histogram distribtuion from the data array itself, see
[distl.histogram_from_data](distl.histogram_from_data.md) or [Histogram.from_data](Histogram.from_data.md).

Treatment under-the-hood:

The densities at each bin-midpoint are linearly interpolated to create
a pdf (which is normalized to an integral of 1).  A numerical integral
of the bins is then performed to create the cdf (again, normalized to 1)
and inverted to create the ppf.  Each of these are then interpolated
whenever accessing [Histogram.pdf](Histogram.pdf.md), [Histogram.cdf](Histogram.cdf.md), [Histogram.ppf](Histogram.ppf.md), etc as
well as used when calling [Histogram.sample](Histogram.sample.md).



* [__init__](Histogram.__init__.md)
* [bins](Histogram.bins.md)
* [cached_sample](Histogram.cached_sample.md)
* [cdf](Histogram.cdf.md)
* [clear_cached_sample](Histogram.clear_cached_sample.md)
* [copy](Histogram.copy.md)
* [density](Histogram.density.md)
* [dist_constructor_argnames](Histogram.dist_constructor_argnames.md)
* [dist_constructor_args](Histogram.dist_constructor_args.md)
* [dist_constructor_func](Histogram.dist_constructor_func.md)
* [dist_constructor_object](Histogram.dist_constructor_object.md)
* [entropy](Histogram.entropy.md)
* [expect](Histogram.expect.md)
* [from_data](Histogram.from_data.md)
* [get_from_cache](Histogram.get_from_cache.md)
* [get_wrap_at](Histogram.get_wrap_at.md)
* [hash](Histogram.hash.md)
* [interval](Histogram.interval.md)
* [isf](Histogram.isf.md)
* [label](Histogram.label.md)
* [logcdf](Histogram.logcdf.md)
* [logpdf](Histogram.logpdf.md)
* [logsf](Histogram.logsf.md)
* [mean](Histogram.mean.md)
* [median](Histogram.median.md)
* [moment](Histogram.moment.md)
* [pdf](Histogram.pdf.md)
* [plot](Histogram.plot.md)
* [plot_cdf](Histogram.plot_cdf.md)
* [plot_gaussian](Histogram.plot_gaussian.md)
* [plot_pdf](Histogram.plot_pdf.md)
* [plot_sample](Histogram.plot_sample.md)
* [ppf](Histogram.ppf.md)
* [sample](Histogram.sample.md)
* [sf](Histogram.sf.md)
* [std](Histogram.std.md)
* [to](Histogram.to.md)
* [to_delta](Histogram.to_delta.md)
* [to_dict](Histogram.to_dict.md)
* [to_file](Histogram.to_file.md)
* [to_gaussian](Histogram.to_gaussian.md)
* [to_histogram](Histogram.to_histogram.md)
* [to_json](Histogram.to_json.md)
* [to_si](Histogram.to_si.md)
* [to_solar](Histogram.to_solar.md)
* [to_uniform](Histogram.to_uniform.md)
* [unit](Histogram.unit.md)
* [var](Histogram.var.md)
* [wrap](Histogram.wrap.md)
* [wrap_at](Histogram.wrap_at.md)
