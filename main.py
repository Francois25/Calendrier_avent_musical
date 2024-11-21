from machine import Pin, PWM, Timer, TouchPad
from time import sleep_ms, sleep
from musiques import liste_music
import time, utime, ntptime
import musiques
import random
import wificonnect
import config

# allumage des leds à la demande --> ok
# 18h00 allumage des les clignotantes --> ok
# 22h extinction des leds clignotantes --> ok
# jouer des champs de Noel à la demande --> ok
# jouer des champts de Noel à heure précise --> ok
# allumage de la led du jour pour trouver le cadeau par appui sur bouton --> ok

ipaddress = wificonnect.connectSTA(ssid=config.ssid, password=config.password)
time.sleep(3)

TOUCH_CONFIG = 600
TOUCHE_ACTIVATION = 300
START_HOUR = 18
STOP_HOUR = 21
MUSIC_HOUR_MIN = 17
MUSIC_HOUR_MAX = 20

touch_music = TouchPad(Pin(2))
touch_music.config(TOUCH_CONFIG)

touch_OnOff = TouchPad(Pin(15))
touch_OnOff.config(TOUCH_CONFIG)

led_aleatoire = Pin(21, Pin.OUT, 0)
buzzer = PWM(Pin(27, Pin.OUT))
buzzer.init(duty=0)
timer = Timer(0)

# Recuperation de la date et heure via le réseau wifi
try:
    ntptime.settime()
    print("Connecté au serveur NTP")
    print("Heure locale: ", utime.localtime())
    time.sleep(1)
except:
    print("Connection au serveur NTP échouée !!")
    buzzer.duty(50)


def musique():
    choix = musiques.random.choice(tuple(liste_music.values()))
    musiques.play(choix[0], choix[1], choix[2])

def allumage_demande():
    # allumer ou éteindre l'éclairage aléatoire manuellement
    if touch_OnOff.read() <= TOUCHE_ACTIVATION and led_aleatoire.value() == 1:
        led_aleatoire.value(0)
        print('eclairage eteint')
    elif touch_OnOff.read() <= TOUCHE_ACTIVATION and led_aleatoire.value() == 0:
        led_aleatoire.value(1)
        print('eclairage allumé')
    else:
        return

def handleInterrupt(timer):
    date_jour = utime.localtime()
    decalage_UTC = 1
    heure = date_jour[3] + decalage_UTC
    minute = date_jour[4]
    jour = date_jour[2]
    mois = date_jour[1]
    annee = date_jour[0]
    print(f"jour : {jour}/{mois}/{annee} - Heure : {heure}:{minute}")
    print(f"Mesure touch :\nmusic: {touch_music.read()}\nOn - Off: {touch_OnOff.read()}")
    print("etat eclairage : ", led_aleatoire.value())
    print(jour, "/", heure, ":",minute)

    # jouer une musique par appui bouton sensitif 
    if touch_music.read() <= TOUCHE_ACTIVATION:
        musique()

    # Avant Noël
    if jour < 25:
        print("configuration : Avant Noël")
        # jouer une musique toutes les heures dans un creneau défini MUSIC_HOUR_MIN et MUSIC_HOUR_MAX
        heure_musique = MUSIC_HOUR_MIN
        minute_musique = 30
        if (heure == heure_musique and minute == minute_musique) and (MUSIC_HOUR_MIN <= heure < MUSIC_HOUR_MAX):
            musique()
            heure_musique += 1
            print("heure prochaine musique auto : ", heure_musique)
            time.sleep(50)
        if heure_musique > MUSIC_HOUR_MAX:
            heure_musique = MUSIC_HOUR_MIN
        
        # alumage aléatoire auto
        if (START_HOUR <= heure < STOP_HOUR) and led_aleatoire.value() == 0:
            led_aleatoire.value(1)
            return
        elif heure >= STOP_HOUR and led_aleatoire.value() == 1:
            led_aleatoire.value(0)
        else:
            allumage_demande()

    # Jour de Noël
    elif date_jour == 25:
        print("configuration : jour de Noël") 
        if 6 < heure < 17 and led_aleatoire.value() == 0:
            led_aleatoire.value(1)
            return
        else:
            allumage_demande()

    # Après Noël, allumage à la demande uniquement
    else:
        print("configuration : Après Noël")
        allumage_demande()


timer.init(period=1000, mode=Timer.PERIODIC, callback=handleInterrupt)