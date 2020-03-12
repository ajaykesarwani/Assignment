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


class FileImpl(absFile):
    """
    """
    def __init__(self, remotePath, localPath):
        self.remotePath = remotePath
        self.localPath = localPath
        
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

    
