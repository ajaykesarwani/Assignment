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
        self.db =  self.connection[dataBase]# replace with actual db
        self.collection = 'mycollection'

    def connect_mongodb(self, *params):
        pass

    def get(self):
        """
        :return: data
        """
        return self.db['mycollection'].find()


    def insert(self, data):
        """
        """
        self.db['mycollection'].insert(data)
