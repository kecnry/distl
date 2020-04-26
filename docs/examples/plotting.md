```python
import distl
import numpy as np
```


```python
u = distl.uniform(3, 7)
gh = distl.gaussian(5, 1.5).to_histogram()
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

# plot_pdf


```python
out = u.plot_pdf(show=True)
```


![png](plotting_files/plotting_7_0.png)



```python
out = gh.plot_pdf(show=True)
```


![png](plotting_files/plotting_8_0.png)


for more options, see the [plot_pdf API docs](../api/BaseDistribution.plot_pdf.md).

# plot_cdf


```python
out = u.plot_cdf(show=True)
```


![png](plotting_files/plotting_11_0.png)



```python
out = gh.plot_cdf(show=True)
```


![png](plotting_files/plotting_12_0.png)


for more options, see the [plot_cdf API docs](../api/BaseDistribution.plot_cdf.md).

# plot_gaussian


```python
out = u.plot_gaussian(show=True)
```


![png](plotting_files/plotting_15_0.png)



```python
out = gh.plot_gaussian(show=True)
```


![png](plotting_files/plotting_16_0.png)


for more options, see the [plot_gaussian API docs](../api/BaseDistribution.plot_gaussian.md).

# plot


```python
out = u.plot(show=True)
```


![png](plotting_files/plotting_19_0.png)



```python
out = u.plot(show=True, plot_gaussian=True)
```


![png](plotting_files/plotting_20_0.png)



```python
out = u.plot(show=True, plot_gaussian=True, plot_gaussian_kwargs={'sigma': 3})
```


![png](plotting_files/plotting_21_0.png)



```python
out = gh.plot(show=True)
```


![png](plotting_files/plotting_22_0.png)



```python
out = gh.plot(200, show=True, plot_gaussian=True)
```


![png](plotting_files/plotting_23_0.png)


for more options, see the [plot API docs](../api/BaseDistribution.plot.md).
