### [Composite](Composite.md).std (property)




Determine the standard deviations of the sampled values.

This is done under-the-hood by converting to a histogram via
[Composite.to_histogram](Composite.to_histogram.md), sampling 10000 times with 100 bins and
calling [Histogram.std](Histogram.std.md).

