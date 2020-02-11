### [BaseMultivariateSliceDistribution](BaseMultivariateSliceDistribution.md).to (method)


```py

def to(self, unit)

```



Convert to different units.  This creates a copy and returns the
new distribution with the new units.  Astropy is required in order to
set and/or use units.

See also:

* [BaseMultivariateSliceDistribution.unit](BaseMultivariateSliceDistribution.unit.md)

Arguments
------------
* `unit` (astropy.unit object): unit to use in the new distribution.
    The current units (see [BaseMultivariateSliceDistribution.unit](BaseMultivariateSliceDistribution.unit.md)) must be able to
    convert to the requested units.

Returns
------------
* the new distribution object

Raises
-----------
* ImportError: if astropy dependency is not met.

