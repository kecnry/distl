### [MVGaussianSlice](MVGaussianSlice.md).__init__ (function)


```py

def __init__(self, multivariate, dimension, unit=None, label=None, label_latex=None, wrap_at=None, uniqueid=None)

```



BaseDistribution is the parent class for all distributions and should
not be used directly by the user.

Any subclass distribution should override the init but call this via
super.  See [Gaussian.__init__](Gaussian.__init__.md) for an example for subclassing.

