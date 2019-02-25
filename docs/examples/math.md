

```python
import npdists
import numpy as np
```

# Math with Integers/Floats


```python
g = npdists.gaussian(10, 2)
```


```python
print(g)
```

    <npdists.gaussian loc=10.0 scale=2.0>



```python
out = g.plot(show=True)
```


![png](math_files/math_4_0.png)


multiplying a [Gaussian distribution](../api/Gaussian.md) by a float or integer treats that float or integer as a [Delta distribution](../api/Delta.md).  In this case, it is able to return another [Gaussian distribution](../api/Gaussian.md).  When unable to return a supported distribution type, a [Composite distribution](../api/Composite.md) will be returned instead.


```python
print(2*g)
```

    <npdists.gaussian loc=20.0 scale=4.0>



```python
print(g*2)
```

    <npdists.gaussian loc=20.0 scale=4.0>



```python
out = (g*2).plot(show=True)
```


![png](math_files/math_8_0.png)


Note that this gives us the same resulting distribution as if we defined a [Delta distribution](../api/Delta.md) manually and multiplied by that.


```python
d = npdists.delta(2)
```


```python
print(g*d)
```

    <npdists.gaussian loc=20.0 scale=4.0>



```python
out = (g*d).plot(show=True)
```


![png](math_files/math_12_0.png)


If we multiply in the other order, we'll get a [Composite distribution](../api/Composite.md), but see that it gives us the same resulting sample.

Do note, however that [Composite.plot_dist](../api/Composite.plot_dist.md) will not show anything, as it is sampling from multiple underlying distributions.


```python
print(d*g)
```

    <npdists.delta value=2.0>*<npdists.gaussian loc=10.0 scale=2.0>



```python
out = (d*g).plot(show=True)
```


![png](math_files/math_15_0.png)


Note that since the floats/integers are treated as distributions, `2*g` is **not** equivalent to `g+g` (note the change in the x-limit scale on the plot below compared to those above).


```python
print(g+g)
```

    <npdists.gaussian loc=10.0 scale=2.0>+<npdists.gaussian loc=10.0 scale=2.0>



```python
out = (g+g).plot(show=True)
```


![png](math_files/math_18_0.png)


# Supported Operators

* multiplication
* division
* addition
* subtraction
* np.sin, np.cos, np.tan


```python
g = npdists.gaussian(2*np.pi, np.pi/6)
```


```python
print(np.sin(g))
```

    sin(<npdists.gaussian loc=6.28318530718 scale=0.523598775598>)



```python
out = np.sin(g).plot(show=True)
```


![png](math_files/math_22_0.png)



```python
out = np.cos(g).plot(show=True)
```


![png](math_files/math_23_0.png)



```python
out = np.tan(g).plot(show=True)
```


![png](math_files/math_24_0.png)



```python

```
