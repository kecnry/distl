from nose.tools import assert_raises

import distl
import numpy as np
import astropy.units as u

def test_gaussian():
    # passing string
    print("*** test_methods.test_gaussian 1")
    assert_raises(TypeError, distl.gaussian, 0, "a")
    print("*** test_methods.test_gaussian 2")

    # too many args
    assert_raises(TypeError, distl.gaussian, 0, 1, 1)
    print("*** test_methods.test_gaussian 3")

    d = distl.gaussian(unit=u.deg)
    print("*** test_methods.test_gaussian 4")

    d.to(u.rad)
    print("*** test_methods.test_gaussian 5")

    d.to('rad')
    print("*** test_methods.test_gaussian 6")

    d_with_unit = distl.gaussian(unit='deg')
    print("*** test_methods.test_gaussian 7")

    d_with_label = distl.gaussian(label='mylabel')
    print("*** test_methods.test_gaussian 8")


    d_with_wrap_at = distl.gaussian(10, 2, wrap_at=12)
    print("*** test_methods.test_gaussian 9")

    d = distl.gaussian(5, 10)
    print("*** test_methods.test_gaussian 10")


    d = distl.normal(5, 10)
    print("*** test_methods.test_gaussian 11")


    d = d.copy()
    print("*** test_methods.test_gaussian 12")


    for d in [d, d_with_unit, d_with_label, d_with_wrap_at]:
        _test_conversions(d)
        _test_methods_properties(d)
        # _test_plotting(d)
        _test_json(d)

    print("*** test_methods.test_gaussian 13")


def test_uniform():
    assert_raises(TypeError, distl.uniform, 0, "a")

    # too many args
    assert_raises(TypeError, distl.uniform, 0, 1, 1)

    d = distl.uniform(5, 10)
    d = distl.boxcar(5, 10)
    d = d.copy()

    _test_conversions(d)
    _test_methods_properties(d)
    # _test_plotting(d)
    _test_json(d)

def test_delta():
    # passing string
    assert_raises(TypeError, distl.delta, "a")

    # too many args
    assert_raises(TypeError, distl.delta, 0, 1)


    d = distl.delta(1)
    d = d.copy()

    _test_conversions(d)
    _test_methods_properties(d)
    # _test_plotting(d)
    _test_json(d)

def test_histogram():
    d = distl.histogram_from_data(distl.normal().sample(size=100))
    d = distl.histogram_from_bins(d.bins, d.density)
    d = d.copy()

    _test_conversions(d)
    _test_methods_properties(d)
    # _test_plotting(d)
    _test_json(d)

def test_samples():
    d = distl.samples(distl.normal().sample(size=100))
    d = d.copy()

    _test_conversions(d)
    _test_methods_properties(d)
    # _test_plotting(d)
    _test_json(d)

def test_composite():
    u = distl.uniform()
    d = distl.delta()
    g = distl.gaussian()
    g2 = distl.gaussian(3, 1)

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

    d = d.copy()
    c = g*u

    # TODO: include delta in this logic: |/& currently chokes because of intervals
    for dist in [d*u, c*u, d+u, c+u, g|u, c|u, g&u, c&u, np.sin(u), distl._distl.Composite('__mul__', (u, g, g)), distl._distl.Composite('__or__', (u, g, g2))]:
        print("test_composite dist=", dist)
        _test_conversions(dist)
        _test_methods_properties(dist)
        # _test_plotting(dist)
        _test_json(dist)

def test_function():
    u = distl.uniform()
    d = distl.delta()
    g = distl.gaussian()

    def func(u, d, g):
        return u*d+g

    d = distl.function(func, (u,d), {'g': g})
    d = d.copy()

    _test_conversions(d)
    _test_methods_properties(d)
    # _test_plotting(d)
    _test_json(d)

def test_mvgaussian():
    print("*** test_methods.test_mvgaussian 1")
    d = distl.mvgaussian([5,10, 12],
                           np.array([[ 2,  1, -1],
                                     [ 1,  2,  1],
                                     [-1,  1,  2]]),
                           allow_singular=True,
                           labels=['a', 'b', 'c'])

    print("*** test_methods.test_mvgaussian 2")

    d_with_units = d.copy()
    print("*** test_methods.test_mvgaussian 3")

    d_with_units.units = ['solRad', 'deg', 'kg']

    print("*** test_methods.test_mvgaussian 4")

    for d in [d, d_with_units]:
        print("*** test_methods.test_mvgaussian 5")

        _test_conversions(d)
        print("*** test_methods.test_mvgaussian 6")

        _test_methods_properties(d)
        print("*** test_methods.test_mvgaussian 7")

        # _test_plotting(d)
        _test_json(d)
        print("*** test_methods.test_mvgaussian 8")


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
    # _test_plotting(d)
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
    # _test_plotting(d)
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
    # _test_plotting(d)
    _test_json(d)

def test_mvsamples():
    mvg = distl.mvgaussian([5,10, 12],
                           np.array([[ 2,  1, -1],
                                     [ 1,  2,  1],
                                     [-1,  1,  2]]),
                           allow_singular=True,
                           labels=['a', 'b', 'c'])

    d = distl.mvsamples(mvg.sample(size=100), labels=['a', 'b', 'c'])
    d = d.copy()

    _test_conversions(d)
    _test_methods_properties(d)
    # _test_plotting(d)
    _test_json(d)

def test_mvsamplesslice():
    mvg = distl.mvgaussian([5,10, 12],
                           np.array([[ 2,  1, -1],
                                     [ 1,  2,  1],
                                     [-1,  1,  2]]),
                           allow_singular=True,
                           labels=['a', 'b', 'c'])

    d = distl.mvsamples(mvg.sample(size=100), labels=['a', 'b', 'c'])
    d = d.slice('a')
    d = d.copy()

    _test_conversions(d)
    _test_methods_properties(d)
    # _test_plotting(d)
    _test_json(d)

def test_gaussian_around():
    d = distl.gaussian_around(scale=1)
    assert_raises(ValueError, d.sample)

    _test_json(d)

    d.sample(value=5)
    d(5)
    d.value = 5
    d()

    _test_methods_properties(d)
    # _test_plotting(d)
    _test_json(d)

def test_uniform_around():
    d = distl.uniform_around(width=1)
    assert_raises(ValueError, d.sample)

    _test_json(d)

    d.sample(value=5)
    d(5)
    d.value = 5
    d()

    _test_methods_properties(d)
    # _test_plotting(d)
    _test_json(d)

def test_delta_around():
    d = distl.delta_around()
    assert_raises(ValueError, d.sample)

    _test_json(d)

    d.sample(value=5)
    d(5)
    d.value = 5
    d()

    _test_methods_properties(d)
    # _test_plotting(d)
    _test_json(d)

def _test_conversions(d):
    print("*** test_methods.test_conversions 1")
    if isinstance(d, distl._distl.BaseMultivariateDistribution):
        print("*** test_methods.test_conversions MV ({})".format(d.__class__.__name__))
        if d.__class__.__name__ not in ['MVHistogram']:
            print("*** test_methods.test_conversions MV to_mvhistogram")
            d.to_mvhistogram(N=100)
        if d.__class__.__name__ not in ['MVGaussian']:
            print("*** test_methods.test_conversions MV to_mvgaussian")
            if d.__class__.__name__ in ['MVSamples']:
                # doesn't take N as an argument
                d.to_mvgaussian()
            else:
                d.to_mvgaussian(N=100)
        if d.__class__.__name__ not in ['MVSamples']:
            print("*** test_methods.test_conversions MV to_mvsamples")
            d.to_mvsamples(N=100)

        print("*** test_methods.test_conversions MV 2")

        d.to_univariate(dimension='a')
        print("*** test_methods.test_conversions MV 3")

        d.to_gaussian(dimension='a')
        print("*** test_methods.test_conversions MV 4")

        d.to_histogram(dimension='a')
        print("*** test_methods.test_conversions MV 5")

        d.to_samples(dimension='a')
        print("*** test_methods.test_conversions MV 6")

        d.slice(dimension='a')
        print("*** test_methods.test_conversions MV 7")

        d.take_dimensions(['a', 'c'])
        print("*** test_methods.test_conversions MV 8")


    elif isinstance(d, distl._distl.BaseMultivariateSliceDistribution):
        print("*** test_methods.test_conversions MVS 1")

        d.change_slice_dimension('b')
        print("*** test_methods.test_conversions MVS 2")


        d.to_univariate()
        print("*** test_methods.test_conversions MVS 3")


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
        if d.__class__.__name__ not in ['Samples']:
            d.to_samples()
    else:
        raise NotImplementedError("test_conversions for class {} not implemented".format(d.__class__.__name__))

def _test_methods_properties(d):
    if isinstance(d, distl._distl.BaseMultivariateDistribution):
        d.labels
        d.labels_latex
        d.units
        d.wrap_ats

        if d.__class__.__name__ not in ['MVGaussian']:
            d.calculate_means()
            d.calculate_covariances()
        else:
            d.mean
            d.cov

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
        d.label_latex
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
        d ** 2
        # TODO: fix division
        # d / 2
        d + 2
        d - 2
        np.sin(d)
        np.cos(d)
        np.tan(d)
        np.arcsin(d)
        np.arccos(d)
        np.arctan(d)
        np.arctan2(d, g)
        np.log(d)
        np.log10(d)

        if d.__class__.__name__ not in ['MVHistogram', 'MVSamples']:
            # passing value
            d.pdf(0)
            d.logpdf(0)

        if d.__class__.__name__ not in ['MVHistogram', 'Samples', 'MVSamples', 'MVSamplesSlice']:
            d.cdf(0)
            d.logcdf(0)

        if d.__class__.__name__ not in ['Samples', 'MVSamples', 'MVSamplesSlice']:
            d.sf(0)
            d.logsf(0)
            d.isf(0)

            d.moment(1)
            d.entropy()

        # d.expect(...)

        d.uncertainties()
        d.uncertainties(tex=True)
        d.median()
        d.mean()
        d.var()
        d.std()
        d.interval(0.99)


    elif isinstance(d, distl._distl.BaseAroundGenerator):
        d.label
        d.label_latex
        d.unit
        d.wrap_at
        d.value

        d.pdf(0)

    else:
        raise NotImplementedError("test_methods_properties for class {} not implemented".format(d.__class__.__name__))

    d.copy()
    d.hash
    if not isinstance(d, distl._distl.Function):
        d.to_json()
    d.to_dict()

    d.sample(size=2)
    d.sample()
    # TODO: need to fix caching for MVHistogramSlice, MVSamplesSlice
    # TODO: need to fix MVGaussian support in Python 2 on travis
    # TODO: cache the underyling frozen distribution for BaseAroundGenerators and then provide better error message when cache clears
    if d.__class__.__name__ not in ['MVHistogramSlice', 'MVHistogram', 'MVSamples', 'MVSamplesSlice', 'MVGaussian'] and not isinstance(d, distl._distl.BaseAroundGenerator):
        d.pdf()
        d.logpdf()

        if d.__class__.__name__ not in ['Samples']:
            d.cdf()
            d.logcdf()

def _test_plotting(d):
    if isinstance(d, distl._distl.BaseMultivariateDistribution):
        pass

    elif isinstance(d, distl._distl.BaseUnivariateDistribution):
        if d.__class__.__name__ not in ['MVHistogram']:
            d.plot_pdf()
        if d.__class__.__name__ not in ['MVHistogram', 'Samples', 'MVSamples', 'MVSamplesSlice']:
            d.plot(plot_sample=False, plot_pdf=False, plot_cdf=True)
            d.plot_cdf()
        if not isinstance(d, distl._distl.BaseMultivariateSliceDistribution):
            if d.__class__.__name__ not in ['Gaussian']:
                d.plot(plot_gaussian=True)
                d.plot_gaussian()

    elif isinstance(d, distl._distl.BaseAroundGenerator):
        pass

    else:
        raise NotImplementedError("test_plotting for class {} not implemented".format(d.__class__.__name__))

    d.plot()
    d.plot(color='blue')
    d.plot(plot_sample_kwargs={'color': 'blue'})
    d.plot_sample()


def _test_json(d):
    if not isinstance(d, distl._distl.Function):
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
    test_samples()
    test_composite()
    test_function()
    test_mvgaussian()
    test_mvgaussianslice()
    test_mvhistogram()
    test_mvhistogramslice()
    test_mvsamples()
    test_mvsamplesslice()

    test_gaussian_around()
    test_uniform_around()
    test_delta_around()
