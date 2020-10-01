### [MVHistogram](MVHistogram.md).plot_sample (function)


```py

def plot_sample(self, size=100000.0, **kwargs)

```



Arguments
---------
* `dimension` (string or int, optional, default=None): choose a single
    dimension to plot.
* `label` (string, optional, default=None): override the label on the
    x-axis.  If not provided or None, will use [MVHistogram.label](MVHistogram.label.md).  Will
    only be used if `show=True`.  Unit will automatically be appended.
    Will be ignored if `xlabel` is provided.
* `unit` (astropy.unit, optional, default=None): units to use along
    the x-axis.  Astropy must be installed.  If `samples` is provided,
    the passed values will be assumed to be in the correct units.
* `wrap_at` (float, None, or False, optional, default=None): value to
    use for wrapping.  See [MVHistogram.wrap](MVHistogram.wrap.md).  If not provided or None,
    will use the value from [MVHistogram.wrap_at](MVHistogram.wrap_at.md).  Note: wrapping is
    computed before changing units, so `wrap_at` must be provided
    according to [MVHistogram.unit](MVHistogram.unit.md) not `unit`.  Will be ignored
    if `samples` is provided.
* `xlabel` (string, optional, default=None): override the label on the
    x-axis without appending the unit.  Will override `label`.
* `samples` (array, optional, default=None): plot specific sampled
    values instead of calling [MVHistogram.sample](MVHistogram.sample.md) internally.  Will override
    `size`.
* `plot_uncertainties` (tuple or bool, optional, default=True): if True,
    will default to (1,2,3).
    If provided as a list or tuple, then `quantiles` shown in the 1D
    histograms will be set to the appropriate quantile for the first
    sigma in the passed list/tuple and will be used for the uncertainties
    in the axes titles. `levels` will be set to the appropriate 2-D volume levels for each
    item in the list and used as contours. See [MVHistogram.uncertainties](MVHistogram.uncertainties.md).
* `**kwargs`: additional kwargs are passed to [corner.corner](https://corner.readthedocs.io/en/latest/api.html#corner.corner)

Returns
------------
* the figure from [corner.corner](https://corner.readthedocs.io/en/latest/api.html#corner.corner)

