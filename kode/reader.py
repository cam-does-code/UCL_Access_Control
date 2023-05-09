from RPi import GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
kort = {
    'id': 'null'
}

def read():
    print("Placer dit id kort på læseren")
    id, text = reader.read()
    print(id)
    print(text)
    kort['id'] = str(id)