### [BaseMultivariateDistribution](BaseMultivariateDistribution.md).__init__ (function)


```py

def __init__(self, units=None, labels=None, wrap_ats=None, *args, **kwargs)

```



BaseDistribution is the parent class for all distributions and should
not be used directly by the user.

Any subclass distribution should override the init but call this via
super.  See [Gaussian.__init__](Gaussian.__init__.md) for an example for subclassing.

