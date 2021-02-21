### [Gaussian_Around](Gaussian_Around.md).copy (function)


```py

def copy(self)

```



Make a copy of the distribution object.  When sampled together via
a [DistributionCollection](DistributionCollection.md) or [CompositeDistribution](CompositeDistribution.md), both copies
will be sampled simultaneously and remain linked.  To break this link,
use [Gaussian_Around](Gaussian_Around.md).deepcopy&gt; instead.

Returns
---------
* a copy of the distribution object

