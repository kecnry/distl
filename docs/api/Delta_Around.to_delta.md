### [Delta_Around](Delta_Around.md).to_delta (function)


```py

def to_delta(self, value=None)

```



Expose the "frozen" [Delta](Delta.md) distribution at a certain
[Delta_Around.value](Delta_Around.value.md) as the central value.

Arguments
----------
* `value` (float, default=None): value to use for the central value.
    If not provided, will default to [Delta_Around.value](Delta_Around.value.md).  If
    that is not set, then an error will be raised.

Returns
----------
* [Delta](Delta.md) object

