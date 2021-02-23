### [Function](Function.md).sample_args_kwargs (function)


```py

def sample_args_kwargs(self, size=None, seed={}, cache_sample=False)

```



Sample from [Function.args](Function.args.md) and [Function.kwargs](Function.kwargs.md)

See also:

* [Function.sample](Function.sample.md)

Arguments
-----------
* `size` (int or tuple or None, optional, default=None): size/shape of the
    resulting array.
* `seed` (dict, optional, default={}): seeds (as uniqueid: seed pairs) to
    pass to underlying distributions.
* `cache_sample` (bool, optional, default=False): whether to override the
    existing [Function.cached_sample](Function.cached_sample.md).

