### [Gaussian_Around](Gaussian_Around.md).to (function)


```py

def to(self, unit)

```



Convert to different units.  This creates a copy and returns the
new distribution with the new units.  Astropy is required in order to
set and/or use units.

See also:

* [Gaussian_Around.unit](Gaussian_Around.unit.md)
* [Gaussian_Around.to_si](Gaussian_Around.to_si.md)
* [Gaussian_Around.to_solar](Gaussian_Around.to_solar.md)

Arguments
------------
* `unit` (astropy.unit object): unit to use in the new distribution.
    The current units (see [Gaussian_Around.unit](Gaussian_Around.unit.md)) must be able to
    convert to the requested units.

Returns
------------
* the new distribution object

Raises
-----------
* ImportError: if astropy dependency is not met.

