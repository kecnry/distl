### [DistributionCollection](DistributionCollection.md).plot_func (function)


```py

def plot_func(self, func, x, N=1000, func_kwargs={}, show=False)

```



Draw samples from a callable function and plot.

The passed callable `func` will be called with arguments `x` followed by
the individually drawn values from each distribution in `dists` (in order
provided) and then any additional `func_kwargs`.

See also:

* [DistributionCollection.sample_func](DistributionCollection.sample_func.md)
* [DistributionCollection.sample](DistributionCollection.sample.md)

Arguments
-----------
* `func` (callable): callable function
* `x` (array like): x values to pass to `func`.
* `N` (int, optional, default=1000): number of samples to draw.
* `func_kwargs` (dict, optional): additional keyword arguments to pass to
    `func`.
* `show` (bool, optional, default=False): whether to call plt.show()

Returns
-----------
* list of created matplotlib artists

Raises
-----------
* ImportError: if matplotlib is not imported

