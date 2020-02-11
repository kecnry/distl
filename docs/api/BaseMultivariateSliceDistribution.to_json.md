### [BaseMultivariateSliceDistribution](BaseMultivariateSliceDistribution.md).to_json (method)


```py

def to_json(self, **kwargs)

```



Return the json representation of the distribution object.

The resulting dictionary can be restored to the original object
via [distl.from_json](distl.from_json.md).

See also:

* [BaseMultivariateSliceDistribution.to_dict](BaseMultivariateSliceDistribution.to_dict.md)
* [BaseMultivariateSliceDistribution.to_file](BaseMultivariateSliceDistribution.to_file.md)

Arguments
---------
* `**kwargs`: all keyword arguments will be sent to json.dumps

Returns
--------
* string

