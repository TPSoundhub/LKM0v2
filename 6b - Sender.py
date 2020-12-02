# 6b - Sender.py
# Accelerometer data fra x-akse sendt på radio som tekst - Version 1.0 18-Nov-2020
# Først importeres det generelle microbit bibliotek (for at læse accelerometer værdier)
# samt radio for at  kunne sende værdierne på radio.
from microbit import *
import radio

display.show("6b-S")              # Udskriver en tekst på display for at identificere MB når der kommer strøm på 

radio.on()
radio.config(channel=60)          # hvis kanal angives skal det være samme kanal i både sender og modtager
                                  # Hvis kanal ikke angives er default kanal nr 7 i begge
while True:
    acc_x,acc_y,acc_z = accelerometer.get_values()   
    f_num = acc_x+1000            # adderer 1000 for at få de fleste værdier positive - se modtager..
    print(f_num,"  ",type(f_num)) # test udskrift for at vise hvad vi har fået fra funktionskaldet til accelerometeret
    radio.send(str(f_num))        # radio.send() funktionen sender tekst strenge så tal f_num skal konverteres
    sleep(50)                     # Bør bruge samme værdi i både sender og modtager. Samme takt.