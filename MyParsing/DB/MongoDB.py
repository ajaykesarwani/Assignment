"""
"""
#from pymongo import MongoClient
import pymongo
from DB.Database import Database
import json


class MongoDB(Database):
    """
    """

    def __init__(self, uri, dataBase):
        #self.connection = MongoClient()
        self.connection = pymongo.MongoClient('localhost',27017)
        self.db = dataBase # replace with actual db
        self.collection = 'mycollection'

    def connect_mongodb(self, *params):
        pass

    def insert(self, data):
        """
        """
        print type(data)
        document = json.loads(data)
        print "the type of document"
        print(type(document))
        #print document
        self.db.insert(document)
        print "insertion done successfully"