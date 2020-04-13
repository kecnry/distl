### [MVSamples](MVSamples.md).calculate_covariances (function)


```py

def calculate_covariances(self, N=1000000)

```



Return the covariances about the mean from the samples ([MVSamples.samples](MVSamples.samples.md) if [MVSamples.weights](MVSamples.weights.md)
is not provided, otherwise [MVSamples.samples_weighted](MVSamples.samples_weighted.md))

Under-the-hood, this calls `np.cov` on [MVSamples.samples](MVSamples.samples.md) or [MVSamples.samples_weighted](MVSamples.samples_weighted.md)

See also:

* [MVSamples.calculate_means](MVSamples.calculate_means.md)
* [MVSamples.calculate_means_covariances](MVSamples.calculate_means_covariances.md)

Arguments
----------
* `N` (int, optional, default=1e6): number of samples to draw before
    computing covariances.  Only applicable if [MVSamples.weights](MVSamples.weights.md) is not None.

Returns
---------
* MxM square matrix of floats.

