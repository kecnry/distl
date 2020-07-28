## Samples (class)


A Samples distribution stores individual samples and draws randomly from them.

NOTE: [Samples.weights](Samples.weights.md) is only supported with scipy version 1.2+

Treatment under-the-hood:

* [Samples.sample](Samples.sample.md), [Samples.mean](Samples.mean.md), [Samples.median](Samples.median.md), [Samples.std](Samples.std.md), and
[Samples.var](Samples.var.md) act directly on the stored array in [Samples.samples](Samples.samples.md), unless
[Samples.weights](Samples.weights.md) are provided, in which case will act on a drawn sample
from [Samples.sample](Samples.sample.md) (with the exception of [Samples.mean](Samples.mean.md) which calls
numpy.average under-the-hood and passes [Samples.samples](Samples.samples.md) and [Samples.weights](Samples.weights.md)).

* all other methods requiring a probability to be computed ([Samples.pdf](Samples.pdf.md) etc)
rely on a KDE with [Samples.samples](Samples.samples.md), [Samples.weights](Samples.weights.md), and [Samples.bw_method](Samples.bw_method.md).
See https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gaussian_kde.html



* [__init__](Samples.__init__.md)
* [arccos](Samples.arccos.md)
* [arcsin](Samples.arcsin.md)
* [arctan](Samples.arctan.md)
* [arctan2](Samples.arctan2.md)
* [bw_method](Samples.bw_method.md)
* [cached_sample](Samples.cached_sample.md)
* [cdf](Samples.cdf.md)
* [clear_cached_sample](Samples.clear_cached_sample.md)
* [copy](Samples.copy.md)
* [cos](Samples.cos.md)
* [dist_constructor_args](Samples.dist_constructor_args.md)
* [dist_constructor_func](Samples.dist_constructor_func.md)
* [dist_constructor_object](Samples.dist_constructor_object.md)
* [entropy](Samples.entropy.md)
* [expect](Samples.expect.md)
* [get_wrap_at](Samples.get_wrap_at.md)
* [hash](Samples.hash.md)
* [interval](Samples.interval.md)
* [isf](Samples.isf.md)
* [label](Samples.label.md)
* [label_latex](Samples.label_latex.md)
* [log](Samples.log.md)
* [log10](Samples.log10.md)
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
* [plot_uncertainties](Samples.plot_uncertainties.md)
* [ppf](Samples.ppf.md)
* [sample](Samples.sample.md)
* [samples](Samples.samples.md)
* [sf](Samples.sf.md)
* [sin](Samples.sin.md)
* [std](Samples.std.md)
* [tan](Samples.tan.md)
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
* [uncertainties](Samples.uncertainties.md)
* [unit](Samples.unit.md)
* [var](Samples.var.md)
* [weights](Samples.weights.md)
* [wrap](Samples.wrap.md)
* [wrap_at](Samples.wrap_at.md)
