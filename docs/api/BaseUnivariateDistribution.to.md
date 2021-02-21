### [BaseUnivariateDistribution](BaseUnivariateDistribution.md).to (function)


```py

def to(self, unit, strip_units=False)

```



Convert to different units.  This creates a copy and returns the
new distribution with the new units.  Astropy is required in order to
set and/or use units.

See also:

* [BaseUnivariateDistribution.unit](BaseUnivariateDistribution.unit.md)
* [BaseUnivariateDistribution.to_si](BaseUnivariateDistribution.to_si.md)
* [BaseUnivariateDistribution.to_solar](BaseUnivariateDistribution.to_solar.md)

Arguments
------------
* `unit` (astropy.unit object): unit to use in the new distribution.
    The current units (see [BaseUnivariateDistribution.unit](BaseUnivariateDistribution.unit.md)) must be able to
    convert to the requested units.
* `strip_units` (bool, optional, default=False): whether to strip the
    units from the returned object

Returns
------------
* the new distribution object

Raises
-----------
* ImportError: if astropy dependency is not met.

