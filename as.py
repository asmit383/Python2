from pymongo import MongoClient
client=MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.4.2")
db=client["aiml"]
collection=db["test1"]
number=0
for x in collection.find():
    number+=1
    print(x)
print("NO of data",number)    
  
 
    
client.close()