"""
    abstract class to Connect to Remote Server
"""
import abc


class RemoteServer(object):
    """
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def connect_remote_server(self, *params):
        pass
