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

    def parse_csv(fileName):
        """
        """
        data = []
        
        file_data = pd.read_csv(fileName)
        print("File Contain is")
        print(file_data)
        count_row = file_data.shape[0]
        print(count_row)
        for j in range(count_row-1):
            print(file_data["Object Name"].iloc[j+1])
            abc = str(file_data["Object Name"].iloc[j+1])
            object = abc.split(",")
            local_cell_Id = object[1].split("=")
            cell_Id = local_cell_Id[1]
            print("printing cell_Id",cell_Id)
            file_data_row = file_data.iloc[j+1]
            file_data_json = json.loads(file_data_row.to_json(orient='records'))
            data[cell_Id] = file_data_json
                
        return data
                
    def store_document(fileNames)
        """
        """
        for i in range(len(fileNames)):
            print("Reading fileName...", fileNames[i])
            data = parse_csv(fileNames[i]
            
            #db_cm.remove()
            db_cm.update(data)
            #storing as a dictionary where key is cell_d  and value is row : into the mongoDB


