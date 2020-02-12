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




    2.954209607232361




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




    9.089030111111642




```python
h.ppf(0.5)
```




    4.1367621032365145




```python
h.mean()
```

    /home/kyle/.local/lib/python3.7/site-packages/scipy/stats/_distn_infrastructure.py:1675: IntegrationWarning: The maximum number of subdivisions (50) has been achieved.
      If increasing the limit yields no improvement it is advised to analyze 
      the integrand in order to determine the difficulties.  If the position of a 
      local difficulty can be determined (singularity, discontinuity) one will 
      probably gain from splitting up the interval and calling the integrator 
      on the subranges.  Perhaps a special-purpose integrator should be used.
      return integrate.quad(self._mom_integ1, 0, 1, args=(m,)+args)[0]





    4.152677471447151




```python
h.ppf([0.25, 0.5, 0.75])
```




    array([2.75884038, 4.1367621 , 5.55750496])




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
