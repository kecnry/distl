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

def test_sample():
    distl.uniform().sample()
    distl.uniform().pdf(0)
    distl.uniform().ppf(0.5)


if __name__ == '__main__':
    test_create()
    test_create_errors()
    test_conversions()
    test_sample()
