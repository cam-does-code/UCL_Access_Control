from connect_db import user_lookup, ok
from reader import read
from main import camera
from access import access_ok, access_denied

state = 1

while True:
    if state == 1:
        print('state 1')
        read()
        state = 2
    if state == 2:
        print('state 2')
        user_lookup()
        x = ok.get('access')
        print(x)
        if x == 1:
            state = 3
        elif x == 0:
            state = 5
        exit
    if state == 3:
        print('state 3')
        camera()
        state = 4
    if state == 4:
        print('state 4')
        access_ok()
        state = 1
    if state == 5:
        print('state 5')
        access_denied()
        state = 1