
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import dotenv
import os
import logging

dotenv.load_dotenv()
logger = logging.getLogger(__name__)



class InitializeMongoDB:
    def __init__(self,url,db_name):
        self.url = url
        self.db = None
        self.client = MongoClient(self.url, server_api=ServerApi('1'))


        try:
            self.client.admin.command('ping')
            logger.info("Successfully initialize the database")
            self.db = self.client[db_name]

        except Exception as e:
            logger.error(e)
        
    
    def get_collection(self,collection_name):
        if self.db is None:
            logger.error("Database not initialized. Please check the connection.")
            return None
        return self.db[collection_name]
        




if __name__=="__main__":
    url = os.getenv("MONGO_DB_URL")
    db = InitializeMongoDB(url,"Cluster0")