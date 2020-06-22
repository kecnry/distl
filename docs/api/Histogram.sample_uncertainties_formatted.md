### [Histogram](Histogram.md).sample_uncertainties_formatted (function)


```py

def sample_uncertainties_formatted(self, sigma=1, samples=None)

```



Expose (asymmetric) uncertainties for the distribution(s) at a given
value of `sigma`.

This first determines the appropriate `quantiles` to pass to
[Histogram.sample_quantiles](Histogram.sample_quantiles.md) using scipy.state.norm.cdf([`-sigma`, `0`, `sigma`])
and then formats those into a Latex friendly representation.

See also:
* [Histogram.sample_quantiles](Histogram.sample_quantiles.md)

Arguments
-----------
* `sigma` (int, optional, default=1): number of standard deviations to
    expose.
* `samples` (array-type, optional, default=None): samples to use.  If
    not provided, [Histogram.sample](Histogram.sample.md) will be called with `size=1e6`.

Returns
---------
* [Latex](Latex.md) object with [Latex.as_latex](Latex.as_latex.md) and [Latex.as_string](Latex.as_string.md) properties.
