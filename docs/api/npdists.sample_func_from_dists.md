### [npdists](npdists.md).sample_func_from_dists (function)


```py

def sample_func_from_dists(dists, func, x, N=1000, func_kwargs={})

```



Draw samples from a callable function.

See also:

* [npdists.plot_func_from_dists](npdists.plot_func_from_dists.md)

Arguments
-----------
* `dists` (list or tuple of distribution objects): distribution objects from
    which to sample.
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
* ImportError: if scipy is not imported

