### [Delta](Delta.md).to_file (method)


```py

def to_file(self, filename, **kwargs)

```



Save the json representation of the distribution object to a file.

The resulting file can be restored to the original object
via [npdists.from_file](npdists.from_file.md).

See also:

* [BaseDistribution.to_dict](BaseDistribution.to_dict.md)
* [BaseDistribution.to_json](BaseDistribution.to_json.md)

Arguments
----------
* `filename` (string): path to the file to be created (will overwrite
    if already exists)
* `**kwargs`: all keyword arguments will be sent to json.dumps

Returns
--------
* string: the filename

