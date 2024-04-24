# mongo_connection.py
from pymongo import MongoClient

from sadif.config_loader import ConfigLoader


class MongoDBConnection:
    def __init__(self):
        config_instance = ConfigLoader()
        self.mongo_config = config_instance
        self.client = None

    def connect(self):
        print(self.mongo_config.get("mongodb_url"))
        if self.client is None:
            self.client = MongoClient(self.mongo_config.get("mongodb_url"))
        return self.client

    def get_database(self, db_name):
        if self.client is None:
            self.connect()
        return self.client[db_name]
