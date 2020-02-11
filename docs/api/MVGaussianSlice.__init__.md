### [MVGaussianSlice](MVGaussianSlice.md).__init__ (function)


```py

def __init__(self, multivariate, dimension)

```



BaseDistribution is the parent class for all distributions and should
not be used directly by the user.

Any subclass distribution should override the init but call this via
super.

For example:

```py
def __init__(self, start, stop, step):
    super(MyClass, self).__init__(('start', start, is_float), ('stop', stop, is_float), ('step', step, is_float))
```

All of these "descriptors" will then be available to get and set via
their attribute names

