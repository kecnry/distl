### [Uniform_Around](Uniform_Around.md).to_uniform (function)


```py

def to_uniform(self, value=None)

```



Expose the "frozen" [Uniform](Uniform.md) distribution at a certain
[Uniform_Around.value](Uniform_Around.value.md) as the central value.

* [Uniform.low](Uniform.low.md) will be set to [Uniform_Around.value](Uniform_Around.value.md) - [Uniform_Around.width](Uniform_Around.width.md) / 2
* [Uniform.high](Uniform.high.md) will be set to [Uniform_Around.value](Uniform_Around.value.md) + [Uniform_Around.width](Uniform_Around.width.md) / 2

Arguments
----------
* `value` (float, default=None): value to use for the central value.
    If not provided, will default to [Uniform_Around.value](Uniform_Around.value.md).  If
    that is not set, then an error will be raised.

Returns
----------
* [Uniform](Uniform.md) object

