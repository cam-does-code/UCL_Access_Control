from time import sleep
from RPi import GPIO
from mfrc522 import SimpleMFRC522
from pymongo import MongoClient
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import datetime

GPIO.setmode(GPIO.BOARD)

RST = 36
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()
# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Load default font.
#font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype('Roboto-BoldCondensed.ttf', 27)

monogodb_URL = "mongodb+srv://admin:admin@clusterfms.pbcxras.mongodb.net/?retryWrites=true&w=majority"
reader = SimpleMFRC522()

client = MongoClient(monogodb_URL)
db = client.get_database("harald")
col_users = db.get_collection('users')

dblist = client.list_database_names()
if "harald" in dblist:
  print("The database exists.")

fornavn = "test"
efternavn = "testesen"

try:
    while True:
        print("Placer dit id kort på læseren")
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        draw.text((x, top+0),  "Scan", font=font, fill=255)
        draw.text((x, top+30), "Nyt Kort", font=font, fill=255)
        disp.image(image)
        disp.display()
        id, text = reader.read()
        print("ID:" + str(id))
        data = {"id": str(id),"fornavn": fornavn,"efternavn": efternavn, "timestamp":datetime.datetime.now()}
        y = col_users.insert_one(data)
        print(y.inserted_id)
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        draw.text((x, top+0),  "Bruger", font=font, fill=255)
        draw.text((x, top+30), "Oprettet", font=font, fill=255)
        disp.image(image)
        disp.display()
        sleep(5)
                
except KeyboardInterrupt:
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.text((x, top+24),       "Stoppet", font=font, fill=255)
    disp.image(image)
    disp.display()
    GPIO.cleanup()