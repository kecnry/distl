### [Delta](Delta.md).uncertainties (function)


```py

def uncertainties(self, sigma=1, tex=False)

```



Expose (zero by default) uncertainties for the distribution(s) at a given
value of `sigma`.

Arguments
-----------
* `sigma` (int, optional, default=1): number of standard deviations to
    expose - will still give zero uncertainty!
* `tex` (bool, optional, default=False): return as a formatted latex
    string.

Returns
---------
* if not `tex`: a list of triplets where each triplet is lower, median, upper
* if `tex`: [Latex](Latex.md) object with [Latex.as_latex](Latex.as_latex.md) and [Latex.as_string](Latex.as_string.md) properties.

