### [MVHistogramSlice](MVHistogramSlice.md).uncertainties (function)


```py

def uncertainties(self, sigma=1, tex=False)

```



Expose the uncertainties by calling [MVHistogramSlice.multivariate](MVHistogramSlice.multivariate.md) and then
passing [MVHistogramSlice.dimension](MVHistogramSlice.dimension.md), `sigma` and `tex` to the respective
`uncertainties` function.

