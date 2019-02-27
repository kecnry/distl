### [Composite](Composite.md).logp (method)


```py

def logp(self, x, unit=None)

```



Give the log probability of the underlying distribution for a given value
x.

Arguments
----------
* `x` (float or array array): x-values at which to compute the logps.
    If `unit` is not None, the value of `x` are assumed to be in the
    original units
    [Composite.unit](Composite.unit.md), not `unit`.
* `unit` (astropy.unit, optional, default=None): unit of the values
    in `x`.  If None or not provided, will assume they're provided in
    [Composite.unit](Composite.unit.md).

Returns
---------
* array: array of density/y values.

