### [DistributionCollection](DistributionCollection.md).to_dict (function)


```py

def to_dict(self, exclude=[])

```



Return the dictionary representation of the distribution object.

The resulting dictionary can be restored to the original object
via [distl.from_dict](distl.from_dict.md).

See also:

* [DistributionCollection.to_json](DistributionCollection.to_json.md)
* [DistributionCollection.to_file](DistributionCollection.to_file.md)

Arguments
----------
* `exclude` (list, optional, default=[]): list of keys to exclude.

Returns
--------
* dictionary

