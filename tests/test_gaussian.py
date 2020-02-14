from nose.tools import assert_raises

import distl

def test_create():
    g = distl.gaussian(5, 10)
    g = distl.normal(5, 10)

def test_create_errors():
    # passing string
    assert_raises(ValueError, distl.gaussian, 0, "a")

    # too many args
    assert_raises(TypeError, distl.gaussian, 0, 1, 1)

def test_conversions():
    g = distl.gaussian()
    g.to_histogram()
    g.to_uniform()
    g.to_delta()
    g.to_delta(loc='mean')
    g.to_delta(loc='median')
    g.to_delta(loc='sample')

def test_sample():
    g = distl.gaussian()
    g.sample()
    g.pdf(0)
    g.logpdf(0)
    g.cdf(0)
    g.logcdf(0)
    g.sf(0)
    g.logsf(0)
    g.isf(0)

    g.moment(1)
    g.entropy()

    # g.expect(...)

    g.median()
    g.mean()
    g.var()
    g.std()
    g.interval(0.99)



    distl.gaussian().ppf(0.5)

def test_json():
    distl.from_dict(distl.gaussian().to_dict())


if __name__ == '__main__':
    test_create()
    test_create_errors()
    test_conversions()
    test_sample()
    test_json()
