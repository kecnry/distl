## Function (class)


A function distribution consisting of some callable function along with
args/kwargs which can each be other Distribution objects.

For example:

```py
def func(a, b, c=1, d=5):
return a*b + c*d

a = distl.gaussian(10, 2)
b = distl.uniform(3, 5)
d = 6
f = distl.function(func, args=(a, b), kwargs={'d': d}, vectorized=True)
print(f)
```

Note: using [Function.to_file](Function.to_file.md) or [from_file](from_file.md) requires the `dill` package
to be installed.

Treatment "under-the-hood":

* sampling is handled by sampling the underyling children and
therefore can retain covariances.  The pdfs, cdfs, and ppfs are
created by taking [Function.hist_samples](Function.hist_samples.md) samples,
converting to a [Histogram](Histogram.md) with 100 bins,
and using the underlying [scipy.stats.rv_histogram](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_histogram.html),
thereby losing all covariances.




* [__init__](Function.__init__.md)
* [arccos](Function.arccos.md)
* [arcsin](Function.arcsin.md)
* [arctan](Function.arctan.md)
* [arctan2](Function.arctan2.md)
* [args](Function.args.md)
* [cached_sample](Function.cached_sample.md)
* [cached_sample_children](Function.cached_sample_children.md)
* [cdf](Function.cdf.md)
* [clear_cached_sample](Function.clear_cached_sample.md)
* [copy](Function.copy.md)
* [dist_constructor_argnames](Function.dist_constructor_argnames.md)
* [dist_constructor_args](Function.dist_constructor_args.md)
* [dist_constructor_func](Function.dist_constructor_func.md)
* [dist_constructor_object](Function.dist_constructor_object.md)
* [dists](Function.dists.md)
* [entropy](Function.entropy.md)
* [expect](Function.expect.md)
* [func](Function.func.md)
* [get_from_cache](Function.get_from_cache.md)
* [get_wrap_at](Function.get_wrap_at.md)
* [hash](Function.hash.md)
* [hist_samples](Function.hist_samples.md)
* [interval](Function.interval.md)
* [isf](Function.isf.md)
* [kwargs](Function.kwargs.md)
* [label](Function.label.md)
* [log](Function.log.md)
* [log10](Function.log10.md)
* [logcdf](Function.logcdf.md)
* [logpdf](Function.logpdf.md)
* [logsf](Function.logsf.md)
* [mean](Function.mean.md)
* [median](Function.median.md)
* [moment](Function.moment.md)
* [pdf](Function.pdf.md)
* [plot](Function.plot.md)
* [plot_cdf](Function.plot_cdf.md)
* [plot_gaussian](Function.plot_gaussian.md)
* [plot_pdf](Function.plot_pdf.md)
* [plot_sample](Function.plot_sample.md)
* [ppf](Function.ppf.md)
* [sample](Function.sample.md)
* [sample_args_kwargs](Function.sample_args_kwargs.md)
* [sf](Function.sf.md)
* [std](Function.std.md)
* [to](Function.to.md)
* [to_delta](Function.to_delta.md)
* [to_dict](Function.to_dict.md)
* [to_file](Function.to_file.md)
* [to_gaussian](Function.to_gaussian.md)
* [to_histogram](Function.to_histogram.md)
* [to_json](Function.to_json.md)
* [to_samples](Function.to_samples.md)
* [to_si](Function.to_si.md)
* [to_solar](Function.to_solar.md)
* [to_uniform](Function.to_uniform.md)
* [uncertainties](Function.uncertainties.md)
* [unit](Function.unit.md)
* [var](Function.var.md)
* [vectorized](Function.vectorized.md)
* [wrap](Function.wrap.md)
* [wrap_at](Function.wrap_at.md)
