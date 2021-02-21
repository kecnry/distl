### [Function](Function.md).to_json (function)


```py

def to_json(self, export_func_as_path=False, **kwargs)

```



json is not supported for [Function](Function.md) distributions as the [Function.func](Function.func.md)
object must be stored via dill.  See [Function.to_dict](Function.to_dict.md) or [Function.to_file](Function.to_file.md).

