### [MVSamples](MVSamples.md).calculate_covariances (function)


```py

def calculate_covariances(self)

```



Return the covariances about the mean from the [MVSamples](MVSamples.md).

Under-the-hood, this calls `np.cov` on [MVSamples.samples](MVSamples.samples.md)

See also:

* [MVSamples.calculate_means](MVSamples.calculate_means.md)
* [MVSamples.calculate_means_covariances](MVSamples.calculate_means_covariances.md)

Returns
---------
* MxM square matrix of floats.

