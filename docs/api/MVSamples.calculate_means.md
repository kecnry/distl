### [MVSamples](MVSamples.md).calculate_means (function)


```py

def calculate_means(self, N=1000000)

```



Return the weighted mean values from the samples ([MVSamples.samples](MVSamples.samples.md) if [MVSamples.weights](MVSamples.weights.md)
is not provided, otherwise [MVSamples.samples_weighted](MVSamples.samples_weighted.md))

See also:

* [MVSamples.calculate_covariances](MVSamples.calculate_covariances.md)
* [MVSamples.calculate_means_covariances](MVSamples.calculate_means_covariances.md)

Arguments
----------
* `N` (int, optional, default=1e6): number of samples to draw before
    computing means.  Only applicable if [MVSamples.weights](MVSamples.weights.md) is not None.

Returns
-------
* list of floats: the mean value per dimension

