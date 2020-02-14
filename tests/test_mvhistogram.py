from nose.tools import assert_raises

import distl
import numpy as np

def _mvh():
    return distl.mvgaussian([5,10, 12],
                           np.array([[ 2,  1, -1],
                                     [ 1,  2,  1],
                                     [-1,  1,  2]]),
                           allow_singular=True,
                           labels=['a', 'b', 'c']).to_mvhistogram()

def test_create():
    mvh = _mvh()

    mvg = distl.mvgaussian([5,10, 12],
                           np.array([[ 2,  1, -1],
                                     [ 1,  2,  1],
                                     [-1,  1,  2]]),
                           allow_singular=True,
                           labels=['a', 'b', 'c'])

    mvh = distl.mvhistogram_from_data(mvg.sample(size=100))

# def test_create_errors():
#     # passing string
#     assert_raises(ValueError, distl.gaussian, 0, "a")
#
#     # too many args
#     assert_raises(TypeError, distl.gaussian, 0, 1, 1)

def test_conversions():
    mvh = _mvh()
    mvh.to_mvgaussian()
    mvh.to_univariate(dimension='a')
    mvh.to_gaussian(dimension='a')
    mvh.to_histogram(dimension='a')
    mvh.slice(dimension='a')
    mvh.take_dimensions(['a', 'c'])

def test_sample():
    mvh = _mvh()

    mvh.sample()
    # TODO: support pdf for mvh
    # mvh.pdf([5, 10, 12])

    # assert_raises(AttributeError, mvh.ppf, 0.5)

def test_json():
    distl.from_dict(_mvh().to_dict())


if __name__ == '__main__':
    test_create()
    test_create_errors()
    test_conversions()
    test_sample()
    test_json()
