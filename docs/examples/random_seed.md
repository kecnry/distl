

```python
import npdists
import numpy as np
```


```python
g = npdists.gaussian(10, 2)
```

npdists obeys the seed set in `np.random.seed`.


```python
np.random.seed(1234)
g.sample()
```




    10.942870327464986




```python
np.random.seed(1234)
g.sample()
```




    10.942870327464986



Alternatively, pass `seed` to [sample](../api/BaseDistribution.sample.md), [plot](../api/BaseDistribution.plot.md), or [plot_sample](../api/BaseDistribution.plot_sample.md).


```python
g.sample(seed=1234)
```




    10.942870327464986




```python
g.sample()
```




    7.618048610587071



The random seed is respected for all distribution types, including [Histogram](../api/Histogram.md).


```python
h = g.to_histogram()
```


```python
h.sample()
```




    8.57624521281888




```python
h.sample(seed=1234)
```




    8.7221165939664




```python
h.sample(seed=1234)
```




    8.7221165939664


