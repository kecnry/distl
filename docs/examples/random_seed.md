```python
import distl
import numpy as np
```


```python
g = distl.gaussian(10, 2)
```

**distl** obeys the seed set in `np.random.seed`.


```python
np.random.seed(1234)
g.sample()
```




    8.255378595638142




```python
np.random.seed(1234)
g.sample()
```




    8.255378595638142



Alternatively, pass `seed` to [sample](../api/BaseDistribution.sample.md), [plot](../api/BaseDistribution.plot.md), or [plot_sample](../api/BaseDistribution.plot_sample.md).


```python
g.sample(seed=1234)
```




    8.255378595638142




```python
g.sample()
```




    10.62204778579605



The random seed is respected for all distribution types, including [Histogram](../api/Histogram.md).


```python
h = g.to_histogram()
```


```python
h.sample()
```




    11.062801594324343




```python
h.sample(seed=1234)
```




    7.253562541644463




```python
h.sample(seed=1234)
```




    7.253562541644463



If you want a random seed to be used to multiple calls in the same execution, you can access a random array of integers via [get_random_seed](../api/distl.get_random_seed.md) which can then be passed on to either np.random.seed or sample.


```python
seed = distl.get_random_seed()
```


```python
g.sample(seed=seed)
```




    6.561067923451439




```python
g.sample(seed=seed)
```




    6.561067923451439




```python
g.sample(seed=distl.get_random_seed())
```




    11.27810575248316




```python

```
