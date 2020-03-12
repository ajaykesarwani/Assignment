"""
    abstract class of File
"""
import abc


class FileOperation(object):
    """
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, *params):
        pass

    @abc.abstractmethod
    def download(self):
        pass

    @abc.abstractmethod
    def parse_csv(self, *params):
        pass

    @abc.abstractmethod
    def store_document(self,*params):
        pass

