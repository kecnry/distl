import numpy as _np
import json as _json
from collections import OrderedDict

import matplotlib.pyplot as _plt


################## VALIDATORS ###################

# these all must accept a single value and return a boolean if it matches the condition as well as any alterations to the value
# NOTE: the docstring is used as the error message if the test fails

# def is_unit(value):
#     """must be an astropy unit"""
#     if not _has_astropy:
#         raise ImportError("astropy must be installed for unit support")
#     if (isinstance(value, units.Unit) or isinstance(value, units.IrreducibleUnit) or isinstance(value, units.CompositeUnit)):
#         return True, value
#     else:
#         return False, value

# def is_unit_or_unitstring(value):
#     """must be an astropy.unit"""
#     if is_unit(value)[0]:
#         return True, value
#     try:
#         unit = units.Unit(value)
#     except:
#         return False, value
#     else:
#         return True, unit
#
# def is_unit_or_unitstring_or_none(value):
#     """must be an astropy unit or None"""
#     if value is None:
#         return True, value
#     return is_unit_or_unitstring(value)

def is_bool(value):
    """must be boolean"""
    return isinstance(value, bool), value

def is_float(value):
    """must be a float"""
    return isinstance(value, float) or isinstance(value, int) or isinstance(value, _np.float64), float(value)

def is_int(value):
    """must be an integer"""
    return isinstance(value, int), value

def is_int_positive(value):
    """must be a positive integer"""
    return isinstance(value, int) and value > 0, value

def is_int_positive_or_none(value):
    """must be a postive integer or None"""
    return is_int_positive or value is None, value

def is_valid_shape(value):
    """must be a positive integer or a tuple/list of positive integers"""
    if is_int_positive(value):
        return True, value
    elif isinstance(value, tuple) or isinstance(value, list):
        for v in value:
            if not is_int_positive(v):
                return False, value
        return True, value
    else:
        return False, value

def is_iterable(value):
    """must be an iterable (list, array, tuple)"""
    return isinstance(value, _np.ndarray) or isinstance(value, list) or isinstance(value, tuple), value



######################## DISTRIBUTION FUNCTIONS ###############################

def gaussian(x, loc, scale):
    return 1./_np.sqrt(2*_np.pi*scale**2) * _np.exp(-(x-loc)**2/(2.*scale**2))

def uniform(x, low, high):
    return _np.asarray((x >= low) * (x <= high), dtype='int') / float(high - low)

######################## DISTRIBUTION ABSTRACT CLASS ###########################

class BaseDistribution(object):
    """
    BaseDistribution should be subclassed by any type of distribution creation classesAny subclass
    MUST define the following:
    __init__ (see docs below)
    mean, std properties
    """
    def __init__(self,
                 dist_func, dist_args,
                 sample_func, sample_args,
                 *args):
        """
        all subclasses MUST parse args and send in as tuples via super so that
        order is preserved.
        For example:
        def __init__(self, start, stop, step):
            super(MyClass, self).__init__(('start', start, is_float), ('stop', stop, is_float), ('step', step, is_float))
        All of these "descriptors" will then be available to get and set via
        their attribute names
        """
        self._descriptors = OrderedDict()
        self._validators = OrderedDict()

        self._dist_func = dist_func
        self._dist_args = dist_args

        self._sample_func = sample_func
        self._sample_args = sample_args

        for item in args:
            valid, validated_value = item[2](item[1])
            if valid:
                self._descriptors[item[0]] = validated_value
            else:
                raise ValueError("{} {}, got {}".format(item[0], item[2].__doc__, item[1]))
            self._validators[item[0]] = item[2]

    def __getattr__(self, name):
        """
        for anything that isn't overriden here, call the method on the array itself
        """
        if name in ['_descriptors', '_validators', '_sample_func', '_sample_args', '_dist_func', '_dist_args']:
            # then we need to actually get the attribute
            return super(BaseDistribution, self).__getattr__(name)
        elif name in self._descriptors.keys():
            # then get the item in the dictionary
            return self._descriptors.get(name)
        else:
            raise AttributeError("{} does not have attribute '{}'".format(self.__class__.__name__.lower(), name))

    def __setattr__(self, name, value):
        """
        """
        if name in ['_descriptors', '_validators', '_sample_func', '_sample_args', '_dist_func', '_dist_args', '__class__']:
            return super(BaseDistribution, self).__setattr__(name, value)
        elif name in self._descriptors.keys():
            valid, validated_value = self._validators[name](value)
            if valid:
                self._descriptors[name] = validated_value
            else:
                raise ValueError("{} {}".format(name, validator.__doc__))
        else:
            return setattr(self.array, name, value)

    def __repr__(self):
        descriptors = " ".join(["{}={}".format(k,v) for k,v in self._descriptors.items()])
        return "<{} {}>".format(self.__class__.__name__.lower(), descriptors)

    @property
    def mean(self):
        raise NotImplementedError

    @property
    def std(self):
        raise NotImplementedError

    @property
    def dist_func(self):
        return self._dist_func

    @property
    def dist_args(self):
        return tuple(getattr(self, k) for k in self._dist_args)

    @property
    def sample_func(self):
        return self._sample_func

    @property
    def sample_args(self):
        return tuple(getattr(self, k) for k in self._sample_args)

    def sample(self, size=None):
        return self.sample_func(*self.sample_args, size=size)

    # def plot_func(self, show=False, **kwargs):
    #     ret = _plt.hist(self.sample(size), **kwargs)
    #     if show:
    #         _plt.show()
    #
    #     return ret

    def plot(self, size=1000, plot_sample=True, plot_dist=True, show=False, **kwargs):
        ret = []
        if plot_sample:
            ret_sample = self.plot_sample(size=size, show=False, **kwargs)
            xmin, xmax = _plt.gca().get_xlim()
        else:
            ret_sample = None
            sample = self.sample(size=size)
            xmin = _np.min(sample)
            xmax = _np.max(sample)

        if plot_dist:
            x = _np.linspace(xmin, xmax, 1001)
            ret_dist = self.plot_dist(x, show=False, **{k:v for k,v in kwargs.items() if k not in ['bins']})
        else:
            ret_dist = None


        if show:
            _plt.xlabel('value')
            _plt.ylabel('density')
            _plt.show()

        return (ret_sample, ret_dist)


    def plot_sample(self, size=1000, show=False, **kwargs):
        ret = _plt.hist(self.sample(size), density=True, **kwargs)
        if show:
            _plt.xlabel('value')
            _plt.ylabel('density')
            _plt.show()

        return ret

    def plot_dist(self, x, show=False, **kwargs):
        if self.dist_func is not None:
            ret = _plt.plot(x, self.dist_func(x, *self.dist_args), **kwargs)
        else:
            ret = None

        if show:
            _plt.xlabel('value')
            _plt.ylabel('density')
            _plt.show()

        return ret




    def to_dict(self):
        """
        dump a representation of the nparray object to a dictionary.  The
        nparray object should then be able to be fully restored via
        nparray.from_dict
        """
        def _json_safe(v):
            if isinstance(v, _np.ndarray):
                return v.tolist()
            # elif is_unit(v)[0]:
            #     return v.to_string()
            else:
                return v
        d = {k:_json_safe(v) for k,v in self._descriptors.items()}
        d['npdists'] = self.__class__.__name__.lower()
        return d

    def to_json(self, **kwargs):
        """
        dump a representation of the nparray object to a json-formatted string.
        The nparray object should then be able to be fully restored via
        nparray.from_json
        """
        return _json.dumps(self.to_dict(), **kwargs)

    def to_file(self, filename, **kwargs):
        """
        dump a representation of the nparray object to a json-formatted file.
        The nparray object should then be able to be fully restored via
        nparray.from_file
        @parameter str filename: path to the file to be created (will overwrite
            if already exists)
        @rtype: str
        @returns: the filename
        """
        f = open(filename, 'w')
        f.write(self.to_json(**kwargs))
        f.close()
        return filename


####################### DISTRIBUTION SUB-CLASSES ###############################

class Histogram(BaseDistribution):
    def __init__(self, bins, density):
        super(Histogram, self).__init__(None, None,
                                        self._sample_from_hist, ('bins', 'density'),
                                        ('bins', bins, is_iterable), ('density', density, is_iterable))

    @classmethod
    def from_data(cls, data, bins=10, range=None, weights=None):
        hist, bin_edges = _np.histogram(data, bins=bins, range=range, weights=weights, density=True)

        return cls(bin_edges, hist)

    def _sample_from_hist(self, bins, counts, size=None):
        if size is None:
            size = 1
            # if not isinstance(size, int):
                # raise TypeError("size must be of type int or None")

            # return np.array([self._sample_from_hist(bins=bins, counts=counts, size=None) for size in range(size)])

        # adopted from: https://stackoverflow.com/a/17822210
        bin_midpoints = self.bins[:-1] + _np.diff(self.bins)/2
        cdf = _np.cumsum(self.density)
        cdf = cdf / float(cdf[-1])

        values = _np.random.rand(size)
        value_bins = _np.searchsorted(cdf, values)
        random_from_cdf = bin_midpoints[value_bins]

        return random_from_cdf

    @property
    def mean(self):
        bin_midpoints = self.bins[:-1] + _np.diff(self.bins)/2
        mean = _np.average(bin_midpoints, weights=self.density)
        return mean

    @property
    def std(self):
        bin_midpoints = self.bins[:-1] + _np.diff(self.bins)/2
        mean = _np.average(bin_midpoints, weights=self.density)

        var = _np.average((bin_midpoints - mean)**2, weights=self.density)
        sigma = _np.sqrt(var)
        return sigma

    def to_gaussian(self):
        return Gaussian(self.mean, self.std)

    def to_uniform(self, sigma=1.0):
        return self.to_gaussian().to_uniform(sigma=sigma)



class Gaussian(BaseDistribution):
    def __init__(self, loc=0.0, scale=0.0):
        super(Gaussian, self).__init__(gaussian, ('loc', 'scale'),
                                       _np.random.normal, ('loc', 'scale'),
                                       ('loc', loc, is_float), ('scale', scale, is_float))

    @property
    def mean(self):
        return self.loc

    @property
    def std(self):
        return self.scale

    def to_uniform(self, sigma=1.0):
        low = self.loc - self.scale * sigma
        high = self.loc + self.scale * sigma
        return Uniform(low, high)

    def to_histogram(self, N=1000, bins=10, range=None):
        return Histogram.from_data(self.sample(size=N), bins=bins, range=range)

class Uniform(BaseDistribution):
    def __init__(self, low=0.0, high=1.0):
        super(Uniform, self).__init__(uniform, ('low', 'high'),
                                      _np.random.uniform, ('low', 'high'),
                                      ('low', low, is_float), ('high', high, is_float))

    @property
    def mean(self):
        return (self.low+self.high) / 2.0

    def to_gaussian(self, sigma=1.0):
        loc = self.mean
        scale = (self.high - self.low) / (2.0 * sigma)
        return Gaussian(loc, scale)

    def to_histogram(self, N=1000, bins=None, range=None):
        return Histogram.from_data(self.sample(size=N), bins=bins, range=range)
