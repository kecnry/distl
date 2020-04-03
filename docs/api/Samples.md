## Samples (class)


A Samples distribution stores individual samples and draws randomly from them.

Treatment under-the-hood:

* [Samples.sample](Samples.sample.md), [Samples.mean](Samples.mean.md), [Samples.median](Samples.median.md), [Samples.std](Samples.std.md), and
[Samples.var](Samples.var.md) act directly on the stored array in [Samples.samples](Samples.samples.md).
* all other methods act on a histogram generated on-the-fly (but not stored),
using [Samples.samples](Samples.samples.md) and [Samples.bins](Samples.bins.md).  See [Samples.to_histogram](Samples.to_histogram.md)
and [Histogram](Histogram.md) for more details.




* [__init__](Samples.__init__.md)
* [bins](Samples.bins.md)
* [cached_sample](Samples.cached_sample.md)
* [cdf](Samples.cdf.md)
* [clear_cached_sample](Samples.clear_cached_sample.md)
* [copy](Samples.copy.md)
* [dist_constructor_argnames](Samples.dist_constructor_argnames.md)
* [dist_constructor_args](Samples.dist_constructor_args.md)
* [dist_constructor_func](Samples.dist_constructor_func.md)
* [dist_constructor_object](Samples.dist_constructor_object.md)
* [entropy](Samples.entropy.md)
* [expect](Samples.expect.md)
* [get_from_cache](Samples.get_from_cache.md)
* [get_wrap_at](Samples.get_wrap_at.md)
* [hash](Samples.hash.md)
* [interval](Samples.interval.md)
* [isf](Samples.isf.md)
* [label](Samples.label.md)
* [logcdf](Samples.logcdf.md)
* [logpdf](Samples.logpdf.md)
* [logsf](Samples.logsf.md)
* [mean](Samples.mean.md)
* [median](Samples.median.md)
* [moment](Samples.moment.md)
* [nsamples](Samples.nsamples.md)
* [pdf](Samples.pdf.md)
* [plot](Samples.plot.md)
* [plot_cdf](Samples.plot_cdf.md)
* [plot_gaussian](Samples.plot_gaussian.md)
* [plot_pdf](Samples.plot_pdf.md)
* [plot_sample](Samples.plot_sample.md)
* [ppf](Samples.ppf.md)
* [sample](Samples.sample.md)
* [samples](Samples.samples.md)
* [sf](Samples.sf.md)
* [std](Samples.std.md)
* [to](Samples.to.md)
* [to_delta](Samples.to_delta.md)
* [to_dict](Samples.to_dict.md)
* [to_file](Samples.to_file.md)
* [to_gaussian](Samples.to_gaussian.md)
* [to_histogram](Samples.to_histogram.md)
* [to_json](Samples.to_json.md)
* [to_samples](Samples.to_samples.md)
* [to_si](Samples.to_si.md)
* [to_solar](Samples.to_solar.md)
* [to_uniform](Samples.to_uniform.md)
* [unit](Samples.unit.md)
* [var](Samples.var.md)
* [wrap](Samples.wrap.md)
* [wrap_at](Samples.wrap_at.md)
