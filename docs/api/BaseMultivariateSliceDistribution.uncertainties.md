### [BaseMultivariateSliceDistribution](BaseMultivariateSliceDistribution.md).uncertainties (function)


```py

def uncertainties(self, sigma=1, tex=False)

```



Expose the uncertainties by calling [BaseMultivariateSliceDistribution.multivariate](BaseMultivariateSliceDistribution.multivariate.md) and then
passing [BaseMultivariateSliceDistribution.dimension](BaseMultivariateSliceDistribution.dimension.md), `sigma` and `tex` to the respective
`uncertainties` function.

