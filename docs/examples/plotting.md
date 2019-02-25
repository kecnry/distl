

```python
import npdists
import numpy as np
```


```python
u = npdists.uniform(3, 7)
gh = npdists.gaussian(5, 1.5).to_histogram()
```

# plot_sample


```python
out = u.plot_sample(show=True)
```


![png](plotting_files/plotting_3_0.png)



```python
out = gh.plot_sample(show=True)
```


![png](plotting_files/plotting_4_0.png)


for more options, see the [plot_sample API docs](../api/BaseDistribution.plot_sample.md).

# plot_dist


```python
x = np.linspace(0, 10, 201)
out = u.plot_dist(x, show=True)
```


![png](plotting_files/plotting_7_0.png)



```python
x = np.linspace(0, 10, 201)
out = gh.plot_dist(x, show=True)
```


![png](plotting_files/plotting_8_0.png)


for more options, see the [plot_dist API docs](../api/BaseDistribution.plot_dist.md).

# plot_gaussian


```python
x = np.linspace(0, 10, 201)
out = u.plot_gaussian(x, show=True)
```


![png](plotting_files/plotting_11_0.png)



```python
x = np.linspace(0, 10, 201)
out = gh.plot_gaussian(x, show=True)
```


![png](plotting_files/plotting_12_0.png)


for more options, see the [plot_gaussian API docs](../api/BaseDistribution.plot_gaussian.md).

# plot


```python
out = u.plot(show=True)
```


![png](plotting_files/plotting_15_0.png)



```python
out = u.plot(show=True, plot_gaussian=True)
```


![png](plotting_files/plotting_16_0.png)



```python
out = u.plot(show=True, plot_gaussian=True, plot_gaussian_kwargs={'sigma': 3})
```


![png](plotting_files/plotting_17_0.png)



```python
out = gh.plot(show=True)
```


![png](plotting_files/plotting_18_0.png)



```python
out = gh.plot(200, show=True, plot_gaussian=True)
```


![png](plotting_files/plotting_19_0.png)


for more options, see the [plot API docs](../api/BaseDistribution.plot.md).
