### [BaseMultivariateDistribution](BaseMultivariateDistribution.md).wrap (function)


```py

def wrap(self, value, wrap_at=None)

```



Wrap values via modulo:

```py
value % wrap_at
```

See also:

* [BaseMultivariateDistribution.wrap_at](BaseMultivariateDistribution.wrap_at.md)
* [BaseMultivariateDistribution.get_wrap_at](BaseMultivariateDistribution.get_wrap_at.md)

Arguments
------------
* `value` (float or array): values to wrap
* `wrap_at` (float, optional, default=None): value to use for the upper-limit.
    If not provided or None, will use [BaseMultivariateDistribution.wrap_at](BaseMultivariateDistribution.wrap_at.md).  If False,
    will return `value` unwrapped.

Returns
----------
* (float or array): same shape/type as input `value`.

