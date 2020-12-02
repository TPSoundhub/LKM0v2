# 6a - sender 1.py - enkelt besked til alle på default kanal med default sendestyrke
from microbit import *
import radio

radio.on()

while True:
    radio.send("Hej alle i 1x - Alt OK ? ")
    sleep(100)