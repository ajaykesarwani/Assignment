"""
"""
from pymongo import MongoClient


class MongoDB(Database):
    """
    """
    def __init__(self, uri, dataBase):
        self.connection = MongoClient(uri)
        self.db = conn.database  # replace with actual db
        self.collection = db.collection

    
    def update(self, document):
        """
        """
        self.db.update(document)
