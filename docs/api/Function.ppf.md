### [Function](Function.md).ppf (function)


```py

def ppf(self, q, unit=None, as_quantity=False, wrap_at=None)

```



Expose the percent point function (ppf; iverse of cdf - percentiles) at
values of `q`.

See [scipy docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.ppf.html)

This method is just a wrapper around the scipy.stats method on
[Function.dist_constructor_object](Function.dist_constructor_object.md) with unit-conversions, support for
quantity objects, and wrapping done on the returned result.

See also:

* [Function.pdf](Function.pdf.md)
* [Function.cdf](Function.cdf.md)
* [Function.sample](Function.sample.md)

Arguments
----------
* `q` (float or array): percentiles at which to expose the ppf
* `unit` (astropy.unit, optional, default=None): unit of the exposed
    values.  If None or not provided, will assume they're provided in
    [Function.unit](Function.unit.md).
* `as_quantity` (bool, optional, default=False): whether to return an
    astropy quantity object instead of just the value.  Astropy must
    be installed.
* `wrap_at` (float, None, or False, optional, default=None): value to
    use for wrapping.  See [Function.wrap](Function.wrap.md).  If not provided or None,
    will use the value from [Function.wrap_at](Function.wrap_at.md).  Note: wrapping is
    computed before changing units, so `wrap_at` must be provided
    according to [Function.unit](Function.unit.md) not `unit`.

Returns
---------
* (float or array) ppf values of the same type/shape as `q`

