import numpy as _np
from scipy import stats as _stats
from scipy import interpolate as _interpolate
from scipy import integrate as _integrate
import json as _json
from collections import OrderedDict

from . import stats_custom as _stats_custom

try:
    import matplotlib.pyplot as _plt
except ImportError:
    _has_mpl = False
else:
    _has_mpl = True

try:
    import corner
except ImportError:
    _has_corner = False
else:
    _has_corner = True

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

_math_symbols = {'__mul__': '*', '__add__': '+', '__sub__': '-', '__div__': '/', '__and__': '&', '__or__': '|'}

_builtin_attrs = ['unit', 'label', 'wrap_at', 'dimension', 'dist_constructor_argnames', 'dist_constructor_args', 'dist_constructor_func', 'dist_constructor_object']

_physical_types_to_si = {'length': 'solRad',
                         'mass': 'solMass',
                         'temperature': 'solTeff',
                         'power': 'solLum',
                         'time': 'd',
                         'speed': 'solRad/d',
                         'angle': 'rad',
                         'angular speed': 'rad/d',
                         'dimensionless': ''}

_physical_types_to_solar = {'length': 'm',
                            'mass': 'kg',
                            'temperature': 'K',
                            'power': 'W',
                            'time': 's',
                            'speed': 'm/s',
                            'angle': 'rad',
                            'angular speed': 'rad/s',
                            'dimensionless': ''}

############################# HELPER FUNCTIONS #################################

def get_random_seed():
    """
    Return a random seed which can be passed to <BaseDistribution.sample>.

    This allows for using a consistent/reproducible but still random seed instead
    of manually passing some arbitrary integer (like 1234).

    Returns
    ------------
    * (array): array of 624 32-bit integers which can be used as a seed to
        np.random.seed or <BaseDistribution.sample>.
    """
    return _np.random.get_state()[1]


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
    valid_maths += ['__and__', '__or__']
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

def is_callable_or_none(value):
    if value is None:
        return True, value
    else:
        return is_callable(value)

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

def is_square_matrix(value):
    """must be a square 2D matrix"""
    return isinstance(value, _np.ndarray) and len(value.shape)==2 and value.shape[0]==value.shape[1], value


######################## DISTRIBUTION ABSTRACT CLASS ###########################

class BaseDistribution(object):
    """
    BaseDistribution is the parent class for all distributions and should
    not be used directly by the user.

    Any subclass distribution should override the following:

    * <BaseDistribution.__init__>
    """
    def __init__(self, unit, label, wrap_at,
                 dist_constructor_func, dist_constructor_argnames,
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

        self._dist_constructor_func = dist_constructor_func
        self._dist_constructor_argnames = dist_constructor_argnames

        self._dist_constructor_object_cache = None
        self._parents_with_cache = []

        self.label = label
        self.unit = unit
        self.wrap_at = wrap_at

        for item in args:
            if item[0] in _builtin_attrs:
                raise KeyError("{} is a protected attribute.".format(item[0]))

            valid, validated_value = item[2](item[1])
            if valid:
                self._descriptors[item[0]] = validated_value
            else:
                raise ValueError("{} {}, got {}".format(item[0], item[2].__doc__, item[1]))
            self._validators[item[0]] = item[2]

    def __getattr__(self, name):
        """
        for anything that isn't overriden here, expose the values in self._descriptors
        """
        if not name.startswith('_') and name in self._descriptors.keys():
            # then get the item in the dictionary
            return self._descriptors.get(name)
        else:
            try:
                return super(BaseDistribution, self).__getattr__(name)
            except:
                raise AttributeError("{} does not have attribute {}".format(self.__class__.__name__.lower(), name))

    def __setattr__(self, name, value):
        """
        """
        if not name.startswith('_') and name in self._descriptors.keys():
            valid, validated_value = self._validators[name](value)
            if valid:
                # clear the cache first since the underlying constructor object
                # will now need to be rebuilt.  This also bubbles up to anything
                # in self._parents_with_cache
                self._dist_constructor_object_clear_cache()
                # and then set the value in the dictionary
                self._descriptors[name] = validated_value
            else:
                raise ValueError("{} {}".format(name, validator.__doc__))
        else:
            try:
                return super(BaseDistribution, self).__setattr__(name, value)
            except:
                raise AttributeError("{} does not have attribute '{}'".format(self.__class__.__name__.lower(), name))

    ### REPRESENTATIONS

    def __repr__(self):
        descriptors = " ".join(["{}={}".format(k,v) for k,v in self._descriptors.items()])
        if self.unit is not None:
            descriptors += " unit={}".format(self.unit)
        if self.wrap_at is not None:
            descriptors += " wrap_at={}".format(self.wrap_at)
        if hasattr(self, 'dimension'):
            descriptors += " dimension={}".format(self.dimension)
        if self.label is not None:
            descriptors += " label={}".format(self.label)
        return "<npdists.{} {}>".format(self.__class__.__name__.lower(), descriptors)

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
        return self.median()

    ### COPYING

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

    ### IO

    @property
    def hash(self):
        """
        """
        # return hash(frozenset({k:v for k,v in self.to_dict().items() if k not in ['dimension']}))
        return hash(str({k:v for k,v in self.to_dict().items() if k not in ['dimension']}))

    def to_dict(self):
        """
        Return the dictionary representation of the distribution object.

        The resulting dictionary can be restored to the original object
        via <npdists.from_dict>.

        See also:

        * <<class>.to_json>
        * <<class>.to_file>

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
            d['unit'] = str(self.unit.to_string())
        if self.label is not None:
            d['label'] = self.label
        if self.wrap_at is not None:
            d['wrap_at'] = self.wrap_at
        if hasattr(self, 'dimension') and self.dimension is not None:
            d['dimension'] = self.dimension
        return d

    def to_json(self, **kwargs):
        """
        Return the json representation of the distribution object.

        The resulting dictionary can be restored to the original object
        via <npdists.from_json>.

        See also:

        * <<class>.to_dict>
        * <<class>.to_file>

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

        * <<class>.to_dict>
        * <<class>.to_json>

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

    ### MATH AND COMPARISON OPERATORS

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

    def __and__(self, other):
        if not isinstance(other, BaseDistribution):
            raise TypeError("cannot use & (and) logic between types {} and {}".format(self.__class__.__name__, type(other)))

        return Composite("__and__", self, other)

    def __or__(self, other):
        if not isinstance(other, BaseDistribution):
            raise TypeError("cannot use | (or) logic between types {} and {}".format(self.__class__.__name__, type(other)))

        return Composite("__or__", self, other)

    def sin(self):
        if self.unit is not None:
            dist = self.to(_units.rad)
        else:
            dist = self

        return Composite("sin", dist, label="sin({})".format(self.label) if self.label is not None else None)

    def cos(self):
        if self.unit is not None:
            dist = self.to(_units.rad)
        else:
            dist = self

        return Composite("cos", dist, label="cos({})".format(self.label) if self.label is not None else None)

    def tan(self):
        if self.unit is not None:
            dist = self.to(_units.rad)
        else:
            dist = self

        return Composite("tan", dist, label="tan({})".format(self.label) if self.label is not None else None)

    ### LABEL

    @property
    def label(self):
        """
        The label of the distribution object.  When not None, this is used for
        the x-label when plotting (see <<class>.plot>) and for the
        string representation for any math in a <Composite> or <Function>
        distribution.
        """
        return self._label

    @label.setter
    def label(self, label):
        if not (label is None or isinstance(label, str)):
            raise TypeError("label must be of type str")

        self._label = label

    ### UNITS AND UNIT CONVERSIONS

    @property
    def unit(self):
        """
        The units of the distribution.  Astropy is required in order to set
        and/or use distributions with units.

        See also:

        * <<class>.to>
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        if isinstance(unit, str):
            unit = _units.Unit(unit)

        if not (unit is None or isinstance(unit, _units.Unit) or isinstance(unit, _units.CompositeUnit) or isinstance(unit, _units.IrreducibleUnit)):
            raise TypeError("unit must be of type astropy.units.Unit, got {} (type: {})".format(unit, type(unit)))

        self._unit = unit

    def to(self, unit):
        """
        Convert to different units.  This creates a copy and returns the
        new distribution with the new units.  Astropy is required in order to
        set and/or use units.

        See also:

        * <<class>.unit>

        Arguments
        ------------
        * `unit` (astropy.unit object): unit to use in the new distribution.
            The current units (see <<class>.unit>) must be able to
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
        if new_dist.wrap_at is not None and new_dist.wrap_at is not False:
            new_dist.wrap_at *= factor
        new_dist *= factor
        return new_dist

    def to_si(self):
        """
        """
        physical_type = self.unit.physical_type

        if physical_type not in _physical_types_to_si.keys():
            raise NotImplementedError("cannot convert object with physical_type={} to SI units".format(physical_type))

        return self.to(_units.Unit(_physical_types_to_si.get(physical_type)))

    def to_solar(self):
        """
        """
        physical_type = self.unit.physical_type

        if physical_type not in _physical_types_to_solar.keys():
            raise NotImplementedError("cannot convert object with physical_type={} to solar units".format(physical_type))

        return self.to(_units.Unit(_physical_types_to_solar.get(physical_type)))

    ### CONVENIENCE METHODS FOR SAMPLING/WRAPPING/PLOTTING

    @property
    def wrap_at(self):
        """
        Value at which to wrap all sampled values.  If <<class>.unit> is not None,
        then the value of `wrap_at` is the same as the set units.

        If `False`: will not wrap
        If `None`: will wrap on range 0-2pi (0-360 deg) if <<class>.unit> are angular
            or 0-1 if <<class>.unit> are cycles.
        If float: will wrap on range 0-`wrap_at`.

        See also:

        * <<class>.get_wrap_at>
        * <<class>.wrap>

        Returns
        ---------
        * (float or None)
        """
        return self._wrap_at

    @wrap_at.setter
    def wrap_at(self, wrap_at):
        if wrap_at is None or wrap_at is False:
            self._wrap_at = wrap_at

        elif not (isinstance(wrap_at, float) or isinstance(wrap_at, int)):
            raise TypeError("wrap_at={} must be of type float, int, False, or None".format(wrap_at))

        else:
            self._wrap_at = wrap_at

    def get_wrap_at(self, wrap_at=None):
        """
        Get the computed value used for wrapping, given `wrap_at` as an optional
        override to the attribute <<class>.wrap_at>.

        See also:

        * <<class>.wrap_at>
        * <<class>.wrap>

        Arguments
        ------------
        * `wrap_at` (float or False or None, optional, default=None): override
            the value of <<class>.wrap_at>.

        Returns
        ----------
        * The computed wrapping value, accounting for <<class>.unit> if `wrap_at`
            is None.
        """

        if wrap_at is None:
            wrap_at = self.wrap_at

        if wrap_at is None:
            if _has_astropy and self.unit is not None:
                if self.unit.physical_type == 'angle':
                    if self.unit.to_string() == 'deg':
                        wrap_at = 360
                    elif self.unit.to_string() == 'cycle':
                        wrap_at = 1
                    elif self.unit.to_string() == 'rad':
                        wrap_at = 2 * _np.pi
                    else:
                        raise NotImplementedError("wrapping for angle unit {} not implemented.".format(self.unit.to_string()))
            else:
                wrap_at = False

        return wrap_at

    def wrap(self, value, wrap_at=None):
        """
        Wrap values via modulo:

        ```py
        value % wrap_at
        ```

        See also:

        * <<class>.wrap_at>
        * <<class>.get_wrap_at>

        Arguments
        ------------
        * `value` (float or array): values to wrap
        * `wrap_at` (float, optional, default=None): value to use for the upper-limit.
            If not provided or None, will use <<class>.wrap_at>.  If False,
            will return `value` unwrapped.

        Returns
        ----------
        * (float or array): same shape/type as input `value`.
        """
        wrap_at = self.get_wrap_at(wrap_at)

        if wrap_at is False or wrap_at is None:
            return value

        return value % wrap_at


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

    ### PROPERTIES/METHODS THAT EXPOSE UNDERLYING SCIPY.STATS FUNCTIONALITY

    @property
    def dist_constructor_func(self):
        """
        Return the callable function to access the underlying distribution
        constructor (often the scipy.stats random variable generator function).

        See also:

        * <<class>.dist_constructor_args>
        * <<class>.dist_constructor_object>

        Returns
        -------
        * callable function
        """
        return self._dist_constructor_func

    @property
    def dist_constructor_argnames(self):
        """
        """
        return self._dist_constructor_argnames

    @property
    def dist_constructor_args(self):
        """
        Return the arguments to pass to the the underlying distribution
        constructor (often the scipy.stats random variable generator function)

        See also:

        * <<class>.dist_constructor_func>
        * <<class>.dist_constructor_object>

        Returns
        -------
        * tuple
        """
        return [getattr(self, a) for a in self.dist_constructor_argnames]

    def _dist_constructor_object_clear_cache(self):
        """
        """
        # print("*** clearing cache {}".format(self))
        self._dist_constructor_object_cache = None
        for parent in self._parents_with_cache:
            parent._dist_constructor_object_clear_cache()

    @property
    def dist_constructor_object(self):
        """
        Return the instantiated underlying distribution constructor (often the
        scipy.stats random variable object).

        See also:

        * <<class>.dist_constructor_func>
        * <<class>.dist_constructor_args>

        Returns
        -------
        * object
        """
        if self._dist_constructor_object_cache is None:
            self._dist_constructor_object_cache = self.dist_constructor_func(*self.dist_constructor_args)

        return self._dist_constructor_object_cache

    def pdf(self, x, unit=None):
        """
        Expose the probability density function (pdf) at values of `x`.

        Arguments
        ----------
        * `x` (float or array): x-values at which to expose the pdf
        * `unit` (astropy.unit, optional, default=None): unit of the values
            in `x`.  If None or not provided, will assume they're provided in
            <<class>.unit>.

        Returns
        ---------
        * (float or array) pdf values of the same type/shape as `x`
        """
        # x is assumed to be in the new units
        if unit is not None:
            if self.unit is None:
                raise ValueError("can only convert units on Distributions with units set")
            # convert to original units
            x = (x * unit).to(self.unit).value

        try:
            return self.dist_constructor_object.pdf(x)
        except AttributeError:
            raise NotImplementedError("{} does not support pdf".format(self.__class__.__name__))

    def logpdf(self, x, unit=None):
        """
        Expose the log-probability density function (log of pdf) at values of `x`.

        Arguments
        ----------
        * `x` (float or array): x-values at which to expose the logpdf
        * `unit` (astropy.unit, optional, default=None): unit of the values
            in `x`.  If None or not provided, will assume they're provided in
            <<class>.unit>.

        Returns
        ---------
        * (float or array) logpdf values of the same type/shape as `x`
        """
        # x is assumed to be in the new units
        if unit is not None:
            if self.unit is None:
                raise ValueError("can only convert units on Distributions with units set")
            # convert to original units
            x = (x * unit).to(self.unit).value

        try:
            return self.dist_constructor_object.logpdf(x)
        except AttributeError:
            raise NotImplementedError("{} does not support logpdf".format(self.__class__.__name__))

    def cdf(self, x, unit=None):
        """
        Expose the cummulative density function (cdf) at values of `x`.

        Arguments
        ----------
        * `x` (float or array): x-values at which to expose the cdf
        * `unit` (astropy.unit, optional, default=None): unit of the values
            in `x`.  If None or not provided, will assume they're provided in
            <<class>.unit>.

        Returns
        ---------
        * (float or array) cdf values of the same type/shape as `x`
        """
        # x is assumed to be in the new units
        if unit is not None:
            if self.unit is None:
                raise ValueError("can only convert units on Distributions with units set")
            # convert to original units
            x = (x * unit).to(self.unit).value

        try:
            return self.dist_constructor_object.cdf(x)
        except AttributeError:
            raise NotImplementedError("{} does not support cdf".format(self.__class__.__name__))

    def logcdf(self, x, unit=None):
        """
        Expose the log-cummulative density function (log of cdf) at values of `x`.

        Arguments
        ----------
        * `x` (float or array): x-values at which to expose the logcdf
        * `unit` (astropy.unit, optional, default=None): unit of the values
            in `x`.  If None or not provided, will assume they're provided in
            <<class>.unit>.

        Returns
        ---------
        * (float or array) logcdf values of the same type/shape as `x`
        """
        # x is assumed to be in the new units
        if unit is not None:
            if self.unit is None:
                raise ValueError("can only convert units on Distributions with units set")
            # convert to original units
            x = (x * unit).to(self.unit).value

        try:
            return self.dist_constructor_object.logcdf(x)
        except AttributeError:
            raise NotImplementedError("{} does not support logcdf".format(self.__class__.__name__))

    def sample(self, *args, **kwargs):
        # must be implemented by any subclasses
        raise NotImplementedError("sample not implemented for {}".format(self.__class__.__name__))

    def plot(self, *args, **kwargs):
        # must be implemented by any subclasses
        raise NotImplementedError("plot not implemented for {}".format(self.__class__.__name__))


class BaseUnivariateDistribution(BaseDistribution):

    def ppf(self, q, unit=None, as_quantity=False, wrap_at=None):
        """
        Expose the percent point function (ppf; iverse of cdf - percentiles) at
        values of `q`.

        Arguments
        ----------
        * `q` (float or array): percentiles at which to expose the ppf
        * `unit` (astropy.unit, optional, default=None): unit of the exposed
            values.  If None or not provided, will assume they're provided in
            <<class>.unit>.
        * `as_quantity` (bool, optional, default=False): whether to return an
            astropy quantity object instead of just the value.  Astropy must
            be installed.
        * `wrap_at` (float, None, or False, optional, default=None): value to
            use for wrapping.  See <<class>.wrap>.  If not provided or None,
            will use the value from <<class>.wrap_at>.  Note: wrapping is
            computed before changing units, so `wrap_at` must be provided
            according to <<class>.unit> not `unit`.

        Returns
        ---------
        * (float or array) ppf values of the same type/shape as `x`
        """
        try:
            ppf = self.dist_constructor_object.ppf(q)
        except AttributeError:
            raise NotImplementedError("{} does not support ppf".format(self.__class__.__name__))

        return self._return_with_units(self.wrap(ppf, wrap_at=wrap_at), unit=unit, as_quantity=as_quantity)

    def median(self, unit=None, as_quantity=False, wrap_at=None):
        """
        Expose the median of the distribution.

        Arguments
        ----------
        * `unit` (astropy.unit, optional, default=None): unit of the values
            in `x` to expose.  If None or not provided, will assume they're in
            <<class>.unit>.
        * `as_quantity` (bool, optional, default=False): whether to return an
            astropy quantity object instead of just the value.  Astropy must
            be installed.
        * `wrap_at` (float, None, or False, optional, default=None): value to
            use for wrapping.  See <<class>.wrap>.  If not provided or None,
            will use the value from <<class>.wrap_at>.  Note: wrapping is
            computed before changing units, so `wrap_at` must be provided
            according to <<class>.unit> not `unit`.

        Returns
        ---------
        * (float) median of the distribution in units `unit`.
        """
        try:
            median = self.dist_constructor_object.median()
        except AttributeError:
            raise NotImplementedError("{} does not support median".format(self.__class__.__name__))

        return self._return_with_units(self.wrap(median, wrap_at=wrap_at), unit=unit, as_quantity=as_quantity)

    def mean(self, unit=None, as_quantity=False, wrap_at=None):
        """
        Expose the mean of the distribution.

        Arguments
        ----------
        * `unit` (astropy.unit, optional, default=None): unit of the values
            in `x` to expose.  If None or not provided, will assume they're in
            <<class>.unit>.
        * `as_quantity` (bool, optional, default=False): whether to return an
            astropy quantity object instead of just the value.  Astropy must
            be installed.
        * `wrap_at` (float, None, or False, optional, default=None): value to
            use for wrapping.  See <<class>.wrap>.  If not provided or None,
            will use the value from <<class>.wrap_at>.  Note: wrapping is
            computed before changing units, so `wrap_at` must be provided
            according to <<class>.unit> not `unit`.

        Returns
        ---------
        * (float) mean of the distribution in units `unit`.
        """
        try:
            mean = self.dist_constructor_object.mean()
        except AttributeError:
            raise NotImplementedError("{} does not support mean".format(self.__class__.__name__))

        return self._return_with_units(self.wrap(mean, wrap_at=wrap_at), unit=unit, as_quantity=as_quantity)

    def var(self, unit=None, as_quantity=False, wrap_at=None):
        """
        Expose the variance of the distribution.

        Arguments
        ----------
        * `unit` (astropy.unit, optional, default=None): unit of the values
            in `x` to expose.  If None or not provided, will assume they're in
            <<class>.unit>.
        * `as_quantity` (bool, optional, default=False): whether to return an
            astropy quantity object instead of just the value.  Astropy must
            be installed.
        * `wrap_at` (float, None, or False, optional, default=None): value to
            use for wrapping.  See <<class>.wrap>.  If not provided or None,
            will use the value from <<class>.wrap_at>.  Note: wrapping is
            computed before changing units, so `wrap_at` must be provided
            according to <<class>.unit> not `unit`.

        Returns
        ---------
        * (float) variance of the distribution in units `unit`.
        """
        try:
            var = self.dist_constructor_object.var()
        except AttributeError:
            raise NotImplementedError("{} does not support var".format(self.__class__.__name__))

        return self._return_with_units(self.wrap(var, wrap_at=wrap_at), unit=unit, as_quantity=as_quantity)

    def std(self, unit=None, as_quantity=False, wrap_at=None):
        """
        Expose the standard deviation of the distribution.

        Arguments
        ----------
        * `unit` (astropy.unit, optional, default=None): unit of the values
            in `x` to expose.  If None or not provided, will assume they're in
            <<class>.unit>.
        * `as_quantity` (bool, optional, default=False): whether to return an
            astropy quantity object instead of just the value.  Astropy must
            be installed.
        * `wrap_at` (float, None, or False, optional, default=None): value to
            use for wrapping.  See <<class>.wrap>.  If not provided or None,
            will use the value from <<class>.wrap_at>.  Note: wrapping is
            computed before changing units, so `wrap_at` must be provided
            according to <<class>.unit> not `unit`.

        Returns
        ---------
        * (float) standard deviation of the distribution in units `unit`.
        """
        try:
            std = self.dist_constructor_object.std()
        except AttributeError:
            raise NotImplementedError("{} does not support std".format(self.__class__.__name__))

        return self._return_with_units(self.wrap(std, wrap_at=wrap_at), unit=unit, as_quantity=as_quantity)

    def interval(self, alpha, unit=None, as_quantity=False, wrap_at=None):
        """
        Expose the range that contains alpha percent of the distribution.

        Arguments
        ----------
        * `alpha` (float):
        * `unit` (astropy.unit, optional, default=None): unit of the values
            in `x` to expose.  If None or not provided, will assume they're in
            <<class>.unit>.
        * `as_quantity` (bool, optional, default=False): whether to return an
            astropy quantity object instead of just the value.  Astropy must
            be installed.
        * `wrap_at` (float, None, or False, optional, default=None): value to
            use for wrapping.  See <<class>.wrap>.  If not provided or None,
            will use the value from <<class>.wrap_at>.  Note: wrapping is
            computed before changing units, so `wrap_at` must be provided
            according to <<class>.unit> not `unit`.

        Returns
        ---------
        * (array) endpoints in units `unit`.
        """
        try:
            interval = self.dist_constructor_object.interval(alpha)
        except AttributeError:
            raise NotImplementedError("{} does not support interval".format(self.__class__.__name__))

        # we call np.asarray so that wrapping and units works on an array object instead of a tuple
        return self._return_with_units(self.wrap(_np.asarray(interval), wrap_at=wrap_at), unit=unit, as_quantity=as_quantity)

    ### remaining (unimplemented) scipy.stats methods
        # rvs(loc=0, scale=1, size=1, random_state=None)
        # Random variates.
        #
        # sf(x, loc=0, scale=1)
        # Survival function (also defined as 1 - cdf, but sf is sometimes more accurate).
        #
        # logsf(x, loc=0, scale=1)
        # Log of the survival function.
        #
        # isf(q, loc=0, scale=1)
        # Inverse survival function (inverse of sf).
        #
        # moment(n, loc=0, scale=1)
        # Non-central moment of order n
        #
        # stats(loc=0, scale=1, moments=’mv’)
        # Mean(‘m’), variance(‘v’), skew(‘s’), and/or kurtosis(‘k’).
        #
        # entropy(loc=0, scale=1)
        # (Differential) entropy of the RV.
        #
        # fit(data, loc=0, scale=1)
        # Parameter estimates for generic data.
        #
        # expect(func, args=(), loc=0, scale=1, lb=None, ub=None, conditional=False, **kwds)
        # Expected value of a function (of one argument) with respect to the distribution.
        #

    ### SAMPLING

    def sample(self, size=None, unit=None, as_quantity=False, wrap_at=None, seed=None):
        """
        Sample from the distribution.

        See also:

        * <<class>.ppf>

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
        * `wrap_at` (float, None, or False, optional, default=None): value to
            use for wrapping.  See <<class>.wrap>.  If not provided or None,
            will use the value from <<class>.wrap_at>.  Note: wrapping is
            computed before changing units, so `wrap_at` must be provided
            according to <<class>.unit> not `unit`.
        * `seed` (int, optional): seed to pass to np.random.seed
            prior to sampling.

        Returns
        ---------
        * float or array: float if `size=None`, otherwise a numpy array with
            shape defined by `size`.
        """
        if isinstance(seed, dict):
            seed = seed.get(self.hash, None)

        # print("{} seed: {}".format(self, seed))

        if seed is not None:
            _np.random.seed(seed)


        return self._return_with_units(self.wrap(self.dist_constructor_object.rvs(size=size), wrap_at=wrap_at), unit=unit, as_quantity=as_quantity)

    ### PLOTTING

    def _xlabel(self, unit=None, label=None):
        label = label if label is not None else self.label
        l = 'value' if label is None else label
        if _has_astropy and self.unit is not None and self.unit not in [_units.dimensionless_unscaled]:
            l += ' ({})'.format(unit if unit is not None else self.unit)

        return l


    def plot(self, size=1e5, unit=None,
             wrap_at=None, seed=None,
             plot_sample=True, plot_sample_kwargs={'color': 'gray'},
             plot_pdf=True, plot_pdf_kwargs={'color': 'red'},
             plot_cdf=False, plot_cdf_kwargs={'color': 'green'},
             plot_gaussian=False, plot_gaussian_kwargs={'color': 'blue'},
             label=None, show=False, **kwargs):
        """
        Plot both the analytic distribution function as well as a sampled
        histogram from the distribution.  Requires matplotlib to be installed.

        See also:

        * <<class>.plot_sample>
        * <<class>.plot_pdf>
        * <<class>.plot_gaussian>

        Arguments
        -----------
        * `size` (int, optional, default=1e5): number of points to sample for
            the histogram.  See also <<class>.sample>.
        * `unit` (astropy.unit, optional, default=None): units to use along
            the x-axis.  Astropy must be installed.
        * `wrap_at` (float, None, or False, optional, default=None): value to
            use for wrapping.  See <<class>.wrap>.  If not provided or None,
            will use the value from <<class>.wrap_at>.  Note: wrapping is
            computed before changing units, so `wrap_at` must be provided
            according to <<class>.unit> not `unit`.
        * `seed` (int, optional): seed to use when sampling.  See also
            <<class>.sample>.
        * `plot_sample` (bool, optional, default=True): whether to plot the
            histogram from sampling.  See also <<class>.plot_sample>.
        * `plot_sample_kwargs` (dict, optional, default={'color': 'gray'}):
            keyword arguments to send to <<class>.plot_sample>.
        * `plot_pdf` (bool, optional, default=True): whether to plot the
            analytic form of the underlying distribution, if applicable.
            See also <<class>.plot_pdf>.
        * `plot_pdf_kwargs` (dict, optional, default={'color': 'red'}):
            keyword arguments to send to <<class>.plot_pdf>.
        * `plot_cdf` (bool, optional, default=True): whether to plot the
            analytic form of the cdf, if applicable.
            See also <<class>.plot_cdf>.
        * `plot_cdf_kwargs` (dict, optional, default={'color': 'green'}):
            keyword arguments to send to <<class>.plot_cdf>.
        * `plot_gaussian` (bool, optional, default=False): whether to plot
            a guassian distribution fit to the sample.  Only supported for
            distributions that have <<class>.to_gaussian> methods.
        * `plot_gaussian_kwargs` (dict, optional, default={'color': 'blue'}):
            keyword arguments to send to <<class>.plot_gaussian>.
        * `label` (string, optional, default=None): override the label on the
            x-axis.  If not provided or None, will use <<class>.label>.  Will
            only be used if `show=True`.
        * `show` (bool, optional, default=True): whether to show the resulting
            matplotlib figure.
        * `**kwargs`: all keyword arguments (except for `bins`) will be passed
            on to <<class>.plot_pdf> and <<class>.plot_gaussian> and all
            keyword arguments will be passed on to <<class>.plot_sample>.
            Keyword arguments defined in `plot_sample_kwargs`,
            `plot_pdf_kwargs`, and `plot_gaussian_kwargs`
            will override the values sent in `kwargs`.

        Returns
        --------
        * tuple: the return values from <<class>.plot_sample> (or None if
            `plot_sample=False`), <<class>.plot_pdf> (or None if `plot_pdf=False`),
            <<class>.plot_cdf> (or None if `plot_cdf=False`),
            and <Gaussian.plot_pdf> (or None if `plot_gaussian=False`).

        Raises
        --------
        * ImportError: if matplotlib dependency is not met.
        """
        if not _has_mpl:
            raise ImportError("matplotlib required for plotting")

        ret = []

        if plot_sample:
            # we have to make a copy here, otherwise setdefault will change the
            # defaults in the function declaration for successive calls
            plot_sample_kwargs = plot_sample_kwargs.copy()
            for k,v in kwargs.items():
                plot_sample_kwargs.setdefault(k,v)
            ret_sample = self.plot_sample(size=int(size), unit=unit, wrap_at=wrap_at, seed=seed, show=False, **plot_sample_kwargs)
        else:
            ret_sample = None

        if plot_gaussian or plot_pdf or plot_cdf:
            # we need to know the original x-range, before wrapping
            # sample = self.sample(size=size, unit=unit, wrap_at=False)
            # xmin = _np.min(sample)
            # xmax = _np.max(sample)
            xmin, xmax = self.interval(0.999, wrap_at=False, unit=unit)
            x = _np.linspace(xmin-(xmax-xmin)*0.1, xmax+(xmax-xmin)*0.1, 1000)

        if plot_gaussian:
            if not hasattr(self, 'to_gaussian'):
                raise NotImplementedError("{} cannot plot with `plot_gaussian=True`".format(self.__class__.__name__))
            # we have to make a copy here, otherwise setdefault will change the
            # defaults in the function declaration for successive calls
            plot_gaussian_kwargs = plot_gaussian_kwargs.copy()
            for k,v in kwargs.items():
                if k in ['bins']:
                    continue
                plot_gaussian_kwargs.setdefault(k,v)
            ret_gauss = self.plot_gaussian(x, unit=unit, wrap_at=wrap_at, show=False, **plot_gaussian_kwargs)

        else:
            ret_gauss = None

        if plot_pdf:
            # we have to make a copy here, otherwise setdefault will change the
            # defaults in the function declaration for successive calls
            plot_pdf_kwargs = plot_pdf_kwargs.copy()
            for k,v in kwargs.items():
                if k in ['bins']:
                    continue
                plot_pdf_kwargs.setdefault(k,v)
            ret_pdf = self.plot_pdf(x, unit=unit, wrap_at=wrap_at, show=False, **plot_pdf_kwargs)
        else:
            ret_pdf = None

        if plot_cdf:
            # we have to make a copy here, otherwise setdefault will change the
            # defaults in the function declaration for successive calls
            plot_cdf_kwargs = plot_cdf_kwargs.copy()
            for k,v in kwargs.items():
                if k in ['bins']:
                    continue
                plot_cdf_kwargs.setdefault(k,v)
            ret_cdf = self.plot_cdf(x, unit=unit, wrap_at=wrap_at, show=False, **plot_cdf_kwargs)
        else:
            ret_cdf = None

        if show:
            _plt.xlabel(self._xlabel(unit, label=label))
            _plt.ylabel('density')
            _plt.show()

        return (ret_sample, ret_pdf, ret_cdf, ret_gauss)


    def plot_sample(self, size=100000, unit=None,
                    wrap_at=None, seed=None,
                    label=None, show=False, **kwargs):
        """
        Plot both a sampled histogram from the distribution.  Requires
        matplotlib to be installed.

        See also:

        * <<class>.plot>
        * <<class>.plot_pdf>
        * <<class>.plot_gaussian>

        Arguments
        -----------
        * `size` (int, optional, default=100000): number of points to sample for
            the histogram.  See also <<class>.sample>.
        * `unit` (astropy.unit, optional, default=None): units to use along
            the x-axis.  Astropy must be installed.
        * `wrap_at` (float, None, or False, optional, default=None): value to
            use for wrapping.  See <<class>.wrap>.  If not provided or None,
            will use the value from <<class>.wrap_at>.  Note: wrapping is
            computed before changing units, so `wrap_at` must be provided
            according to <<class>.unit> not `unit`.
        * `seed` (int, optional): seed to use when sampling.  See also
            <<class>.sample>.
        * `label` (string, optional, default=None): override the label on the
            x-axis.  If not provided or None, will use <<class>.label>.  Will
            only be used if `show=True`.
        * `show` (bool, optional, default=True): whether to show the resulting
            matplotlib figure.
        * `**kwargs`: all keyword arguments will be passed on to plt.hist.  If
            not provided, `bins` will default to the stored bins for <Histogram>
            distributions, otherwise will default to 25.

        Returns
        --------
        * the return from plt.hist

        Raises
        --------
        * ImportError: if matplotlib dependency is not met.
        """
        if not _has_mpl:
            raise ImportError("matplotlib required for plotting")

        if hasattr(self, 'bins'):
            # let's default to the stored bins (probably only the case for
            # histogram distributions)
            if wrap_at or self.wrap_at:
                kwargs.setdefault('bins', len(self.bins))
            else:
                kwargs.setdefault('bins', self.bins)
        else:
            kwargs.setdefault('bins', 25)

        # TODO: wrapping can sometimes cause annoying things with bins due to a large datagap.
        # Perhaps we should bin and then wrap?  Or bin before wrapping and get a guess at the
        # appropriate bins
        samples = self.sample(size, unit=unit, wrap_at=wrap_at, seed=seed)
        try:
            ret = _plt.hist(samples, density=True, **kwargs)
        except AttributeError:
            # TODO: determine which version of matplotlib
            # TODO: this still doesn't handle the same
            ret = _plt.hist(samples, normed=True, **kwargs)

        if show:
            _plt.xlabel(self._xlabel(unit, label=label))
            _plt.ylabel('density')
            _plt.show()

        return ret

    def plot_pdf(self, x=None, unit=None, wrap_at=None,
                  label=None, show=False, **kwargs):
        """
        Plot the pdf function.  Requires matplotlib to be installed.

        See also:

        * <<class>.plot>
        * <<class>.plot_sample>
        * <<class>.plot_gaussian>

        Arguments
        -----------
        * `x` (array, optional, default=None): the numpy array at which to
            sample the value on the x-axis.  If `unit` is not None, the value
            of `x` are assumed to be in the original units <<class>.unit>,
            not `unit`.  If not provided or None, `x` will be based to cover
            the 99.9% of all distributions (see <<class>.interval>) with 1000
            points and 10% padding.
        * `unit` (astropy.unit, optional, default=None): units to use along
            the x-axis.  Astropy must be installed.
        * `wrap_at` (float, None, or False, optional, default=None): value to
            use for wrapping.  See <<class>.wrap>.  If not provided or None,
            will use the value from <<class>.wrap_at>.  Note: wrapping is
            computed before changing units, so `wrap_at` must be provided
            according to <<class>.unit> not `unit`.
        * `label` (string, optional, default=None): override the label on the
            x-axis.  If not provided or None, will use <<class>.label>.  Will
            only be used if `show=True`.
        * `show` (bool, optional, default=True): whether to show the resulting
            matplotlib figure.
        * `**kwargs`: all keyword arguments will be passed on to plt.plot.  Note:
            if wrapping is enabled, either via `wrap_at` or <<class>.wrap_at>,
            the resulting line will break when wrapping, resulting in using multiple
            colors.  Sending `color` as a keyword argument will prevent this
            matplotlib behavior.  Calling this through <<class>.plot> with
            `plot_gaussian=True` defaults to sending `color='blue'` through
            the `plot_gaussian_kwargs` argument.

        Returns
        --------
        * the return from plt.plot

        Raises
        --------
        * ImportError: if matplotlib dependency is not met.
        """
        if not _has_mpl:
            raise ImportError("matplotlib required for plotting")

        if x is None:
            # TODO: test how this plays with units
            xmin, xmax = self.interval(0.999, wrap_at=False, unit=unit)
            x = _np.linspace(xmin-(xmax-xmin)*0.1, xmax+(xmax-xmin)*0.1, 1000)

        # x is assumed to be in new units
        if hasattr(self, 'pdf'):
            y = self.pdf(x, unit=unit)
            x = self.wrap(x, wrap_at=wrap_at)

            # if unit is not None:
                # print "*** converting from {} to {}".format(self.unit, unit)
                # print "*** before convert", x.min(), x.max()
                # x = (x*self.unit).to(unit).value
                # print "*** after convert", x.min(), x.max()

            # handle wrapping by making multiple calls to plot whenever the sign
            # changes direction
            split_inds = _np.where(x[1:]-x[:-1] < 0)[0]
            xs, ys = _np.split(x, split_inds+1), _np.split(y, split_inds+1)
            for x,y in zip(xs, ys):
                ret = _plt.plot(x, y, **kwargs)
        else:
            return None


        if show:
            _plt.xlabel(self._xlabel(unit, label=label))
            _plt.ylabel('density')
            _plt.show()

        return ret

    def plot_cdf(self, x=None, unit=None, wrap_at=None,
                  label=None, show=False, **kwargs):
        """
        Plot the pdf function.  Requires matplotlib to be installed.

        See also:

        * <<class>.plot>
        * <<class>.plot_sample>
        * <<class>.plot_gaussian>

        Arguments
        -----------
        * `x` (array, optional, default=None): the numpy array at which to
            sample the value on the x-axis.  If `unit` is not None, the value
            of `x` are assumed to be in the original units <<class>.unit>,
            not `unit`.  If not provided or None, `x` will be based to cover
            the 99.9% of all distributions (see <<class>.interval>) with 1000
            points and 10% padding.
        * `unit` (astropy.unit, optional, default=None): units to use along
            the x-axis.  Astropy must be installed.
        * `wrap_at` (float, None, or False, optional, default=None): value to
            use for wrapping.  See <<class>.wrap>.  If not provided or None,
            will use the value from <<class>.wrap_at>.  Note: wrapping is
            computed before changing units, so `wrap_at` must be provided
            according to <<class>.unit> not `unit`.
        * `label` (string, optional, default=None): override the label on the
            x-axis.  If not provided or None, will use <<class>.label>.  Will
            only be used if `show=True`.
        * `show` (bool, optional, default=True): whether to show the resulting
            matplotlib figure.
        * `**kwargs`: all keyword arguments will be passed on to plt.plot.  Note:
            if wrapping is enabled, either via `wrap_at` or <<class>.wrap_at>,
            the resulting line will break when wrapping, resulting in using multiple
            colors.  Sending `color` as a keyword argument will prevent this
            matplotlib behavior.  Calling this through <<class>.plot> with
            `plot_gaussian=True` defaults to sending `color='blue'` through
            the `plot_gaussian_kwargs` argument.

        Returns
        --------
        * the return from plt.plot

        Raises
        --------
        * ImportError: if matplotlib dependency is not met.
        """
        if not _has_mpl:
            raise ImportError("matplotlib required for plotting")

        if x is None:
            # TODO: test how this plays with units
            xmin, xmax = self.interval(0.999, wrap_at=False, unit=unit)
            x = _np.linspace(xmin-(xmax-xmin)*0.1, xmax+(xmax-xmin)*0.1, 1000)

        # x is assumed to be in new units
        if hasattr(self, 'cdf'):
            y = self.cdf(x, unit=unit)
            x = self.wrap(x, wrap_at=wrap_at)

            # if unit is not None:
                # print "*** converting from {} to {}".format(self.unit, unit)
                # print "*** before convert", x.min(), x.max()
                # x = (x*self.unit).to(unit).value
                # print "*** after convert", x.min(), x.max()

            # handle wrapping by making multiple calls to plot whenever the sign
            # changes direction
            split_inds = _np.where(x[1:]-x[:-1] < 0)[0]
            xs, ys = _np.split(x, split_inds+1), _np.split(y, split_inds+1)
            for x,y in zip(xs, ys):
                ret = _plt.plot(x, y, **kwargs)
        else:
            return None


        if show:
            _plt.xlabel(self._xlabel(unit, label=label))
            _plt.ylabel('cummulative density')
            _plt.show()

        return ret

    def plot_gaussian(self, x=None, unit=None, wrap_at=None,
                      label=None, show=False, **kwargs):
        """
        Plot the gaussian distribution that would result from calling
        <<class>.to_gaussian> with the same arguments.

        Note that for distributions in which <<class>.to_gaussian> calls
        <<class>.to_histogram> under-the-hood, this could result in slightly
        different distributions for each call.

        See also:

        * <<class>.plot>
        * <<class>.plot_sample>
        * <<class>.plot_pdf>

        Arguments
        -----------
        * `x` (array, optional, default=None): the numpy array at which to
            sample the value on the x-axis.  If `unit` is not None, the value
            of `x` are assumed to be in the original units <<class>.unit>,
            not `unit`.  If not provided or None, `x` will be based to cover
            the 99.9% of all distributions (see <<class>.interval>) with 1000
            points and 10% padding.
        * `unit` (astropy.unit, optional, default=None): units to use along
            the x-axis.  Astropy must be installed.
        * `wrap_at` (float, None, or False, optional, default=None): value to
            use for wrapping.  See <<class>.wrap>.  If not provided or None,
            will use the value from <<class>.wrap_at>.  Note: wrapping is
            computed before changing units, so `wrap_at` must be provided
            according to <<class>.unit> not `unit`.
        * `label` (string, optional, default=None): override the label on the
            x-axis.  If not provided or None, will use <<class>.label>.  Will
            only be used if `show=True`.
        * `show` (bool, optional, default=True): whether to show the resulting
            matplotlib figure.
        * `**kwargs`: keyword arguments for `sigma`, `N`, `bins`, `range` will
            be passed on to <<class>.to_gaussian> (must be accepted by the
            given distribution type).  All other keyword arguments will be passed
            on to <Gaussian.plot_pdf> on the resulting distribution.

        Returns
        --------
        * the return from plt.plot

        Raises
        --------
        * ImportError: if matplotlib dependency is not met.
        """
        if not _has_mpl:
            raise ImportError("matplotlib required for plotting")

        if x is None:
            # TODO: test how this plays with units
            xmin, xmax = self.interval(0.999, wrap_at=False, unit=unit)
            x = _np.linspace(xmin-(xmax-xmin)*0.1, xmax+(xmax-xmin)*0.1, 1000)

        to_gauss_keys = ['sigma', 'N', 'bins', 'range']
        g = self.to_gaussian(**{k:v for k,v in kwargs.items() if k in to_gauss_keys})

        if unit is not None:
            g = g.to(unit)
            if wrap_at is not None and wrap_at is not False:
                wrap_at = (wrap_at * self.unit).to(unit).value

        # TODO: this time wrap_at is assumed to be in the plotted units, not the original... do we need to convert?
        ret = g.plot_pdf(x, wrap_at=wrap_at, **{k:v for k,v in kwargs.items() if k not in to_gauss_keys})

        if show:
            _plt.xlabel(self._xlabel(unit, label=label))
            _plt.ylabel('density')
            _plt.show()
        return ret

    ### CONVERSION TO OTHER DISTRIBUTION TYPES

    def to_histogram(self, N=100000, bins=10, range=None, wrap_at=None):
        """
        Convert the <<class>> distribution to a <Histogram> distribution.

        Under-the-hood, this calls <<class>.sample> with `size=N` and `wrap_at=False`
        and passes the resulting array as well as the requested `bins` and `range`
        to <Histogram.from_data>.

        Arguments
        -----------
        * `N` (int, optional, default=100000): number of samples to use for
            the histogram.
        * `bins` (int, optional, default=10): number of bins to use for the
            histogram.
        * `range` (tuple or None): range to use for the histogram.
        * `wrap_at` (float or None, optional, default=None): value to set for
            `wrap_at` of the returned <Histogram>.  If None or not provided,
            will default to <<class>.wrap_at>.

        Returns
        --------
        * a <Histogram> object
        """
        return Histogram.from_data(self.sample(size=N, wrap_at=False),
                                   bins=bins, range=range,
                                   unit=self.unit, label=self.label, wrap_at=wrap_at if wrap_at is not None else self.wrap_at)


class BaseMultivariateDistribution(BaseDistribution):
    def __init__(self, *args, **kwargs):
        # TODO: handle units, labels, wrap_ats
        dimension = kwargs.pop('dimension', None)

        super(BaseMultivariateDistribution, self).__init__(*args, **kwargs)

        self.dimension = dimension

    @property
    def label(self):
        """
        """
        if self.dimension is None:
            return self._label
        else:
            return self._label[self.dimension]

    @label.setter
    def label(self, label):
        if not (label is None or isinstance(label, list)):
            raise TypeError("label must be of type list")

        self._label = label

    @property
    def dimensions(self):
        """
        """
        return range(self.ndimensions)

    def get_dimension_by_label(self, dimension):
        """
        """
        if isinstance(dimension, str) and dimension in self.label:
            dimension = self.label.index(dimension)
        return dimension

    @property
    def dimension(self):
        """
        See also:

        * <<class>.sample>

        Returns
        ---------
        * (int or None): dimension of the multivariate distribution to sample.
            If None, will return an array of values for all available parameters.
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        dimension = self.get_dimension_by_label(dimension)

        if not (isinstance(dimension, int) or dimension is None):
            raise TypeError("dimension must be of type int")

        # TODO: check to make sure within valid range?  Then we'll probably have to set after super

        self._dimension = dimension

    def take_dimension(self, dimension=None):
        """

        Arguments
        ----------
        * `dimension` (int, list of ints, or None, optional, default=None)
        """
        if dimension is None:
            dimension = self.dimensions
        if not isinstance(dimension, str) and hasattr(dimension, '__iter__'):
            return [self.take_dimension(d) for d in dimension]

        d = self.copy()
        d.dimension = dimension
        return d

    def pdf(self, x):
        if hasattr(x, '__iter__'):
            raise TypeError('x must an array with length ndimensions')

        return super(BaseMultivariateDistribution, self).pdf(x)

    def logpdf(self, x):
        if hasattr(x, '__iter__'):
            raise TypeError('x must an array with length ndimensions')

        return super(BaseMultivariateDistribution, self).logpdf(x)

    def cdf(self, x):
        if hasattr(x, '__iter__'):
            raise TypeError('x must an array with length ndimensions')

        return super(BaseMultivariateDistribution, self).cdf(x)

    def logcdf(self, x):
        if hasattr(x, '__iter__'):
            raise TypeError('x must an array with length ndimensions')

        return super(BaseMultivariateDistribution, self).logcdf(x)


    def sample(self, size=None, dimension=None):
        """
        Sample from the distribution.

        Arguments
        -----------
        * `size` (int or tuple or None, optional, default=None): size/shape of the
            resulting array.
        * `dimension`: (int, optional): dimension of the multivariate distribution
            to sample.  If not provided or None, will default to <<class>.dimension>.

        Returns
        ---------
        * float or array: float if `size=None`, otherwise a numpy array with
            shape defined by `size`.
        """

        # TODO: add support for per-dimension unit, wrap_at, as_quantity (and pass in to_mvhistogram)

        dimension = self.get_dimension_by_label(dimension if dimension is not None else self.dimension)
        sample = self.dist_constructor_object.rvs(size=size)

        if dimension is not None:
            if len(sample.shape) == 1:
                return sample[dimension]
            else:
                return sample[:, dimension]
        else:
            return sample

    def plot(self, *args, **kwargs):
        """
        """
        dimension = self.get_dimension_by_label(kwargs.pop('dimension', None))
        if dimension is not None:
            return self.take_dimension(dimension).plot(*args, **kwargs)
        elif self.dimension is not None:
            return super(BaseMultivariateDistribution, self).plot(*args, **kwargs)
        else:
            # then we need to do a corner plot
            if not _has_corner:
                raise ImportError("corner must be installed to plot multivariate distributions.  Either install corner or pass a value to dimension to plot a 1D distribution.")

            return corner.corner(self.sample(size=int(1e5)), labels=self.label, **kwargs)

    def to_histogram(self, N=100000, bins=10, range=None, dimension=None, wrap_at=None):
        """
        Convert the <<class>> distribution to a <Histogram> distribution.

        Under-the-hood, this calls <<class>.sample> with `size=N` and `wrap_at=False`
        and passes the resulting array as well as the requested `bins` and `range`
        to <Histogram.from_data>.

        Arguments
        -----------
        * `N` (int, optional, default=100000): number of samples to use for
            the histogram.
        * `bins` (int, optional, default=10): number of bins to use for the
            histogram.
        * `range` (tuple or None): range to use for the histogram.
        * `dimension` (int or string, default=None): dimension to use
            when flattening to the 1-D histogram distribution. If not proivded
            or None, will use value from <<class>.dimension>.  `dimension` is
            therefore REQUIRED if <<class>.dimension> is None.
        * `wrap_at` (float or None, optional, default=None): value to set for
            `wrap_at` of the returned <Histogram>.  If None or not provided,
            will default to <<class>.wrap_at>.

        Returns
        --------
        * a <Histogram> object

        Raises
        ---------
        * ValueError: if `dimension` and <<class>.dimension> are both None.
        """
        if dimension is None:
            dimension = self.dimension

        dimension = self.get_dimension_by_label(dimension)

        if dimension is None:
            raise ValueError("must provide dimension.")

        unit = self.unit[dimension] if isinstance(self.unit, list) else self.unit
        label = self.label[dimension] if isinstance(self.label, list) else self.label
        if wrap_at is None:
            wrap_at = self.wrap_at[dimension] if isinstance(self.wrap_at, list) else self.wrap_at

        return Histogram.from_data(self.sample(dimension=dimension, size=N, wrap_at=False),
                                   bins=bins, range=range,
                                   unit=unit, label=label, wrap_at=wrap_at)


class DistributionCollection(object):
    """
    <DistributionCollection> allows sampling from multiple distribution objects
    simultaneously, respecting all underlying covariances whenever possible.
    """
    def __init__(self, *distributions):
        # if isinstance(distributions, BaseDistribution):
            # distributions = [distributions]

        # if not (isinstance(distributions, list) or isinstance(distributions, tuple)):
            # raise TypeError("distributions must be a list or tuple of distribution objects")
        if not _np.all(isinstance(dist, BaseDistribution) for dist in distributions):
            raise ValueError("all items in distributions must be of type BaseDistribution")

        self._dists = distributions

    @property
    def distributions(self):
        return self._dists

    @property
    def distributions_unpacked(self):
        # first well expand any Composite distributions to access the underlying
        # distributions
        def unpack_dists(dist):
            if isinstance(dist, Composite):
                dists = []
                for dist in dist.dists:
                    dists += unpack_dists(dist)
                return dists
            else:
                return [dist]

        dists_all = []
        for dist in self.distributions:
            dists_all += unpack_dists(dist)

        return dists_all

    def sample(self, *args, **kwargs):
        """
        Sample from multiple distributions with random seeds automatically determined,
        but applied to distributions of the same underlying multivariate distribution
        automatically.

        For each unique <BaseDistribution.hash> in the distributions in `dists` a
        random seed will be generated and applied to <BaseDistribution.sample>
        for all distributionis in `dists` which share that same hash value.  By doing
        so, any <BaseMultivariateDistribution> which samples from the same underlying
        multivariate distribution (but for a different
        <BaseMultivariateDistribution.dimension>), will be correctly sampled to account
        for the covariance/correlation between parameters, but all other 1-D
        <BaseDistribution> objects will be sampled with their own independent
        random seeds.

        Arguments
        -------------
        * `*args`: all positional arguments are sent to <BaseDistribution.sample>
            for each item in `dists`.
        * `**kwargs`: all keyword arguments are sent to <BaseDistribution.sample>
            for each item in `dists`.  Note: `seed` is forbidden and will raise
            a ValueError.

        Returns
        -------------
        * (list): list of samples, in same order as <<class>.distributions>.

        Raises
        ----------
        * ValueError: if `seed` is passed.
        """
        if 'seed' in kwargs.keys():
            raise ValueError("seeds are automatically determined: cannot pass seed")

        seeds = kwargs.pop('seeds', {})
        if seeds is None:
            seeds = {}

        for i,dist in enumerate(self.distributions_unpacked):
            seeds.setdefault(dist.hash, get_random_seed()[i])


        samples = [dist.sample(*args, seed=seeds, **kwargs) for dist in self.distributions]
        return _np.asarray(samples).T


    def logpdf(self, values):
        """

        Arguments
        ------------
        * `values` (list, tuple, or array): list of values in same length and
            order as <<class>.distributions>.

        Returns
        ----------
        * float
        """
        logpdf = 0.0
        dists_dict = {}
        values_dict = {}

        for dist,value in zip(self.distributions, values):
            hash = dist.hash
            if hash in dists_dict.keys():
                dists_dict[hash] += [dist]
                values_dict[hash] += [value]
            else:
                dists_dict[hash] = [dist]
                values_dict[hash] = [value]

        for dists, values in zip(dists_dict.values(), values_dict.values()):
            for dist, value in zip(dists, values):
                logpdf += dist.logpdf(value)
            # logpdf += dists[0].logp(values, dimension=[dist.dimension for dist in dists]) #* len(dists)

        return logpdf

    def sample_func(self, func, x, N=1000, func_kwargs={}):
        """
        Draw samples from a callable function.

        See also:

        * <<class>.plot_func>

        Arguments
        -----------
        * `func` (callable): callable function
        * `x` (array like): x values to pass to `func`.
        * `N` (int, optional, default=1000): number of samples to draw.
        * `func_kwargs` (dict, optional): additional keyword arguments to pass to
            `func`.


        Returns
        -----------
        * an array of models with shape (N, len(x))

        Raises
        -----------
        """
        # TODO: allow passing args to sample_from_dists
        # TODO: optimize this by doing all sampling first?
        sample_args = [self.sample() for i in range(N)]
        models = _np.array([func(x, *sample_args[i], **func_kwargs) for i in range(N)])
        return models

    def plot_func(self, func, x, N=1000, func_kwargs={}, show=False):
        """
        Draw samples from a callable function and plot.

        The passed callable `func` will be called with arguments `x` followed by
        the individually drawn values from each distribution in `dists` (in order
        provided) and then any additional `func_kwargs`.

        See also:

        * <<class>.sample_func>
        * <<class>.sample>

        Arguments
        -----------
        * `func` (callable): callable function
        * `x` (array like): x values to pass to `func`.
        * `N` (int, optional, default=1000): number of samples to draw.
        * `func_kwargs` (dict, optional): additional keyword arguments to pass to
            `func`.
        * `show` (bool, optional, default=False): whether to call plt.show()

        Returns
        -----------
        * list of created matplotlib artists

        Raises
        -----------
        * ImportError: if matplotlib is not imported
        """


        if not _has_mpl:
            raise ImportError("plot_func requires matplotlib.")

        models = self.sample_func(func, x, N=N, func_kwargs=func_kwargs)

        # TODO: allow options for sigma boundaries
        bounds = _np.percentile(models, 100 * _norm.cdf([-2, -1, 1, 2]), axis=0)

        ret1 = _plt.fill_between(x, bounds[0, :], bounds[-1, :],
                         label="95\% uncertainty", facecolor="#03A9F4", alpha=0.4)
        ret2 = _plt.fill_between(x, bounds[1, :], bounds[-2, :],
                         label="68\% uncertainty", facecolor="#0288D1", alpha=0.4)

        if show:
            _plt.show()

        return ret1, ret2



########################## UNIVARIATE DISTRIBUTIONS ############################


class Composite(BaseUnivariateDistribution):
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
    sin_g = np.sin(g)
    print(sin_g)
    ```

    Currently supported operators include:

    * multiplication, division, addition, subtraction
    * np.sin, np.cos, np.tan (but not math.sin, etc)
    * bitwise and (&), bitwise or (|)

    When doing math between a distribution and a float or integer, that float/int
    will be treated as a <Delta> distribution.  In some simple cases, the
    applicable distribution type will be returned, but in other cases,
    a <Composite> distribution will be returned.  For example, multiplying
    a <Uniform> or <Gaussian> distribution by a float will return another
    <Uniform> or <Gaussian> distribution, respectively.

    Limitations and treatment "under-the-hood":

    * &: the pdfs of the two underlying distributions are sampled over their
        99.99\% intervals and multiplied to create a new pdf.  A spline is then
        fit to the pdf and integrated to create the cdf (which is inverted to
        create the ppf function).  Each of these are then linearly interpolated
        to create the underlying scipy.stats object.  This object is then used
        for sampling as well as accessing the <<class>.pdf>, <<class>.cdf>,
        <<class>.ppf>, etc.  For this reason, the and operator does not support
        retaining covariances at all.

    * |: the pdfs and cdfs of the two underlying distributions are sampled over their
        99.9\% intervals and added to create the new pdfs and cdfs, respectively
        (and the cdf inverted to create the ppf function).  Each of these are then
        linearly interpolated to create the underlying scipy.stats object.  This
        object is then used for any call to the underlying call EXCEPT for sampling.
        Sampling is handled by randomly choosing which child distribution to sample
        from and then sampling from that distribution.  Or operators are therefore
        able to retain covariances for <<class>.sample>, but not for any calls
        to <<class>.pdf>, <<class>.cdf>, or <<class>.ppf>.

    * all others: sampling is handled by sampling the underyling children and
        therefore can retain covariances.  The pdfs, cdfs, and ppfs are
        created by taking 1 million samples, converting to a <Histogram>,
        and linearly interpolating between the bins, thereby losing all covariances.

    """
    def __init__(self, math, dist1, dist2=None, unit=None, label=None, wrap_at=None):
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
        * `wrap_at` (float, None, or False, optional, default=None): value to
            use for wrapping.  If None and `unit` are angles, will default to
            2*pi (or 360 degrees).  If None and `unit` are cycles, will default
            to 1.0.

        Returns
        ---------
        * a <Composite> object.
        """

        # TODO: do we need to make copies of dist1 and dist2?
        dist1 = dist1.copy()
        if dist2 is not None:
            dist2 = dist2.copy()

        super(Composite, self).__init__(unit, label, wrap_at,
                                        _stats_custom.generic_pdf_cdf_ppf, ('_pdf_cdf_ppf_callables'),
                                        ('math', math, is_math), ('dist1', dist1, is_distribution), ('dist2', dist2, is_distribution_or_none))

        if _has_astropy:
            if dist1.unit is not None:
                if dist2 is None:
                    # trig always gives unitless
                    self.unit = _units.dimensionless_unscaled
                elif dist2.unit is not None:
                    if math in ['__add__', '__sub__', '__and__', '__or__']:
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

        # do some paperwork so changes to descriptors in the children bubble
        # up and will call self._dist_constructor_object_clear_cache()
        dist1._parents_with_cache.append(self)
        if dist2 is not None:
            dist2._parents_with_cache.append(self)


    def __repr__(self):
        return "<npdists.{} {} unit={}>".format(self.__class__.__name__.lower(), self.__str__(), self.unit if self.unit is not None else "None")

    def __str__(self):
        if self.dist2 is not None:
            return "{}{}{}".format(self.dist1.__str__(), _math_symbols.get(self.math, self.math), self.dist2.__str__())
        else:
            return "{}({})".format(_math_symbols.get(self.math, self.math), self.dist1.__str__())

    @property
    def dists(self):
        if self.dist2 is not None:
            return [self.dist1, self.dist2]
        else:
            return [self.dist1]

    @property
    def hash(self):
        """
        """
        if self.dist2 is not None:
            if self.dist1.hash == self.dist2.hash:
                return self.dist1.hash
            else:
                # NOTE (IMPORTANT): then we are going to "forget" these when
                # nesting ComposisteDistributions
                # return super(CompositeDistribution, self).hash()
                return [self.dist1.hash, self.dist2.hash]
        else:
            return self.dist1.hash


    @property
    def _pdf_cdf_ppf_callables(self):
        # TODO: how do we need to handle units here... do we always need to
        # convert to SI before doing anything?  Or keep quantities?  Or do math
        # on units after?

        if self.math in ['__and__', '__or__']:
            dist1range = self.dist1.interval(0.9999, wrap_at=False)
            dist2range = self.dist2.interval(0.9999, wrap_at=False)

            # we'll set the sampling so each distribution gets its range sample 1000 times, append, and then sort
            x = _np.append(_np.linspace(dist1range[0]-0.1*(dist1range[1]-dist1range[0]),
                                        dist1range[1]+0.1*(dist1range[1]-dist1range[0]),
                                        int(1e4)),
                           _np.linspace(dist2range[0]-0.1*(dist2range[1]-dist2range[0]),
                                        dist2range[1]+0.1*(dist2range[1]-dist2range[0]),
                                        int(1e4)))
            x.sort()
            if self.math == '__and__':
                pdf = self.dist1.pdf(x) * self.dist2.pdf(x)
                # unfortunately we'll need to integrate to get the cdf... we'll do that later
                cdf = None
            elif self.math == '__or__':
                pdf = self.dist1.pdf(x) + self.dist2.pdf(x)
                cdf = self.dist1.cdf(x) + self.dist2.cdf(x)
            else:
                raise NotImplementedError()

            # make sure pdf is normalized correctly
            pdf_integral = _np.sum(pdf[1:]*abs(x[1:]-x[:-1]))
            pdf /= pdf_integral

            pdf_call = _stats_custom.interpolate_callable(x, pdf)

            if cdf is None:
                # print("*** integrating to compute cdf over spline (this may be slow... we'll eventually cache this so it only needs to be done once until an attribute is changed)")
                spline = _interpolate.UnivariateSpline(x, pdf, k=1, s=0)
                def _spline_int_single(xi):
                    return spline.integral(x[0], xi)

                cdf_vec = _np.vectorize(_spline_int_single)
                cdf = cdf_vec(x)

            # make sure cdf is normalized correctly
            cdf /= cdf[-1]

            ppf_call = _stats_custom.interpolate_callable(cdf, x)

            # make sure interpolation on the right always gives 1, not the fill_value of 0
            cdf_call = _stats_custom.interpolate_callable(_np.append(x, _np.inf), _np.append(cdf, 1.0))

            return pdf_call, cdf_call, ppf_call

        elif self.dist2 is not None:


        # elif self.dist2 is None:
        #     dist1range = self.dist1.interval(0.9999, wrap_at=False)
        #     xorig = _np.linspace(dist1range[0]-0.1*(dist1range[1]-dist1range[0]),
        #                          dist1range[1]+0.1*(dist1range[1]-dist1range[0]),
        #                          int(1e4))
        #
        #     # TODO: handle angle units correctly! (if self.dist1.unit is degrees, convert to radians first!)
        #     x = getattr(_np, self.math)(xorig)
        #     sort = x.argsort()
        #     x = x[sort]
        #     pdf = self.dist1.pdf(xorig)[sort]
        #     cdf = self.dist1.cdf(xorig)[sort]
        #
        #     # make sure pdf is normalized correctly
        #     pdf_integral = _np.sum(pdf[1:]*abs(x[1:]-x[:-1]))
        #     pdf /= pdf_integral
        #
        #     pdf_call = _stats_custom.interpolate_callable(x, pdf)
        #
        #     # make sure cdf is normalized correctly
        #     cdf /= cdf[-1]
        #
        #     ppf_call = _stats_custom.interpolate_callable(cdf, x)
        #
        #     # make sure interpolation on the right always gives 1, not the fill_value of 0
        #     cdf_call = _stats_custom.interpolate_callable(_np.append(x, _np.inf), _np.append(cdf, 1.0))
        #
        #     return pdf_call, cdf_call, ppf_call

        else:
            # TODO: how do we send reasonable defaults here to know how to bin?
            # Should we look at the ranges of the children like we do for
            # and/or?
            return self.to_histogram(N=int(1e6), bins=100, wrap_at=False)._pdf_cdf_ppf_callables

    @property
    def dist_constructor_args(self):
        return self._pdf_cdf_ppf_callables

    def _sample_from_children(self, math, dist1, dist2, seed={}, size=None):
        if math == '__and__':
            raise NotImplementedError("cannot sample from children with & logic")
        elif self.math == '__or__':
            # choose randomly between the two child Distributions
            choice = _np.random.randint(0,2)
            if size is None:
                dist = [dist1, dist2][choice]
                return dist.sample(size=size, seed=seed, as_quantity=_has_astropy and self.unit not in [None, _units.dimensionless_unscaled])
            else:
                # NOTE: // for python2 and 3 will do floor division, returning an integer
                size1 = size//2
                size2 = size//2
                if (size % 2) != 0:
                    # then size is odd, so we'll use the randomly drawn choice
                    # to determine which child distribution gets the extra sample
                    if choice == 0:
                        size1 += 1
                    else:
                        size2 += 1

                return _np.concatenate((dist1.sample(size=size1, seed=seed, as_quantity=_has_astropy and self.unit not in [None, _units.dimensionless_unscaled]),
                                        dist2.sample(size=size2, seed=seed, as_quantity=_has_astropy and self.unit not in [None, _units.dimensionless_unscaled])))

        elif self.dist2 is not None:
            # NOTE: this will account for multivariate, but only for THESE 2
            # if there are nested CompositeDistributions, then the seed will be lost

            # samples = sample_from_dists((dist1, dist2), seeds=seed, size=size)
            # TODO: OPTIMIZE: should we cache the collection?
            samples = DistributionCollection(dist1, dist2).sample(seeds=seed, size=size)
            if size is not None:
                return getattr(samples[:,0], math)(samples[:,1])
            else:
                return getattr(samples[0], math)(samples[1])
        else:
            # if math in ['sin', 'cos', 'tan'] and _has_astropy and dist1.unit is not None:
            #     unit = _units.rad
            # else:
            #     unit = None
            return getattr(_np, math)(dist1.sample(size=size, seed=seed, as_quantity=_has_astropy and self.unit not in [None, _units.dimensionless_unscaled]))



            return self._return_with_units(self.wrap(self._sample_from_children(*self.sample_args, size=size, seed=seed), wrap_at=wrap_at), unit=unit, as_quantity=as_quantity)


    def sample(self, size=None, unit=None, as_quantity=False, wrap_at=None, seed={}):
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
        * `wrap_at` (float, None, or False, optional, default=None): value to
            use for wrapping.  See <<class>.wrap>.  If not provided or None,
            will use the value from <<class>.wrap_at>.  Note: wrapping is
            computed before changing units, so `wrap_at` must be provided
            according to <<class>.unit> not `unit`.
        * `seed` (dict, optional, default={}): seeds (as hash: seed pairs) to
            pass to underlying distributions.

        Returns
        ---------
        * float or array: float if `size=None`, otherwise a numpy array with
            shape defined by `size`.
        """
        if self.math in ['__and__']:
            # fallback on using the interpolated combined pdf/cdf/ppf

            # TODO: technically we could support sample_from_children with a
            # while loop... but that is likely more expensive:
            # while True:
            #     sampled_value = dist1.rvs()
            #     chance = dist2.pdf(sampled_value)
            #     q = _np.random.random()
            #     if q <= chance:
            #         return sample_value
            return super(Composite, self).sample(size=size, unit=unit, as_quantity=as_quantity, wrap_at=wrap_at, seed=seed)
        else:
            # NOTE: even though in these cases we sample from the underlying children
            # (and therefore can account for covariances from multivariate children),
            # calls to pdf/cdf/ppf will still need to merge and interpolate
            # and will ignore these covariances.
            return self._return_with_units(self.wrap(self._sample_from_children(self.math, self.dist1, self.dist2, size=size, seed=seed), wrap_at=wrap_at), unit=unit, as_quantity=as_quantity)


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
        return self.to_histogram(N=N, bins=bins, range=range).to_gaussian()

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
        return self.to_histogram(N=N, bins=bins, range=range).to_uniform(sigma=sigma)


class Histogram(BaseUnivariateDistribution):
    """
    A Histogram distribution stores a discrete PDF and allows sampling from
    that binned density distribution.

    To create a Histogram distribution from already binned data, see
    <npdists.histogram_from_bins> or <Histogram.__init__>.  To create a
    Histogram distribtuion from the data array itself, see
    <npdists.histogram_from_data> or <Histogram.from_data>.

    Treatment under-the-hood:

    The densities at each bin-midpoint are linearly interpolated to create
    a pdf (which is normalized to an integral of 1).  A numerical integral
    of the bins is then performed to create the cdf (again, normalized to 1)
    and inverted to create the ppf.  Each of these are then interpolated
    whenever accessing <<class>.pdf>, <<class>.cdf>, <<class>.ppf>, etc as
    well as used when calling <<class>.sample>.
    """
    def __init__(self, bins, density, unit=None, label=None, wrap_at=None):
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
        * `wrap_at` (float, None, or False, optional, default=None): value to
            use for wrapping.  If None and `unit` are angles, will default to
            2*pi (or 360 degrees).  If None and `unit` are cycles, will default
            to 1.0.

        Returns
        --------
        * a <Histogram> object
        """
        super(Histogram, self).__init__(unit, label, wrap_at,
                                        _stats_custom.generic_pdf_cdf_ppf, ('_pdf_cdf_ppf_callables'),
                                        ('bins', bins, is_iterable), ('density', density, is_iterable))

    @classmethod
    def from_data(cls, data, bins=10, range=None, weights=None,
                  label=None, unit=None, wrap_at=None):
        """
        Create a <Histogram> distribution from data.  Note that under-the-hood
        a linear interpolator is used between the bins for the pdf, cdf, and ppf
        functions (and for sampling).

        This can also be created from a function at the top-level as:

        * <npdists.histogram_from_data>

        See also:

        * <Histogram.__init__>
        * <npdists.histogram_from_bins>

        Arguments
        --------------
        * `data` (np.array object): 1D array of values.
        * `bins` (int or array, optional, default=10): number of bins or value
            of bin edges.  Passed to np.histogram.
        * `range` (tuple, optional, default=None): passed to np.histogram.
        * `weights` (array, optional, default=None): passed to np.histogram.
        * `unit` (astropy.units object, optional): the units of the provided values.
        * `label` (string, optional): a label for the distribution.  This is used
            for the x-label while plotting the distribution, as well as a shorthand
            notation when creating a <Composite> distribution.
        * `wrap_at` (float, None, or False, optional, default=None): value to
            use for wrapping.  If None and `unit` are angles, will default to
            2*pi (or 360 degrees).  If None and `unit` are cycles, will default
            to 1.0.

        Returns
        --------
        * a <Histogram> object
        """
        hist, bin_edges = _np.histogram(data, bins=bins, range=range, weights=weights, density=True)

        return cls(bin_edges, hist, label=label, unit=unit, wrap_at=wrap_at)

    @property
    def _pdf_cdf_ppf_callables(self):
        bincenters = _np.mean(_np.vstack([self.bins[0:-1], self.bins[1:]]), axis=0)
        pdf = self.density
        pdf_call = _stats_custom.interpolate_callable(bincenters, pdf)

        bincenters = _np.mean(_np.vstack([self.bins[0:-1], self.bins[1:]]), axis=0)
        cdf = _np.cumsum(self.density)
        cdf = cdf / float(cdf[-1])

        ppf_call = _stats_custom.interpolate_callable(cdf, bincenters)

        # make sure interpolation on the right always gives 1, not the fill_value of 0
        cdf_call = _stats_custom.interpolate_callable( _np.append(bincenters, _np.inf), _np.append(cdf, 1.0))

        return pdf_call, cdf_call, ppf_call

    @property
    def dist_constructor_args(self):
        return self._pdf_cdf_ppf_callables

    def to_gaussian(self):
        """
        Convert the <Histogram> distribution to a <Gaussian> distribution by
        adopting the values of <Histogram.median> and <Histogram.std>.

        Returns
        --------
        * a <Gaussian> object
        """
        dco = self.dist_constructor_object
        return Gaussian(dco.median(), dco.std(), label=self.label, unit=self.unit, wrap_at=self.wrap_at)

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

class Delta(BaseUnivariateDistribution):
    """
    A Delta distribution will _always_ return the central values.  In most cases,
    there is no need to manually create a Delta distribution.  But when doing
    math on other <BaseDistribution> objects, <Delta> distributions are often
    created for clarity.

    Can be created from the top-level via the <npdists.delta> convenience function.
    """
    def __init__(self, loc=0.0, unit=None, label=None, wrap_at=None):
        """
        Create a <Delta> distribution.

        This can also be created from a function at the top-level as:

        * <npdists.delta>

        Arguments
        --------------
        * `loc` (float or int, default=0.0): the loc at which the delta function is True.
        * `unit` (astropy.units object, optional): the units of the provided values.
        * `label` (string, optional): a label for the distribution.  This is used
            for the x-label while plotting the distribution, as well as a shorthand
            notation when creating a <Composite> distribution.
        * `wrap_at` (float, None, or False, optional, default=None): value to
            use for wrapping.  If None and `unit` are angles, will default to
            2*pi (or 360 degrees).  If None and `unit` are cycles, will default
            to 1.0.

        Returns
        --------
        * a <Delta> object
        """
        super(Delta, self).__init__(unit, label, wrap_at,
                                    _stats_custom.delta, ('loc',),
                                    ('loc', loc, is_float))

    def __mul__(self, other):
        if isinstance(other, Delta):
            other = other.loc

        if (isinstance(other, float) or isinstance(other, int)):
            dist = self.copy()
            dist.loc *= other
            return dist

        return super(Delta, self).__mul__(other)

    def __div__(self, other):
        return self.__mul__(1./other)

    def __add__(self, other):
        if isinstance(other, Delta):
            other = other.loc

        if (isinstance(other, float) or isinstance(other, int)):
            dist = self.copy()
            dist.loc += other
            return dist

        return super(Delta, self).__add__(other)

    def __sub__(self, other):
        return self.__add__(-1*other)

    def __float__(self):
        return self.loc

    def to_uniform(self):
        """
        Convert the <Delta> distribution to a <Uniform> distribution in which
        both the lower and upper bounds are the same as the value.

        Returns
        ----------
        * a <Uniform> object
        """
        low = self.loc
        high = self.loc
        return Uniform(low, high, label=self.label, unit=self.unit, wrap_at=self.wrap_at)

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
        return Gaussian(self.loc, 0.0, label=self.label, unit=self.unit, wrap_at=self.wrap_at)


class Gaussian(BaseUnivariateDistribution):
    """
    A Gaussian (or Normal) distribution uses [scipy.stats.norm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html)
    to sample values from a gaussian function.

    Can be created from the top-level via the <npdists.gaussian> or
    <npdists.normal> convenience functions.
    """
    def __init__(self, loc=0.0, scale=1.0, unit=None, label=None, wrap_at=None):
        """
        Create a <Gaussian> distribution.

        This can also be created from a function at the top-level as:

        * <npdists.gaussian>

        Arguments
        --------------
        * `loc` (float or int, default=0.0): the central value (mean) of the
            gaussian distribution.
        * `scale` (float or int, default=1.0): the scale (sigma) of the gaussian
            distribution.
        * `unit` (astropy.units object, optional): the units of the provided values.
        * `label` (string, optional): a label for the distribution.  This is used
            for the x-label while plotting the distribution, as well as a shorthand
            notation when creating a <Composite> distribution.
        * `wrap_at` (float, None, or False, optional, default=None): value to
            use for wrapping.  If None and `unit` are angles, will default to
            2*pi (or 360 degrees).  If None and `unit` are cycles, will default
            to 1.0.

        Returns
        --------
        * a <Gaussian> object
        """
        super(Gaussian, self).__init__(unit, label, wrap_at,
                                       _stats.norm, ('loc', 'scale'),
                                       ('loc', loc, is_float), ('scale', scale, is_float))

    def __mul__(self, other):
        if isinstance(other, Delta):
            other = other.loc

        if (isinstance(other, float) or isinstance(other, int)):
            dist = self.copy()
            dist.loc *= other
            dist.scale *= other
            return dist

        return super(Gaussian, self).__mul__(other)

    def __div__(self, other):
        return self.__mul__(1./other)

    def __add__(self, other):
        if isinstance(other, Delta):
            other = other.loc

        if (isinstance(other, float) or isinstance(other, int)):
            dist = self.copy()
            dist.loc += other
            return dist

        return super(Gaussian, self).__add__(other)

    def __sub__(self, other):
        return self.__add__(-1*other)

    def __float__(self):
        return self.loc

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
        return Uniform(low, high, label=self.label, unit=self.unit, wrap_at=self.wrap_at)


class Uniform(BaseUnivariateDistribution):
    """
    A Uniform (or Boxcar) distribution gives equal weights to all values within
    the defined range and uses [scipy.stats.uniform](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.uniform.html)
    to sample values.

    Can be created from the top-level via the <npdists.uniform> or
    <npdists.boxcar> convenience functions.
    """
    def __init__(self, low=0.0, high=1.0, unit=None, label=None, wrap_at=None):
        """
        Create a <Uniform> distribution.

        This can also be created from a function at the top-level as:

        * <npdists.uniform>

        Arguments
        --------------
        * `low` (float or int, default=0.0): the lower limit of the uniform distribution.
        * `high` (float or int, default=1.0): the upper limits of the uniform distribution.
            Must be higher than `low` unless `wrap_at` is provided or `unit`
            is provided as angular (rad, deg, cycles).
        * `unit` (astropy.units object, optional): the units of the provided values.
        * `label` (string, optional): a label for the distribution.  This is used
            for the x-label while plotting the distribution, as well as a shorthand
            notation when creating a <Composite> distribution.
        * `wrap_at` (float, None, or False, optional, default=None): value to
            use for wrapping.  If None and `unit` are angles, will default to
            2*pi (or 360 degrees).  If None and `unit` are cycles, will default
            to 1.0.

        Returns
        --------
        * a <Uniform> object
        """
        super(Uniform, self).__init__(unit, label, wrap_at,
                                       _stats.uniform, ('low', 'width'),
                                       ('low', low, is_float), ('high', high, is_float))

    def __mul__(self, other):
        if isinstance(other, Delta):
            other = other.loc

        if (isinstance(other, float) or isinstance(other, int)):
            dist = self.copy()
            dist.low *= other
            dist.high *= other
            return dist

        return super(Uniform, self).__mul__(other)


    def __div__(self, other):
        return self.__mul__(1./other)

    def __add__(self, other):
        if isinstance(other, Delta):
            other = other.loc

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

    @property
    def width(self):
        return self.high - self.low

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
        loc = self.median()
        scale = (self.high - self.low) / (2.0 * sigma)
        return Gaussian(loc, scale, unit=self.unit, label=self.label, wrap_at=self.wrap_at)

######################### MULTIVARIATE DISTRIBUTIONS ###########################

class MVGaussian(BaseMultivariateDistribution):
    def __init__(self, mean=0.0, cov=1.0, allow_singular=False, unit=None, label=None, wrap_at=None):
        """
        Create a <MVGaussian> distribution.

        This can also be created from a function at the top-level as:

        * <npdists.mvgaussian>

        Arguments
        --------------
        * `mean` (float or int, default=0.0): the central value of the gaussian distribution.
        * `cov` (float or int, default=1.0): the scale (sigma) of the gaussian distribution.
        * `unit` (astropy.units object, optional): the units of the provided values.
        * `label` (string, optional): a label for the distribution.  This is used
            for the x-label while plotting the distribution, as well as a shorthand
            notation when creating a <Composite> distribution.
        * `wrap_at` (float, None, or False, optional, default=None): value to
            use for wrapping.  If None and `unit` are angles, will default to
            2*pi (or 360 degrees).  If None and `unit` are cycles, will default
            to 1.0.

        Returns
        --------
        * a <MVGaussian> object
        """
        super(MVGaussian, self).__init__(unit, label, wrap_at,
                                         _stats.multivariate_normal, ('mean', 'cov', 'allow_singular'),
                                         ('mean', mean, is_iterable), ('cov', cov, is_square_matrix), ('allow_singular', allow_singular, is_bool))

    @property
    def ndimensions(self):
        """
        """
        return len(self.mean)

    def to_mvhistogram(self, N=1e6, bins=15, range=None):
        """
        Convert the <<class>> distribution to an <MVHistogram> distribution.

        Under-the-hood, this calls <<class>.sample> with `size=N` and `wrap_at=False`
        and passes the resulting array as well as the requested `bins` and `range`
        to <MVHistogram.from_data>.

        Arguments
        -----------
        * `N` (int, optional, default=1e6): number of samples to use for
            the histogram.
        * `bins` (int, optional, default=15): number of bins to use for the
            histogram.
        * `range` (tuple or None): range to use for the histogram.

        Returns
        --------
        * an <MVHistogram> object
        """
        # TODO: if sample is updated to take wrap_at/wrap_ats... pass wrap_at=False here
        return MVHistogram.from_data(self.sample(size=int(N)),
                                     bins=bins, range=range,
                                     unit=self.unit, label=self.label, wrap_at=self.wrap_at)


class MVHistogram(BaseMultivariateDistribution):
    """

    Treatment under-the-hood:

    * When sampling, a random value between 0 and 1 is drawn.  The N-dimensional
    bins are then unraveled and integrated to create a flattened cdf.  The
    cdf is then linearly interpolated to find the index of the unraveled bins
    in which to sample, as well as the relative location in the bin.  The selected
    bin is then artificially subdivided by the same shape grid as the original
    binning and linearly interpolated based on the remainder to return a single
    value for <<class>.sample>.

    * Means and covariances (see <<class>.calculate_means_covariances>,
    <<class>.calculate_means>, <<class>.calculate_covariances>) are calculated
    by sampling (with a default size of 1e5), and determining the mean and covariances
    on that sample.

    """
    def __init__(self, bins, density, unit=None, label=None, wrap_at=None):
        """
        """
        super(MVHistogram, self).__init__(unit, label, wrap_at,
                                          None, None,
                                          ('bins', bins, is_iterable), ('density', density, is_iterable))

    @classmethod
    def from_data(cls, data, bins=10, range=None, weights=None,
                  label=None, unit=None, wrap_at=None):
        """
        """
        # TODO:  what version of numpy introduced density?  Do we need a try/except or to check the version?
        try:
            hist, bin_edges = _np.histogramdd(data, bins=bins, range=range, weights=weights, density=True)
        except TypeError:
            hist, bin_edges = _np.histogramdd(data, bins=bins, range=range, weights=weights, normed=True)


        return cls(_np.asarray(bin_edges), hist, label=label, unit=unit, wrap_at=wrap_at)

    def pdf(self, x):
        # TODO: N-dimension interpolation of (self.bins, self.density)
        raise NotImplementedError("pdf not supported for {} distribution".format(self.__class__.__name__))

    def logpdf(self, x):
        raise NotImplementedError("pdf not supported for {} distribution".format(self.__class__.__name__))

    @property
    def _cdf_per_bin(self):
        cdf = _np.cumsum(self.density)
        cdf /= float(cdf[-1])
        return cdf

    def cdf(self, x):
        # TODO: N-dimensional interpolation of (self.bins, self._cdf_per_bin)
        raise NotImplementedError("pdf not supported for {} distribution".format(self.__class__.__name__))

    def logcdf(self, x):
        raise NotImplementedError("pdf not supported for {} distribution".format(self.__class__.__name__))

    def ppf(self, q):
        # adapted from: https://stackoverflow.com/a/17822210
        #
        # MV case
        # density, bins = np.histogramdd(chain_flat, normed=True)
        # bins = np.asarray(bins)
        #
        # 1D case
        # density, bins = np.histogram(np.random.rand(1000), normed=True)
        # bins = np.asarray([bins])

        if _np.any(q > 1) or _np.any(q < 0):
            raise ValueError("q must be between 0 and 1")

        if isinstance(q, float):
            return_single = True
            q = _np.asarray([q])
        else:
            return_single = False
            q = _np.asarray(q)

        # this is cdf on the unraveled densities
        cdf = self._cdf_per_bin

        unraveled_index_float = _np.interp(q, cdf, range(len(cdf)))
        # print("unraveled_index_float: {}".format(unraveled_index_float))

        unraveled_index = unraveled_index_float.astype(int)
        unraveled_index_rem = unraveled_index_float - unraveled_index
        # print("unraveled_index: {}, unraveled_index_rem: {}".format(unraveled_index, unraveled_index_rem))

        # multivariate case
        ind_per_dim = _np.unravel_index(unraveled_index, self.density.shape)
        # now we'll essentially subdivide each bin by the shape of the original grid so that we can linearly interpolate inside the chosen bin
        rem_per_dim = _np.asarray(_np.unravel_index((unraveled_index_rem*len(cdf)).astype(int), self.density.shape)).astype(float) / _np.asarray(self.density.shape)[:, _np.newaxis]
        bin_width_per_dim = _np.row_stack([_np.diff(b) for b in self.bins])
        # print("ind_per_dim: {}".format(ind_per_dim))
        # print("bin_width_per_dim: {}".format(bin_width_per_dim))
        # print("rem_per_dim: {}".format(rem_per_dim))

        # b[ind] is the lower-edge of the bin... so we want to interpolate based on that bin_width
        values_from_bins = _np.column_stack([self.bins[dim,ind_this_dim]+bin_width_per_dim[dim,ind_this_dim]*rem_per_dim[dim] for dim,ind_this_dim in enumerate(ind_per_dim)])

        if return_single:
            return values_from_bins[0]
        else:
            return values_from_bins

    @property
    def ndimensions(self):
        """
        """
        return self.bins.shape[0]

    def sample(self, size=None, dimension=None):
        """
        """
        dimension = self.get_dimension_by_label(dimension if dimension is not None else self.dimension)
        if dimension is not None:
            bins = self.bins[dimension]
            density = self.density[dimension]
        else:
            bins = self.bins
            density = self.density

        q = _np.random.rand(size if size is not None else 1)
        return self.ppf(q)

    def plot(self, *args, **kwargs):
        """
        """
        # TODO: add plot_mvgaussian or plot_gaussian options to overplot the MVGaussian pdfs/contours

        dimension = self.get_dimension_by_label(kwargs.get('dimension', None))
        if dimension is not None:
            kwargs.setdefault('bins', self.bins[dimension])

        return super(MVHistogram, self).plot(*args, **kwargs)

    def calculate_means_covariances(self, N=1e5):
        """
        Return the weighted mean values and covariances from the histogram.

        See also:

        * <MVHistogram.calculate_means>
        * <MVHistogram.calculate_covariances>

        Arguments
        ---------
        * `N` (int, default=1e5): number of samples to use to pass to
            `np.cov`.

        Returns
        -------
        * means (array of floats), covariances (matrix)
        """
        # means could also be self.ppf(0.5)

        # TODO: pass wrap_at=False once supported
        samples = self.sample(size=int(N))
        # means = [_np.mean(samples[:,d] for d in range(self.dimensions))]
        means = _np.mean(samples, axis=0)
        covariances = _np.cov(samples.T)
        return means, covariances

    def calculate_means(self, N=1e5):
        """
        Return the weighted mean values from the histogram.

        See also:

        * <MVHistogram.calculate_covariances>
        * <MVHistogram.calculate_means_covariances>

        Arguments
        ---------
        * `N` (int, default=1e5): number of samples to use to pass to
            `np.cov`.

        Returns
        -------
        * list of floats: the mean value per dimension
        """
        return self.calculate_means_covariances(N=N)[0]

    def calculate_covariances(self, N=1e5):
        """
        Return the covariances about the mean from the histogram.

        Under-the-hood, this calls `np.cov` on the output from <<class>.sample>
        with `N` samples.

        See also:

        * <MVHistogram.calculate_means>
        * <MVHistogram.calculate_means_covariances>

        Arguments
        ---------
        * `N` (int, default=1e5): number of samples to use to pass to
            `np.cov`.

        Returns
        ---------
        * MxM square matrix of floats.
        """
        return self.calculate_means_covariances(N=N)[1]


    def to_mvgaussian(self, N=1e5, allow_singular=False):
        """
        Convert the <<class>> distribution to an <MVGaussian> distribution.

        See also:

        * <MVHistogram.calculate_means>
        * <MVHistogram.calculate_covariances>

        Arguments
        ---------
        * `N` (int, default=1e5): number of samples to use when calling
            <<class>.calculate_means> and <<class>.calculate_covariances>.
        * `allow_singular` (bool, optional, default=False): value to pass to
            <MVGaussian>.

        Returns
        --------
        * an <MVGaussian> object
        """
        mean, cov = self.calculate_means_covariances(N)
        return MVGaussian(mean, cov, allow_singular=allow_singular, unit=self.unit, label=self.label, wrap_at=self.wrap_at)
