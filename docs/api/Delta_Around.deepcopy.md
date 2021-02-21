### [Delta_Around](Delta_Around.md).deepcopy (function)


```py

def deepcopy(self)

```



Make an independent copy of the distribution object.  When sampled together
via a [DistributionCollection](DistributionCollection.md) or [CompositeDistribution](CompositeDistribution.md), the copies
will be sampled independently rather than linked.  To retain this link,
use [Delta_Around.copy](Delta_Around.copy.md) instead.

Returns
----------
* a copy of the distribution object

