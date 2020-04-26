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




    10.789669535659701



# Array with Provided Length


```python
g.sample(10)
```




    array([ 9.09694541,  9.31352028, 10.40406612, 10.52130123, 10.3764356 ,
           10.93701938,  8.43606923, 10.53048898,  8.8298526 , 11.85001243])



# Array with Provided Shape


```python
g.sample((10,2))
```




    array([[ 9.33015946, 10.31420464],
           [ 8.41161393,  9.17433621],
           [ 5.73650174, 10.63096007],
           [ 8.52208797, 10.69091009],
           [ 7.70444445, 12.1848834 ],
           [11.26853669,  8.33741499],
           [ 8.56517628, 10.12439032],
           [ 7.41173352, 10.66900302],
           [ 8.45315491,  8.40058422],
           [11.64554389,  9.8042616 ]])



See [sample API docs](../api/BaseDistribution.sample.md) for more options.
