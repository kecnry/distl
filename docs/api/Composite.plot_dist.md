### [Composite](Composite.md).plot_dist (method)


```py

def plot_dist(self, x, unit=None, wrap_at=None, label=None, show=False, **kwargs)

```



Plot the analytic distribution function.  Requires matplotlib to be installed.

See also:

* [Composite.plot](Composite.plot.md)
* [Composite.plot_sample](Composite.plot_sample.md)
* [Composite.plot_gaussian](Composite.plot_gaussian.md)

Arguments
-----------
* `x` (np array): the numpy array at which to sample the value on the
    x-axis.  If `unit` is not None, the value of `x` are assumed to be
    in the original units [Composite.unit](Composite.unit.md), not `unit`.
* `unit` (astropy.unit, optional, default=None): units to use along
    the x-axis.  Astropy must be installed.
* `wrap_at` (float, None, or False, optional, default=None): value to
    use for wrapping.  See [Composite.wrap](Composite.wrap.md).  If not provided or None,
    will use the value from [Composite.wrap_at](Composite.wrap_at.md).  Note: wrapping is
    computed before changing units, so `wrap_at` must be provided
    according to [Composite.unit](Composite.unit.md) not `unit`.
* `label` (string, optional, default=None): override the label on the
    x-axis.  If not provided or None, will use [Composite.label](Composite.label.md).  Will
    only be used if `show=True`.
* `show` (bool, optional, default=True): whether to show the resulting
    matplotlib figure.
* `**kwargs`: all keyword arguments will be passed on to plt.plot.  Note:
    if wrapping is enabled, either via `wrap_at` or [Composite.wrap_at](Composite.wrap_at.md),
    the resulting line will break when wrapping, resulting in using multiple
    colors.  Sending `color` as a keyword argument will prevent this
    matplotlib behavior.  Calling this through [Composite.plot](Composite.plot.md) with
    `plot_gaussian=True` defaults to sending `color='blue'` through
    the `plot_gaussian_kwargs` argument.

Returns
--------
* the return from plt.plot

Raises
--------
* ImportError: if matplotlib dependency is not met.

