

```python
import npdists
import numpy as np
```


```python
g = npdists.gaussian(10, 2)
```


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




```python
g.sample()
```




    7.618048610587071




```python
h = g.to_histogram()
```


```python
h.sample()
```




    8.57624521281888




```python
np.random.seed(1234)
h.sample()
```




    8.7221165939664




```python
np.random.seed(1234)
h.sample()
```




    8.7221165939664


