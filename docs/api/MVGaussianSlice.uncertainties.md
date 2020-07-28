### [MVGaussianSlice](MVGaussianSlice.md).uncertainties (function)


```py

def uncertainties(self, sigma=1, tex=False)

```



Expose the uncertainties by calling [MVGaussianSlice.multivariate](MVGaussianSlice.multivariate.md) and then
passing [MVGaussianSlice.dimension](MVGaussianSlice.dimension.md), `sigma` and `tex` to the respective
`uncertainties` function.

