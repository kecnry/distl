### [MVHistogramSlice](MVHistogramSlice.md).to (function)


```py

def to(self, unit)

```



Convert to different units.  This creates a copy and returns the
new distribution with the new units.  Astropy is required in order to
set and/or use units.

See also:

* [MVHistogramSlice.unit](MVHistogramSlice.unit.md)
* [MVHistogramSlice.to_si](MVHistogramSlice.to_si.md)
* [MVHistogramSlice.to_solar](MVHistogramSlice.to_solar.md)

Arguments
------------
* `unit` (astropy.unit object): unit to use in the new distribution.
    The current units (see [MVHistogramSlice.unit](MVHistogramSlice.unit.md)) must be able to
    convert to the requested units.

Returns
------------
* the new distribution object

Raises
-----------
* ImportError: if astropy dependency is not met.

