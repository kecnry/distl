### [DistributionCollection](DistributionCollection.md).sample_func (function)


```py

def sample_func(self, func, x, N=1000, func_kwargs={})

```



Draw samples from a callable function.

See also:

* [DistributionCollection.plot_func](DistributionCollection.plot_func.md)

Arguments
-----------
* `func` (callable): callable function
* `x` (array like): x values to pass to `func`.
* `N` (int, optional, default=1000): number of samples to draw.
* `func_kwargs` (dict, optional): additional keyword arguments to pass to
    `func`.


Returns
-----------
* an array of models with shape (N, len(x))

Raises
-----------

