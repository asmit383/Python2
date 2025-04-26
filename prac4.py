from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.4.2")
db = client["aiml"]
collection = db["student"]


for doc in collection.find({"Score": {"$gt": 80}}):
    print(doc)

client.close()
