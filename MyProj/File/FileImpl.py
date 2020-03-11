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

    def parse_csv(self, fileName):
        """
        """
        header = True
        try:
            with open(fileName) as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                while True:
                    if header:
                        keys = next(reader).split(",")
                    else:
                        yield dict(zip(keys, next(reader).split(",")))
        except StopIteration:
            pass
        except Exception as err:
            print "Error while parsing the file %s\n%s" % (fileName, err)

    def insert_files(self, fileName):
        """
        """
        try:
            documentObj = self.parse_csv(fileName)
            while True:
                document = next(documentObj)
                self.dbConnection.update(document)
                print document
        except StopIteration:
            print "%s inserted into DB" % fileName
        except Exception as err:
            print "Error while inserting file %s into DB" % err
        finally:
            Files.delete(fileName)

    @staticmethod
    def delete(fileName):
        """
        """
        try:
            os.remove(fileName)
        except Exception as err:
            print "Error while deleting the file %s\n%s" % (fileName, err)

    def start_insert_processes(self):
        """
        """
        noOfThreadsToBeSpawned = 2
        breakMainLoop = False
        with self.dbConnection as conn:
            while True:
                tList = []
                for _ in range(noOfThreadsToBeSpawned):
                    fileName = self.downloadQueue.get()
                    if not (fileName == "completed" or fileName == "error"):
                        t = threading.Thread(target=self.insert_files, args=(fileName,))
                        tList.append(t)
                    else:
                        print "all files recieved"
                        for t in tList:
                            t.start()
                        for t in tList:
                            t.join()
                        breakMainLoop = True
                        break
                if breakMainLoop:
                    break
                for t in tList:
                    t.start()
                for t in tList:
                    t.join()



