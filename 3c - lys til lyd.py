# 3c - lys til lyd.py
# Konvertering af lys intensitet til lyd (pitch) Version 1.1 10-Nov-2020
# Importer de nødvendige biblioteker/moduler.
# Den generelle microbit for at nå display.read_light_level() fundktionen
# og music for at nå music.pitch() funktionen
from microbit import *
import music

# Lys niveau kan have værdier mellem 0 og 255
# pitch kan håndtere værdier mellem 0 og 3906Hz. Vi kan høre fra ca. 50Hz.
# - derfor lys niveau*14+50 som 'fornuftig' frekvens til pitch funktionen
while True:
    x = display.read_light_level()
    music.pitch(x*14+50)
    print(x)
    sleep(100)