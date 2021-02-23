### [Function](Function.md).to_file (function)


```py

def to_file(self, filename, export_func_as_path=False, **kwargs)

```



Save the distribution object to a file using dill.

See also:

* [Function.to_dict](Function.to_dict.md)

Arguments
----------
* `filename` (string): path to the file to be created (will overwrite
    if already exists)

Returns
--------
* string: the filename

