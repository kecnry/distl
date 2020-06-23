## MVHistogram (class)



Treatment under-the-hood:

* When sampling, a random value between 0 and 1 is drawn.  The N-dimensional
bins are then unraveled and integrated to create a flattened cdf.  The
cdf is then linearly interpolated to find the index of the unraveled bins
in which to sample, as well as the relative location in the bin.  The selected
bin is then artificially subdivided by the same shape grid as the original
binning and linearly interpolated based on the remainder to return a single
value for [MVHistogram.sample](MVHistogram.sample.md).

* Means and covariances (see [MVHistogram.calculate_means_covariances](MVHistogram.calculate_means_covariances.md),
[MVHistogram.calculate_means](MVHistogram.calculate_means.md), [MVHistogram.calculate_covariances](MVHistogram.calculate_covariances.md)) are calculated
by sampling (with a default size of 1e5), and determining the mean and covariances
on that sample.




* [__init__](MVHistogram.__init__.md)
* [arccos](MVHistogram.arccos.md)
* [arcsin](MVHistogram.arcsin.md)
* [arctan](MVHistogram.arctan.md)
* [arctan2](MVHistogram.arctan2.md)
* [bins](MVHistogram.bins.md)
* [cached_sample](MVHistogram.cached_sample.md)
* [calculate_covariances](MVHistogram.calculate_covariances.md)
* [calculate_means](MVHistogram.calculate_means.md)
* [calculate_means_covariances](MVHistogram.calculate_means_covariances.md)
* [cdf](MVHistogram.cdf.md)
* [clear_cached_sample](MVHistogram.clear_cached_sample.md)
* [copy](MVHistogram.copy.md)
* [density](MVHistogram.density.md)
* [dist_constructor_argnames](MVHistogram.dist_constructor_argnames.md)
* [dist_constructor_args](MVHistogram.dist_constructor_args.md)
* [dist_constructor_func](MVHistogram.dist_constructor_func.md)
* [dist_constructor_object](MVHistogram.dist_constructor_object.md)
* [from_data](MVHistogram.from_data.md)
* [get_from_cache](MVHistogram.get_from_cache.md)
* [get_wrap_at](MVHistogram.get_wrap_at.md)
* [hash](MVHistogram.hash.md)
* [labels](MVHistogram.labels.md)
* [log](MVHistogram.log.md)
* [log10](MVHistogram.log10.md)
* [logcdf](MVHistogram.logcdf.md)
* [logpdf](MVHistogram.logpdf.md)
* [ndimensions](MVHistogram.ndimensions.md)
* [pdf](MVHistogram.pdf.md)
* [plot](MVHistogram.plot.md)
* [plot_cdf](MVHistogram.plot_cdf.md)
* [plot_gaussian](MVHistogram.plot_gaussian.md)
* [plot_pdf](MVHistogram.plot_pdf.md)
* [plot_sample](MVHistogram.plot_sample.md)
* [ppf](MVHistogram.ppf.md)
* [sample](MVHistogram.sample.md)
* [slice](MVHistogram.slice.md)
* [take_dimensions](MVHistogram.take_dimensions.md)
* [to_dict](MVHistogram.to_dict.md)
* [to_file](MVHistogram.to_file.md)
* [to_gaussian](MVHistogram.to_gaussian.md)
* [to_histogram](MVHistogram.to_histogram.md)
* [to_json](MVHistogram.to_json.md)
* [to_mvgaussian](MVHistogram.to_mvgaussian.md)
* [to_mvsamples](MVHistogram.to_mvsamples.md)
* [to_samples](MVHistogram.to_samples.md)
* [to_univariate](MVHistogram.to_univariate.md)
* [uncertainties](MVHistogram.uncertainties.md)
* [units](MVHistogram.units.md)
* [wrap_ats](MVHistogram.wrap_ats.md)
