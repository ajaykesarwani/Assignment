"""
 Utility Class
"""

"""
def singleton(cls):
    instance = cls()
    cls.__new__ = cls.__call__ = lambda cls: instance
    cls.__init__ = lambda self: None
    return instance
"""


class Singleton(object):
    """
    """
    instance = False

    def __new__(cls, *args, **kwargs):
        """
        """
        if not Singleton.instance:
            Singleton.instance = object.__new__(cls, *args, **kwargs)
        return Singleton.instance
