### [MVSamples](MVSamples.md).calculate_means_covariances (function)


```py

def calculate_means_covariances(self, N=1000000)

```



Return the weighted mean values and covariances from the samples
([MVSamples.samples](MVSamples.samples.md) if [MVSamples.weights](MVSamples.weights.md)
is not provided, otherwise [MVSamples.samples_weighted](MVSamples.samples_weighted.md)).

See also:

* [MVSamples.calculate_means](MVSamples.calculate_means.md)
* [MVSamples.calculate_covariances](MVSamples.calculate_covariances.md)

Arguments
----------
* `N` (int, optional, default=1e6): number of samples to draw before
    computing means/covariances.  Only applicable if [MVSamples.weights](MVSamples.weights.md) is not None.

Returns
-------
* means (array of floats), covariances (matrix)

