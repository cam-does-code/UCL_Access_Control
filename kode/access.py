from pymongo import MongoClient
from time import sleep
from RPi import GPIO
from reader import kort
import datetime

monogodb_URL = "mongodb+srv://admin:admin@clusterfms.pbcxras.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(monogodb_URL)
db = client.get_database("harald")
collection = db.get_collection('access')

def access_ok():
    LED_Green = 18
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED_Green,GPIO.OUT)
    GPIO.output(LED_Green, GPIO.HIGH)
    print("Godkendt. Velkommen")
    data = {"id": kort,"timestamp":datetime.datetime.now()}
    x = collection.insert_one(data)
    print(x.inserted_id)
    sleep(5)
    GPIO.output(LED_Green, GPIO.LOW)
    GPIO.cleanup()


def access_denied():
    LED_Red = 16
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED_Red,GPIO.OUT)
    GPIO.output(LED_Red, GPIO.HIGH)
    print("Ukendt Kort! Ingen adgang!")
    sleep(5)
    GPIO.output(LED_Red, GPIO.LOW)
    GPIO.cleanup()                    


