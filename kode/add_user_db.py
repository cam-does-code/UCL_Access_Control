from time import sleep
from RPi import GPIO
from mfrc522 import SimpleMFRC522
from pymongo import MongoClient
import datetime

monogodb_URL = "mongodb+srv://admin:admin@clusterfms.pbcxras.mongodb.net/?retryWrites=true&w=majority"
reader = SimpleMFRC522()

client = MongoClient(monogodb_URL)
db = client.get_database("harald")
col_users = db.get_collection('users')

dblist = client.list_database_names()
if "harald" in dblist:
  print("The database exists.")

# collist = db.list_collection_names()
# if "access" in collist:
#   print("The collection exists.")

# data = {     
#     "id": str(id),
#     "timestamp":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  
#     }

fornavn = "test"
efternavn = "testesen"

try:
    while True:
        print("Placer dit id kort på læseren")
        id, text = reader.read()
        print("ID:" + str(id))
        data = {"id": str(id),"fornavn": fornavn,"efternavn": efternavn, "timestamp":datetime.datetime.now()}
        x = col_users.insert_one(data)
        print(x.inserted_id)
        sleep(5)
                
except KeyboardInterrupt:
    GPIO.cleanup()