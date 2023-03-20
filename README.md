# Komponentliste
| Komponent                        | Formål | Antal | Pris | Link                                                         |
|----------------------------------|--------|-------|------|--------------------------------------------------------------|
| Raspberry Pi                     |        | 1     |      | https://www.raspberrypi.com/products/raspberry-pi-4-model-b/ |
| Raspberry Pi I/O Cable Extension |        | 1     |      |                                                              |
| Breadboard                       |        | 1     |      |                                                              |
| Kamera                           |        | 1     | 171  | https://dk.rs-online.com/web/p/raspberry-pi-kameraer/9132673 |
| RFID Sensor                      |        | 1     |      |                                                              |
| RFID Kort                        |        | 1     |      |                                                              |
| Lås                              |        | 1     |      |                                                              |
| 3D-Print Produktkasse            |        | 1     |      |                                                              |



# Current Ideas:

### Adgangskontrol

Et system til at sikre og registrere adgangen til datacentret. Personen der ønsker adgang skal scanne sit Id-kort, kombineret med en biometrisk bekræftelse i form af ansigtsgenkendelse eller fingeraftryk.
Når datacentret forlades, tjekker man igen ud med sit Id-kort. I en database logges både indgang og udgang.

 

### Temperaturstyring

Et system til at sikre en mere præcis overvågning og registrering af temperatur og luftfugtighed i et serverrack.
Der placeres fx 2 sensorer i hvert rack til måling. Data lagres i en online database og det undersøges om det er muligt at udveksle data med PLC styringen, så data kan aflæses på nuværende HMI.


Communication: Discord
File sharing: Gitlab/Discord
Meeting planning: 


### Links

https://www.raspberrypi.com/products/raspberry-pi-4-model-b/

https://raspberrypi.dk/en/shop/category/raspberry-pi-camera/
https://www.elektor.com/new/new-in-the-store/makerfabs-rc522-rfid-reader-with-cards-kit-13-56-mhz?srsltid=Ad5pg_F1xdY1Y62EhLhw9c3aEBhWYHOgw4rFzF9x8xDabeXx1c5VfY4ut54



import paho.mqtt.client as paho
broker="192.168.1.184"
port=1883
def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass
client1= paho.Client("control1")                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker,port)                                 #establish connection
ret= client1.publish("house/bulb1","on")

while True:
    client1.publish('sut min diller, harald')