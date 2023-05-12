from pymongo import MongoClient
import datetime

monogodb_URL = "mongodb+srv://admin:admin@clusterfms.pbcxras.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(monogodb_URL)
db = client.get_database("harald")
collection = db.get_collection('users')

dblist = client.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")

collist = db.list_collection_names()
if "customers" in collist:
  print("The collection exists.")

data = {     
    "id": "19962016327",
    "fornavn": "Harald",
    "efternavn": "Haraldsen",
    "timestamp":datetime.datetime.now(),  
    }


x = collection.insert_one(data)

print(x.inserted_id)