### [MVHistogram](MVHistogram.md).calculate_covariances (function)


```py

def calculate_covariances(self, N=100000.0)

```



Return the covariances about the mean from the histogram.

Under-the-hood, this calls `np.cov` on the output from [MVHistogram.sample](MVHistogram.sample.md)
with `N` samples.

See also:

* [MVHistogram.calculate_means](MVHistogram.calculate_means.md)
* [MVHistogram.calculate_means_covariances](MVHistogram.calculate_means_covariances.md)

Arguments
---------
* `N` (int, default=1e5): number of samples to use to pass to
    `np.cov`.

Returns
---------
* MxM square matrix of floats.

