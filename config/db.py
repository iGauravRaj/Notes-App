from dotenv import load_dotenv
from os import getenv
from pymongo import MongoClient
load_dotenv()

mongo_uri = getenv("MONGODB_URI")

# Database Name: Notes
# Collection Name: Notes

conn = MongoClient(mongo_uri)