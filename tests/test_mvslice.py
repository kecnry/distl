from nose.tools import assert_raises

import distl
import numpy as np

def test_slice():
    mvg = distl.mvgaussian([5,10, 12],
                           np.array([[ 2,  1, -1],
                                     [ 1,  2,  1],
                                     [-1,  1,  2]]),
                           allow_singular=True,
                           labels=['a', 'b', 'c'])

    mvg_ab = mvg.take_dimensions(['a', 'b'])

    mvg_a = mvg.slice('a')
    mvg_b = mvg.slice('b')

def test_math():
    mvg = distl.mvgaussian([5,10, 12],
                           np.array([[ 2,  1, -1],
                                     [ 1,  2,  1],
                                     [-1,  1,  2]]),
                           allow_singular=True,
                           labels=['a', 'b', 'c'])

    mvg_a = mvg.slice('a')
    mvg_b = mvg.slice('b')

    g = distl.gaussian(10, 2)

    assert_raises(TypeError, mvg_a.__and__, mvg_b)
    assert_raises(TypeError, mvg_a.__and__, g)
    assert_raises(TypeError, g.__and__, mvg_a)


if __name__ == '__main__':
    test_slice()
    test_math()
