"""TODO
"""
import os

from dv_sounds import __path__ as dirpath


def get_dirpath():
    """TODO

    Returns
    -------

    """
    return dirpath[0]


def get_filepath(filename):
    """TODO

    Parameters
    ----------
    filename

    Returns
    -------

    """
    return os.path.join(get_dirpath(), filename)
