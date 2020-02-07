```python
import distl
import numpy as np
```


```python
g = distl.gaussian(5,2)
```


```python
g.sample()
```




    0.07401217191565479




```python
g.sample_ppf(0.5)
```




    5.0




```python
g.mean
```




    5.0




```python
g.sample_ppf([0.25, 0.5])
```




    array([3.6510205, 5.       ])




```python
h = g.to_histogram()
```


```python
h.sample()
```




    4.424695149285333




```python
h.sample_ppf(0.5)
```




    4.601943803662765




```python
h.mean  # NOTE: under-the-hood this now calls sample_ppf(0.5)
```




    4.601943803662765




```python
h.sample_ppf([0.25, 0.5, 0.75])
```




    array([3.01692611, 4.6019438 , 6.1869615 ])




```python
distl.uniform(0,10).sample_ppf(0.5)
```




    5.0




```python
distl.delta(0.2).sample_ppf(0.5)
```




    0.2




```python
h.logp(4.6)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-16-45dabcd11cf0> in <module>()
    ----> 1 h.logp(4.6)
    

    /home/kyle/.local/lib/python2.7/site-packages/distl-0.1.0.dev0-py2.7.egg/distl/distl.pyc in logp(self, x, unit)
       1067         * array: array of density/y values.
       1068         """
    -> 1069         densities = self.distribution(x=x, unit=unit)
       1070         return _np.log(densities)
       1071 


    /home/kyle/.local/lib/python2.7/site-packages/distl-0.1.0.dev0-py2.7.egg/distl/distl.pyc in distribution(self, x, unit)
       1046 
       1047         # print "*** x passed to dist_func", x.min(), x.max()
    -> 1048         return self.dist_func(x, *self.dist_args)
       1049 
       1050     def logp(self, x, unit=None):


    /home/kyle/.local/lib/python2.7/site-packages/distl-0.1.0.dev0-py2.7.egg/distl/distl.pyc in histogram(x, bins, density)
        367     out = _np.zeros_like(x)
        368     filter_in_range = (x >= bins.min()) & (x < bins.max())
    --> 369     out[filter_in_range] = density[_np.digitize(x[filter_in_range], bins)-1]
        370     return out
        371 


    TypeError: 'float' object has no attribute '__getitem__'



```python

```
