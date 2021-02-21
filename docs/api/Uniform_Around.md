## Uniform_Around (class)


Create a [Uniform](Uniform.md) distribution which will always be centered to the face-value
of the parameter.  Some methods of the underlying [Uniform](Uniform.md) distribution are
available, but must either have [Uniform_Around.value](Uniform_Around.value.md) set or passed as
a keyword-argument.  Calling the object with a value will also return
the underlying "frozen" [Uniform](Uniform.md) distribution (see [Uniform_Around.to_uniform](Uniform_Around.to_uniform.md)).


For example:

```py
ua = distl.uniform_around(width=2)
ua.sample(value=5)
ua.value = 6
ua.sample()
ua(7).sample()
```




* [__init__](Uniform_Around.__init__.md)
* [arccos](Uniform_Around.arccos.md)
* [arcsin](Uniform_Around.arcsin.md)
* [arctan](Uniform_Around.arctan.md)
* [arctan2](Uniform_Around.arctan2.md)
* [copy](Uniform_Around.copy.md)
* [cos](Uniform_Around.cos.md)
* [deepcopy](Uniform_Around.deepcopy.md)
* [label](Uniform_Around.label.md)
* [label_latex](Uniform_Around.label_latex.md)
* [log](Uniform_Around.log.md)
* [log10](Uniform_Around.log10.md)
* [pdf](Uniform_Around.pdf.md)
* [plot](Uniform_Around.plot.md)
* [plot_cdf](Uniform_Around.plot_cdf.md)
* [plot_pdf](Uniform_Around.plot_pdf.md)
* [plot_sample](Uniform_Around.plot_sample.md)
* [sample](Uniform_Around.sample.md)
* [sin](Uniform_Around.sin.md)
* [tan](Uniform_Around.tan.md)
* [to](Uniform_Around.to.md)
* [to_dict](Uniform_Around.to_dict.md)
* [to_file](Uniform_Around.to_file.md)
* [to_json](Uniform_Around.to_json.md)
* [to_si](Uniform_Around.to_si.md)
* [to_solar](Uniform_Around.to_solar.md)
* [to_uniform](Uniform_Around.to_uniform.md)
* [uniqueid](Uniform_Around.uniqueid.md)
* [unit](Uniform_Around.unit.md)
* [value](Uniform_Around.value.md)
* [width](Uniform_Around.width.md)
* [wrap_at](Uniform_Around.wrap_at.md)
