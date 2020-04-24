## Gaussian_Around (class)


Create a [Gaussian](Gaussian.md) distribution which will always be centered to the face-value
of the parameter.  Some methods of the underlying [Gaussian](Gaussian.md) distribution are
available, but must either have [Gaussian_Around.value](Gaussian_Around.value.md) set or passed as
a keyword-argument.  Calling the object with a value will also return
the underlying "frozen" [Gaussian](Gaussian.md) distribution (see [Gaussian_Around.to_gaussian](Gaussian_Around.to_gaussian.md)).


For example:

```py
ga = distl.gaussian_around(scale=2)
ga.sample(value=5)
ga.value = 6
ga.sample()
ga(7).sample()
```




* [__init__](Gaussian_Around.__init__.md)
* [arccos](Gaussian_Around.arccos.md)
* [arcsin](Gaussian_Around.arcsin.md)
* [arctan](Gaussian_Around.arctan.md)
* [arctan2](Gaussian_Around.arctan2.md)
* [copy](Gaussian_Around.copy.md)
* [hash](Gaussian_Around.hash.md)
* [label](Gaussian_Around.label.md)
* [log](Gaussian_Around.log.md)
* [log10](Gaussian_Around.log10.md)
* [pdf](Gaussian_Around.pdf.md)
* [plot](Gaussian_Around.plot.md)
* [plot_cdf](Gaussian_Around.plot_cdf.md)
* [plot_pdf](Gaussian_Around.plot_pdf.md)
* [plot_sample](Gaussian_Around.plot_sample.md)
* [sample](Gaussian_Around.sample.md)
* [scale](Gaussian_Around.scale.md)
* [to](Gaussian_Around.to.md)
* [to_dict](Gaussian_Around.to_dict.md)
* [to_file](Gaussian_Around.to_file.md)
* [to_gaussian](Gaussian_Around.to_gaussian.md)
* [to_json](Gaussian_Around.to_json.md)
* [to_si](Gaussian_Around.to_si.md)
* [to_solar](Gaussian_Around.to_solar.md)
* [unit](Gaussian_Around.unit.md)
* [value](Gaussian_Around.value.md)
* [wrap_at](Gaussian_Around.wrap_at.md)
