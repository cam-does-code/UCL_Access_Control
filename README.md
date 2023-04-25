# B2C Business
Projekt Harald V2.1 skal startes op i et ApS selskab. 
Årsagen til dette er, at ApS-selskabet kun kræver en opstarts indskydelse på Kr. 40.000, hvor et A/S kræver et indskud på Kr. 400.000.     
En anden fordel ved ApS’et er, at det ikke kræver en bestyrelse.    
Havde vi skulle oprette selskabet i 2020, så havde vi valgt et IVS, da opstarts indskydelsen kun var på Kr. 1.     
I 2021 valgte man dog, at lukke for selskabsformen IVS, og herefter skulle alle IVS selskaber omkonveteres til ApS’er.    

![OrgChart](https://cdn.discordapp.com/attachments/1084777803553177644/1099961159102238760/image.png "OrgChart")

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

Temperatursensor    
Fugtighedsmåler    
Adgangskontrol med kortlæser  

### Adgangskontrol

Et system til at sikre og registrere adgangen til datacentret. Personen der ønsker adgang skal scanne sit Id-kort, kombineret med en biometrisk bekræftelse i form af ansigtsgenkendelse eller fingeraftryk.
Når datacentret forlades, tjekker man igen ud med sit Id-kort. I en database logges både indgang og udgang.

 

### Temperaturstyring

Et system til at sikre en mere præcis overvågning og registrering af temperatur og luftfugtighed i et serverrack.
Der placeres fx 2 sensorer i hvert rack til måling. Data lagres i en online database og det undersøges om det er muligt at udveksle data med PLC styringen, så data kan aflæses på nuværende HMI.  


### Database:

Til uploading af temperatur     
Til uploading af fugtighed    
Til uploading af hvem som har brugt sit kort til at få adgang til datarum    



### Eventuelt: 

Strømovervågning    
Skræm/display til visning af temperatur i datarummet    
Alarm/notifikation failsafe    
Måling af temperatur i både top og bund af skabene.     
”Toiletlås” til dør  


Communication: Discord
File sharing: Gitlab/Discord
Meeting planning: 




