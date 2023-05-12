from connect_db import user_lookup, ok
from reader import read
from main import camera, face_auth
from access import access_ok, access_denied

state = 1

try:
    while True:
        if state == 1: # Scanner kortet
            print('state 1')
            read()
            state = 2
        if state == 2: # Kontrollere om det scannede kort findes i brugerdatabasen
            print('state 2')
            user_lookup()
            x = ok.get('access') 
            print(x)
            if x == 1: # Hvis den retunerede værdi er 1, findes ID-kortet i DB og ansigtskendelsen startes.
                state = 3
            elif x == 0: # Hvis værdien er = 0, findes ID-kortet ikke og brugeren afvises.
                state = 5
        if state == 3: # Starter kameraet og ansigtsgenkendelsen
            print('state 3')
            camera()
            auth = face_auth.get('auth')
            print(auth)
            if auth == 1: # Ansigt genkendt. 
                state = 4
            elif auth == 0: # Hvis det korrekte ansigt ikke er genkendt inden for 10 sekunder, nægtes adgangen.
                state = 5
        if state == 4: # Brugeren er genkendt og der gives adgang til datacenteret. Adgangen registreres i databasen.
            print('state 4')
            access_ok()
            state = 1
        if state == 5:# Brugeren blev ikke genkendt, adgang afvises.
            print('state 5')
            access_denied()
            state = 1
except KeyboardInterrupt:
    print(' Stop!')