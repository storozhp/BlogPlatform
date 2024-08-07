from pymongo import MongoClient
from dotenv import load_dotenv
from os import getenv


load_dotenv()

try:
    client = MongoClient(getenv("MONGO_URL"))
    database = client[getenv("DATABASE_NAME")]

    users_collection = database[getenv("USERS_COLLECTION")]
    posts_collection = database[getenv("POSTS_COLLECTION")]
except Exception as e:
    print(e)
