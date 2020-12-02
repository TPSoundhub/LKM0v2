# badge ex.py
# Et eksempel på hvordan badge kan laves. Version 1.1 01-dec-2020
# Tilpas funktionalitet som I vil have den. Andre lyde og billeder. Evt anden værdi for TÆRSKEL
#
# Først import af nødvendige moduler:
#
from microbit import *
import radio
import music

# Sæt radio op til at kommunikere på bestemt kanal - og tænd for radio så MB kan sende/modtage
radio.config(channel=80,power=0)   # Brug kanal som I har til den enkelte gruppe og sæt power til
radio.on()                         # svageste sendestyrke med power = 0. Tænd for radio'en
#
# Antal omgange i een trigger undersøgelses periode, samt tærskel værdi for at sige nogen er tæt på.
#
ANTAL_OMGANGE = 20
TÆRSKEL       = 14  # Det antal ud af ANTAL_OMGANGE som bruges til at sige der er nu kommet post nok til at sige der er nogen nærved
#
# Tilstande
ALARM = 0
OK    = 1
tilstand = OK # initielt er vi i OK tilstand.
#
# Trigger funktion, der returnerer True hvis der er nogen for tæt på (nærved). Og som udsender heart beat
# Tilpas koden så det passer bedst muligt med afstandskravet ved at justere TÆRSKEL værdi.
# Betingelsen er 'bare' at der er modtaget mere end TÆRSKEL 'heart_beats' (post i postkassen)
# ud af det antal gange der checkes post (ANTAL_OMGANGE). 
#
def trigger():
    nof_heart_beats = 0
    for x in range(0,ANTAL_OMGANGE):
        sleep(100)
        radio.send("Heart beat")                  # Hver gang vi checker for post sender vi post - for at have ens funktion i begge ender
        heart_beat = radio.receive()
        if heart_beat:                            # Det samme som "details != None" - Betingelse "noget modtaget" vs "ingenting modtaget"
            nof_heart_beats = nof_heart_beats + 1       
    print("Antal heart beats: ",nof_heart_beats," Antal omgange: ",ANTAL_OMGANGE)  # test udskrift som kan fjernes i endeligt produkt!!
    if nof_heart_beats>TÆRSKEL:  
        t = True  # Tæt på
    else:
        t = False # Langt nok fra
    return t
 
def lav_alarm():
    # tilpas med lyd og billed/animation i MicroBit display som I synes det skal være
    # Test udskrift - som kan fjernes i endeligt produkt
    print("Nu er der alarm - Der er een som er kommet for tæt på")
    # Her vises sur smiley og en et lille beep med høj frekvens, som kører i baggrund
    display.show(Image.SAD)
    music.pitch(1000,500,wait=False)
    
def gentag_alarm():
    # tilpas med lyd og billed/animation i MicroBit display som I synes det skal være.
    # Test udskrift - som kan fjernes i endeligt produkt
    print("Der er fortsat een for tæt på - Hvad skal vi gøre for at få vedkommende til at tage afstand?")
    # Her laver vi bare et lille beep med høj frekvens, og til at køre i baggrund
    music.pitch(3000,500,wait=False)       
    
def stop_alarm():
    # tilpas med lyd og billed/animation i MicroBit display som I synes det skal være.
    # Test udskrift - som kan fjernes i endeligt produkt
    print("Den der var for tæt på er nu kommet på afstand - Skal vi give positiv kvittering og hvad er det? Hvad duer?")
    # Her cleares display og evt lyd stoppes
    display.clear()
    music.stop()

def alt_ok():
    # tilpas med lyd og billed/animation i MicroBit display som I synes det skal være.
    # Test udskrift - som kan fjernes i endeligt produkt
    print("Alt OK ingen for tæt på - Skal der være noget som indikerer at badge er i live?")
    # Her sætter vi midterste pixel til lav intensitet.
    display.set_pixel(2,2,3)         

#
# Hoved program løkke

while True:
    nærved = trigger()
    if nærved and tilstand == OK:
        lav_alarm()
        tilstand = ALARM
    elif nærved and tilstand == ALARM:
        gentag_alarm()
    elif not nærved and tilstand == ALARM:
        stop_alarm()
        tilstand = OK
    else:                                   # den sidste af mulighederne "not nærved and tilstand == OK" 
        alt_ok()
