### [npdists](npdists.md).function (function)


```py

def function(func, unit, label, *args)

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
* `*args`: all additional positional arguments will be passed on to
    `func` when sampling.  These can be, but are not limited to,
    other distribution objects.

Returns
---------
* a [Function](Function.md) object.

