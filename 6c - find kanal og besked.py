# 6c - find kanal og besked
from microbit import *
import radio

radio.on()
# Trin 1: find kanal
#for x in range(0,83,1):
#    radio.config(channel=x)
#    f=radio.receive()
#    print("Channel: ",x," Modtaget besked: ",f)
#    sleep(100)                                  # vigtigt med samme timing som i sender!
                                                 # Er det nul kan den nå igennem alle
                                                 # inden der modtages noget. 100 ms er lang tid...

# Trin 2: find besked - Check den kanal ud I har fundet ... 
radio.config(channel=77)         # Trin 3 : når det ikke er på 77 er det så alligevel 76.. Prøv..
while True:
    f = radio.receive()
    print(f)
    sleep(100)
    
# Hvad er beskeden - Hvad er næste opgave