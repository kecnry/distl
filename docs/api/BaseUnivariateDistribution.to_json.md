### [BaseUnivariateDistribution](BaseUnivariateDistribution.md).to_json (function)


```py

def to_json(self, **kwargs)

```



Return the json representation of the distribution object.

The resulting dictionary can be restored to the original object
via [distl.from_json](distl.from_json.md).

See also:

* [BaseUnivariateDistribution.to_dict](BaseUnivariateDistribution.to_dict.md)
* [BaseUnivariateDistribution.to_file](BaseUnivariateDistribution.to_file.md)

Arguments
---------
* `**kwargs`: all keyword arguments will be sent to json.dumps

Returns
--------
* string

