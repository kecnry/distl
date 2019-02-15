### [Composite](Composite.md).mean (property)




Determine the mean sampled value.

This is done under-the-hood by converting to a histogram via
[Composite.to_histogram](Composite.to_histogram.md), sampling 10000 times with 100 bins and
calling [Histogram.mean](Histogram.mean.md).

