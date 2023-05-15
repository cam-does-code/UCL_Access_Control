from connect_db import user_lookup, ok
from reader import read
from main import camera, face_auth
from access import access_ok, access_denied
import time

import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

RST = 3
state = 1
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
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
font = ImageFont.load_default()

try:
    while True:
        if state == 1: # Scanner kortet
            draw.text((x, top),       "Scan Kort", font=font, fill=255)
            print('state 1')
            read()
            state = 2
        if state == 2: # Kontrollere om det scannede kort findes i brugerdatabasen
            print('state 2')
            user_lookup()
            x = ok.get('access') 
            draw.text((x, top),       "Kort Godkendt", font=font, fill=255)
            if x == 1: # Hvis den retunerede værdi er 1, findes ID-kortet i DB og ansigtskendelsen startes.
                state = 3
            elif x == 0: # Hvis værdien er = 0, findes ID-kortet ikke og brugeren afvises.
                state = 5
        if state == 3: # Starter kameraet og ansigtsgenkendelsen
            print('state 3')
            draw.text((x, top),       "Scanner Ansigt", font=font, fill=255)
            camera()
            auth = face_auth.get('auth')
            print(auth)
            if auth == 1: # Ansigt genkendt. 
                state = 4
            elif auth == 0: # Hvis det korrekte ansigt ikke er genkendt inden for 10 sekunder, nægtes adgangen.
                state = 5
        if state == 4: # Brugeren er genkendt og der gives adgang til datacenteret. Adgangen registreres i databasen.
            print('state 4')
            draw.text((x, top),       "Godkendt", font=font, fill=255)
            access_ok()
            state = 1
        if state == 5:# Brugeren blev ikke genkendt, adgang afvises.
            print('state 5')
            draw.text((x, top),       "Afvist", font=font, fill=255)
            access_denied()
            state = 1
except KeyboardInterrupt:
    print(' Stop!')
    draw.text((x, top),       "Annulleret", font=font, fill=255)