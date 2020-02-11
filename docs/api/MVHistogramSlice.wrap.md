### [MVHistogramSlice](MVHistogramSlice.md).wrap (function)


```py

def wrap(self, value, wrap_at=None)

```



Wrap values via modulo:

```py
value % wrap_at
```

See also:

* [MVHistogramSlice.wrap_at](MVHistogramSlice.wrap_at.md)
* [MVHistogramSlice.get_wrap_at](MVHistogramSlice.get_wrap_at.md)

Arguments
------------
* `value` (float or array): values to wrap
* `wrap_at` (float, optional, default=None): value to use for the upper-limit.
    If not provided or None, will use [MVHistogramSlice.wrap_at](MVHistogramSlice.wrap_at.md).  If False,
    will return `value` unwrapped.

Returns
----------
* (float or array): same shape/type as input `value`.

