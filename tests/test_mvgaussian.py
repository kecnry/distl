from nose.tools import assert_raises

import distl
import numpy as np

def _mvg():
    return distl.mvgaussian([5,10, 12],
                           np.array([[ 2,  1, -1],
                                     [ 1,  2,  1],
                                     [-1,  1,  2]]),
                           allow_singular=True,
                           labels=['a', 'b', 'c'])

def test_create():
    mvg = _mvg()

# def test_create_errors():
#     # passing string
#     assert_raises(ValueError, distl.gaussian, 0, "a")
#
#     # too many args
#     assert_raises(TypeError, distl.gaussian, 0, 1, 1)

def test_conversions():
    mvg = _mvg()
    mvg.to_mvhistogram()
    mvg.to_univariate(dimension='a')
    mvg.to_gaussian(dimension='a')
    mvg.to_histogram(dimension='a')
    mvg.slice(dimension='a')
    mvg.take_dimensions(['a', 'c'])

def test_sample():
    mvg = _mvg()

    mvg.sample()
    mvg.pdf([5, 10, 12])

    # assert_raises(AttributeError, mvg.ppf, 0.5)

def test_json():
    distl.from_dict(_mvg().to_dict())


if __name__ == '__main__':
    test_create()
    test_create_errors()
    test_conversions()
    test_sample()
    test_json()
