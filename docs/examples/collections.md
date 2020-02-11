```python
import distl
import numpy as np
```

First we'll create a [gaussian](../api/gaussian.md), [uniform](../api/uniform.md), and [multivariate gaussian](../api/mvaussian.md) distributions.


```python
g = distl.gaussian(10, 2, label='gaussian')
```


```python
u = distl.uniform(0, 5, label='uniform')
```


```python
mvg = distl.mvgaussian([5,10, 12], 
                       np.array([[ 2,  1, -1], 
                                 [ 1,  2,  1], 
                                 [-1,  1,  2]]),
                       allow_singular=True,
                       labels=['mvg_a', 'mvg_b', 'mvg_c'])
```

Now let's imagine a scenario where we want to draw from the following "parameters": 'gaussian', 'uniform', 'mvg_a', and 'mvg_c' (but let's say we don't want 'mvg_b').  Here we want to *maintain* the covariances between 'mvg_a' and 'mvg_c' while *independently* sampling from 'gaussian' and 'uniform'.

To learn about slicing multivariate distributions, see [multivariate slicing](./multivariate_slice.md).

To do this, we'll create a [DistributionCollection](../api/DistributionCollection.md)


```python
dc = distl.DistributionCollection(g, u, mvg.slice('mvg_a'), mvg.slice('mvg_c'))
```


```python
dc.to_dict()
```




    {'distl': 'DistributionCollection',
     'args': [{'loc': 10.0,
       'scale': 2.0,
       'distl': 'Gaussian',
       'label': 'gaussian'},
      {'low': 0.0, 'high': 5.0, 'distl': 'Uniform', 'label': 'uniform'},
      {'distl': 'MVGaussianSlice',
       'multivariate': {'mean': [5, 10, 12],
        'cov': [[2, 1, -1], [1, 2, 1], [-1, 1, 2]],
        'allow_singular': True,
        'distl': 'MVGaussian',
        'labels': ['mvg_a', 'mvg_b', 'mvg_c']},
       'dimension': 0},
      {'distl': 'MVGaussianSlice',
       'multivariate': {'mean': [5, 10, 12],
        'cov': [[2, 1, -1], [1, 2, 1], [-1, 1, 2]],
        'allow_singular': True,
        'distl': 'MVGaussian',
        'labels': ['mvg_a', 'mvg_b', 'mvg_c']},
       'dimension': 2}]}




```python
distl.from_dict(dc.to_dict())
```




    <distl.distl.DistributionCollection at 0x7f05d2b738d0>




```python
sampled_values = dc.sample()
print(sampled_values)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-8-dd652afc8ae6> in <module>
    ----> 1 sampled_values = dc.sample()
          2 print(sampled_values)


    ~/.local/lib/python3.7/site-packages/distl-0.1.0.dev0-py3.7.egg/distl/distl.py in sample(self, *args, **kwargs)
       2936         sample_kwargs = {k:v for k,v in kwargs.items() if k not in ['seeds']}
       2937         # print("*** seeds: {}, sample_kwargs: {}".format(seeds, sample_kwargs))
    -> 2938         samples = _np.asarray([dist.sample(*args, seed=seeds, **sample_kwargs) for dist in self.distributions]).T
       2939 
       2940         if cache_values:


    ~/.local/lib/python3.7/site-packages/distl-0.1.0.dev0-py3.7.egg/distl/distl.py in <listcomp>(.0)
       2936         sample_kwargs = {k:v for k,v in kwargs.items() if k not in ['seeds']}
       2937         # print("*** seeds: {}, sample_kwargs: {}".format(seeds, sample_kwargs))
    -> 2938         samples = _np.asarray([dist.sample(*args, seed=seeds, **sample_kwargs) for dist in self.distributions]).T
       2939 
       2940         if cache_values:


    TypeError: sample() got an unexpected keyword argument 'seed'



```python
dc.pdf(sampled_values)
```

Now let's consider a more complex example: let's sample from 'gaussian * mvg_a' and 'mvg_c'.  Here we want to covariance between 'mvg_a' and 'mvg_c' respected, even though there is a math operation on the result.


```python
#dc = distl.DistributionCollection(g * mvg.slice('mvg_a'), mvg.slice('mvg_c'))
```


```python
#dc.sample()
```


```python
#dc.pdf()
```


```python

```
