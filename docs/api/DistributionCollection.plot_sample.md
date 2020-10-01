### [DistributionCollection](DistributionCollection.md).plot_sample (function)


```py

def plot_sample(self, size=100000.0, **kwargs)

```



Arguments
------------
* `labels`
* `range`
* `plot_uncertainties` (tuple or bool, optional, default=True): if True,
    will default to (1,2,3).
    If provided as a list or tuple, then `quantiles` shown in the 1D
    histograms will be set to the appropriate quantile for the first
    sigma in the passed list/tuple and will be used for the uncertainties
    in the axes titles. `levels` will be set to the appropriate 2-D volume levels for each
    item in the list and used as contours. See [DistributionCollection.uncertainties](DistributionCollection.uncertainties.md).
* `**kwargs`: additional kwargs are passed to [corner.corner](https://corner.readthedocs.io/en/latest/api.html#corner.corner)

