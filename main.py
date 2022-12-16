import time, utime, ntptime
import musiques
import random
import wificonnect
import config
from machine import Pin, PWM, Timer, TouchPad
from time import sleep_ms, sleep
from musiques import liste_music
from datetime import datetime


# allumage des leds à la demande --> ok
# 18h00 allumage des les clignotantes
# 22h extinction des leds clignotantes
# jouer des champs de Noel à la demande --> ok
# jouer des champts de Noel à heure précise
# allumage de la led du jour pour trouver le cadeau par appui sur bouton --> ok

ipaddress = wificonnect.connectSTA(ssid=config.ssid, password=config.password)

try:
    ntptime.settime()
    print("Connecté au serveur NTP")
    print("Heure locale: ", utime.localtime())
except:
    print("Connection au serveur NTP échouée !!")

        
TOUCH_CONFIG = 600
TOUCHE_ACTIVATION = 300
touch_music = TouchPad(Pin(15))
touch_OnOff = TouchPad(Pin(2))
touch_music.config(TOUCH_CONFIG), touch_OnOff.config(TOUCH_CONFIG)

led_aleatoire = Pin(21, Pin.OUT, 0)
buzzer = PWM(Pin(27, Pin.OUT))
buzzer.init(duty=0)
timer = Timer(0)

date_jour = datetime.today()
print(date_jour)

def musique():
    choix = musiques.random.choice(tuple(liste_music.values()))
    musiques.play(choix[0], choix[1], choix[2])

def allumage_demande():
    # allumer ou éteindre l'éclairage aléatoire manuellement
    if touch_OnOff.read() <= TOUCHE_ACTIVATION and led_aleatoire.value() == 1:
        led_aleatoire.value(0)
    elif touch_OnOff.read() <= TOUCHE_ACTIVATION and led_aleatoire.value() == 0:
        led_aleatoire.value(1)
    else:
        pass

def handleInterrupt(timer):
    print(f"Mesure touch :\nmusic: {touch_music.read()}\nOn - Off: {touch_OnOff.read()}")
    # jouer une musique par appui bouton sensitif 
    if touch_music.read() <= TOUCHE_ACTIVATION:
        musique()

    # Avant Noël
    if date_jour.day < 25:
        # jouer une musique toutes les heures
        heure_musique = config.MUSIC_HOUR_MIN
        minute_musique = 30
        if (date_jour.hour == heure_musique and date_jour.minute == minute_musique) and config.MUSIC_HOUR_MIN < date_jour.hour < config.MUSIC_HOUR_MAX:
            musique()
            heure_musique += 1
            if heure_musique > 23:
                heure_musique = config.MUSIC_HOUR_MIN

        # alumage aléatoire auto
        if config.START_HOUR < date_jour.hour < config.STOP_HOUR and led_aleatoire.value() == 0:
            led_aleatoire.value(1)
        else:
            allumage_demande()

    # Jour de Noël
    elif date_jour == 25:
        if 6 < date_jour.hour < 17 and led_aleatoire.value() == 0:
            led_aleatoire.value(1)
        else:
            allumage_demande()

    # Après Noël, allumage à la demande uniquement
    else:
        allumage_demande()


        

timer.init(period=1000, mode=Timer.PERIODIC, callback=handleInterrupt)

