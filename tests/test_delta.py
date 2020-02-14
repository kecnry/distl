from nose.tools import assert_raises

import distl

def test_create():
    d = distl.delta(1)

def test_create_errors():
    # passing string
    assert_raises(ValueError, distl.delta, "a")

    # too many args
    assert_raises(TypeError, distl.delta, 0, 1)

def test_conversions():
    distl.delta().to_histogram()
    distl.delta().to_gaussian()
    distl.delta().to_uniform()

def test_sample():
    d = distl.delta()
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
    distl.from_dict(distl.delta().to_dict())


if __name__ == '__main__':
    test_create()
    test_create_errors()
    test_conversions()
    test_sample()
    test_json()
