## MVHistogram (class)



Treatment under-the-hood:

* When sampling, a random value between 0 and 1 is drawn.  The N-dimensional
bins are then unraveled and integrated to create a flattened cdf.  The
cdf is then linearly interpolated to find the index of the unraveled bins
in which to sample, as well as the relative location in the bin.  The selected
bin is then artificially subdivided by the same shape grid as the original
binning and linearly interpolated based on the remainder to return a single
value for &lt;[class](class.md).sample&gt;.

* Means and covariances (see &lt;[class](class.md).calculate_means_covariances&gt;,
&lt;[class](class.md).calculate_means&gt;, &lt;[class](class.md).calculate_covariances&gt;) are calculated
by sampling (with a default size of 1e5), and determining the mean and covariances
on that sample.




* [__init__](MVHistogram.__init__.md)
* [calculate_covariances](MVHistogram.calculate_covariances.md)
* [calculate_means](MVHistogram.calculate_means.md)
* [calculate_means_covariances](MVHistogram.calculate_means_covariances.md)
* [cdf](MVHistogram.cdf.md)
* [copy](MVHistogram.copy.md)
* [dimension](MVHistogram.dimension.md)
* [dimensions](MVHistogram.dimensions.md)
* [dist_constructor_argnames](MVHistogram.dist_constructor_argnames.md)
* [dist_constructor_args](MVHistogram.dist_constructor_args.md)
* [dist_constructor_func](MVHistogram.dist_constructor_func.md)
* [dist_constructor_object](MVHistogram.dist_constructor_object.md)
* [from_data](MVHistogram.from_data.md)
* [get_dimension_by_label](MVHistogram.get_dimension_by_label.md)
* [get_wrap_at](MVHistogram.get_wrap_at.md)
* [hash](MVHistogram.hash.md)
* [label](MVHistogram.label.md)
* [logcdf](MVHistogram.logcdf.md)
* [logpdf](MVHistogram.logpdf.md)
* [ndimensions](MVHistogram.ndimensions.md)
* [pdf](MVHistogram.pdf.md)
* [plot](MVHistogram.plot.md)
* [ppf](MVHistogram.ppf.md)
* [sample](MVHistogram.sample.md)
* [take_dimension](MVHistogram.take_dimension.md)
* [to](MVHistogram.to.md)
* [to_dict](MVHistogram.to_dict.md)
* [to_file](MVHistogram.to_file.md)
* [to_histogram](MVHistogram.to_histogram.md)
* [to_json](MVHistogram.to_json.md)
* [to_mvgaussian](MVHistogram.to_mvgaussian.md)
* [to_si](MVHistogram.to_si.md)
* [to_solar](MVHistogram.to_solar.md)
* [unit](MVHistogram.unit.md)
* [wrap](MVHistogram.wrap.md)
* [wrap_at](MVHistogram.wrap_at.md)
