## Composite (class)


A composite distribution consisting of some math operator between one or two
other Distribution objects.

For example:

```py
g = distl.gaussian(10, 2)
u = distl.gaussian(1, 5)

c = g * u
print(c)
```

or:

```py
import numpy as np
g = distl.gaussian(0, 1)
sin_g = np.sin(g)
print(sin_g)
```

Currently supported operators include:

* multiplication, division, addition, subtraction
* np.sin, np.cos, np.tan (but not math.sin, etc)
* bitwise and (&amp;), bitwise or (|)

When doing math between a distribution and a float or integer, that float/int
will be treated as a [Delta](Delta.md) distribution.  In some simple cases, the
applicable distribution type will be returned, but in other cases,
a [Composite](Composite.md) distribution will be returned.  For example, multiplying
a [Uniform](Uniform.md) or [Gaussian](Gaussian.md) distribution by a float will return another
[Uniform](Uniform.md) or [Gaussian](Gaussian.md) distribution, respectively.

Limitations and treatment "under-the-hood":

* &amp;: the pdfs of the two underlying distributions are sampled over their
99.99\% intervals and multiplied to create a new pdf.  A spline is then
fit to the pdf and integrated to create the cdf (which is inverted to
create the ppf function).  Each of these are then linearly interpolated
to create the underlying scipy.stats object.  This object is then used
for sampling as well as accessing the [Composite.pdf](Composite.pdf.md), [Composite.cdf](Composite.cdf.md),
[Composite.ppf](Composite.ppf.md), etc.  For this reason, the and operator does not support
retaining covariances at all.

* |: the pdfs and cdfs of the two underlying distributions are sampled over their
99.9\% intervals and added to create the new pdfs and cdfs, respectively
(and the cdf inverted to create the ppf function).  Each of these are then
linearly interpolated to create the underlying scipy.stats object.  This
object is then used for any call to the underlying call EXCEPT for sampling.
Sampling is handled by randomly choosing which child distribution to sample
from and then sampling from that distribution.  Or operators are therefore
able to retain covariances for [Composite.sample](Composite.sample.md), but not for any calls
to [Composite.pdf](Composite.pdf.md), [Composite.cdf](Composite.cdf.md), or [Composite.ppf](Composite.ppf.md).

* all others: sampling is handled by sampling the underyling children and
therefore can retain covariances.  The pdfs, cdfs, and ppfs are
created by taking 1 million samples, converting to a [Histogram](Histogram.md),
and using the underlying [scipy.stats.rv_histogram](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_histogram.html),
thereby losing all covariances.




* [__init__](Composite.__init__.md)
* [arccos](Composite.arccos.md)
* [arcsin](Composite.arcsin.md)
* [arctan](Composite.arctan.md)
* [arctan2](Composite.arctan2.md)
* [cached_sample](Composite.cached_sample.md)
* [cached_sample_children](Composite.cached_sample_children.md)
* [cdf](Composite.cdf.md)
* [clear_cached_sample](Composite.clear_cached_sample.md)
* [copy](Composite.copy.md)
* [dist_constructor_argnames](Composite.dist_constructor_argnames.md)
* [dist_constructor_args](Composite.dist_constructor_args.md)
* [dist_constructor_func](Composite.dist_constructor_func.md)
* [dist_constructor_object](Composite.dist_constructor_object.md)
* [dists](Composite.dists.md)
* [entropy](Composite.entropy.md)
* [expect](Composite.expect.md)
* [get_from_cache](Composite.get_from_cache.md)
* [get_wrap_at](Composite.get_wrap_at.md)
* [hash](Composite.hash.md)
* [interval](Composite.interval.md)
* [isf](Composite.isf.md)
* [label](Composite.label.md)
* [log](Composite.log.md)
* [log10](Composite.log10.md)
* [logcdf](Composite.logcdf.md)
* [logpdf](Composite.logpdf.md)
* [logsf](Composite.logsf.md)
* [math](Composite.math.md)
* [mean](Composite.mean.md)
* [median](Composite.median.md)
* [moment](Composite.moment.md)
* [pdf](Composite.pdf.md)
* [plot](Composite.plot.md)
* [plot_cdf](Composite.plot_cdf.md)
* [plot_gaussian](Composite.plot_gaussian.md)
* [plot_pdf](Composite.plot_pdf.md)
* [plot_sample](Composite.plot_sample.md)
* [ppf](Composite.ppf.md)
* [sample](Composite.sample.md)
* [sf](Composite.sf.md)
* [std](Composite.std.md)
* [to](Composite.to.md)
* [to_delta](Composite.to_delta.md)
* [to_dict](Composite.to_dict.md)
* [to_file](Composite.to_file.md)
* [to_gaussian](Composite.to_gaussian.md)
* [to_histogram](Composite.to_histogram.md)
* [to_json](Composite.to_json.md)
* [to_samples](Composite.to_samples.md)
* [to_si](Composite.to_si.md)
* [to_solar](Composite.to_solar.md)
* [to_uniform](Composite.to_uniform.md)
* [unit](Composite.unit.md)
* [var](Composite.var.md)
* [wrap](Composite.wrap.md)
* [wrap_at](Composite.wrap_at.md)
