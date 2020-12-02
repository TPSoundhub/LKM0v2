# 2d - find pitch
from microbit import *
import music

for x in range(50,20000,100):    # første runde! Anden runde med range(3850,3950,1)!
    music.pitch(x)
    sleep(100)
    print(x)