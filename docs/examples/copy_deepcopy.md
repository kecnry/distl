```python
import distl
import numpy as np
```

# Copy vs Deepcopy

`distl` assigns each distribution a `uniqueid` which tracks whether copies of underlying distributions should be treated as from the same underlying distribution or independent.

Let's first create a [gaussian](../api/Gaussian.md) distribution and access its automatically assigned random `uniqueid`.



```python
d = distl.gaussian(5, 1)
```


```python
print(d.uniqueid)
```

    qXmRdLGhfHpHnaDtVqhD


When calling [copy](../api/BaseDistribution.copy.md), this `uniqueid` is retained which links the new copy to the original.


```python
print(d.copy().uniqueid)
```

    qXmRdLGhfHpHnaDtVqhD


Calling [deepcopy](../api/BaseDistribution.deepcopy.md), however, assigns a new random `uniqueid`, effectively unlinking the two distribution objects.


```python
print(d.deepcopy().uniqueid)
```

    tRqFpWAZWlZvWbzHHrYQ


# Implications in CompositeDistributions and math operations

By default, using math operators on distributions will use [copy](../api/BaseDistribution.copy.md).  To force unlinking the distributions, you must call [deepcopy](../api/BaseDistribution.deepcopy.md) manually.

Here we'll show that the original distribution and the distribution after applying math operators maintain the same `uniqueid`, by default, and are therefore sampled simultaneously.


```python
d = distl.gaussian(5, 1)
```


```python
print(d.uniqueid)
```

    yzjcXLHzImrgJDsJGKms



```python
print((5*d).uniqueid)
```

    yzjcXLHzImrgJDsJGKms


We can see the implications of this in action when a [CompositeDistribution](../api/CompositeDistribution.md) contains two or more "copies" of the same underlying distribution.

In this case, we'll create a distribution for `d + 5*d`.  By default, the underlying references to `d` will remain linked when creating the CompositeDistribution (i.e. when sampling the CompositeDistribution, the same value will be drawn from all instances of `d` before applying the math operators between them).


```python
comp = d + 5*d
```


```python
_ = comp.plot(show=True)
```


![png](copy_deepcopy_files/copy_deepcopy_14_0.png)


If we instead force the two instances to be unlinked by using a deepcopy, the two references to `d` are sampled independently before applying the math operators.  Here we can see that this does result in a slightly different distribution (in the case of simple operations between gaussian distributions, this only affects the spread on the resulting distribution).


```python
comp_indep = d + 5*d.deepcopy()
```


```python
_ = comp_indep.plot(show=True)
```


![png](copy_deepcopy_files/copy_deepcopy_17_0.png)


# Implications in Function Distributions

Similarly, a [Function Distribution](../api/Function.md) will sample from any input distributions following these same rules.  This does work even if `vectorized=False`, although it does get more computationally expensive.


```python
def custom_math(a, b):
    return a + 5*b
```


```python
f = distl.function(custom_math, args=(d, d))
```


```python
_ = f.plot(show=True)
```


![png](copy_deepcopy_files/copy_deepcopy_21_0.png)



```python
f_indep = distl.function(custom_math, args=(d, d.deepcopy()))
```


```python
_ = f_indep.plot(show=True)
```


![png](copy_deepcopy_files/copy_deepcopy_23_0.png)


# Implications in DistributionCollections

This sampling logic can be seen even more clearly in the corner plots within [DistributionCollections](../api/DistributionCollection.md).  First we'll create a collection with `d` and `5*d`.  Since this creates a linked copy by default, we can see that the resulting samples strictly follow a 1:1 relationship.


```python
dc = distl.DistributionCollection(d, comp, f)
```


```python
_ = dc.plot(show=True)
```


![png](copy_deepcopy_files/copy_deepcopy_27_0.png)


If instead we force a deepcopy, both resulting Gaussian distributions are sampled independently from each other and no longer show this correlation.


```python
dc_indep = distl.DistributionCollection(d, comp_indep, f_indep)
```


```python
_ = dc_indep.plot(show=True)
```


![png](copy_deepcopy_files/copy_deepcopy_30_0.png)



```python

```
