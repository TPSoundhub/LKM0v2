from microbit import *

while True:
    x = compass.get_field_strength()
    print(x)
    sleep(100)