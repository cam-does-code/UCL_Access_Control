from connect_db import user_lookup, ok
from reader import read
from main import camera, face_auth
from access import access_ok, access_denied
from RPi import GPIO
from time import sleep

import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

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

# Default state.
state = 1

try:
    while True:
        if state == 1: # Scanner kortet
            draw.rectangle((0,0,width,height), outline=0, fill=0)
            draw.text((x, top+24),       "Scan Kort", font=font, fill=255)
            disp.image(image)
            disp.display()
            print('state 1')
            read()
            state = 2
        if state == 2: # Kontrollere om det scannede kort findes i brugerdatabasen
            print('state 2')
            user_lookup()
            x = ok.get('access') 
            draw.rectangle((0,0,width,height), outline=0, fill=0)
            draw.text((x, top+0),  "Kontrollerer", font=font, fill=255)
            draw.text((x, top+30), "ID", font=font, fill=255)
            disp.image(image)
            disp.display()
            sleep(3)
            if x == 1: # Hvis den retunerede værdi er 1, findes ID-kortet i DB og ansigtskendelsen startes.
                state = 3
            elif x == 0: # Hvis værdien er = 0, findes ID-kortet ikke og brugeren afvises.
                state = 5
        if state == 3: # Starter kameraet og ansigtsgenkendelsen
            print('state 3')
            draw.rectangle((0,0,width,height), outline=0, fill=0)
            draw.text((x, top+0),  "Scanner", font=font, fill=255)
            draw.text((x, top+30),"Ansigt", font=font, fill=255)
            disp.image(image)
            disp.display()
            camera()
            auth = face_auth.get('auth')
            print(auth)
            if auth == 1: # Ansigt genkendt. 
                state = 4
            elif auth == 0: # Hvis det korrekte ansigt ikke er genkendt inden for 10 sekunder, nægtes adgangen.
                state = 5
        if state == 4: # Brugeren er genkendt og der gives adgang til datacenteret. Adgangen registreres i databasen.
            print('state 4')
            draw.rectangle((0,0,width,height), outline=0, fill=0)
            draw.text((x, top+24),       "Godkendt", font=font, fill=255)
            disp.image(image)
            disp.display()
            access_ok()
            state = 1
        if state == 5:# Brugeren blev ikke genkendt, adgang afvises.
            print('state 5')
            draw.rectangle((0,0,width,height), outline=0, fill=0)
            draw.text((x, top+24),       "Afvist", font=font, fill=255)
            disp.image(image)
            disp.display()
            access_denied()
            state = 1
except KeyboardInterrupt:
    print(' Stop!')
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.text((x, top+24),       "Annulleret", font=font, fill=255)
    disp.image(image)
    disp.display()
    GPIO.cleanup() 