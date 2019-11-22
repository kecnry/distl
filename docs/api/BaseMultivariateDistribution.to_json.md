### [BaseMultivariateDistribution](BaseMultivariateDistribution.md).to_json (method)


```py

def to_json(self, **kwargs)

```



Return the json representation of the distribution object.

The resulting dictionary can be restored to the original object
via [npdists.from_json](npdists.from_json.md).

See also:

* [BaseMultivariateDistribution.to_dict](BaseMultivariateDistribution.to_dict.md)
* [BaseMultivariateDistribution.to_file](BaseMultivariateDistribution.to_file.md)

Arguments
---------
* `**kwargs`: all keyword arguments will be sent to json.dumps

Returns
--------
* string

