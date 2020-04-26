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




    4.260728995561935




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




    array([4.78309535])




```python
mvh_a.sample(size=3)
```




    array([3.50506257, 5.88685093, 5.18974214])




```python
mvh_a.bins
```




    array([-1.49088376, -0.61949778,  0.25188821,  1.1232742 ,  1.99466019,
            2.86604618,  3.73743216,  4.60881815,  5.48020414,  6.35159013,
            7.22297611,  8.0943621 ,  8.96574809,  9.83713408, 10.70852006,
           11.57990605])




```python
mvh_a.density
```




    array([4.19251167e-05, 5.37798048e-04, 3.86289351e-03, 1.99158761e-02,
           7.12134249e-02, 1.73769489e-01, 2.96085294e-01, 3.50197608e-01,
           2.85108142e-01, 1.61436276e-01, 6.25739595e-02, 1.72644739e-02,
           3.25570216e-03, 3.75880356e-04, 5.49363598e-05])




```python
out = mvh_a.plot(show=True, bins=10)
```


![png](multivariate_slice_files/multivariate_slice_30_0.png)



```python
out = mvh_a.to_univariate().plot(show=True)
```


![png](multivariate_slice_files/multivariate_slice_31_0.png)

