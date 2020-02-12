### [MVHistogram](MVHistogram.md).take_dimensions (function)


```py

def take_dimensions(self, dimensions)

```



Take multiple dimensions from the multivariate distribution (and remove
all others), returning another [MVHistogram](MVHistogram.md) object.

See also:

* [MVHistogram.slice](MVHistogram.slice.md)
* [MVHistogram.to_univariate](MVHistogram.to_univariate.md)

Arguments
----------
* `dimension` (list of strings or ints): the labels or indices of the
    dimensions to include in the new distribution.

Returns
----------
* [MVHistogram](MVHistogram.md) object or [Histogram](Histogram.md) if only one dimension provided

