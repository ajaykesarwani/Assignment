"""
    abstract class to Connect to MongoDB
"""
import abc


class Database(object):
    """
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def connect_mongodb(self, *params):
        pass

    @abc.abstractmethod
    def update(self, *params):
        pass

