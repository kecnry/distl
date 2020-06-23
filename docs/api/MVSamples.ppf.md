### [MVSamples](MVSamples.md).ppf (function)


```py

def ppf(self, q)

```



Expose the percent point function (ppf; iverse of cdf - percentiles) at
values of `q` directly from [MVSamples.samples](MVSamples.samples.md) and [MVSamples.weights](MVSamples.weights.md)
using [corner.quantile](https://corner.readthedocs.io/en/latest/api.html#corner.quantile).

See also:

* [MVSamples.pdf](MVSamples.pdf.md)
* [MVSamples.cdf](MVSamples.cdf.md)
* [MVSamples.sample](MVSamples.sample.md)

Arguments
----------
* `q` (float or array): percentiles at which to expose the ppf

Returns
---------
* (float or array) ppf values of the same type/shape as `q`

