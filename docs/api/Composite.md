## Composite (class)


A composite distribution consisting of some math operator between one or two
other Distribution objects.

For example:

```py
g = npdists.gaussian(10, 2)
u = npdists.gaussian(1, 5)

c = g * u
print(c)
```

or:

```py
import numpy as np
g = npdists.gaussian(0, 1)
sing = np.sin(g)
print(sing)
```

Currently supported operators include:

* multiplication, division, addition, subtraction
* np.sin, np.cos, np.tan (but not math.sin, etc)

When doing math between a distribution and a float or integer, that float/int
will be treated as a [Delta](Delta.md) distribution.  In some simple cases, the
applicable distribution type will be returned, but in other cases,
a [Composite](Composite.md) distribution will be returned.  For example, multiplying
a [Uniform](Uniform.md) or [Gaussian](Gaussian.md) distribution by a float will return another
[Uniform](Uniform.md) or [Gaussian](Gaussian.md) distribution, respectively.




* [__init__](Composite.__init__.md)
* [copy](Composite.copy.md)
* [dist_args](Composite.dist_args.md)
* [dist_func](Composite.dist_func.md)
* [distribution](Composite.distribution.md)
* [label](Composite.label.md)
* [mean](Composite.mean.md)
* [plot](Composite.plot.md)
* [plot_dist](Composite.plot_dist.md)
* [plot_sample](Composite.plot_sample.md)
* [sample](Composite.sample.md)
* [sample_args](Composite.sample_args.md)
* [sample_func](Composite.sample_func.md)
* [std](Composite.std.md)
* [to](Composite.to.md)
* [to_dict](Composite.to_dict.md)
* [to_file](Composite.to_file.md)
* [to_gaussian](Composite.to_gaussian.md)
* [to_histogram](Composite.to_histogram.md)
* [to_json](Composite.to_json.md)
* [to_uniform](Composite.to_uniform.md)
* [unit](Composite.unit.md)
