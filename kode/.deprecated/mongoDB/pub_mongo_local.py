from pymongo import MongoClient
import datetime

client = MongoClient("localhost", 27017)
db = client.get_database("harald")
collection = db.get_collection('users')

dblist = client.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")

collist = db.list_collection_names()
if "customers" in collist:
  print("The collection exists.")

data = {     
    "id": "xxxxxxxx",
    "fornavn": "Harald",
    "efternavn": "Haraldsen",
    "timestamp":datetime.datetime.now(),  
    }


x = collection.insert_one(data)

print(x.inserted_id)