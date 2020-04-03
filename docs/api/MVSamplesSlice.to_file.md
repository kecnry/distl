### [MVSamplesSlice](MVSamplesSlice.md).to_file (function)


```py

def to_file(self, filename, **kwargs)

```



Save the json representation of the distribution object to a file.

The resulting file can be restored to the original object
via [distl.from_file](distl.from_file.md).

See also:

* [MVSamplesSlice.to_dict](MVSamplesSlice.to_dict.md)
* [MVSamplesSlice.to_json](MVSamplesSlice.to_json.md)

Arguments
----------
* `filename` (string): path to the file to be created (will overwrite
    if already exists)
* `**kwargs`: all keyword arguments will be sent to json.dumps

Returns
--------
* string: the filename

