### [Gaussian_Around](Gaussian_Around.md).to_gaussian (function)


```py

def to_gaussian(self, value=None)

```



Expose the "frozen" [Gaussian](Gaussian.md) distribution at a certain
[Gaussian_Around.value](Gaussian_Around.value.md) as [Gaussian.loc](Gaussian.loc.md).

Arguments
----------
* `value` (float, default=None): value to use for [Gaussian.loc](Gaussian.loc.md).
    If not provided, will default to [Gaussian_Around.value](Gaussian_Around.value.md).  If
    that is not set, then an error will be raised.

Returns
----------
* [Gaussian](Gaussian.md) object

