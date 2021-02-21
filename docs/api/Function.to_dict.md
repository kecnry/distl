### [Function](Function.md).to_dict (function)


```py

def to_dict(self, export_func_as_path=False, **kwargs)

```



Return the dictionary representation of the distribution object.

The resulting dictionary can be restored to the original object
via [distl.from_dict](distl.from_dict.md).

See also:

* [Function.to_json](Function.to_json.md)
* [Function.to_file](Function.to_file.md)

Arguments
----------
* `exclude` (list, optional, default=[]): list of keys to exclude.

Returns
--------
* dictionary

