# 7b - Sender.py  - opgave: udvid til 8 key's ved at kombinere p0,1 og 2
# Sender 3 værdier for hhv pin 0, 1 og 2 på radio - Version 1.0 18-Nov-2020
# Først importeres det generelle microbit bibliotek (for at læse on pin 0-3 is_touched()) og vise på display
# samt radio for at  kunne sende værdierne på radio.
from microbit import *
import radio

display.show("7b-S")              # Udskriver en tekst på display for at identificere MB når der kommer strøm på 
sleep(1000)                       # Venter 1 sekund for inden vi går videre for at besked kan ses færdig.

radio.on()
radio.config(channel=80)          # hvis kanal angives skal det være samme kanal i både sender og modtager
                                  # Hvis kanal ikke angives er default kanal nr 7 i begge
while True:
    p0 = pin0.is_touched()
    p1 = pin1.is_touched()
    p2 = pin2.is_touched()
    if p0:
        key = "1"
    elif p1:
        key = "2"
    elif p2:
        key = "4"
    else:
        key = "0"

    radio.send(key)               # radio.send() funktionen sender og det er key så ingen grund til konvertering
    display.show(key)             # viser key på MBs display
    sleep(50)                     # Bør bruge samme værdi i både sender og modtager. Samme takt.