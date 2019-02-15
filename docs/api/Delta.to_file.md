### [Delta](Delta.md).to_file (method)


```py

def to_file(self, filename, **kwargs)

```



dump a representation of the nparray object to a json-formatted file.
The nparray object should then be able to be fully restored via
nparray.from_file
@parameter str filename: path to the file to be created (will overwrite
    if already exists)
@rtype: str
@returns: the filename

