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




    9.363830414799237



# Array with Provided Length


```python
g.sample(10)
```




    array([ 8.13594017,  7.55094737, 10.01511405, 11.35780328,  9.28976051,
            9.70241559,  9.70012331, 10.23110774, 12.11860968, 13.76593667])



# Array with Provided Shape


```python
g.sample((10,2))
```




    array([[ 9.29652028,  7.96911427],
           [11.82821468,  6.80802023],
           [13.6460268 , 12.84581522],
           [11.43470535, 11.19477575],
           [11.01194094, 13.02438131],
           [11.69820643, 12.08105554],
           [11.55445203, 11.22269268],
           [10.34630208,  6.59967548],
           [ 7.82689357,  8.99333027],
           [10.90310932,  9.8181325 ]])



See [sample API docs](../api/BaseDistribution.sample.md) for more options.
