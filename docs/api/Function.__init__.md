### [Function](Function.md).__init__ (method)


```py

def __init__(self, func, unit, label, wrap_at, *args)

```



Create a [Function](Function.md) distribution from some callable function and
any number of arguments, including distribution objects.

This can also be created from a function at the top-level as:

* [npdists.function](npdists.function.md)

Arguments
----------
* `func` (callable function): the callable function to be called to
    sample the distribution.
* `unit` (astropy.units object or None): the units of the provided values.
* `label` (string or None): a label for the distribution.  This is used
    for the x-label while plotting the distribution, as well as a shorthand
    notation when creating a [Composite](Composite.md) distribution.
* `wrap_at` (float, None, or False, optional, default=None): value to
    use for wrapping.  If None and `unit` are angles, will default to
    2*pi (or 360 degrees).  If None and `unit` are cycles, will default
    to 1.0.
* `*args`: all additional positional arguments will be passed on to
    `func` when sampling.  These can be, but are not limited to,
    other distribution objects.

Returns
---------
* a [Function](Function.md) object.

