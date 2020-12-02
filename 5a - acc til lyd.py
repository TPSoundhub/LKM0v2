# 5b - acc til lyd.py
# Omsæt accelerometerværdi i x-aksen til lyd (pitch) Version 1.0 12-Nov-2020
# Først importeres det generelle microbit bibliotek (for at nå accelerometer funktionen)
# og music (for at nå music.pitch() funktionen)
from microbit import *

# Bruger accelerometer.get_values() til at hente værdier i alle 3-akser, selvom
# programmet her kun bruger værdi i x-retningen. Dvs vip højre/venstre med knap a til venstre.
# Prøv med de andre akser for at blive fortrolig med dem.
#
while True:
    acc_x,acc_y,acc_z = accelerometer.get_values()
    print(acc_x)                                   
#    music.pitch(abs(acc_x))                       # den hurtige løsning
                                                   # - abs() laver neg til pos

    freq = acc_x+1500           # adderer tilstrækkelig stor værdi
    if freq>50 and freq<3907:   # tester at det er i området for at være sikker
        music.pitch(freq)
    sleep(50)