### [distl](distl.md).get_random_seed (function)


```py

def get_random_seed()

```



Return a random seed which can be passed to [BaseDistribution.sample](BaseDistribution.sample.md).

This allows for using a consistent/reproducible but still random seed instead
of manually passing some arbitrary integer (like 1234).

Returns
------------
* (array): array of 624 32-bit integers which can be used as a seed to
    np.random.seed or [BaseDistribution.sample](BaseDistribution.sample.md).

