### [MVSamples](MVSamples.md).take_dimensions (function)


```py

def take_dimensions(self, dimensions)

```



Take multiple dimensions from the multivariate distribution (and remove
all others), returning another [MVSamples](MVSamples.md) object.

See also:

* [MVSamples.slice](MVSamples.slice.md)
* [MVSamples.to_univariate](MVSamples.to_univariate.md)

Arguments
----------
* `dimension` (list of strings or ints): the labels or indices of the
    dimensions to include in the new distribution.

Returns
----------
* [MVSamples](MVSamples.md) object or [Samples](Samples.md) if only one dimension provided

