### [BaseUnivariateDistribution](BaseUnivariateDistribution.md).expect (method)


```py

def expect(self, func, args=(), lb=None, ub=None, conditional=False, **kwargs)

```



Expose the expected value of a function (of one argument) with respect
to the distribution.

See [scipy docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.expect.html)

This method is just a wrapper around the scipy.stats method on
[BaseUnivariateDistribution.dist_constructor_object](BaseUnivariateDistribution.dist_constructor_object.md) after doing any requested unit-conversions.

Arguments
-----------
* `func` (callable): passed directly to scipy (see link above)
* `args` (tuple, optional): passed directly to scipy (see link above)
* `lb` (float, optional): passed directly to scipy (see link above)
* `ub` (float, optional): passed directly to scipy (see link above)
* `conditional` (bool, optional, default=False): passed directly to scipy (see link above)
* `**kwargs`: passed directly to scipy (see link above)

Returns
---------
* the output from scipy (see link above)

