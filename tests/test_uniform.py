from nose.tools import assert_raises

import distl

def test_create():
    g = distl.uniform(5, 10)
    g = distl.boxcar(5, 10)

def test_create_errors():
    # passing string
    assert_raises(ValueError, distl.uniform, 0, "a")

    # too many args
    assert_raises(TypeError, distl.uniform, 0, 1, 1)

def test_conversions():
    distl.uniform().to_histogram()
    distl.uniform().to_gaussian()
    distl.uniform().to_delta()
    distl.uniform().to_delta(loc='mean')
    distl.uniform().to_delta(loc='median')
    distl.uniform().to_delta(loc='sample')

def test_sample():
    d = distl.uniform()
    d.sample()
    d.pdf(0)
    d.logpdf(0)
    d.cdf(0)
    d.logcdf(0)
    d.sf(0)
    d.logsf(0)
    d.isf(0)

    d.moment(1)
    d.entropy()

    # d.expect(...)

    d.median()
    d.mean()
    d.var()
    d.std()
    d.interval(0.99)

    d.ppf(0.5)

def test_json():
    distl.from_dict(distl.uniform().to_dict())


if __name__ == '__main__':
    test_create()
    test_create_errors()
    test_conversions()
    test_sample()
    test_json()
