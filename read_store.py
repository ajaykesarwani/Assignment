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
        print("Coping only the CSV file from one folder to other!!!")
        now = str(datetime.now())[:19]
        now = now.replace(":", "_")
        src_dir = "C:\\Users\\USER\\Desktop\\Assignment\\SrcFile\\"
        for filename in os.listdir(src_dir):
            #print("Name of File ",filename)
            _filename_ext = filename.split(".")
            dst_dir = "C:\\Users\USER\\Desktop\\Assignment\DestFile"+ '\\'+str(_filename_ext[0]) + "_" + str(now) + ".csv"
            shutil.copy(src_dir+filename, dst_dir)

    def readFile(self):
        fileNames = glob('C:\Users\USER\Desktop\Assignment\DestFile\*.csv')
        return fileNames

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
        for i in range(len(fileNames)):
            print("Reading fileName...", fileNames[i])
            file_data = pd.read_csv(fileNames[i])
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
                print("storing data in mongodb",file_data_json)
                #store the data into DB
                db_cm.remove()
                db_cm.insert(data)
            count_row=0
                # inserting the as a dictionary where key is cell_d  and value is row : into the mongoDB


temp = read_store()
temp.downloadFile() #here it's just coping from one folder to other
fileNames = temp.readFile()
temp.connect_DB_store(fileNames)
