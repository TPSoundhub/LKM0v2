# 6b - Modtager.py
# Forventer at modtage en tal værdi fra radio som kan bruges til at lave en lyd. - Version 1.0 18-Nov-2020
# Vil IKKE virke hvis der modtages andet end et tal.
# Sikrer selv at værdi er mellem 50 og 3907 før den kalder music.pitch() med det tal der modtages
from microbit import *
import music
import radio

display.show("6b-M")                 # Udskriver på MB display for at identificere

radio.on()
radio.config(channel=60)             # Hvis kanal angives skal det være samme kanal i både sender og modtager
                                     # Hvis kanal ikke angives er default 7 i begge.
nof_nones = 0

while True:
    f_str = radio.receive()
    print(f_str,"  ",type(f_str))    # Test udskrift af hvad vi modtager i shell incl typen af det
    if f_str:                        # Det samme som "f_str != None:"  men IKKE som "f_str == True:"
        f_num = int(f_str)           # Men altså 'noget er modtaget' fra funktionen. Her en streng vi konverterer
        nof_nones = 0
        if (f_num>50) and (f_num<3907):
            music.pitch(f_num)
        else:
            music.stop()
    else: nof_nones = nof_nones+1
    if nof_nones > 20 : music.stop()
    sleep(50)