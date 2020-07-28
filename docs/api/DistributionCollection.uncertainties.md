### [DistributionCollection](DistributionCollection.md).uncertainties (function)


```py

def uncertainties(self, sigma=1, tex=False)

```



Expose (asymmetric or symmetric) uncertainties for the distribution(s) at a given
value of `sigma`.

This just loops over the individual [DistributionCollection.dists](DistributionCollection.dists.md)
and calls uncertainties on each.  See:

* [Composite.uncertainties](Composite.uncertainties.md)
* [Delta.uncertainties](Delta.uncertainties.md)
* [Function.uncertainties](Function.uncertainties.md)
* [Gaussian.uncertainties](Gaussian.uncertainties.md)
* [Samples.uncertainties](Samples.uncertainties.md)
* [Histogram.uncertainties](Histogram.uncertainties.md)
* [MVGaussian.uncertainties](MVGaussian.uncertainties.md)
* [MVHistogram.uncertainties](MVHistogram.uncertainties.md)
* [MVSamples.uncertainties](MVSamples.uncertainties.md)

Arguments
-----------
* `sigma` (int, optional, default=1): number of standard deviations to
    expose.
* `tex` (bool, optional, default=False): return as a formatted latex
    string.

Returns
---------
* if not `tex`: a list of triplets where each triplet is lower, median, upper
* if `tex`: [Latex](Latex.md) object with [Latex.as_latex](Latex.as_latex.md) and [Latex.as_string](Latex.as_string.md) properties.

