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
    def start_download_processes(self, *params):
        pass

    @abc.abstractmethod
    def start_insert_processes(self, *params):
        pass

    @abc.abstractmethod
    def parse_csv(self, *params):
        pass

    @abc.abstractmethod
    def delete(self, *params):
        pass

