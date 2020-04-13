### [MVSamples](MVSamples.md).sample (function)


```py

def sample(self, size=None, dimension=None, seed=None, cache_sample=True)

```



Sample from the  samples ([MVSamples.samples](MVSamples.samples.md) if [MVSamples.weights](MVSamples.weights.md)
is not provided, otherwise [MVSamples.samples_weighted](MVSamples.samples_weighted.md))

Arguments
----------
* `size`
* `dimension`
* `seed` (int, optional): seed to pass to np.random.seed
    prior to sampling.
* `cache_sample` (bool, optional, default=True): whether to override the
    existing [MVSamples.cached_sample](MVSamples.cached_sample.md).

