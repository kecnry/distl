### [BaseAroundGenerator](BaseAroundGenerator.md).to_dict (function)


```py

def to_dict(self, exclude=[])

```



Return the dictionary representation of the distribution object.

The resulting dictionary can be restored to the original object
via [distl.from_dict](distl.from_dict.md).

See also:

* [BaseAroundGenerator.to_json](BaseAroundGenerator.to_json.md)
* [BaseAroundGenerator.to_file](BaseAroundGenerator.to_file.md)

Arguments
----------
* `exclude` (list, optional, default=[]): list of keys to exclude.

Returns
--------
* dictionary

