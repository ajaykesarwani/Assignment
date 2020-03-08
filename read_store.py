import sys
import pandas as pd
import pymongo
import json
import os
import shutil
from datetime import datetime
from glob import glob
import pysftp

#myHostname = "localhost"
#myUsername = ""
#myPassword = ""

#with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:
#    print "Connection succesfully stablished ... "
#
#    # Define the file that you want to download from the remote directory
#    remoteFilePath = '/var/MyFolder/SampleFile.csv'
#
#    # Define the local path where the file will be saved
#    # or absolute "C:\Users\sdkca\Desktop\TUTORIAL.txt"
#    localFilePath = './SampleFile.txt'
#
#    sftp.get(remoteFilePath, localFilePath)
#
# connection closed automatically at the end of the with-block


data = {}

class read_store:
    fileName=""
    def downloadFile(self):
        print("Trying to connect to Remote Serve")
        # copying the file from one folder to other
        now = str(datetime.now())[:19]
        now = now.replace(":", "_")
        src_dir = "C:\Users\USER\Desktop\Assignment\SrcFile\SampleFile.csv"
        dst_dir = "C:\Users\USER\Desktop\Assignment\DestFile\SampleFile"+"_" + str(now) + ".csv"
        shutil.copy(src_dir, dst_dir)

    def readFile(self):
        fileNames = glob('C:\Users\USER\Desktop\Assignment\DestFile\*.csv')
        print("printing the fileName")
        print(type(fileNames))
        print(fileNames)
        type(fileNames)
        #dataframes = [pd.read_csv(f) for f in fileNames]
        return fileNames

        #print("printing the contain of file")
        #print(dataframes[0])

    def connect_DB_store(self , fileNames):
        #Establishing Connection: Default port number: 27017
        try:
            mng_client = pymongo.MongoClient('localhost', 27017)
            print("Connected successfully!!!")
        except:
            print("Could not connect to MongoDB")
        # database
        mongodb_name = 'mydb'
        mng_db = mng_client[mongodb_name]
        #collection names
        collection = 'myCollection'
        db_cm = mng_db[collection]

        #reading csv file using pandas
        list = []
        for i in range(len(fileNames)):
            print("fileName...")
            print(fileNames[i])
            file_data = pd.read_csv(fileNames[i])
            print("FileData of")
            print(fileNames[i])
            print("file_data")
            print(file_data)
            count_row = file_data.shape[0]
            print("count_row")
            print(count_row)

            for j in range(count_row-2):
                print("firstRow")
                print(file_data["Object Name"].iloc[1])
                abc = str(file_data["Object Name"].iloc[1])
                list = abc.split(",")
                local_cell_Id = list[1].split("=")
                cell_Id = local_cell_Id[1]
                print(cell_Id)
                file_data_ = file_data.iloc[1]
                file_data_json = json.loads(file_data_.to_json(orient='records'))

                key = cell_Id
                data[key] = file_data_json
                print(data)
                print("after completin")
                print(dict(data))
                #data_json = json.dumps(dict(data))
                #print(data_json)
                #store the data into DB
                db_cm.remove()
                db_cm.insert(data)
                # inserting the as a dictionary where key is name of file and value is file as a document: into the mongoDB



#if __name__ == "__main__":
#    #filepath =""
#    fileName = "SampleFile.csv"
#    read_CSVfile_and_store(fileName)


temp = read_store()
temp.downloadFile() #here it's just coping from one folder to other
fileNames = temp.readFile()
temp.connect_DB_store(fileNames)