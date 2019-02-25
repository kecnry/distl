

```python
import npdists
```


```python
g = npdists.gaussian(10, 2)
```

# Single Value


```python
g.sample()
```




    13.217041997434517



# Array with Provided Length


```python
g.sample(10)
```




    array([ 8.07893271, 12.51150027,  7.56756268,  7.29151051,  5.55049747,
            8.67495845, 11.61104165, 10.11544651, 11.96864228, 10.54677169])



# Array with Provided Shape


```python
g.sample((10,2))
```




    array([[12.6637285 ,  7.79738486],
           [ 8.17135149,  8.80355407],
           [ 9.59770103,  9.77390044],
           [ 7.63640789, 12.83637633],
           [11.45185415,  9.61588616],
           [ 9.34486669,  6.7753359 ],
           [ 8.57059685,  6.13572224],
           [ 6.19055418, 10.57607297],
           [12.0645297 ,  8.842074  ],
           [10.40693098,  9.75658836]])



See [sample API docs](../api/BaseDistribution.sample.md) for more options.
