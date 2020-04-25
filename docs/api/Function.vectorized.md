### [Function](Function.md).vectorized (property)




whether [Function.func](Function.func.md) supports passing arrays to [Function.args](Function.args.md) and [Function.kwargs](Function.kwargs.md).
Note: not-vectorized will take significantly longer for large samples.  The defaults
for `size` in [Function.plot](Function.plot.md) and [Function.plot_sample](Function.plot_sample.md) and the underlying
[Histogram](Histogram.md) samples are lowered to 10000 in the case where vectorized is disabled.

