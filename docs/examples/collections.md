```python
import distl
import numpy as np
```

[DistributionCollections](../api/DistributionCollection.md) allow for sampling (and computing probabilities) on multiple distributions simultaneously, respecting any covariances between the distributions within that set.

# "Simple Case" (Univariate only)

Let's first look at the simplest case possible with two univariate distributions.  As these will be drawn independently, there is little gained by using a [DistributionCollection](../api/DistributionCollection.md) over simply handling the two objects separately, but this example shows the syntax without having to deal with complex subtle points.


```python
g = distl.gaussian(10, 2, label='gaussian')
u = distl.uniform(0, 5, label='uniform')
```


```python
dc = distl.DistributionCollection(g, u)
```


```python
dc
```




    <distl.distl.DistributionCollection at 0x7fac5bb87890>



When calling [sample](../api/DistributionCollection.sample.md), values are returned for each distribution in the order they were passed when initializing the object.


```python
dc.sample()
```




    array([7.94423774, 3.38192392])



If ever unsure, we can access the underlying distribution objects via the [distributions](../api/DistributionCollection.distributions.md) or [labels](../api/DistributionCollection.labels.md) properties.


```python
dc.distributions
```




    [<distl.gaussian loc=10.0 scale=2.0 label=gaussian>,
     <distl.uniform low=0.0 high=5.0 label=uniform>]




```python
dc.labels
```




    ['gaussian', 'uniform']



If passing `size` to [sample](../api/DistributionCollection.sample.md), we get a matrix with shape (`size`, `len(distributions)`)


```python
dc.sample(size=3)
```




    array([[13.05648357,  3.17603292],
           [ 7.23378384,  3.35741225],
           [10.18171253,  2.41334386]])



We can also call [plot](../api/DistributionCollection.plot.md) or [plot_sample](../api/DistributionCollection.plot_sample.md).  Here we're shown a corner plot and see that the samples were drawn independently (without any covariances).


```python
out = dc.plot(show=True)
```


![png](collections_files/collections_14_0.png)


Additionally, we can access [pdf](../api/DistributionCollection.pdf.md), [logpdf](../api/DistributionCollection.logpdf.md), [cdf](../api/DistributionCollection.cdf.md), and [logcdf](../api/DistributionCollection.logcdf.md). These all take a single argument which must be a list/tuple/array with the same length as the number of distributions.

In the case of univariate distributions, pdf and cdf will be simply the product of the values from the children distributions, and logpdf and logcdf the products.  However, this is where subtle complications come into place with [Composite](../api/Composite.md) and Multivariate distributions, which we'll see in the next few sections.


```python
dc.pdf([10, 5])
```




    0.039894228040143274




```python
g.pdf(10) * u.pdf(5)
```




    0.039894228040143274



# using MultivariateSlice distributions

First we'll create a [gaussian](../api/distl.gaussian.md), [uniform](../api/distl.uniform.md), and [multivariate gaussian](../api/distl.mvgaussian.md) distributions.


```python
g = distl.gaussian(10, 2, label='gaussian')
u = distl.uniform(0, 5, label='uniform')
mvg = distl.mvgaussian([5,10, 12], 
                       np.array([[ 2,  1, -1], 
                                 [ 1,  2,  1], 
                                 [-1,  1,  2]]),
                       allow_singular=True,
                       labels=['mvg_a', 'mvg_b', 'mvg_c'])
```

Now let's imagine a scenario where we want to draw from the following sub-distributions: 'gaussian', 'uniform', 'mvg_a', and 'mvg_c' (but let's say we don't want 'mvg_b').  Here we want to *maintain* the covariances between 'mvg_a' and 'mvg_c' while *independently* sampling from 'gaussian' and 'uniform'.

To learn about slicing multivariate distributions, see [multivariate slicing](./multivariate_slice.md).


```python
dc = distl.DistributionCollection(g, u, mvg.slice('mvg_a'), mvg.slice('mvg_c'))
```


```python
dc.sample()
```




    array([11.26488164,  0.87127455,  5.54918169, 12.94481664])




```python
out = dc.plot(show=True)
```


![png](collections_files/collections_23_0.png)


As in the univariate case, [pdf](../api/DistributionCollection.pdf.md) takes a tuple/list/array with the same length as the provided number of distributions (and in the same order as [labels](../api/DistributionCollection.labels.md).

It is **very** important to note here that this call to pdf does **NOT** account for the covariance between 'mvg_a' and 'mvg_c' (as it would also be necessary to know the assumed value of mvg_b or to collapse along that dimension).

**TODO**: need to support and explain three cases
* treat each as univariates for pdf
* collapse the unused dimensions out and calculate multivariate pdf
* provide unsampled value and calculate multivariate pdf


```python
dc.labels
```




    ['gaussian', 'uniform', 'mvg_a', 'mvg_c']




```python
dc.pdf([10, 5, 5, 11])
```




    0.0024724446692818785



# using Composite distributions

Now let's consider a more complex example: let's sample from 'gaussian * mvg_a' and 'mvg_c'.  Here we want to covariance between 'mvg_a' and 'mvg_c' respected, even though there is a math operation on the result.


```python
# TODO: this won't work until math with multivariates is implemented
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
