from time import sleep
import sys
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()

try:
    while True:
        print("Placer dit id kort på læseren")
        id, text = reader.read()
        print("ID:" + str(id))
        if id == 19962016327:
            print("Godkendt. Velkommen")
        else:
            print("Ukendt Kort! Ingen adgang!")
        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()