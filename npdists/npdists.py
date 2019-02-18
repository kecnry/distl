import numpy as _np
import json as _json
from collections import OrderedDict

try:
    import matplotlib.pyplot as _plt
except ImportError:
    _has_mpl = False
else:
    _has_mpl = True

try:
    from astropy import units as _units
except ImportError:
    _has_astropy = False
else:
    _has_astropy = True

try:
    import dill as _dill
except ImportError:
    _has_dill = False
else:
    _has_dill = True

_math_symbols = {'__mul__': '*', '__add__': '+', '__sub__': '-', '__div__': '/'}

################## VALIDATORS ###################

# these all must accept a single value and return a boolean if it matches the condition as well as any alterations to the value
# NOTE: the docstring is used as the error message if the test fails

def is_distribution(value):
    """must be an npdists Distribution object"""
    if isinstance(value, dict) and 'npdists' in value.keys():
        # TODO: from_dict probably not available since its in __init__.py
        return True, from_dict(value)
    return isinstance(value, BaseDistribution), value

def is_distribution_or_none(value):
    """must be an npdists Distribution object or None"""
    if value is None:
        return True, value
    else:
        return is_distribution(value)

def is_math(value):
    """must be a valid math operator"""
    # TODO: make this more robust checking
    valid_maths = ['__add__', '__radd__', '__sub__', '__rsub__', '__mul__', '__rmul__', '__div__', '__rdiv__']
    valid_maths += ['sin', 'cos', 'tan']
    return value in valid_maths, value

def is_callable(value):
    """must be a callable function"""
    if isinstance(value, str):
        # try to "undill"
        if _has_dill:
            value = _dill.loads(value)
        else:
            raise ImportError("'dill' package required to load functions")
    return hasattr(value, 'func_name'), value

def is_unit(value):
    """must be an astropy unit"""
    if not _has_astropy:
        raise ImportError("astropy must be installed for unit support")
    if (isinstance(value, _units.Unit) or isinstance(value, _units.IrreducibleUnit) or isinstance(value, _units.CompositeUnit)):
        return True, value
    else:
        return False, value

def is_unit_or_unitstring(value):
    """must be an astropy.unit"""
    if is_unit(value)[0]:
        return True, value
    try:
        unit = _units.Unit(value)
    except:
        return False, value
    else:
        return True, unit

def is_unit_or_unitstring_or_none(value):
    """must be an astropy unit or None"""
    if value is None:
        return True, value
    return is_unit_or_unitstring(value)

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

def delta(x, value):
    return _np.asarray(x==value, dtype='int')

def gaussian(x, loc, scale):
    return 1./_np.sqrt(2*_np.pi*scale**2) * _np.exp(-(x-loc)**2/(2.*scale**2))

def uniform(x, low, high):
    return _np.asarray((x >= low) * (x <= high), dtype='int') / float(high - low)

######################## DISTRIBUTION ABSTRACT CLASS ###########################

class BaseDistribution(object):
    """
    BaseDistribution is the parent class for all distributions and should
    not be used directly by the user.

    Any subclass distribution should override the following:

    * <BaseDistribution.__init__>
    * <BaseDistribution.mean>
    * <BaseDistribution.std>
    """
    def __init__(self, unit, label,
                 dist_func, dist_args,
                 sample_func, sample_args,
                 *args):
        """
        BaseDistribution is the parent class for all distributions and should
        not be used directly by the user.

        Any subclass distribution should override the init but call this via
        super.

        For example:

        ```py
        def __init__(self, start, stop, step):
            super(MyClass, self).__init__(('start', start, is_float), ('stop', stop, is_float), ('step', step, is_float))
        ```

        All of these "descriptors" will then be available to get and set via
        their attribute names
        """
        self._descriptors = OrderedDict()
        self._validators = OrderedDict()

        self._dist_func = dist_func
        self._dist_args = dist_args

        self._sample_func = sample_func
        self._sample_args = sample_args

        self.label = label
        self.unit = unit

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
        if name in ['_descriptors', '_validators', '_sample_func', '_sample_args', '_dist_func', '_dist_args', '_unit', 'unit', '_label', 'label']:
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
        if name in ['_descriptors', '_validators', '_sample_func', '_sample_args', '_dist_func', '_dist_args', '__class__', '_unit', 'unit', '_label', 'label']:
            return super(BaseDistribution, self).__setattr__(name, value)
        elif name in self._descriptors.keys():
            valid, validated_value = self._validators[name](value)
            if valid:
                self._descriptors[name] = validated_value
            else:
                raise ValueError("{} {}".format(name, validator.__doc__))
        else:
            raise AttributeError("{} does not have attribute '{}'".format(self.__class__.__name__.lower(), name))

    def __repr__(self):
        descriptors = " ".join(["{}={}".format(k,v) for k,v in self._descriptors.items()])
        return "<npdists.{} {} unit={}>".format(self.__class__.__name__.lower(), descriptors, self.unit)

    def __str__(self):
        if self.label is not None:
            return "{"+self.label+"}"
        else:
            return self.__repr__()

    def __float__(self):
        """
        by default, have the float representation come from sampling, but
        subclasses can/should override this to be the central/median/mode if
        possible
        """
        return self.sample()

    def __lt__(self, other):
        if isinstance(other, BaseDistribution):
            return self.__float__() < other.__float__()
        return self.__float__() < other

    def __le__(self, other):
        if isinstance(other, BaseDistribution):
            return self.__float__() <= other.__float__()
        return self.__float__() <= other

    def __gt__(self, other):
        if isinstance(other, BaseDistribution):
            return self.__float__() > other.__float__()
        return self.__float__() > other

    def __ge__(self, other):
        if isinstance(other, BaseDistribution):
            return self.__float__() >= other.__float__()
        return self.__float__() >= other

    def __copy__(self):
        return self.__class__(unit=self.unit, label=self.label, **self._descriptors)

    def __deepcopy__(self, memo):
        return self.__copy__()

    def copy(self):
        """
        Make a copy of the distribution object.

        Returns
        ---------
        * a copy of the distribution object
        """
        return self.__copy__()

    def __mul__(self, other):
        if _has_astropy and is_unit(other)[0]:
            copy = self.copy()
            copy.unit = other
            return copy

        elif isinstance(other, BaseDistribution):
            return Composite("__mul__", self, other)
        elif isinstance(other, float) or isinstance(other, int):
            return self.__mul__(Delta(other))
        else:
            raise TypeError("cannot multiply {} by type {}".format(self.__class__.__name__, type(other)))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __div__(self, other):
        if isinstance(other, BaseDistribution):
            return Composite("__div__", self, other)
        elif isinstance(other, float) or isinstance(other, int):
            return self.__div__(Delta(other))
        else:
            raise TypeError("cannot divide {} by type {}".format(self.__class__.__name__, type(other)))

    def __rdiv__(self, other):
        if isinstance(other, BaseDistribution):
            return Composite("__rdiv__", self, other)
        elif isinstance(other, float) or isinstance(other, int):
            return self.__rdiv__(Delta(other))
        else:
            raise TypeError("cannot divide {} by type {}".format(self.__class__.__name__, type(other)))

    def __add__(self, other):
        if isinstance(other, BaseDistribution):
            return Composite("__add__", self, other)
        elif isinstance(other, float) or isinstance(other, int):
            return self.__add__(Delta(other))
        else:
            raise TypeError("cannot add {} by type {}".format(self.__class__.__name__, type(other)))

    # def __radd__(self, other):
    #     return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, BaseDistribution):
            return Composite("__sub__", self, other)
        elif isinstance(other, float) or isinstance(other, int):
            return self.__sub__(Delta(other))
        else:
            raise TypeError("cannot subtract {} by type {}".format(self.__class__.__name__), type(other))

    def sin(self):
        return Composite("sin", self)

    def cos(self):
        return Composite("cos", self)

    def tan(self):
        return Composite("tan", self)

    @property
    def label(self):
        """
        The label of the distribution object.  When not None, this is used for
        the x-label when plotting (see <BaseDistribution.plot>) and for the
        string representation for any math in a <Composite> or <Function>
        distribution.
        """
        return self._label

    @label.setter
    def label(self, label):
        if not (label is None or isinstance(label, str)):
            raise TypeError("label must be of type str")

        self._label = label

    @property
    def unit(self):
        """
        The units of the distribution.  Astropy is required in order to set
        and/or use distributions with units.

        See also:

        * <BaseDistribution.to>
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        if not (unit is None or isinstance(unit, _units.Unit) or isinstance(unit, _units.CompositeUnit) or isinstance(unit, _units.IrreducibleUnit)):
            raise TypeError("unit must be of type astropy.units.Unit")

        self._unit = unit

    def to(self, unit):
        """
        Convert to different units.  This creates a copy and returns the
        new distribution with the new units.  Astropy is required in order to
        set and/or use units.

        See also:

        * <BaseDistribution.unit>

        Arguments
        ------------
        * `unit` (astropy.unit object): unit to use in the new distribution.
            The current units (see <BaseDistribution.unit>) must be able to
            convert to the requested units.

        Returns
        ------------
        * the new distribution object

        Raises
        -----------
        * ImportError: if astropy dependency is not met.
        """
        if not _has_astropy:
            raise ImportError("astropy required to handle units")

        if self.unit is None:
            raise ValueError("distribution object does not have a unit")

        factor = self.unit.to(unit)

        new_dist = self.copy()
        new_dist.unit = unit
        new_dist *= factor
        return new_dist

    @property
    def mean(self):
        """
        msean is not implemented for this distribution type.

        Raises
        --------
        * NotImplementedError
        """
        raise NotImplementedError

    @property
    def std(self):
        """
        std is not implemented for this distribution type.

        Raises
        --------
        * NotImplementedError
        """
        raise NotImplementedError

    @property
    def dist_func(self):
        """
        Return the callable function to access the distribution function, if
        available.

        See also:

        * <BaseDistribution.dist_args>
        * <BaseDistribution.distribution>

        Returns
        -------
        * callable function
        """
        return self._dist_func

    @property
    def dist_args(self):
        """
        Return the arguments sent to the distribution function.

        See also:

        * <BaseDistribution.dist_func>
        * <BaseDistribution.distribution>

        Returns
        --------
        * tuple
        """

        return tuple(getattr(self, k) for k in self._dist_args)

    @property
    def sample_func(self):
        """
        Return the callable function to sample the distribution, if available.

        See also:

        * <BaseDistribution.sample_args>
        * <BaseDistribution.sample>

        Returns
        --------
        * callable function
        """
        return self._sample_func

    @property
    def sample_args(self):
        """
        Return the arguments sent to the sample function.

        See also:

        * <BaseDistribution.sample_func>
        * <BaseDistribution.sample>

        Returns
        --------
        * tuple
        """
        return tuple(getattr(self, k) for k in self._sample_args)

    def _return_with_units(self, value, unit=None, as_quantity=False):
        if (as_quantity or unit) and not _has_astropy:
            raise ImportError("astropy required to return quantity objects")

        if unit is None and not as_quantity:
            return value

        if self.unit is not None:
            value *= self.unit

        if unit is not None:
            if self.unit is None:
                raise ValueError("can only return unit if unit is set for distribution")

            if not _has_astropy:
                raise ImportError("astropy must be installed for unit support")

            value = value.to(unit)


        if as_quantity:
            return value
        else:
            return value.value

    def sample(self, size=None, unit=None, as_quantity=False):
        """
        Sample from the distribution.

        Arguments
        -----------
        * `size` (int or tuple or None, optional, default=None): size/shape of the
            resulting array.
        * `unit` (astropy.unit, optional, default=None): unit to convert the
            resulting sample(s).  Astropy must be installed in order to convert
            units.
        * `as_quantity` (bool, optional, default=False): whether to return an
            astropy quantity object instead of just the value.  Astropy must
            be installed.

        Returns
        ---------
        * float or array: float if `size=None`, otherwise a numpy array with
            shape defined by `size`.
        """
        return self._return_with_units(self.sample_func(*self.sample_args, size=size), unit=unit, as_quantity=as_quantity)

    def distribution(self, x, unit=None, as_quantity=False):
        """
        Give the density (y) values of the underlying distribution for a given
        array of values (x).

        Arguments
        ----------
        * `x` (array): x-values at which to compute the densities.
        * `unit` (astropy.unit, optional, default=None): unit to convert the
            resulting array.  Astropy must be installed in order to convert units.
        * `as_quantity` (bool, optional, default=False): whether to return an
            astropy quantity object instead of just an array.  Astropy must
            be installed.

        Returns
        ---------
        * array: array of density/y values.
        """
        # x is assumed to be in the new units
        if unit is not None:
            if self.unit is None:
                raise ValueError("can only convert units on Distributions with units set")
            # convert to original units
            x = (x * unit).to(self.unit).value
        return self._return_with_units(self.dist_func(x, *self.dist_args), unit=unit, as_quantity=as_quantity)


    # def plot_func(self, show=False, **kwargs):
    #     ret = _plt.hist(self.sample(size), **kwargs)
    #     if show:
    #         _plt.show()
    #
    #     return ret

    def _xlabel(self, unit=None):
        l = 'value'
        if _has_astropy and self.unit is not None:
            l += ' ({})'.format(unit if unit is not None else self.unit)

        return l


    def plot(self, size=100000, unit=None, plot_sample=True, plot_dist=True, show=False, **kwargs):
        """
        Plot both the analytic distribution function as well as a sampled
        histogram from the distribution.  Requires matplotlib to be installed.

        See also:

        * <BaseDistribution.plot_sample>
        * <BaseDistribution.plot_dist>

        Arguments
        -----------
        * `size` (int, optional, default=100000): number of points to sample for
            the histogram.  See also <BaseDistribution.sample>.
        * `unit` (astropy.unit, optional, default=None): units to use along
            the x-axis.  Astropy must be installed.
        * `plot_sample` (bool, optional, default=True): whether to plot the
            histogram from sampling.  See also <BaseDistribution.plot_sample>.
        * `plot_dist` (bool, optional, default=True): whether to plot the
            analytic form of the underlying distribution, if applicable.
            See also <BaseDistribution.plot_dist>.
        * `show` (bool, optional, default=True): whether to show the resulting
            matplotlib figure.
        * `**kwargs`: all keyword arguments (except for `bins`) will be passed
            on to <BaseDistribution.plot_dist> and all keyword arguments will
            be passed on to <BaseDistribution.plot_sample>.

        Returns
        --------
        * tuple: the return values from both <BaseDistribution.plot_sample> and
            <BaseDistribution.plot_dist>.

        Raises
        --------
        * ImportError: if matplotlib dependency is not met.
        """
        if not _has_mpl:
            raise ImportError("matplotlib required for plotting")

        ret = []

        if plot_sample:
            kwargs.setdefault('bins', 25)

            ret_sample = self.plot_sample(size=size, unit=unit, show=False, **kwargs)
            xmin, xmax = _plt.gca().get_xlim()
        else:
            ret_sample = None
            sample = self.sample(size=size, unit=unit)
            xmin = _np.min(sample)
            xmax = _np.max(sample)

        if plot_dist:
            x = _np.linspace(xmin, xmax, 1001)
            ret_dist = self.plot_dist(x, unit=unit, show=False, **{k:v for k,v in kwargs.items() if k not in ['bins']})
        else:
            ret_dist = None

        if show:
            _plt.xlabel(self._xlabel(unit))
            _plt.ylabel('density')
            _plt.show()

        return (ret_sample, ret_dist)


    def plot_sample(self, size=100000, unit=None, show=False, **kwargs):
        """
        Plot both a sampled histogram from the distribution.  Requires
        matplotlib to be installed.

        See also:

        * <BaseDistribution.plot>
        * <BaseDistribution.plot_dist>

        Arguments
        -----------
        * `size` (int, optional, default=100000): number of points to sample for
            the histogram.  See also <BaseDistribution.sample>.
        * `unit` (astropy.unit, optional, default=None): units to use along
            the x-axis.  Astropy must be installed.
        * `show` (bool, optional, default=True): whether to show the resulting
            matplotlib figure.
        * `**kwargs`: all keyword arguments will be passed on to plt.hist.

        Returns
        --------
        * the return from plt.hist

        Raises
        --------
        * ImportError: if matplotlib dependency is not met.
        """
        if not _has_mpl:
            raise ImportError("matplotlib required for plotting")

        ret = _plt.hist(self.sample(size, unit=unit), density=True, **kwargs)
        if show:
            _plt.xlabel(self._xlabel(unit))
            _plt.ylabel('density')
            _plt.show()

        return ret

    def plot_dist(self, x, unit=None, show=False, **kwargs):
        """
        Plot the analytic distribution function.  Requires matplotlib to be installed.

        See also:

        * <BaseDistribution.plot>
        * <BaseDistribution.plot_sample>

        Arguments
        -----------
        * `x` (np array): the numpy array at which to sample the value on the
            x-axis.
        * `unit` (astropy.unit, optional, default=None): units to use along
            the x-axis.  Astropy must be installed.
        * `show` (bool, optional, default=True): whether to show the resulting
            matplotlib figure.
        * `**kwargs`: all keyword arguments will be passed on to plt.plot

        Returns
        --------
        * the return from plot.plot

        Raises
        --------
        * ImportError: if matplotlib dependency is not met.
        """
        if not _has_mpl:
            raise ImportError("matplotlib required for plotting")

        # x is assumed to be in new units
        if self.dist_func is not None:
            ret = _plt.plot(x, self.distribution(x, unit=unit, as_quantity=False), **kwargs)
        else:
            ret = None

        if show:
            _plt.xlabel(self._xlabel(unit))
            _plt.ylabel('density')
            _plt.show()

        return ret

    def to_dict(self):
        """
        Return the dictionary representation of the distribution object.

        The resulting dictionary can be restored to the original object
        via <npdists.from_dict>.

        See also:

        * <BaseDistribution.to_json>
        * <BaseDistribution.to_file>

        Returns
        --------
        * dictionary
        """
        def _json_safe(v):
            if isinstance(v, _np.ndarray):
                return v.tolist()
            elif isinstance(v, list) or isinstance(v, tuple):
                return [_json_safe(li) for li in v]
            elif isinstance(v, BaseDistribution):
                return v.to_dict()
            elif hasattr(v, 'func_name'):
                if _has_dill:
                    return _dill.dumps(v)
                else:
                    raise ImportError("'dill' package required to export functions to dictionary")
            # elif is_unit(v)[0]:
            #     return v.to_string()
            else:
                return v
        d = {k:_json_safe(v) for k,v in self._descriptors.items()}
        d['npdists'] = self.__class__.__name__.lower()
        if self.unit is not None:
            d['unit'] = self.unit.to_string()
        if self.label is not None:
            d['label'] = self.label
        return d

    def to_json(self, **kwargs):
        """
        Return the json representation of the distribution object.

        The resulting dictionary can be restored to the original object
        via <npdists.from_json>.

        See also:

        * <BaseDistribution.to_dict>
        * <BaseDistribution.to_file>

        Arguments
        ---------
        * `**kwargs`: all keyword arguments will be sent to json.dumps

        Returns
        --------
        * string
        """
        try:
            return _json.dumps(self.to_dict(), ensure_ascii=True, **kwargs)
        except:
            if _has_dill:
                return _dill.dumps(self)
            else:
                raise ImportError("dumping file requires 'dill' package")

    def to_file(self, filename, **kwargs):
        """
        Save the json representation of the distribution object to a file.

        The resulting file can be restored to the original object
        via <npdists.from_file>.

        See also:

        * <BaseDistribution.to_dict>
        * <BaseDistribution.to_json>

        Arguments
        ----------
        * `filename` (string): path to the file to be created (will overwrite
            if already exists)
        * `**kwargs`: all keyword arguments will be sent to json.dumps

        Returns
        --------
        * string: the filename
        """
        f = open(filename, 'w')
        f.write(self.to_json(**kwargs))
        f.close()
        return filename


####################### DISTRIBUTION SUB-CLASSES ###############################

class Composite(BaseDistribution):
    """
    A composite distribution consisting of some math operator between one or two
    other Distribution objects.

    For example:

    ```py
    g = npdists.gaussian(10, 2)
    u = npdists.gaussian(1, 5)

    c = g * u
    print(c)
    ```

    or:

    ```py
    import numpy as np
    g = npdists.gaussian(0, 1)
    sing = np.sin(g)
    print(sing)
    ```

    Currently supported operators include:

    * multiplication, division, addition, subtraction
    * np.sin, np.cos, np.tan (but not math.sin, etc)

    When doing math between a distribution and a float or integer, that float/int
    will be treated as a <Delta> distribution.  In some simple cases, the
    applicable distribution type will be returned, but in other cases,
    a <Composite> distribution will be returned.  For example, multiplying
    a <Uniform> or <Gaussian> distribution by a float will return another
    <Uniform> or <Gaussian> distribution, respectively.

    """
    def __init__(self, math, dist1, dist2=None, unit=None, label=None):
        """
        Create a <Composite> distribution from two other distributions.

        Most likely, users will create Composite objects through math operators
        directly.  See examples on the <Composite> overview page.

        Arguments
        ----------
        * `math`: operator to be used between the two distributions.  Must
            be a valid and implemented operator.
        * `dist1` (<BaseDistribution>)
        * `dist2` (<BaseDistribution>, optional, default=None): the second
            distribution is required for most operators.  Some operators
            (e.g. sin, cos, tan) only take one distribution as an argument.
        * `unit` (astropy.units object, optional): the units of the provided values.
        * `label` (string, optional): a label for the distribution.  This is used
            for the x-label while plotting the distribution, as well as a shorthand
            notation when creating a <Composite> distribution.

        Returns
        ---------
        * a <Composite> object.
        """
        super(Composite, self).__init__(unit, label,
                                        None, None,
                                        self._sample_from_children, ('math', 'dist1', 'dist2'),
                                        ('math', math, is_math), ('dist1', dist1, is_distribution), ('dist2', dist2, is_distribution_or_none))

        if _has_astropy:
            if dist1.unit is not None:
                if dist2 is None:
                    # trig always gives unitless
                    self.unit = _units.dimensionless_unscaled
                elif dist2.unit is not None:
                    if math in ['__add__', '__sub__']:
                        if dist1.unit == dist2.unit:
                            self.unit = dist1.unit
                        else:
                            # TODO: if they're convertible, we should handle the scaling automatically
                            raise ValueError("units do not match")
                    elif hasattr(dist1.unit, math):
                        self.unit = getattr(dist1.unit, math)(dist2.unit)
                    else:
                        raise ValueError("cannot determine new unit from {}{}{}".format(dist1.unit, _math_symbols.get(math, math), dist2.unit))
                else:
                    self.unit = dist1.unit
            elif dist2 is not None and dist2.unit is not None:
                self.unit = dist2.unit
            else:
                self.unit = None


    def __repr__(self):
        return "<npdists.{} {} unit={}>".format(self.__class__.__name__.lower(), self.__str__(), self.unit if self.unit is not None else "None")

    def __str__(self):
        if self.dist2 is not None:
            return "{}{}{}".format(self.dist1.__str__(), _math_symbols.get(self.math, self.math), self.dist2.__str__())
        else:
            return "{}({})".format(_math_symbols.get(self.math, self.math), self.dist1.__str__())


    def _sample_from_children(self, math, dist1, dist2, size=None):
        if self.dist2 is not None:
            return getattr(dist1.sample(size=size), math)(dist2.sample(size=size))
        else:
            # if math in ['sin', 'cos', 'tan'] and _has_astropy and dist1.unit is not None:
            #     unit = _units.rad
            # else:
            #     unit = None
            return getattr(_np, math)(dist1.sample(size=size, as_quantity=_has_astropy and self.unit not in [None, _units.dimensionless_unscaled]))

    def __float__(self):
        return self.mean
        # return self.sample()

        # if self.dist2 is not None:
            # return getattr(dist1.mean, math)(dist2.mean)
        # else:
            # return getattr(_np, math)(dist1.mean)



    @property
    def mean(self):
        """
        Determine the mean sampled value.

        This is done under-the-hood by converting to a histogram via
        <Composite.to_histogram>, sampling 10000 times with 100 bins and
        calling <Histogram.mean>.
        """
        return self.to_histogram(N=10000, bins=100).mean

    @property
    def std(self):
        """
        Determine the standard deviations of the sampled values.

        This is done under-the-hood by converting to a histogram via
        <Composite.to_histogram>, sampling 10000 times with 100 bins and
        calling <Histogram.std>.
        """
        return self.to_histogram(N=10000, bins=100).std

    def to_histogram(self, N=1000, bins=10, range=None):
        """
        Convert the <Composite> distribution to a <Histogram> distribution.

        Under-the-hood, this calls <Composite.sample> with `size=N` and passes
        the resulting array as well as the requested `bins` and `range`
        to <Histogram.from_data>.

        Arguments
        -----------
        * `N` (int, optional, default=1000): number of samples to use for
            the histogram.
        * `bins` (int, optional, default=10): number of bins to use for the
            histogram.
        * `range` (tuple or None): range to use for the histogram.

        Returns
        --------
        * a <Histogram> object
        """
        return Histogram.from_data(self.sample(size=N), bins=bins, range=range, label=self.label, unit=self.unit)

    def to_gaussian(self, N=1000, bins=10, range=None):
        """
        Convert the <Composite> distribution to a <Gaussian> distribution via
        a <Histogram> distribution.

        Under-the-hood, this calls <Composite.to_histogram> with the requested
        values of `N`, `bins`, and `range` and then calls <Histogram.to_gaussian>.

        Arguments
        -----------
        * `N` (int, optional, default=1000): number of samples to use for
            the histogram.
        * `bins` (int, optional, default=10): number of bins to use for the
            histogram.
        * `range` (tuple or None): range to use for the histogram.

        Returns
        --------
        * a <Gaussian> object
        """
        return self.to_histogram(N=N, bins=bins, range=range, label=self.label, unit=self.unit).to_gaussian()

    def to_uniform(self, sigma=1.0, N=1000, bins=10, range=None):
        """
        Convert the <Composite> distribution to a <Uniform> distribution via
        a <Histogram> distribution.

        Under-the-hood, this calls <Composite.to_histogram> with the requested
        values of `N`, `bins`, and `range` and then calls <Histogram.to_uniform>
        with the requested value of `sigma`.

        Arguments
        -----------
        * `sigma` (float, optional, default=1.0): the number of standard deviations
            to adopt as the lower and upper bounds of the uniform distribution.
        * `N` (int, optional, default=1000): number of samples to use for
            the histogram.
        * `bins` (int, optional, default=10): number of bins to use for the
            histogram.
        * `range` (tuple or None): range to use for the histogram.

        Returns
        --------
        * a <Uniform> object
        """
        return self.to_histogram(N=N, bins=bins, range=range, label=self.label, unit=self.unit).to_uniform(sigma=sigma)

class Function(BaseDistribution):
    """
    A Function distribution allows for any python callable to be stored that
    utilizes distributions under-the-hood.  When calling <Function.sample>,
    any argument passed to the function that is a <BaseDistribution> object
    will be sampled prior to being passed to the callable function.

    In order to save or load these distributions, it is necessary to have
    the `dill` package installed.  Note that you should not load from untrusted
    sources, as any executable could be contained in the callable function.

    See:

    * <Function.to_dict>
    * <Function.to_json>
    * <Function.to_file>

    for documentation on loading and saving Function distributions.
    """
    def __init__(self, func, unit, label, *args):
        """
        Create a <Function> distribution from some callable function and
        any number of arguments, including distribution objects.

        This can also be created from a function at the top-level as:

        * <npdists.function>

        Arguments
        ----------
        * `func` (callable function): the callable function to be called to
            sample the distribution.
        * `unit` (astropy.units object or None): the units of the provided values.
        * `label` (string or None): a label for the distribution.  This is used
            for the x-label while plotting the distribution, as well as a shorthand
            notation when creating a <Composite> distribution.
        * `*args`: all additional positional arguments will be passed on to
            `func` when sampling.  These can be, but are not limited to,
            other distribution objects.

        Returns
        ---------
        * a <Function> object.
        """
        super(Function, self).__init__(unit, label,
                                       None, None,
                                       self._sample_from_function, ('func', 'args'),
                                       ('func', func, is_callable), ('args', args, is_iterable))

    def _sample_from_function(self, func, args, size=None):
        args = (a.sample(size=size) if isinstance(a, BaseDistribution) else a for a in args)
        return func(*args)

    def __float__(self):
        return self.mean
        # return self.sample()

    @property
    def mean(self):
        """
        Determine the mean sampled value.

        This is done under-the-hood by converting to a histogram via
        <Function.to_histogram>, sampling 10000 times with 100 bins and
        calling <Histogram.mean>.
        """
        return self.to_histogram(N=10000, bins=100).mean

    @property
    def std(self):
        """
        Determine the standard deviations of the sampled values.

        This is done under-the-hood by converting to a histogram via
        <Function.to_histogram>, sampling 10000 times with 100 bins and
        calling <Histogram.std>.
        """
        return self.to_histogram(N=10000, bins=100).std

    def to_histogram(self, N=1000, bins=10, range=None):
        """
        Convert the <Function> distribution to a <Histogram> distribution.

        Under-the-hood, this calls <Function.sample> with `size=N` and passes
        the resulting array as well as the requested `bins` and `range`
        to <Histogram.from_data>.

        Arguments
        -----------
        * `N` (int, optional, default=1000): number of samples to use for
            the histogram.
        * `bins` (int, optional, default=10): number of bins to use for the
            histogram.
        * `range` (tuple or None): range to use for the histogram.

        Returns
        --------
        * a <Histogram> object
        """
        return Histogram.from_data(self.sample(size=N), bins=bins, range=range, label=self.label, unit=self.unit)

    def to_gaussian(self, N=1000, bins=10, range=None):
        """
        Convert the <Function> distribution to a <Gaussian> distribution via
        a <Histogram> distribution.

        Under-the-hood, this calls <Function.to_histogram> with the requested
        values of `N`, `bins`, and `range` and then calls <Histogram.to_gaussian>.

        Arguments
        -----------
        * `N` (int, optional, default=1000): number of samples to use for
            the histogram.
        * `bins` (int, optional, default=10): number of bins to use for the
            histogram.
        * `range` (tuple or None): range to use for the histogram.

        Returns
        --------
        * a <Gaussian> object
        """
        return self.to_histogram(N=N, bins=bins, range=range, label=self.label, unit=self.unit).to_gaussian()

    def to_uniform(self, sigma=1.0, N=1000, bins=10, range=None):
        """
        Convert the <Function> distribution to a <Uniform> distribution via
        a <Histogram> distribution.

        Under-the-hood, this calls <Function.to_histogram> with the requested
        values of `N`, `bins`, and `range` and then calls <Histogram.to_uniform>
        with the requested value of `sigma` (which in turn is calling
        <Histogram.to_gaussian> first).

        Arguments
        -----------
        * `sigma` (float, optional, default=1.0): the number of standard deviations
            to adopt as the lower and upper bounds of the uniform distribution.
        * `N` (int, optional, default=1000): number of samples to use for
            the histogram.
        * `bins` (int, optional, default=10): number of bins to use for the
            histogram.
        * `range` (tuple or None): range to use for the histogram.

        Returns
        --------
        * a <Uniform> object
        """
        return self.to_histogram(N=N, bins=bins, range=range, label=self.label, unit=self.unit).to_uniform(sigma=sigma)


class Histogram(BaseDistribution):
    """
    A Histogram distribution stores a discrete PDF and allows sampling from
    that binned density distribution.

    To create a Histogram distribution from already binned data, see
    <npdists.histogram_from_bins> or <Histogram.__init__>.  To create a
    Histogram distribtuion from the data array itself, see
    <npdists.histogram_from_data> or <Histogram.from_data>.
    """
    def __init__(self, bins, density, unit=None, label=None):
        """
        Create a <Histogram> distribution from bins and density.

        This can also be created from a function at the top-level as:

        * <npdists.histogram_from_bins>

        See also:

        * <Histogram.from_data>
        * <npdists.histogram_from_data>

        Arguments
        --------------
        * `bins` (np.array object): the value of the bin-edges.  Must have one more
            entry than `density`.
        * `density` (np.array object): the value of the bin-densities.  Must have one
            less entry than `bins`.
        * `unit` (astropy.units object, optional): the units of the provided values.
        * `label` (string, optional): a label for the distribution.  This is used
            for the x-label while plotting the distribution, as well as a shorthand
            notation when creating a <Composite> distribution.

        Returns
        --------
        * a <Histogram> object
        """
        super(Histogram, self).__init__(unit, label,
                                        None, None,
                                        self._sample_from_hist, ('bins', 'density'),
                                        ('bins', bins, is_iterable), ('density', density, is_iterable))

    @classmethod
    def from_data(cls, data, bins=10, range=None, weights=None, label=None, unit=None):
        """
        Create a <Histogram> distribution from data.

        This can also be created from a function at the top-level as:

        * <npdists.histogram_from_data>

        See also:

        * <Histogram.__init__>
        * <npdists.histogram_from_bins>

        Arguments
        --------------
        * `data` (np.array object): 1D array of values.
        * `unit` (astropy.units object, optional): the units of the provided values.
        * `label` (string, optional): a label for the distribution.  This is used
            for the x-label while plotting the distribution, as well as a shorthand
            notation when creating a <Composite> distribution.

        Returns
        --------
        * a <Histogram> object
        """
        hist, bin_edges = _np.histogram(data, bins=bins, range=range, weights=weights, density=True)

        return cls(bin_edges, hist, label=label, unit=unit)

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

    def __float__(self):
        return self.mean
        # return self.sample()

    @property
    def mean(self):
        """
        Return the weighted mean value from the histogram.

        See also:

        * <Histogram.mean>

        Returns
        -------
        * float: the mean value
        """
        bin_midpoints = self.bins[:-1] + _np.diff(self.bins)/2
        mean = _np.average(bin_midpoints, weights=self.density)
        return mean

    @property
    def std(self):
        """
        Return the standard deviation about the mean from the histogram.

        See also:

        * <Histogram.mean>

        Returns
        ---------
        * float: the standard deviation
        """
        bin_midpoints = self.bins[:-1] + _np.diff(self.bins)/2
        mean = _np.average(bin_midpoints, weights=self.density)

        var = _np.average((bin_midpoints - mean)**2, weights=self.density)
        sigma = _np.sqrt(var)
        return sigma

    def to_gaussian(self):
        """
        Convert the <Histogram> distribution to a <Gaussian> distribution by
        adopting the values of <Histogram.mean> and <Histogram.std>.

        Returns
        --------
        * a <Gaussian> object
        """
        return Gaussian(self.mean, self.std, label=self.label, unit=self.unit)

    def to_uniform(self, sigma=1.0):
        """
        Convert the <Histogram> distribution to a <Uniform> distribution via
        a <Gaussian> distribution.

        Under-the-hood, this calls <Histogram.to_gaussian> and then calls
        <Gaussian.to_uniform> with the requested value of `sigma`.

        Arguments
        -----------
        * `sigma` (float, optional, default=1.0): the number of standard deviations
            to adopt as the lower and upper bounds of the uniform distribution.

        Returns
        --------
        * a <Uniform> object
        """
        return self.to_gaussian(label=self.label, unit=self.unit).to_uniform(sigma=sigma)

class Delta(BaseDistribution):
    """
    A Delta distribution will _always_ return the central values.  In most cases,
    there is no need to manually create a Delta distribution.  But when doing
    math on other <BaseDistribution> objects, <Delta> distributions are often
    created for clarity.

    Can be created from the top-level via the <npdists.delta> convenience function.
    """
    def __init__(self, value=0.0, unit=None, label=None):
        """
        Create a <Delta> distribution.

        This can also be created from a function at the top-level as:

        * <npdists.delta>

        Arguments
        --------------
        * `value` (float or int, default=0.0): the value at which the delta function is True.
        * `unit` (astropy.units object, optional): the units of the provided values.
        * `label` (string, optional): a label for the distribution.  This is used
            for the x-label while plotting the distribution, as well as a shorthand
            notation when creating a <Composite> distribution.

        Returns
        --------
        * a <Delta> object
        """
        super(Delta, self).__init__(unit, label,
                                    delta, ('value',),
                                    self._sample_from_delta, ('value',),
                                    ('value', value, is_float))

    def _sample_from_delta(self, value, size=None):
        if size is None:
            return value
        else:
            return _np.full(size, value)

    def __mul__(self, other):
        if (isinstance(other, float) or isinstance(other, int)):
            dist = self.copy()
            dist.value *= other
            return dist

        return super(Delta, self).__mul__(other)

    def __div__(self, other):
        return self.__mul__(1./other)

    def __add__(self, other):
        if (isinstance(other, float) or isinstance(other, int)):
            dist = self.copy()
            dist.value += other
            return dist

        return super(Delta, self).__add__(other)

    def __sub__(self, other):
        return self.__add__(-1*other)

    def __float__(self):
        return self.value

    @property
    def mean(self):
        """
        The mean value of a delta function is the value itself.

        Returns
        -------
        * float: the value
        """
        return self.value

    @property
    def std(self):
        """
        The standard deviation of a delta function is 0.0 by definition

        Returns
        --------
        * float: 0.0
        """
        return 0.0

    def to_uniform(self):
        """
        Convert the <Delta> distribution to a <Uniform> distribution in which
        both the lower and upper bounds are the same as the value.

        Returns
        ----------
        * a <Uniform> object
        """
        low = self.value
        high = self.value
        return Uniform(low, high, label=self.label, unit=self.unit)

    def to_gaussian(self):
        """
        Convert the <Delta> distribution to a <Gaussian> distribution in which
        the central value is adopted with a scale/sigma of 0.0.

        See also:

        * <Delta.mean>
        * <Delta.std>

        Returns
        --------
        * a <Gaussian> object
        """
        return Gaussian(self.value, 0.0, label=self.label, unit=self.unit)

    def to_histogram(self, N=1000, bins=10, range=None):
        """
        Convert the <Delta> distribution to a <Histogram> distribution.

        Under-the-hood, this calls <Delta.sample> with `size=N` and passes
        the resulting array as well as the requested `bins` and `range`
        to <Histogram.from_data>.

        Arguments
        -----------
        * `N` (int, optional, default=1000): number of samples to use for
            the histogram.
        * `bins` (int, optional, default=10): number of bins to use for the
            histogram.
        * `range` (tuple or None): range to use for the histogram.

        Returns
        --------
        * a <Histogram> object
        """
        return Histogram.from_data(self.sample(size=N), bins=bins, range=range, label=self.label, unit=self.unit)


class Gaussian(BaseDistribution):
    """
    A Gaussian (or Normal) distribution uses [numpy.random.normal](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.normal.html)
    to sample values from a gaussian function.

    Can be created from the top-level via the <npdists.gaussian> or
    <npdists.normal> convenience functions.
    """
    def __init__(self, loc=0.0, scale=1.0, unit=None, label=None):
        """
        Create a <Gaussian> distribution.

        This can also be created from a function at the top-level as:

        * <npdists.gaussian>

        Arguments
        --------------
        * `loc` (float or int, default=0.0): the central value of the gaussian distribution.
        * `scale` (float or int, default=1.0): the scale (sigma) of the gaussian distribution.
        * `unit` (astropy.units object, optional): the units of the provided values.
        * `label` (string, optional): a label for the distribution.  This is used
            for the x-label while plotting the distribution, as well as a shorthand
            notation when creating a <Composite> distribution.

        Returns
        --------
        * a <Gaussian> object
        """
        super(Gaussian, self).__init__(unit, label,
                                       gaussian, ('loc', 'scale'),
                                       _np.random.normal, ('loc', 'scale'),
                                       ('loc', loc, is_float), ('scale', scale, is_float))

    def __mul__(self, other):
        if (isinstance(other, float) or isinstance(other, int)):
            dist = self.copy()
            dist.loc *= other
            dist.scale *= other
            return dist

        return super(Gaussian, self).__mul__(other)

    def __div__(self, other):
        return self.__mul__(1./other)

    def __add__(self, other):
        if (isinstance(other, float) or isinstance(other, int)):
            dist = self.copy()
            dist.loc += other
            return dist

        return super(Gaussian, self).__add__(other)

    def __sub__(self, other):
        return self.__add__(-1*other)

    def __float__(self):
        return self.loc
        # return self.sample()

    @property
    def mean(self):
        """
        The mean of a <Gaussian> distribution is the value of `loc`, by definition.

        See also:

        * <Gaussian.std>

        Returns
        --------
        * float
        """
        return self.loc

    @property
    def std(self):
        """
        The standard deviation of a <Gaussian> distribution is the value of `scale`,
        by definition.

        See also:

        * <Gaussian.mean>

        Returns
        --------
        * float
        """
        return self.scale

    def to_uniform(self, sigma=1.0):
        """
        Convert the <Gaussian> distribution to a <Uniform> distribution by
        adopting the lower and upper bounds as a certain value of `sigma`
        for the <Gaussian> distribution.

        Arguments
        ----------
        * `sigma` (float, optional, default=1.0): number of standard deviations
            which should be adopted as the lower and upper bounds of the
            <Uniform> distribution.

        Returns
        ---------
        * a <Uniform> distribution
        """
        low = self.loc - self.scale * sigma
        high = self.loc + self.scale * sigma
        return Uniform(low, high, label=self.label, unit=self.unit)

    def to_histogram(self, N=1000, bins=10, range=None):
        """
        Convert the <Gaussian> distribution to a <Histogram> distribution.

        Under-the-hood, this calls <Gaussian.sample> with `size=N` and passes
        the resulting array as well as the requested `bins` and `range`
        to <Histogram.from_data>.

        Arguments
        -----------
        * `N` (int, optional, default=1000): number of samples to use for
            the histogram.
        * `bins` (int, optional, default=10): number of bins to use for the
            histogram.
        * `range` (tuple or None): range to use for the histogram.

        Returns
        --------
        * a <Histogram> object
        """
        return Histogram.from_data(self.sample(size=N), bins=bins, range=range, label=self.label, unit=self.unit)

class Uniform(BaseDistribution):
    """
    A Uniform (or Boxcar) distribution gives equal weights to all values within
    the defined range and uses [numpy.random.uniform](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.uniform.html)
    to sample values.

    Can be created from the top-level via the <npdists.uniform> or
    <npdists.boxcar> convenience functions.
    """
    def __init__(self, low=0.0, high=1.0, unit=None, label=None):
        """
        Create a <Uniform> distribution.

        This can also be created from a function at the top-level as:

        * <npdists.uniform>

        Arguments
        --------------
        * `low` (float or int, default=0.0): the lower limit of the uniform distribution.
        * `high` (float or int, default=1.0): the upper limits of the uniform distribution.
        * `unit` (astropy.units object, optional): the units of the provided values.
        * `label` (string, optional): a label for the distribution.  This is used
            for the x-label while plotting the distribution, as well as a shorthand
            notation when creating a <Composite> distribution.

        Returns
        --------
        * a <Uniform> object
        """
        super(Uniform, self).__init__(unit, label,
                                      uniform, ('low', 'high'),
                                      _np.random.uniform, ('low', 'high'),
                                      ('low', low, is_float), ('high', high, is_float))

    def __mul__(self, other):
        if (isinstance(other, float) or isinstance(other, int)):
            dist = self.copy()
            dist.low *= other
            dist.high *= other
            return dist

        return super(Uniform, self).__mul__(other)


    def __div__(self, other):
        return self.__mul__(1./other)

    def __add__(self, other):
        if (isinstance(other, float) or isinstance(other, int)):
            dist = self.copy()
            dist.low += other
            dist.high += other
            return dist
        # elif isinstance(other, Uniform):
            ## NOTE: this does not seem to be true as we should get a trapezoid if sampling separately
            # dist = self.copy()
            # dist.low += other.low
            # dist.high += other.high
            # return dist

        return super(Uniform, self).__add__(other)


    def __sub__(self, other):
        return self.__add__(-1*other)

    def __float__(self):
        return self.mean
        # return self.sample()

    @property
    def mean(self):
        """
        The mean value of a <Uniform> distribution is the average of the `low`
        and `high` values.

        Returns
        -------
        * float
        """
        return (self.low+self.high) / 2.0

    def to_gaussian(self, sigma=1.0):
        """
        Convert the <Uniform> distribution to a <Gaussian> distribution by
        adopting a certain `sigma`: number of standard deviations which should
        be adopted as the lower and upper bounds of the <Uniform> distribution.

        Arguments
        ----------
        * `sigma` (float, optional, default=1.0): number of standard deviations
            which should be adopted as the lower and upper bounds of the
            <Uniform> distribution.

        Returns
        ---------
        * a <Gaussian> distribution
        """
        loc = self.mean
        scale = (self.high - self.low) / (2.0 * sigma)
        return Gaussian(loc, scale, unit=self.unit, label=self.label)

    def to_histogram(self, N=1000, bins=None, range=None):
        """
        Convert the <Uniform> distribution to a <Histogram> distribution.

        Under-the-hood, this calls <Uniform.sample> with `size=N` and passes
        the resulting array as well as the requested `bins` and `range`
        to <Histogram.from_data>.

        Arguments
        -----------
        * `N` (int, optional, default=1000): number of samples to use for
            the histogram.
        * `bins` (int, optional, default=10): number of bins to use for the
            histogram.
        * `range` (tuple or None): range to use for the histogram.

        Returns
        --------
        * a <Histogram> object
        """
        return Histogram.from_data(self.sample(size=N), bins=bins, range=range, unit=self.unit, label=self.label)
