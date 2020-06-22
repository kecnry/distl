### [MVHistogram](MVHistogram.md).plot_sample (function)


```py

def plot_sample(self, **kwargs)

```



Arguments
---------
* `dimension`
* `label`
* `unit`
* `wrap_at`
* `xlabel`
* `samples`
* `draw_sigmas` (tuple, None, or bool, optional, default=None): if True,
    will default to (1,2,3).  If False, `quantiles` and `levels` will
    not be plotted.  If None, `quantiles` and `levels` will be passed
    directly to [corner.corner](https://corner.readthedocs.io/en/latest/api.html#corner.corner).
    If provided as a list or tuple, then `quantiles` will be set to the
    appropriate quantile for the first sigma in the passed list and
    `levels` will be set to the appropriate 2-D volume levels for each
    item in the list (see `levels` below).
* `quantiles` (tuple or None, optional, default=(0.16, 0.84)): passed
    to [corner.corner](https://corner.readthedocs.io/en/latest/api.html#corner.corner):
    "A list of fractional quantiles to show on the 1-D histograms as
    vertical dashed lines."  Ignored if `draw_sigmas` is not None.
* `levels` (tuple or None, optional, default=(1-np.exp(-0.5))): passed
    to [corner.corner](https://corner.readthedocs.io/en/latest/api.html#corner.corner)
    see [corner: a note about sigmas](https://corner.readthedocs.io/en/latest/pages/sigmas.html).
    Ignored if `draw_sigmas` is not None.

* `**kwargs`: additional kwargs are passed to [corner.corner](https://corner.readthedocs.io/en/latest/api.html#corner.corner)

