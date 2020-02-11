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
    distl.gaussian().to_histogram()
    distl.gaussian().to_uniform()


if __name__ == '__main__':
    test_create()
    test_create_errors()
    test_conversions()
