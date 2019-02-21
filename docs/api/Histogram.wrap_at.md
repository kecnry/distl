### [Histogram](Histogram.md).wrap_at (property)




Value at which to wrap all sampled values.  If [Histogram.unit](Histogram.unit.md) is not None,
then the value of `wrap_at` is the same as the set units.

If `False`: will not wrap
If `None`: will wrap on range 0-2pi (0-360 deg) if [Histogram.unit](Histogram.unit.md) are angular
    or 0-1 if [Histogram.unit](Histogram.unit.md) are cycles.
If float: will wrap on range 0-`wrap_at`.

See also:

* [Histogram.get_wrap_at](Histogram.get_wrap_at.md)
* [Histogram.wrap](Histogram.wrap.md)

Returns
---------
* (float or None)

