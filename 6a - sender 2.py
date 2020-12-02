# 6a - sender 2.py - Besked til alle med nr tilføjet så man kan se om alle kommer igennem
from microbit import *
import radio

radio.on()
besked_nr = 1

while True:
    radio.send("Hej alle i 1x - Alt OK ? "+ str(besked_nr))
    print(besked_nr)
    besked_nr = besked_nr+1
    if besked_nr>9:
        besked_nr = 1
    sleep(100)