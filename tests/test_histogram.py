from nose.tools import assert_raises

import distl

def test_create():
    h = distl.histogram_from_data(distl.normal().sample(size=100))
    h = distl.histogram_from_bins(h.bins, h.density)

# def test_create_errors():
#     # passing string
#     assert_raises(ValueError, distl.histogram_from_data, "a")
#
#     # too many args
#     assert_raises(TypeError, distl.histogram_from_data, 0, 1, 1)

def test_conversions():
    h = distl.gaussian().to_histogram()
    h.to_gaussian()
    h.to_uniform()
    h.to_delta()
    h.to_delta(loc='mean')
    h.to_delta(loc='median')
    h.to_delta(loc='sample')

def test_sample():
    d = distl.gaussian().to_histogram()
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
    distl.from_dict(distl.gaussian().to_histogram().to_dict())


if __name__ == '__main__':
    test_create()
    test_create_errors()
    test_conversions()
    test_sample()
    test_json()
