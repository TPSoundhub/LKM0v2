from microbit import *

while True:
    x = display.read_light_level()
    print(x)
    sleep(100)