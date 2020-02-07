### [MVHistogram](MVHistogram.md).calculate_means_covariances (function)


```py

def calculate_means_covariances(self, N=100000.0)

```



Return the weighted mean values and covariances from the histogram.

See also:

* [MVHistogram.calculate_means](MVHistogram.calculate_means.md)
* [MVHistogram.calculate_covariances](MVHistogram.calculate_covariances.md)

Arguments
---------
* `N` (int, default=1e5): number of samples to use to pass to
    `np.cov`.

Returns
-------
* means (array of floats), covariances (matrix)

