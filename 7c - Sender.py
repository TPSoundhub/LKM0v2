# 7c - Sender.py
# Sender 8 værdier for alle kombinationer af pin 0, 1 og 2 på radio - Version 1.1 25-Nov-2020
# Først importeres det generelle microbit bibliotek (for at læse om pin 0-3 is_touched()) og vise på display
# samt radio for at  kunne sende værdierne på radio.
from microbit import *
import radio

display.show("7c-S")              # Udskriver en tekst på display for at identificere MB når der kommer strøm på 
sleep(1000)                       # Venter 1 sekund for inden vi går videre for at besked kan ses færdig.
radio.on()
radio.config(channel=60)          # hvis kanal angives skal det være samme kanal i både sender og modtager
                                  # Hvis kanal ikke angives er default kanal nr 7 i begge
while True:
    p0 = pin0.is_touched()                # Læser et øjebliksbillede af pin 0,1 og 2 ind i variabler
    p1 = pin1.is_touched()                #         p0      p1      p2         Key
    p2 = pin2.is_touched()                #------------------------------------------------------
    if p0 and p1 and p2:                  #        True    True    True        "7"
        key = "7"                         #
    elif not p0 and p1 and p2:            #        False   True    True        "6"
        key = "6"                         #
    elif p0 and not p1 and p2:            #        True    False   True        "5"
        key = "5"                         #
    elif not p0 and not p1 and p2:        #        False   False   True        "4"
        key = "4"                         #
    elif p0 and p1 and not p2:            #        True    True    False       "3"
        key = "3"                         #
    elif not p0 and p1 and not p2:        #        False   True    False       "2"
        key = "2"                         #
    elif p0 and not p1 and not p2:        #        True    False   False       "1"
        key = "1"                         #
    else:                                 #        False   False   Fasle       "0"  sidste mulighed derfor bare else
        key = "0"
    radio.send(key)               # radio.send() funktionen sender og det er key så ingen grund til konvertering
    display.show(key)             # viser key på MBs display
    sleep(50)                     # Bør bruge samme værdi i både sender og modtager. Samme takt.