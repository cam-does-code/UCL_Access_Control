from time import sleep
from RPi import GPIO
from mfrc522 import SimpleMFRC522
import os

reader = SimpleMFRC522()

try:
    while True:
        print("Placer dit id kort på læseren")
        id, text = reader.read()
        print("ID:" + str(id))
        if id == 19962016327:
            print("Godkendt. Velkommen")
            os.system('python3 pub_mongo.py')
        else:
            print("Ukendt Kort! Ingen adgang!")
        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()