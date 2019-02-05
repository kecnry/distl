from nose.tools import assert_raises

import npdists as npd

def test_create():
    g = npd.gaussian(5, 10)
    g = npd.normal(5, 10)

def test_create_errors():
    # passing string
    assert_raises(ValueError, npd.gaussian, 0, "1")

    # too many args
    assert_raises(TypeError, npd.gaussian, 0, 1, 1)

def test_conversions():
    npd.gaussian().to_histogram()
    npd.gaussian().to_uniform()


if __name__ == '__main__':
    test_create()
    test_create_errors()
    test_conversions()
