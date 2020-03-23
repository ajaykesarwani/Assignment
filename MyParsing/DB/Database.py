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
    def get(self):
        pass

    @abc.abstractmethod
    def insert(self, *params):
        pass
