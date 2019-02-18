from . import npdists as _npdists
from .npdists import BaseDistribution # for isinstance checking
import json as _json

try:
    import dill as _dill
except ImportError:
    _has_dill = False
else:
    _has_dill = True

__version__ = '0.0.1'
version = __version__

def delta(value=0.0, unit=None, label=None):
    """
    Create a <Delta> distribution.

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
    return _npdists.Delta(value, unit=unit, label=label)


def uniform(low=0.0, high=1.0, unit=None, label=None):
    """
    Create a <Uniform> distribution.

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
    return _npdists.Uniform(low, high, unit=unit, label=label)

def boxcar(low=0.0, high=1.0, unit=None, label=None):
    """
    Shortcut to <npdists.uniform>.
    """
    return _npdists.Uniform(low, high, unit=unit, label=label)


def gaussian(loc=0.0, scale=1.0, unit=None, label=None):
    """
    Create a <Gaussian> distribution.

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
    return _npdists.Gaussian(loc, scale, unit=unit, label=label)

def normal(loc=0.0, scale=1.0, unit=None, label=None):
    """
    Shortcut to <npdists.gaussian>.
    """
    return _npdists.Gaussian(loc, scale, unit=unit, label=label)


def histogram_from_bins(bins, density, unit=None, label=None):
    """
    Create a <Histogram> distribution from binned data.

    See also:

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
    return _npdists.Histogram(bins, density, unit=unit, label=label)

def histogram_from_data(data, bins=10, range=None, weights=None, unit=None, label=None):
    """
    Create a <Histogram> distribution from data.

    See also:

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

    return _npdists.Histogram.from_data(data, bins=bins, range=range,
                                        weight=weights, unit=unit, label=label)


def function(func, unit, label, *args):
    """
    Create a <Function> distribution from some callable function and
    any number of arguments, including distribution objects.


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
    return _npdists.Function(func, unit, label, *args)



def from_dict(d):
    """
    Load an npdists object from a dictionary.

    See also:

    * <npdists.from_json>
    * <npdists.from_file>

    Arguments
    -------------
    * `d` (string or dict): dictionary (or json string of a dictionary)
        representing the npdists object.

    Returns
    ----------
    * The appropriate distribution object.
    """
    if isinstance(d, str):
        return from_json(d)

    if not isinstance(d, dict):
        raise TypeError("argument must be of type dict")
    if 'npdists' not in d.keys():
        raise ValueError("input dictionary missing 'nparray' entry")

    classname = d.pop('npdists').title()
    unit = d.pop('unit', None)
    dist = getattr(_npdists, classname)(**d)
    if unit is not None and _has_astropy:
        dist *= _unit.Unit(unit)
    return dist

def from_json(j):
    """
    Load an npdists object from a json-formatted string.

    See also:

    * <npdists.from_dict>
    * <npdists.from_file>

    Arguments
    -------------
    * `s` (string or dict): json formatted dictionary representing the npdists
        object.

    Returns
    ----------
    * The appropriate distribution object.
    """
    if isinstance(j, dict):
        return from_dict(j)

    if not (isinstance(j, str) or isinstance(j, unicode)):
        raise TypeError("argument must be of type str")

    return from_dict(_json.loads(j))

def from_file(filename):
    """
    Load an npdists object from a json filename.

    See also:

    * <npdists.from_dict>
    * <npdists.from_json>

    Arguments
    -------------
    * `s` (string): the filename pointing to a json formatted file representing
        an npdists object.

    Returns
    ----------
    * The appropriate distribution object.
    """
    f = open(filename, 'r')
    try:
        j = _json.load(f)
    except:
        f.close()
        if _has_dill:
            f = open(filename, 'rb')
            d = _dill.load(f)
            f.close()
            return d
        else:
            raise ImportError("file requires 'dill' package to load")
    else:
        f.close()
        return from_dict(j)
