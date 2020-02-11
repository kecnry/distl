```python
import distl
```


```python
g = distl.gaussian(10, 2)
```

# Single Value


```python
g.sample()
```




    11.443571816746996



# Array with Provided Length


```python
g.sample(10)
```




    array([ 9.49565684,  8.8675521 ,  9.19827052, 10.04545421, 11.47262063,
           12.58618471, 10.82845814,  9.37718468,  8.92678708, 10.96833056])



# Array with Provided Shape


```python
g.sample((10,2))
```




    array([[ 8.14803885,  9.96399682],
           [ 8.10415028, 13.53625597],
           [ 9.71480151, 12.85992592],
           [10.09320876, 11.48736323],
           [10.48964987,  7.48370093],
           [10.17449758, 12.31900056],
           [12.275866  , 12.98406454],
           [10.70377134,  9.92967719],
           [ 9.21993244, 10.03651312],
           [ 9.19974877,  8.00902747]])



See [sample API docs](../api/BaseDistribution.sample.md) for more options.
