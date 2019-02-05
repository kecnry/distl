from . import npdists as _npdists
from .npdists import BaseDistribution # for isinstance checking

__version__ = '0.0.1'
version = __version__

def gaussian(*args, **kwargs):
    return _npdists.Gaussian(*args, **kwargs)

def normal(*args, **kwargs):
    return _npdists.Gaussian(*args, **kwargs)

def uniform(*args, **kwargs):
    return _npdists.Uniform(*args, **kwargs)

def boxcar(*args, **kwargs):
    return _npdists.Uniform(*args, **kwargs)

def histogram(*args, **kwargs):
    return _npdists.Histogram(*args, **kwargs)


def from_dict(d):
    """
    load an npdists object from a dictionary
    @parameter str d: dictionary representing the nparray object
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
    load an npdists object from a json-formatted string
    @parameter str j: json-formatted string
    """
    if isinstance(j, dict):
        return from_dict(j)

    if not (isinstance(j, str) or isinstance(j, unicode)):
        raise TypeError("argument must be of type str")

    return from_dict(json.loads(j))

def from_file(filename):
    """
    load an npdists object from a json filename
    @parameter str filename: path to the file
    """
    f = open(filename, 'r')
    j = json.load(f)
    f.close()

    return from_dict(j)
