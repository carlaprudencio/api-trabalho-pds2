import os
from pymongo import MongoClient

class Database:
    def __init__(self, uri):
        self.client = MongoClient(uri)
        self.db = self.client.get_default_database()

    def get_collection(self, collection_name):
        return self.db[collection_name]
