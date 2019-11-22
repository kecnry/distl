```python
import npdists
import numpy as np
```

First we'll create a [multivariate gaussian](../api/MVGaussian.md) distribution by providing the means and covariances of three parameters.


```python
mvg = npdists.mvgaussian([5,10, 12], 
                         np.array([[ 1., 1., -1.], [1, -1, 1], [-1., 1.,  1.]]),
                         label=['a', 'b', 'c'])
```

We can then easily access the means and covariances and see that they exactly match what we set.


```python
mvg.means
```




    [5, 10, 12]




```python
mvg.covariances
```




    array([[ 1.,  1., -1.],
           [ 1., -1.,  1.],
           [-1.,  1.,  1.]])



and plotting will now show a corner plot (if [corner](https://corner.readthedocs.io/en/latest/) is installed)


```python
mvg.plot(show=True)
```

    /home/kyle/.local/lib/python2.7/site-packages/npdists-0.1.0.dev0-py2.7.egg/npdists/npdists.py:952: RuntimeWarning: covariance is not positive-semidefinite.





![png](multivariate_files/multivariate_7_1.png)




![png](multivariate_files/multivariate_7_2.png)


we can now convert this multivariate gaussian distribution into a [multivariate histogram](../api/MVHistogram.md) distribution


```python
mvh = mvg.to_mvhistogram()
```


```python
mvh.plot(show=True)
```




![png](multivariate_files/multivariate_10_0.png)




![png](multivariate_files/multivariate_10_1.png)


Now if we access the means and covariances, we'll see that they are slightly different due to the binning.


```python
mvh.means
```




    [4.925224407767696, 9.917332103497039, 12.012708452098943]




```python
mvh.covariances
```




    array([[ 1.70746864, -0.3386417 , -0.32937709],
           [-0.3386417 ,  1.82331543, -0.33388958],
           [-0.32937709, -0.33388958,  1.73651273]])



If we convert back to a multivariate gaussian, these are the means and covariances that will be adopted.


```python
mvhg = mvh.to_mvgaussian()
```


```python
mvhg.plot(show=True)
```




![png](multivariate_files/multivariate_16_0.png)




![png](multivariate_files/multivariate_16_1.png)



```python
mvhg.means
```




    [4.939194686320406, 9.971444324306338, 11.968570240345853]




```python
mvhg.covariances
```




    array([[ 1.70305748, -0.33501587, -0.31426569],
           [-0.33501587,  1.83181591, -0.34252835],
           [-0.31426569, -0.34252835,  1.74348311]])




```python

```
