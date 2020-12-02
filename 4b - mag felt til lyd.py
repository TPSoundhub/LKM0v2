# 4b - mag felt til lyd.py
# Omsæt magnet felt styrke til lyd (pitch) Version 1.1  0-nov-2020
# Først importeres det generelle microbit bibliotek (for at nå compass() funktionen)
# og music (for at nå music.pitch() funktionen)
from microbit import *
import music

# Da felt styrken ser ud til at kunne nå op til ca. 2.5 mill og altid er positiv
# divideres med 1000 for at ramme indenfor det som pitch kan håndtere.
# MEN skal desuden få det til at være et heltal og ved normal division (/) får vi decimaler.
# - derfor bruges funktionen int() til at konvertere til heltal.
# Adderer 50 til for at vi kan høre det.
while True:
    x = compass.get_field_strength()
    print(x)
    music.pitch(int(x/1000)+50)      # Kan også bruge floor division // - Se python aritmetiske operatorer
    sleep(100)