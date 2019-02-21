### [Histogram](Histogram.md).get_wrap_at (method)


```py

def get_wrap_at(self, wrap_at=None)

```



Get the computed value used for wrapping, given `wrap_at` as an optional
override to the attribute [Histogram.wrap_at](Histogram.wrap_at.md).

See also:

* [Histogram.wrap_at](Histogram.wrap_at.md)
* [Histogram.wrap](Histogram.wrap.md)

Arguments
------------
* `wrap_at` (float or False or None, optional, default=None): override
    the value of [Histogram.wrap_at](Histogram.wrap_at.md).

Returns
----------
* The computed wrapping value, accounting for [Histogram.unit](Histogram.unit.md) if `wrap_at`
    is None.

