### [MVGaussian](MVGaussian.md).ppf (function)


```py

def ppf(self, q, samples=None)

```



Expose the percent point function (ppf; iverse of cdf - percentiles) at
values of `q` from a set of `samples`.  If `samples` is not provided
or None, [MVGaussian.sample](MVGaussian.sample.md) will be called first with `size=1e6`.

See also:
* [MVGaussian.sample](MVGaussian.sample.md)

Arguments
----------
* `q` (float or array): percentiles at which to expose the ppf
* `samples` (array or None, optional, default=None): samples to use
    to determine the ppf.  If not provided, [MVGaussian.sample](MVGaussian.sample.md) will be
    called with `size=1e6`.

Returns
---------
* (float or array) ppf values of the same type/shape as `q`

