### [Uniform](Uniform.md).uncertainties (function)


```py

def uncertainties(self, sigma=1, tex=False, unit=None)

```



Expose (symmetric) uncertainties for the distribution(s) at a given
value of `sigma`.

Arguments
-----------
* `sigma` (int, optional, default=1): number of standard deviations to
    expose.
* `tex` (bool, optional, default=False): return as a formatted latex
    string.
* `unit` (astropy.unit, optional, default=None): unit of the values
    to expose.  If None or not provided, will assume they're in
    [Uniform.unit](Uniform.unit.md).

Returns
---------
* if not `tex`: a list of triplets where each triplet is lower, median, upper
* if `tex`: [Latex](Latex.md) object with [Latex.as_latex](Latex.as_latex.md) and [Latex.as_string](Latex.as_string.md) properties.

