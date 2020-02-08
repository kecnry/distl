from . import distl as _distl

def from_dict(d):
    """
    Load an distl object from a dictionary.

    See also:

    * <distl.from_json>
    * <distl.from_file>

    Arguments
    -------------
    * `d` (string or dict): dictionary (or json string of a dictionary)
        representing the distl object.

    Returns
    ----------
    * The appropriate distribution object.
    """
    if isinstance(d, str):
        return from_json(d)

    if not isinstance(d, dict):
        raise TypeError("argument must be of type dict")
    if 'distl' not in d.keys():
        raise ValueError("input dictionary missing 'distl' entry")

    classname = d.get('distl')
    # unit = d.pop('unit', None)
    # instead of popping distl (which would happen in memory and make that json
    # unloadable again), we'll do a dictionary comprehension.  If this causes
    # performance issues, we could instead accept and ignore distl as
    # a keyword argument to __init__
    dist = getattr(_distl, classname)(**{k:v for k,v in d.items() if k!='distl'})
    # if unit is not None and _has_astropy:
        # dist *= _units.Unit(unit)
    return dist

def from_json(j):
    """
    Load an distl object from a json-formatted string.

    See also:

    * <distl.from_dict>
    * <distl.from_file>

    Arguments
    -------------
    * `s` (string or dict): json formatted dictionary representing the distl
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
    Load an distl object from a json filename.

    See also:

    * <distl.from_dict>
    * <distl.from_json>

    Arguments
    -------------
    * `s` (string): the filename pointing to a json formatted file representing
        an distl object.

    Returns
    ----------
    * The appropriate distribution object.
    """
    f = open(filename, 'r')
    j = _json.load(f)
    f.close()
    return from_dict(j)
