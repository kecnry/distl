### [MVHistogram](MVHistogram.md).calculate_means (function)


```py

def calculate_means(self, N=100000.0)

```



Return the weighted mean values from the histogram.

See also:

* [MVHistogram.calculate_covariances](MVHistogram.calculate_covariances.md)
* [MVHistogram.calculate_means_covariances](MVHistogram.calculate_means_covariances.md)

Arguments
---------
* `N` (int, default=1e5): number of samples to use to pass to
    `np.cov`.

Returns
-------
* list of floats: the mean value per dimension

