from pymongo import MongoClient
client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.4.2")
print("Databases:", client.list_database_names())
db = client["aiml"]
print("Collections in 'mydatabase':", db.list_collection_names())
collection = db["student"]
for doc in collection.find({"Score": {"$gt": 70}}):
    print(doc)
    
    
client.close()
