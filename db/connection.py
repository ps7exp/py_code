import os
import pymongo
from configuration.config import *

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT_DIR, '../database.yml')

config = Config.load_config(CONFIG_PATH)
db_config = config['development']


class Connection:

    @staticmethod
    def connect():
        host = db_config['host']
        db_name = db_config['database']
        db_url = "mongodb://%s:%s/" %(host, 27017,)
        client = pymongo.MongoClient(db_url)
        db = client[db_name]
        try:
            db.command("serverStatus")
        except Exception as e:
            print(e)
        else:
            print("Database connected!")

        return db