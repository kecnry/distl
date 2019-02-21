### [npdists](npdists.md).function (function)


```py

def function(func, unit, label, wrap_at, *args)

```



Create a [Function](Function.md) distribution from some callable function and
any number of arguments, including distribution objects.


Arguments
----------
* `func` (callable function): the callable function to be called to
    sample the distribution.
* `unit` (astropy.units object or None): the units of the provided values.
* `label` (string or None): a label for the distribution.  This is used
    for the x-label while plotting the distribution, as well as a shorthand
    notation when creating a [Composite](Composite.md) distribution.
* `wrap_at` (float or False or None): value to wrap all
    sampled values.  If None, will default to 0-2pi if `unit` is angular
    (0-360 for degrees), or 0-1 if `unit` is cycles.  If False, will not wrap.
    See [Function.wrap_at](Function.wrap_at.md) and [Function.wrap](Function.wrap.md) for more details.
* `*args`: all additional positional arguments will be passed on to
    `func` when sampling.  These can be, but are not limited to,
    other distribution objects.

Returns
---------
* a [Function](Function.md) object.

