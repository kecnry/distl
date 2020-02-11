### [Gaussian](Gaussian.md).to_json (method)


```py

def to_json(self, **kwargs)

```



Return the json representation of the distribution object.

The resulting dictionary can be restored to the original object
via [distl.from_json](distl.from_json.md).

See also:

* [Gaussian.to_dict](Gaussian.to_dict.md)
* [Gaussian.to_file](Gaussian.to_file.md)

Arguments
---------
* `**kwargs`: all keyword arguments will be sent to json.dumps

Returns
--------
* string

