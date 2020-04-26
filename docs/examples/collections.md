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




    <distl.distl.DistributionCollection at 0x7fc84a366510>



When calling [sample](../api/DistributionCollection.sample.md), values are returned for each distribution in the order they were passed when initializing the object.


```python
dc.sample()
```




    array([7.94423774, 1.95210135])



If ever unsure, we can access the underlying distribution objects via the [dists](../api/DistributionCollection.dists.md) or [labels](../api/DistributionCollection.labels.md) properties.


```python
dc.dists
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




    array([[12.04693996,  2.22171585],
           [10.19206936,  2.68623238],
           [ 8.53497014,  3.08658149]])



We can also call [plot](../api/DistributionCollection.plot.md) or [plot_sample](../api/DistributionCollection.plot_sample.md).  Here we're shown a corner plot and see that the samples were drawn independently (without any covariances).


```python
out = dc.plot(show=True)
```


![png](collections_files/collections_14_0.png)


Additionally, we can access [pdf](../api/DistributionCollection.pdf.md), [logpdf](../api/DistributionCollection.logpdf.md), [cdf](../api/DistributionCollection.cdf.md), and [logcdf](../api/DistributionCollection.logcdf.md). These all take a single argument which must be a list/tuple/array with the same length as the number of distributions.


```python
dc.pdf([10, 5])
```




    0.039894228040143274



To see the underlying distributions and the values that will be passed to the `pdf` method on each of those distributions, we can pass the same arguments to [get_distributions_with_values](../api/DistributionCollection.get_distributions_with_values.md).


```python
dc.get_distributions_with_values([10,5])
```




    {<distl.gaussian loc=10.0 scale=2.0 label=gaussian>: 10,
     <distl.uniform low=0.0 high=5.0 label=uniform>: 5}



From this we can see that, in the case of univariate distributions, pdf and cdf will be simply the product of the values from the children distributions, and logpdf and logcdf the sums.  However, this is where subtle complications come into place with [Composite](../api/Composite.md) and Multivariate distributions, which we'll see in the next few sections.


```python
g.pdf(10) * u.pdf(5)
```




    0.039894228040143274



# MultivariateSlice distributions

Note that each distribution passed to a collection must be a univariate or multivariate-slice.  If attempting to pass a multivariate object without slicing to a single dimension, an error will be raised.

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

Yes, in theory you could call sample on `g`, `u`, `mvg` and just ignore the second index in the returned arrays from `mvg.sample`... but a [DistributionCollection](../api/DistributionCollection.md) starts to provide some convenience in this case for both plotting and accessing the probabilities of a given drawn sample.  This becomes especially useful when coupled with [sample caching](./sample_cache.md).

To learn more about slicing multivariate distributions, see [multivariate slicing](./multivariate_slice.md), but in simple terms it allows you to select a single dimension from a multivariate distribution, acting like a univariate distribution but still retaining the underlying covariances of the multivariate distribution.


```python
dc = distl.DistributionCollection(g, u, mvg.slice('mvg_a'), mvg.slice('mvg_c'))
```


```python
dc.sample()
```




    array([ 9.48128528,  2.02930039,  5.79131932, 12.60540779])




```python
out = dc.plot(show=True)
```


![png](collections_files/collections_26_0.png)


As in the univariate case, [pdf](../api/DistributionCollection.pdf.md) takes a tuple/list/array.  This time, the pdf will account for the covariance between 'mvg_a' and 'mvg_c', by default.  As 'mvg_b' is not included, no value will be assumed, but rather will be marginalized over (via [take_dimensions](../api/BaseMultivariateDistribution.take_dimensions.md), see [multivariate examples](./multivariate.md) for more details).


```python
dc.labels
```




    ['gaussian', 'uniform', 'mvg_a', 'mvg_c']




```python
dc.pdf([10, 5, 5, 11])
```




    0.0026266653362734885



which could be computed manually as:


```python
dc.get_distributions_with_values([10, 5, 5, 11])
```




    {<distl.gaussian loc=10.0 scale=2.0 label=gaussian>: 10,
     <distl.uniform low=0.0 high=5.0 label=uniform>: 5,
     <distl.mvgaussian mean=[ 5 12] cov=[[ 2 -1]
      [-1  2]] allow_singular=False labels=['mvg_a', 'mvg_c']>: [5, 11]}




```python
g.pdf(10) * u.pdf(5) * mvg.take_dimensions(['mvg_a', 'mvg_c']).pdf([5, 11])
```




    0.0026266653362734885



To avoid this behavior and instead sum/multiply over the flattened univariate versions of each of the sampled parameters, pass `as_univariates=True` to [pdf](../api/DistributionCollection.pdf.md).


```python
dc.pdf([10, 5, 5, 11], as_univariates=True)
```




    0.0024724446692818785



which could be computed manually as:


```python
dc.get_distributions_with_values([10, 5, 5, 11], as_univariates=True)
```




    {<distl.gaussian loc=10.0 scale=2.0 label=gaussian>: 10,
     <distl.uniform low=0.0 high=5.0 label=uniform>: 5,
     <distl.mvgaussianslice dimension=0 mean=[5, 10, 12] cov=[[ 2  1 -1]
      [ 1  2  1]
      [-1  1  2]] allow_singular=True label=mvg_a)>: 5,
     <distl.mvgaussianslice dimension=2 mean=[5, 10, 12] cov=[[ 2  1 -1]
      [ 1  2  1]
      [-1  1  2]] allow_singular=True label=mvg_c)>: 11}




```python
g.pdf(10) * u.pdf(5) * mvg.to_univariate('mvg_a').pdf(5) * mvg.to_univariate('mvg_c').pdf(11)
```




    0.0024724446692818785



# Composite (math operators) distributions


```python
g1 = distl.gaussian(5, 2, label='g1')
u = distl.gaussian(3, 5, label='u')
g2 = distl.gaussian(25, 1, label='g2')

dc = distl.DistributionCollection(g1, u, u*g2)
```


```python
dc.sample()
```




    array([  4.06251152,   5.77395689, 160.63898803])




```python
out = dc.plot(show=True)
```


![png](collections_files/collections_41_0.png)


Because the [DistributionCollection](../api/DistributionCollection.md) contains a [Composite](../api/Composite.md) distribution, we can either pass the two exposed values and `as_univariates=True` or the three underlying values without.


```python
dc.labels
```




    ['g1', 'u', 'u * g2']




```python
dc.pdf([6, 4, 4*25], as_univariates=True)
```




    4.3007709480577515e-05




```python
dc.get_distributions_with_values([6, 4, 4*25], as_univariates=True)
```




    {<distl.gaussian loc=5.0 scale=2.0 label=g1>: 6,
     <distl.gaussian loc=3.0 scale=5.0 label=u>: 4,
     <distl.composite {u} * {g2} unit=None>: 100}




```python
g1.pdf(6) * u.pdf(4) * (u*g2).pdf(4*25)
```




    4.3007709480577515e-05



If not passing `as_univariates=True`, then we must pass a value for each of the unpacked underlying distributions.  Note that here 'u' is both an independent distribution as well as part of 'u * g2' so must be sent twice (and *must* be sent as the same value or an error will be raised).

Note that under-the-hood the separate passed values for 'u' are checked to make sure they're identical, but are then only included once in the returned probability.


```python
dc.labels_unpacked
```




    ['g1', 'u', 'u', 'g2']




```python
try:
    dc.pdf([6, 4, 5, 25])
except Exception as e:
    print(e)
```

    All passed values for u must be identical



```python
dc.pdf([6, 4, 4, 25])
```




    0.00549234105537757




```python
dc.get_distributions_with_values([6, 4, 4, 25])
```




    {<distl.gaussian loc=5.0 scale=2.0 label=g1>: 6,
     <distl.gaussian loc=3.0 scale=5.0 label=u>: 4,
     <distl.gaussian loc=25.0 scale=1.0 label=g2>: 25}




```python
g1.pdf(6) * u.pdf(4) * g2.pdf(25)
```




    0.00549234105537757



# Composites containing MultivariateSlice distributions

Now let's consider a more complex example: let's sample from 'gaussian * mvg_a' and 'mvg_c'.  Here we want the covariance between 'mvg_a' and 'mvg_c' respected, even though there is a math operation on the result of 'mvg_a'.


```python
dc = distl.DistributionCollection(g * mvg.slice('mvg_a'), mvg.slice('mvg_c'))
```


```python
dc.sample()
```




    array([42.37014023, 12.29659702])




```python
out = dc.plot(show=True)
```


![png](collections_files/collections_57_0.png)


As in the univariate case, [pdf](../api/DistributionCollection.pdf.md) takes a tuple/list/array.  However, in order to respect the covariances, the length of the input must match that of the underlying distributions that were sampled (see [labels_unpacked](../api/DistributionCollection.labels_unpacked.md) or [distributions_unpacked](../api/DistributionCollection.distributions_unpacked.md)).

