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




    4.44817691374605




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




    4.630422729756179




```python
h.ppf(0.5)
```




    5.020110511531116




```python
h.mean()
```




    5.004835016893125




```python
h.ppf([0.25, 0.5, 0.75])
```




    array([3.56834335, 5.02011051, 6.38641965])




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
