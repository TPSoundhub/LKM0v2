# 7b - Modtager.py
# Forventer at modtage en værdi for een tast 1-7 og 0 for ingen tast. - Version 1.0 18-Nov-2020
# For hver af de 7 taster spilles een bestemt tone. Modtages 0 stoppes tone
# Import af de biblioteker der er brug for
from microbit import *
import music
import radio

display.show("7b-M")                 # Udskriver på MB display for at identificere
sleep(1000)

radio.on()
radio.config(channel=60)             # Hvis kanal angives skal det være samme kanal i både sender og modtager
                                     # Hvis kanal ikke angives er default 7 i begge.
nof_nones = 0

while True:
    key_str = radio.receive()
    if key_str:                      # noget modtaget
        nof_nones = 0
        print(key_str)
        if   key_str=="1":
            music.pitch(440)         # A4 - kammertonen.
        elif key_str=="2":
            music.pitch(493)         # B4
        elif key_str=="3":
            music.pitch(523)         # C5
        elif key_str=="4":
            music.pitch(587)         # D5
        elif key_str=="5":
            music.pitch(659)         # E5
        elif key_str=="6":
            music.pitch(698)         # F5
        elif key_str=="7":
            music.pitch(783)         # G5
        elif key_str=="0":
            music.stop()
    else: nof_nones = nof_nones+1
    if nof_nones > 20 :           # sender er slukket eller udenfor rækkevidde. Stop og reset.
        music.stop()              
        music.reset()
        print("Ikke modtaget noget længe")
        nof_nones = 0
    sleep(50)