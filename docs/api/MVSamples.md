## MVSamples (class)



NOTE: [MVSamples.weights](MVSamples.weights.md) is only supported with scipy version 1.2+

Treatment under-the-hood:

* [MVSamples.sample](MVSamples.sample.md), [MVSamples.calculate_means](MVSamples.calculate_means.md), [MVSamples.calculate_covariances](MVSamples.calculate_covariances.md)
act directly on the stored array in [MVSamples.samples](MVSamples.samples.md), unless
[MVSamples.weights](MVSamples.weights.md) are provided, in which case will act on a drawn sample
from [MVSamples.sample](MVSamples.sample.md) (with the exception of [MVSamples.mean](MVSamples.mean.md) which calls
numpy.average under-the-hood and passes [MVSamples.samples](MVSamples.samples.md) and [MVSamples.weights](MVSamples.weights.md)).

* all other methods requiring a probability to be computed ([MVSamples.pdf](MVSamples.pdf.md) etc)
rely on a KDE with [MVSamples.samples](MVSamples.samples.md), [MVSamples.weights](MVSamples.weights.md), and [MVSamples.bw_method](MVSamples.bw_method.md).
See https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gaussian_kde.html




* [__init__](MVSamples.__init__.md)
* [arccos](MVSamples.arccos.md)
* [arcsin](MVSamples.arcsin.md)
* [arctan](MVSamples.arctan.md)
* [arctan2](MVSamples.arctan2.md)
* [bw_method](MVSamples.bw_method.md)
* [cached_sample](MVSamples.cached_sample.md)
* [calculate_covariances](MVSamples.calculate_covariances.md)
* [calculate_means](MVSamples.calculate_means.md)
* [calculate_means_covariances](MVSamples.calculate_means_covariances.md)
* [cdf](MVSamples.cdf.md)
* [clear_cached_sample](MVSamples.clear_cached_sample.md)
* [copy](MVSamples.copy.md)
* [cos](MVSamples.cos.md)
* [deepcopy](MVSamples.deepcopy.md)
* [dist_constructor_args](MVSamples.dist_constructor_args.md)
* [dist_constructor_func](MVSamples.dist_constructor_func.md)
* [dist_constructor_object](MVSamples.dist_constructor_object.md)
* [get_wrap_at](MVSamples.get_wrap_at.md)
* [interval](MVSamples.interval.md)
* [labels](MVSamples.labels.md)
* [labels_latex](MVSamples.labels_latex.md)
* [log](MVSamples.log.md)
* [log10](MVSamples.log10.md)
* [logcdf](MVSamples.logcdf.md)
* [logpdf](MVSamples.logpdf.md)
* [ndimensions](MVSamples.ndimensions.md)
* [nsamples](MVSamples.nsamples.md)
* [pdf](MVSamples.pdf.md)
* [plot](MVSamples.plot.md)
* [plot_cdf](MVSamples.plot_cdf.md)
* [plot_gaussian](MVSamples.plot_gaussian.md)
* [plot_pdf](MVSamples.plot_pdf.md)
* [plot_sample](MVSamples.plot_sample.md)
* [plot_uncertainties](MVSamples.plot_uncertainties.md)
* [ppf](MVSamples.ppf.md)
* [sample](MVSamples.sample.md)
* [samples](MVSamples.samples.md)
* [sin](MVSamples.sin.md)
* [slice](MVSamples.slice.md)
* [take_dimensions](MVSamples.take_dimensions.md)
* [tan](MVSamples.tan.md)
* [to_dict](MVSamples.to_dict.md)
* [to_file](MVSamples.to_file.md)
* [to_gaussian](MVSamples.to_gaussian.md)
* [to_histogram](MVSamples.to_histogram.md)
* [to_json](MVSamples.to_json.md)
* [to_mvgaussian](MVSamples.to_mvgaussian.md)
* [to_mvhistogram](MVSamples.to_mvhistogram.md)
* [to_samples](MVSamples.to_samples.md)
* [to_univariate](MVSamples.to_univariate.md)
* [uncertainties](MVSamples.uncertainties.md)
* [uniqueid](MVSamples.uniqueid.md)
* [units](MVSamples.units.md)
* [weights](MVSamples.weights.md)
* [wrap_ats](MVSamples.wrap_ats.md)
