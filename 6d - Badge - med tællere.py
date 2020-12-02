# 6d-Badge - med tællere og sender.py
# 6d modtager lavet med tællere (nof_heart_beats og nof nones). Version 1.1 02-Dec-2020
# Desuden indsat radio send hvergang der testes for modtaget signal. Sendestyrke sat til 0. (svagest)
# Dermed er det en første forbedring på vej mod en corana badge løsning.
# 
# importer de funktonaliteter der skal bruges - her både music og radio udover det generelle MB bibliotek
from microbit import *
import radio
import music
#
# Sæt radio op til at kommunikere på bestemt kanal - her 80 og tænd for radio så MB kan sende/modtage
radio.config(channel=80,power=0)   # Brug kanal som I har til den enkelte gruppe!
radio.on()

# For at identificere MB som hørende til opgave 6d - men med første forbedring mod en corona badge
display.show("6d-Badge")
sleep(1000)          # Venter 1 sekund

nof_heart_beats = 0
nof_nones = 0

while True:
    radio.send("Heart beat")
    heart_beat = radio.receive()
    if heart_beat:                    # Det samme som "heart_beat != None" - Betingelse "noget modtaget" vs "ingenting modtaget"
        nof_heart_beats = nof_heart_beats + 1   # Antal gange heart beat er modtaget i træk tælles een op.
        nof_nones = 0                 # reset tæller for antal nones i træk - dvs antal gange i træk der IKKE er modtaget noget.
    else:                             # ingenting modtaget
        nof_heart_beats = 0           # reset tæller for antal heart beats i træk
        nof_nones = nof_nones + 1     # antal gange der ikke er modtaget noget i træk tælles een op.
    sleep(100)                        # Pause på 100 ms - hvis den samme pause er i sender delen så kan de følges ad
    
    if nof_heart_beats > 7:           # Mere end 7 heart beats modtaget i træk - det vil vi sige er tæt på
        music.pitch(440,20)           # Lyd i 20 ms med frekvens 440 når signal modtaget - Hvad er en passende alarm lyd for "for tæt på"
        print("8*heart beat i streg") # test udskrift "8*heart beat i streg" i shell når radio signal er modtaget 8 gange i træk
        display.show(Image.HEART)     # Hjerte vises i display på MB - Hvad vil være passende som advarsel/alrm signal?
        nof_heart_beats = 0           # reset tæller for antal heart beats i træk
    if nof_nones > 3:                 # Mere end 3 nones i træk - det vil vi sige betyder der er langt nok i mellem
        print("4*None i streg")       # Tekst "4*None i streg" i shell når radio signal IKKE er modtaget 4 gange i træk
        music.stop()                  # Clear pin setting på music når signal ikke modtages. Har her ikke stor effekt
        display.clear()               # Clear lokal display - skal der være en indikator på at alt er ok - IKKE for tæt på længere?
        nof_nones = 0                 # reset tæller for antal nones i træk - dvs antal gange i træk der IKKE er modtaget noget.
                                      # for at den ikke skal løbe løbsk...

