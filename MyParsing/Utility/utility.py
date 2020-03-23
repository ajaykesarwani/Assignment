"""


"""
import json

import pymongo
from DB.MongoDB import MongoDB


class utility:
    """
    """

    def __init__(self):
        print 'inside init of utility'

    def readDB(self, uri):
        # read data from mongodb
        print "inside readDB"

        try:
            uri = ""
            db = MongoDB(uri, "mylib")  # pymongo.MongoClient('localhost', 27017)
            print "Connected Successfully!!!"
        except:
            print "Could not connect to MongoDB"
        # database
        # db_cm.remove()
        data = db.get()
        print "data type"
        print type(data)
        print 'data fetched successfully'
        response = []
        for doc in data:
            # print doc
            response.append(doc)

        print type(response)
        return json.dumps(response)


    def storeDB(self, data, uri):
        # store data into mongodb
        print 'inside storeDB'
        document = json.loads(data)

        try:
            db = MongoDB(uri, "mylib")  # pymongo.MongoClient('localhost', 27017)
            print "Connected Successfully!!!"
        except:
            print "Could not connect to MongoDB"
        # database
        # db_cm.remove()
        db.insert(document)
        print " Data is successfully stored in DB"
