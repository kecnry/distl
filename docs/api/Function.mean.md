### [Function](Function.md).mean (property)




Determine the mean sampled value.

This is done under-the-hood by converting to a histogram via
[Function.to_histogram](Function.to_histogram.md), sampling 10000 times with 100 bins and
calling [Histogram.mean](Histogram.mean.md).

