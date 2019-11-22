### [MVHistogram](MVHistogram.md).covariances (property)




Return the covariances about the mean from the histogram.

Under-the-hood, this calls `np.cov` on the output from [MVHistogram.sample](MVHistogram.sample.md)
with 1e5 samples.  To adjust the number of samples, use [MVHistogram.get_covariances](MVHistogram.get_covariances.md) instead.

See also:

* [MVHistogram.get_covariances](MVHistogram.get_covariances.md)
* [MVHistogram.means](MVHistogram.means.md)

Returns
---------
* NxN square matrix of floats.

