### [MVGaussian](MVGaussian.md).distribution (method)


```py

def distribution(self, x, unit=None)

```



Give the density (y) values of the underlying distribution for a given
array of values (x).

Arguments
----------
* `x` (array): x-values at which to compute the densities.  If `unit` is
    not None, the value of `x` are assumed to be in the original units
    [MVGaussian.unit](MVGaussian.unit.md), not `unit`.
* `unit` (astropy.unit, optional, default=None): unit of the values
    in `x`.  If None or not provided, will assume they're provided in
    [MVGaussian.unit](MVGaussian.unit.md).

Returns
---------
* array: array of density/y values.

