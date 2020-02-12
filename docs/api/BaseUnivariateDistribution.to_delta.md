### [BaseUnivariateDistribution](BaseUnivariateDistribution.md).to_delta (function)


```py

def to_delta(self, loc='median')

```



Convert the [BaseUnivariateDistribution](BaseUnivariateDistribution.md) distribution to a [Delta](Delta.md) distribution at the
[BaseUnivariateDistribution.median](BaseUnivariateDistribution.median.md) (or [BaseUnivariateDistribution.mean](BaseUnivariateDistribution.mean.md)).

Arguments
------------
* `loc` (string or float, optional, default='median'):  If a float,
    will create a delta function directly at that value.  If 'median' or
    'mean' will use [BaseUnivariateDistribution.median](BaseUnivariateDistribution.median.md) or [BaseUnivariateDistribution.mean](BaseUnivariateDistribution.mean.md), respectively.
    If 'sample', will draw a random sample from [BaseUnivariateDistribution.sample](BaseUnivariateDistribution.sample.md).
    All other strings will raise a ValueError.

Returns
-----------
* a [Delta](Delta.md) object

Raises
----------
* ValueError: if the value of `loc` is not one of 'median', 'mean', 'sample'

