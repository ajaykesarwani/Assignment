import sys
import pandas as pd
import pymongo
import json
import os
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


def read_CSVfile_and_store(fileName):
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
    file_data = pd.read_csv(fileName)

    #print(file_data)
    # for i in range(3):
    #     print(data[i])

    file_data_json = json.loads(file_data.to_json(orient='records'))
    #print(file_data_json)

    key = os.path.splitext(fileName)[0]
    data[key] = file_data_json
    print(data)
    #print("after completing the json")
    #data_json = json.dumps(data)
    #print(data_json)

    #db_cm.remove()
    db_cm.insert(data)
    # inserting the as a dictionary where key is name of file and value is file as a document: into the mongoDB


if __name__ == "__main__":
    #filepath ="" 
    fileName = "SampleFile.csv"
    read_CSVfile_and_store(fileName)

