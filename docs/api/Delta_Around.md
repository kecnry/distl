## Delta_Around (class)


Create a [Delta](Delta.md) distribution which will always be set to the face-value
of the parameter.  All methods of the underlying [Delta](Delta.md) distribution are
available, but must either have [Delta_Around.value](Delta_Around.value.md) set or passed as
a keyword-argument.  Calling the object with a value will also return
the underlying "frozen" [Delta](Delta.md) distribution (see [Delta_Around.to_delta](Delta_Around.to_delta.md)).


For example:

```py
da = distl.delta_around()
da.sample(value=5)
da.value = 6
da.sample()
da(7).sample()
```




* [__init__](Delta_Around.__init__.md)
* [copy](Delta_Around.copy.md)
* [hash](Delta_Around.hash.md)
* [label](Delta_Around.label.md)
* [to](Delta_Around.to.md)
* [to_delta](Delta_Around.to_delta.md)
* [to_dict](Delta_Around.to_dict.md)
* [to_file](Delta_Around.to_file.md)
* [to_json](Delta_Around.to_json.md)
* [to_si](Delta_Around.to_si.md)
* [to_solar](Delta_Around.to_solar.md)
* [unit](Delta_Around.unit.md)
* [value](Delta_Around.value.md)
* [wrap_at](Delta_Around.wrap_at.md)
