from time import sleep
from RPi import GPIO
from mfrc522 import SimpleMFRC522
from pymongo import MongoClient
import datetime

monogodb_URL = "mongodb+srv://admin:admin@clusterfms.pbcxras.mongodb.net/?retryWrites=true&w=majority"
reader = SimpleMFRC522()

LED_Green = 18
LED_Red = 16
GPIO.setup(LED_Green,GPIO.OUT)
GPIO.setup(LED_Red,GPIO.OUT)

client = MongoClient(monogodb_URL)
db = client.get_database("harald")
collection = db.get_collection('access')
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

try:
    while True:
        print("Placer dit id kort på læseren")
        id, text = reader.read()
        print("ID:" + str(id))
        if col_users.find_one({"id": {"$eq": str(id)}}):
            GPIO.output(LED_Green, GPIO.HIGH)
            print("Godkendt. Velkommen")
            data = {"id": str(id),"timestamp":datetime.datetime.now()}
            x = collection.insert_one(data)
            print(x.inserted_id)
        else:
            GPIO.output(LED_Red, GPIO.HIGH)
            print("Ukendt Kort! Ingen adgang!")
        sleep(5)
        GPIO.output(LED_Green, GPIO.LOW)
        GPIO.output(LED_Red, GPIO.LOW)
                
except KeyboardInterrupt:
    GPIO.cleanup()