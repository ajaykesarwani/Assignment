"""
"""
import shutil
import pathlib
import os
import csv
import multiprocessing
import threading
from datetime import datetime
from File.file import FileFileOperation as absFile
#from RS.SFTPConnectRS import SFtpConnectionRS
#from DB.MongoDB import MongoDB
#from src.utils.helper import get_cpu_count


class FileImpl(absFile):
    """
    """
    def __init__(self, remotePath, localPath):
        self.remotePath = remotePath
        self.localPath = localPath
        #self.downloadQueue = downloadQueue
        #self.serverConnection = SFtpConnectRS()
        #self.dbConnection = MongoDB()
    """                                                         
    @property
    def get_local_path(self):
        return self._localPath

    @localPath.setter
    def set_local_path(self, localPath):
        if not os.path.exists(localPath):
            raise Exception("Error occurred: local path %s does not exist" % localPath)
        self._localPath = localPath
"""
    def download(self):
        #Here only coping from one folder to other folder
        now = str(datetime.now())[:19]
        now = now.replace(":", "_")
        for filename in os.listdir(self.remotePath):
            #print("Name of File ",filename)
            _filename_ext = filename.split(".")
            dst_dir = self.localPath+str(_filename_ext[0]) + "_" + str(now) + ".csv"
            shutil.copy(self.remotePath+filename, dst_dir)

    def read_all_filename(self):
        filenames = glob(self.remotePath+'*.csv')
        return filenames

    @staticmethod
    def validate(file_name):
        """
        """
        if file_name.find(".csv") > -1:
            return True

    
