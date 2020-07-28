### [Function](Function.md).__init__ (function)


```py

def __init__(self, func, args, kwargs, vectorized=True, hist_samples=None, unit=None, label=None, label_latex=None, wrap_at=None)

```



Create a [Function](Function.md) distribution from two other distributions.

Arguments
----------
* `func`: callable function that accepts args and kwargs (as floats,
    after being sampled from any distribution objects)
* `args` (list of distribution objects or floats): distribution objects
    or floats to pass as args to `func`.  Any items that are Distribution
    objects will be sampled and passed as floats.
* `kwargs` (dictionary of distribution objects or floats): distribution
    objects or floats to pass as kwargs to `func`.  Any items that are
    Distribution objects will be sampled and passed as floats.
* `vectorized` (bool, optional, default=True): whether `func` supports
    passing arrays to `args` and `kwargs`.
* `hist_samples` (int, optional, default=None): number of samples to draw
    when generating the underlying [Histogram](Histogram.md) distribution used for
    all probability calls.  If not provided or None, this will default
    to 1e6 if `vectorized` or 1e5 if not.  If `func` takes a long time
    or many samples in [Function.sample](Function.sample.md) are rejected and have to be
    re-drawn, it may be necessary to lower `hist_samples`.
* `unit` (astropy.units object, optional): the units returned by `func`.
    Note that any Distribution objects in `args` and `kwargs` should be
    in the appropriate units (as the inputs and outputs to `func` are
    floats and not quantities)
* `label` (string, optional): a label for the distribution.  This is used
    for the x-label while plotting the distribution if `label_latex` is not provided,
    as well as a shorthand notation when creating a [Composite](Composite.md) distribution.
* `label_latex` (string, optional): a latex label for the distribution.  This is used
    for the x-label while plotting.
* `wrap_at` (float, None, or False, optional, default=None): value to
    use for wrapping.  If None and `unit` are angles, will default to
    2*pi (or 360 degrees).  If None and `unit` are cycles, will default
    to 1.0.

Returns
---------
* a [Function](Function.md) object.

