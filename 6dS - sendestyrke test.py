# 6dS - sendestyrke test.py
# Sender med forskellig sende styrke. Version 1.0 18-Nov-2020
# Sende styrken er initielt sat til 0, men kan ændres med tryk på knap a
# Den aktuelle sendestyrke vises i MicroBittens display.
from microbit import *
import radio

radio.on()                 # Tænd for radio
radio.config(channel=10)   # Sæt kanal (mellem 0 og 83 som ikke er brugt af andre).
                           # Brug det kanal nummer I er tildelt i gruppen i både sender og modtager!
p=0                        # Variabel til at holde sendestyrke
radio.config(power=p)      # Sæt sendestyrken. Værdi fra 0 til 7 med stigende sende styrke - initielt sat til 0 

display.show("6d-S")       # Viser hvilken opgave koden hører til i MB dispaly S for at vise det er sender delen.
sleep(1000)                # Venter et sekund, hvorefter den starter med at vise sendestyrken
display.show(str(p))

while True:
    radio.send(str(p))
    if button_a.is_pressed():   # Hvis knap er aktiveret tælles p een op og sende styrken ændres og udskrives på display.
        p=p+1
        if p>7: p=0
        radio.config(power=p)
        display.show(str(p))
    sleep(100)                  # Benyt samme værdi i både sender og modtager
                                # - Modtager har chancen for at modtage alle beskeder og hvis den ikke gør
                                #   er det sandsynligvis fordi modtager er for langt væk.
                                #   Dvs None i modtager indikerer at sender er for langt væk iforhold til sende styrke (eller slukket)
