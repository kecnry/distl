### [MVSamplesSlice](MVSamplesSlice.md).to (function)


```py

def to(self, unit)

```



Convert to different units.  This creates a copy and returns the
new distribution with the new units.  Astropy is required in order to
set and/or use units.

See also:

* [MVSamplesSlice.unit](MVSamplesSlice.unit.md)
* [MVSamplesSlice.to_si](MVSamplesSlice.to_si.md)
* [MVSamplesSlice.to_solar](MVSamplesSlice.to_solar.md)

Arguments
------------
* `unit` (astropy.unit object): unit to use in the new distribution.
    The current units (see [MVSamplesSlice.unit](MVSamplesSlice.unit.md)) must be able to
    convert to the requested units.

Returns
------------
* the new distribution object

Raises
-----------
* ImportError: if astropy dependency is not met.

