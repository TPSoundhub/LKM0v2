# 6dM - sende styrke test.py
# Modtager til radio sende styrke eksperiment/test. Version 1.0 18-Nov-2020
# Giver et kort lydsignal samt udskriver "Heart beat" i shell og viser et hjerte i MB display, hvis den modtager noget
# Hvis der ikke modtages noget udskriver den "None" i shell.
# importer de funktonaliteter der skal bruges - her både music og radio udover det generelle MB bibliotek

from microbit import *
import radio
import music

# Sæt radio op til at kommunikere på bestemt kanal - her 10 og tænd for radio så MB kan sende/modtage
radio.config(channel=80)   # Brug kanal som I har til den enkelte gruppe!
radio.on()

# For at identificere MB som hørende til opgave 6d - modtager delen!
# Den er ikke på nogen måde afgørende for testen af modtagelse af 'signal' på radio.
display.show("6d-M")
sleep(1000)          # Venter 1 sekund

while True:
    heart_beat = radio.receive()
    if heart_beat:                # Det samme som "heart_beat != None" - Betingelse "noget modtaget" vs "ingenting modtaget"
        music.pitch(440,20)       # Lyd i 20 ms med frekvens 440 når signal modtaget
        print("heart beat")       # teksten "heart beat" i shell når radio signal er modtaget
        display.show(Image.HEART) # Hjerte vises i display på MB
    else:
        print("None")             # Tekst "None" i shell når radio signal IKKE er modtaget
        music.stop()              # Clear pin setting på music når signal ikke modtages. Har her ikke stor effekt
        display.clear()           # Clear lokal display
    sleep(100)                  # Pause på 100 ms - hvis den samme pause er i sender delen så kan de følges ad
                                # og er sender og modtager 'helt' tæt på hinanden kommer der ingen 'Nones' i modtager.
                                # Er de langt nok fra hinanden kommer der kun 'None' retur fra kaldet til radio.receive().
                                # Det er naturligvis også tilfældet hvis der ikke er nogen sender på kanalen (slukket).