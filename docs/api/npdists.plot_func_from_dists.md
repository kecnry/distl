### [npdists](npdists.md).plot_func_from_dists (function)


```py

def plot_func_from_dists(dists, func, x, N=1000, func_kwargs={}, show=False)

```



Draw samples from a callable function and plot.

The passed callable `func` will be called with arguments `x` followed by
the individually drawn values from each distribution in `dists` (in order
provided) and then any additional `func_kwargs`.

See also:
* [npdists.sample_func_from_dists](npdists.sample_func_from_dists.md)
* [npdists.sample_from_dists](npdists.sample_from_dists.md)

Arguments
-----------
* `dists` (list or tuple of distribution objects): distribution objects from
    which to sample.
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
* ImportError: if scipy is not imported

