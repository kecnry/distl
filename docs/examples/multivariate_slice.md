```python
import distl
import numpy as np
```

# Multivariate Gaussian

First we'll create a [multivariate gaussian](../api/MVGaussian.md) distribution by providing the means and covariances of three parameters.


```python
mvg = distl.mvgaussian([5,10, 12], 
                       np.array([[ 2,  1, -1], 
                                 [ 1,  2,  1], 
                                 [-1,  1,  2]]),
                       allow_singular=True,
                       labels=['a', 'b', 'c'])
```


```python
fig = mvg.plot(show=True)
```


![png](multivariate_slice_files/multivariate_slice_4_0.png)



```python
mvg_a = mvg.slice('a')
```


```python
mvg_a
```




    <distl.mvgaussianslice dimension=0 mean=[5, 10, 12] cov=[[ 2  1 -1]
     [ 1  2  1]
     [-1  1  2]] allow_singular=True label=a)>




```python
mvg_a.multivariate
```




    <distl.mvgaussian mean=[5, 10, 12] cov=[[ 2  1 -1]
     [ 1  2  1]
     [-1  1  2]] allow_singular=True labels=['a', 'b', 'c']>




```python
mvg_a.dimension
```




    0




```python
mvg_a.label
```




    'a'



The sliced object acts more or less as the univariate version of the multivariate distribution.


```python
mvg_a.loc
```




    5




```python
mvg_a.scale
```




    1.4142135623730951



Sampling draws from the underlying multivariate distribution but only returns the value for the requested dimension.  This means that covariances can be maintained (when using [DistributionCollection](collections.md) or carefully managing the random seeds manually).


```python
mvg_a.sample()
```




    7.455968009585329




```python
out = mvg_a.plot(show=True)
```


![png](multivariate_slice_files/multivariate_slice_15_0.png)


The exposed univariate methods (pdf, cdf, etc) are based on the univariate version (with the exception of ppf, which is disabled).  If you want the probability of drawing a value of 'a', given some values of 'b' and 'c' (for example), then must pass those three values to the underlying multivariate distribution.

**NOTE**: currently there is no ability to plot_pdf of a with fixed values of b and c.... maybe that would be a better use of "slice" and use "flatten" for this current behavior?


```python
out = mvg_a.plot_pdf(show=True)
```


![png](multivariate_slice_files/multivariate_slice_17_0.png)



```python
out = mvg_a.multivariate.plot(show=True)
```


![png](multivariate_slice_files/multivariate_slice_18_0.png)



```python
g_a = mvg_a.to_univariate()
# same as mvg.to_univariate(dimension='a')
```


```python
g_a
```




    <distl.gaussian loc=5.0 scale=1.4142135623730951 label=a>




```python
out = g_a.plot(show=True)
```


![png](multivariate_slice_files/multivariate_slice_21_0.png)



```python
mvh = mvg.to_mvhistogram()
```

# Multivariate Histogram


```python
out = mvh.plot(show=True)
```


![png](multivariate_slice_files/multivariate_slice_24_0.png)



```python
mvh_a = mvh.slice('a')
```


```python
mvh_a.sample()
```




    array([7.39157786])




```python
mvh_a.sample(size=3)
```




    array([7.20360738, 6.20109814, 4.13342284])




```python
mvh_a.bins
```




    array([-2.00694623, -1.06709382, -0.12724141,  0.812611  ,  1.7524634 ,
            2.69231581,  3.63216822,  4.57202063,  5.51187304,  6.45172545,
            7.39157786,  8.33143027,  9.27128268, 10.21113509, 11.1509875 ,
           12.09083991])




```python
mvh_a.density
```




    array([8.04597982e-06, 1.60919596e-04, 1.83314240e-03, 1.26402343e-02,
           5.42674519e-02, 1.54812698e-01, 2.87132859e-01, 3.48774451e-01,
           2.76793775e-01, 1.43459820e-01, 4.85655342e-02, 1.08486628e-02,
           1.54348713e-03, 1.43486640e-04, 1.20689697e-05])




```python
out = mvh_a.plot(show=True, bins=10)
```


![png](multivariate_slice_files/multivariate_slice_30_0.png)



```python
out = mvh_a.to_univariate().plot(show=True)
```


![png](multivariate_slice_files/multivariate_slice_31_0.png)



```python

```
