### [Uniform](Uniform.md).to_delta (function)


```py

def to_delta(self, loc='median')

```



Convert the [Uniform](Uniform.md) distribution to a [Delta](Delta.md) distribution at the
[Uniform.median](Uniform.median.md) (or [Uniform.mean](Uniform.mean.md)).

Arguments
------------
* `loc` (string or float, optional, default='median'):  If a float,
    will create a delta function directly at that value.  If 'median' or
    'mean' will use [Uniform.median](Uniform.median.md) or [Uniform.mean](Uniform.mean.md), respectively.
    If 'sample', will draw a random sample from [Uniform.sample](Uniform.sample.md).
    All other strings will raise a ValueError.

Returns
-----------
* a [Delta](Delta.md) object

Raises
----------
* ValueError: if the value of `loc` is not one of 'median', 'mean', 'sample'

