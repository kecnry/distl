```python
import distl
import numpy as np
```


```python
g = distl.gaussian(5,2)
```


```python
g.sample()
```




    7.840031909021584




```python
g.ppf(0.5)
```




    5.0




```python
g.mean()
```




    5.0




```python
g.ppf([0.25, 0.5])
```




    array([3.6510205, 5.       ])




```python
h = g.to_histogram()
```


```python
h.sample()
```




    4.62891909777962




```python
h.ppf(0.5)
```




    5.008495010321001




```python
h.mean()
```




    4.9954240850940215




```python
h.ppf([0.25, 0.5, 0.75])
```




    array([3.53332597, 5.00849501, 6.4209533 ])




```python
distl.uniform(0,10).ppf(0.5)
```




    5.0




```python
distl.delta(0.2).ppf(0.5)
```




    0.2




```python

```
