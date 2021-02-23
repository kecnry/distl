### [MVSamplesSlice](MVSamplesSlice.md).deepcopy (function)


```py

def deepcopy(self)

```



Make an independent copy of the distribution object.  When sampled together
via a [DistributionCollection](DistributionCollection.md) or [CompositeDistribution](CompositeDistribution.md), the copies
will be sampled independently rather than linked.  To retain this link,
use [MVSamplesSlice.copy](MVSamplesSlice.copy.md) instead.

Returns
----------
* a copy of the distribution object

