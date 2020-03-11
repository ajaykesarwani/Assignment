"""
    SFTPConnectRS class to implement the abstract ConnectRemoteServer Class
"""
import pysftp
from RS.RemoteServer import RemoteServer as absRemoteServer
from Utility.utility import Singleton


class SFTPConnectRS(absRemoteServer, Singleton):
    # initializing the parameter
    def __init__(self, host, user, password, cnopts=None):
        self.host = host
        self.user = user
        self.password = password
        self.cnopts = cnopts

    # overriding abstract method
    def connect_remote_server(self):
        return pysftp.Connection(host=self.host, username=self.user, password=self.password, cnopts=self.cnopts)



