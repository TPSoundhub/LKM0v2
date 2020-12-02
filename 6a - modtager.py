# 6a modtager
from microbit import *
import radio

radio.on()

while True:
    besked = radio.receive()
    print(besked)
    sleep(100)