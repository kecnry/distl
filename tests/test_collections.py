from nose.tools import assert_raises

import distl
import numpy as np

def test_univariates():
    g = distl.gaussian(5, 10)
    u = distl.normal(5, 10)
    dc = distl.DistributionCollection(g, u)

    assert(abs(dc.pdf([5, 7]) - (g.pdf(5) * u.pdf(7))) < 1e-6)

    dc = distl.from_dict(dc.to_dict())
    dc.sample()
    dc.pdf()

def test_mvslice():
    g = distl.gaussian(10, 2, label='gaussian')
    u = distl.uniform(0, 5, label='uniform')
    mvg = distl.mvgaussian([5,10, 12],
                           np.array([[ 2,  1, -1],
                                     [ 1,  2,  1],
                                     [-1,  1,  2]]),
                           allow_singular=True,
                           labels=['mvg_a', 'mvg_b', 'mvg_c'])

    # passing a multivariate (non-sliced) must raise a TypeError
    assert_raises(TypeError, distl.DistributionCollection, g, u, mvg)

    dc = distl.DistributionCollection(g, u, mvg.slice('mvg_a'))
    dc.labels

    dc = distl.from_dict(dc.to_dict())
    dc.sample()
    dc.pdf()

    # passing the wrong shape to pdf should raise a ValueError
    assert_raises(ValueError, dc.pdf, [1,1])
    assert_raises(TypeError, dc.pdf, 1)
    assert_raises(TypeError, dc.pdf, 1.0)


if __name__ == '__main__':
    test_univariates()
    test_mvslice()
