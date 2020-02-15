from nose.tools import assert_raises

import distl
import numpy as np
import astropy.units as u

def test_gaussian():
    # passing string
    assert_raises(ValueError, distl.gaussian, 0, "a")

    # too many args
    assert_raises(TypeError, distl.gaussian, 0, 1, 1)

    d = distl.gaussian(unit=u.deg)
    d.to(u.rad)
    d.to('rad')
    d_with_unit = distl.gaussian(unit='deg')
    d_with_label = distl.gaussian(label='mylabel')
    d_with_wrap_at = distl.gaussian(10, 2, wrap_at=12)
    d = distl.gaussian(5, 10)
    d = distl.normal(5, 10)
    d = d.copy()

    for d in [d, d_with_unit, d_with_label, d_with_wrap_at]:
        _test_conversions(d)
        _test_methods_properties(d)
        _test_plotting(d)
        _test_json(d)

def test_uniform():
    assert_raises(ValueError, distl.uniform, 0, "a")

    # too many args
    assert_raises(TypeError, distl.uniform, 0, 1, 1)

    d = distl.uniform(5, 10)
    d = distl.boxcar(5, 10)
    d = d.copy()

    _test_conversions(d)
    _test_methods_properties(d)
    _test_plotting(d)
    _test_json(d)

def test_delta():
    # passing string
    assert_raises(ValueError, distl.delta, "a")

    # too many args
    assert_raises(TypeError, distl.delta, 0, 1)


    d = distl.delta(1)
    d = d.copy()

    _test_conversions(d)
    _test_methods_properties(d)
    _test_plotting(d)
    _test_json(d)

def test_histogram():
    d = distl.histogram_from_data(distl.normal().sample(size=100))
    d = distl.histogram_from_bins(d.bins, d.density)
    d = d.copy()

    _test_conversions(d)
    _test_methods_properties(d)
    _test_plotting(d)
    _test_json(d)

def test_composite():
    u = distl.uniform()
    d = distl.delta()
    g = distl.gaussian()

    u + d
    u + g
    u - d
    u - g
    u * d
    u * g
    # TODO: fix divisions
    # u / d
    # u / g
    u | g
    u & g

    d = d*u
    d = d.copy()

    for dist in [d*u, d+u, d|u, d&u, np.sin(u)]:
        _test_conversions(dist)
        _test_methods_properties(dist)
        _test_plotting(dist)
        _test_json(dist)

def test_mvgaussian():
    d = distl.mvgaussian([5,10, 12],
                           np.array([[ 2,  1, -1],
                                     [ 1,  2,  1],
                                     [-1,  1,  2]]),
                           allow_singular=True,
                           labels=['a', 'b', 'c'])

    d_with_units = d.copy()
    d_with_units.units = ['solRad', 'deg', 'kg']


    for d in [d, d_with_units]:
        _test_conversions(d)
        _test_methods_properties(d)
        _test_plotting(d)
        _test_json(d)

def test_mvgaussianslice():
    d = distl.mvgaussian([5,10, 12],
                           np.array([[ 2,  1, -1],
                                     [ 1,  2,  1],
                                     [-1,  1,  2]]),
                           allow_singular=True,
                           labels=['a', 'b', 'c'])

    d = d.slice('a')
    d = d.copy()

    _test_conversions(d)
    _test_methods_properties(d)
    _test_plotting(d)
    _test_json(d)


def test_mvhistogram():
    mvg = distl.mvgaussian([5,10, 12],
                           np.array([[ 2,  1, -1],
                                     [ 1,  2,  1],
                                     [-1,  1,  2]]),
                           allow_singular=True,
                           labels=['a', 'b', 'c'])

    d = distl.mvhistogram_from_data(mvg.sample(size=100), labels=['a', 'b', 'c'])
    d = d.copy()

    _test_conversions(d)
    _test_methods_properties(d)
    _test_plotting(d)
    _test_json(d)

def test_mvhistogramslice():
    mvg = distl.mvgaussian([5,10, 12],
                           np.array([[ 2,  1, -1],
                                     [ 1,  2,  1],
                                     [-1,  1,  2]]),
                           allow_singular=True,
                           labels=['a', 'b', 'c'])

    d = distl.mvhistogram_from_data(mvg.sample(size=100), labels=['a', 'b', 'c'])
    d = d.slice('a')
    d = d.copy()

    _test_conversions(d)
    _test_methods_properties(d)
    _test_plotting(d)
    _test_json(d)

def _test_conversions(d):
    if isinstance(d, distl._distl.BaseMultivariateDistribution):
        if d.__class__.__name__ not in ['MVHistogram']:
            d.to_mvhistogram()
        if d.__class__.__name__ not in ['MVGaussian']:
            d.to_mvgaussian()

        d.to_univariate(dimension='a')
        d.to_gaussian(dimension='a')
        d.to_histogram(dimension='a')
        d.slice(dimension='a')
        d.take_dimensions(['a', 'c'])

    elif isinstance(d, distl._distl.BaseMultivariateSliceDistribution):
        d.change_slice_dimension('a')
        d.to_univariate()

    elif isinstance(d, distl._distl.BaseUnivariateDistribution):
        if d.__class__.__name__ not in ['Histogram']:
            d.to_histogram()
        if d.__class__.__name__ not in ['Uniform']:
            d.to_uniform()
        if d.__class__.__name__ not in ['Delta']:
            d.to_delta()
            d.to_delta(loc='mean')
            d.to_delta(loc='median')
            d.to_delta(loc='sample')
    else:
        raise NotImplementedError("tests for class {} not implemented".format(d.__class__.__name__))

def _test_methods_properties(d):
    if isinstance(d, distl._distl.BaseMultivariateDistribution):
        d.labels
        d.units
        d.wrap_ats

        if d.__class__.__name__ not in ['MVGaussian']:
            d.calculate_means()
            d.calculate_covariances()

    elif isinstance(d, distl._distl.BaseUnivariateDistribution):
        if isinstance(d, distl._distl.BaseMultivariateSliceDistribution):
            d.dimension
            d.multivariate

        else:
            d.dist_constructor_func
            d.dist_constructor_argnames
            d.dist_constructor_args
            d.dist_constructor_object

            d.ppf(0.5)



            # TODO: support changing units for MVSlices?
            d * u.solRad

            d2 = d.copy()
            d2.unit = 'cm'
            d2.to('m')
            d2.to_si()
            d2.to_solar()
            d2.sample(as_quantity=True, unit='km')
            d2.unit = None


        d.__repr__()
        str(d)
        d.label
        d.unit
        d.wrap_at
        d.wrap(5)

        d < 5
        d > 5
        d <= 5
        d >= 5
        g = distl.gaussian(5)
        d < g
        d > g
        d <= g
        d >= g

        d * 2
        # TODO: fix division
        # d / 2
        d + 2
        d - 2
        np.sin(d)
        np.cos(d)
        np.tan(d)

        if 'Histogram' not in d.__class__.__name__:
            # passing value
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




    else:
        raise NotImplementedError("tests for class {} not implemented".format(d.__class__.__name__))

    d.copy()
    d.hash
    d.to_json()
    d.to_dict()

    d.sample()
    # TODO: need to fix caching for MVHistogramSlice
    if d.__class__.__name__ not in ['MVHistogramSlice', 'MVHistogram']:
        d.pdf()
        d.logpdf()
        d.cdf()
        d.logcdf()

def _test_plotting(d):
    if isinstance(d, distl._distl.BaseMultivariateDistribution):
        pass

    elif isinstance(d, distl._distl.BaseUnivariateDistribution):
        if 'Histogram' not in d.__class__.__name__:
            d.plot(plot_sample=False, plot_pdf=False, plot_cdf=True)
            d.plot_pdf()
            d.plot_cdf()
        if not isinstance(d, distl._distl.BaseMultivariateSliceDistribution):
            if d.__class__.__name__ not in ['Gaussian']:
                d.plot(plot_gaussian=True)
                d.plot_gaussian()

    else:
        raise NotImplementedError("tests for class {} not implemented".format(d.__class__.__name__))

    d.plot()
    d.plot(color='blue')
    d.plot(plot_sample_kwargs={'color': 'blue'})
    d.plot_sample()


def _test_json(d):
    distl.from_dict(d.to_dict())
    distl.from_json(d.to_json())

    distl.from_dict(d.to_json())
    distl.from_json(d.to_dict())

    distl.from_file(d.to_file('tmp.distl'))


if __name__ == '__main__':
    test_gaussian()
    test_uniform()
    test_delta()
    test_histogram()
    test_composite()
    test_mvgaussian()
    test_mvgaussianslice()
    test_mvhistogram()
    test_mvhistogramslice()
