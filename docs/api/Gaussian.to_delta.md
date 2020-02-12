### [Gaussian](Gaussian.md).to_delta (function)


```py

def to_delta(self, loc='median')

```



Convert the [Gaussian](Gaussian.md) distribution to a [Delta](Delta.md) distribution at the
[Gaussian.median](Gaussian.median.md) (or [Gaussian.mean](Gaussian.mean.md)).

Arguments
------------
* `loc` (string or float, optional, default='median'):  If a float,
    will create a delta function directly at that value.  If 'median' or
    'mean' will use [Gaussian.median](Gaussian.median.md) or [Gaussian.mean](Gaussian.mean.md), respectively.
    If 'sample', will draw a random sample from [Gaussian.sample](Gaussian.sample.md).
    All other strings will raise a ValueError.

Returns
-----------
* a [Delta](Delta.md) object

Raises
----------
* ValueError: if the value of `loc` is not one of 'median', 'mean', 'sample'

