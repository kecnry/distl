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
mvg.sample()
```




    array([ 3.55132717,  9.78715395, 13.23582678])




```python
mvg.sample(size=5)
```




    array([[ 5.23033061,  9.06949021, 10.8391596 ],
           [ 5.51617199, 11.37966572, 12.86349373],
           [ 3.85260322,  8.08953995, 11.23693674],
           [ 6.14967157, 10.06814347, 10.9184719 ],
           [ 2.99347865,  9.33717474, 13.34369609]])



and plotting will now show a corner plot (if [corner](https://corner.readthedocs.io/en/latest/) is installed)


```python
fig = mvg.plot(show=True)
```


![png](multivariate_files/multivariate_6_0.png)


# Multivariate Histogram

we can now convert this multivariate gaussian distribution into a [multivariate histogram](../api/MVHistogram.md) distribution (alternatively we could create a histogram directly from a set of samples or chains via [mvhistogram_from_data](../api/distl.mvhistogram_from_data.md).


```python
mvh = mvg.to_mvhistogram(bins=15)
```


```python
fig = mvh.plot(show=True, size=1e6)
```


![png](multivariate_files/multivariate_9_0.png)



```python
np.asarray(mvh.density.shape)
```




    array([15, 15, 15])



Now if we access the means and covariances, we'll see that they are slightly different due to the binning.


```python
mvh.calculate_means()
```




    array([ 4.96800078,  9.96608606, 11.05088341])




```python
mvh.calculate_covariances()
```




    array([[ 2.14976389,  1.00436435, -0.98909508],
           [ 1.00436435,  2.1466647 ,  1.00202299],
           [-0.98909508,  1.00202299,  2.12926164]])



If we convert back to a multivariate gaussian, these are the means and covariances that will be adopted (technically not exactly as they'll be recomputed from another sampling of the underlying distribution).


```python
mvhg = mvh.to_mvgaussian()
```


```python
fig = mvhg.plot(show=True)
```


![png](multivariate_files/multivariate_16_0.png)



```python
mvhg.mean
```




    array([ 4.96926904,  9.96608361, 11.05252993])




```python
mvhg.cov
```




    array([[ 2.16982623,  1.01293887, -1.00812602],
           [ 1.01293887,  2.14302785,  0.99148548],
           [-1.00812602,  0.99148548,  2.14529892]])



# Take Dimensions


```python
mvg_ac = mvg.take_dimensions(['a', 'c'])
```


```python
mvg_ac.sample()
```




    array([ 5.54537489, 10.75561886])




```python
out = mvg_ac.plot(show=True)
```


![png](multivariate_files/multivariate_22_0.png)



```python
out = mvh.take_dimensions(['a', 'c']).plot(show=True)
```


![png](multivariate_files/multivariate_23_0.png)


## Passing a single dimension to take_dimension

If you pass a single-dimension to take_dimension, then the univariate version of the same type is returned instead.  See the "Converting to Univariate" section below for examples directly calling [to_univariate](../api/BaseMultivariateDistribution.to_univariate.md).


```python
out = mvg.take_dimensions(['a']).plot(show=True)
```


![png](multivariate_files/multivariate_25_0.png)


# Slicing

Slicing allows taking a single dimension while retaining all underlying covariances such that the resulting distribution can undergo [math operations](./math.md), [and/or logic](./and_or.md), and included in [distribution collections](./collections.md).  For more details, see the [slice examples](./slice.md).


```python
mvg_a = mvg.slice('a')
```


```python
mvg_a.sample()
```




    2.3793905616172655




```python
out = mvg_a.plot(show=True)
```


![png](multivariate_files/multivariate_29_0.png)



```python
mvg_a.multivariate
```




    <distl.mvgaussian mean=[5, 10, 12] cov=[[ 2  1 -1]
     [ 1  2  1]
     [-1  1  2]] allow_singular=True labels=['a', 'b', 'c']>



# Converting to Univariate

There are methods to convert directly to the univariate distribution of the same type as the univariate:

* [Multivariate.to_univariate](../api/BaseMultivariateDistribution.to_univariate.md).
* [MultivariateSlice.to_univariate](../api/BaseMultivariateSliceDistribution.to_univariate.md).

When acting on a Multivariate, the requested dimension must be passed.


```python
mvg.to_univariate(dimension='a')
```




    <distl.gaussian loc=5.0 scale=1.4142135623730951 label=a>



Whereas a MultivariateSlice converts using the sliced dimension


```python
mvg_a.to_univariate()
```




    <distl.gaussian loc=5.0 scale=1.4142135623730951 label=a>


