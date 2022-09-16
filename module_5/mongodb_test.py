"""System module."""

from pymongo import MongoClient
URL="mongodb+srv://admin:admin@cluster0.fwchebu.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(URL)
db = client.pytech
print("-- Pytech Collection List --")
print(db.list_collection_names())
