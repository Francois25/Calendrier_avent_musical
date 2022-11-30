from machine import Pin, PWM, Timer, TouchPad
from time import sleep_ms, sleep
import time, utime
import musiques
from musiques import liste_music
import random


# allumage des leds à la demande
# 18h00 allumage des les clignotantes
# 22h extinction des leds clignotantes
# jouer des champs de Noel à la demande
# jouer des champts de Noel à heure précise
# allumage de la led du jour pour trouver le présent par appui sur bouton

def musique():
    choix = musiques.random.choice(tuple(liste_music.values()))
    musiques.play(choix[0], choix[1], choix[2])


def handleInterrupt(timer):
    print(f"Mesure touch :\nmusic: {touch_music.read()}\nOn - Off: {touch_OnOff.read()}")
    if touch_music.read() <= TOUCHE_ACTIVATION:
        musique()
    if touch_OnOff.read() <= TOUCHE_ACTIVATION and led_aleatoire.value() == 1:
        led_aleatoire.value(0)
    elif touch_OnOff.read() <= TOUCHE_ACTIVATION and led_aleatoire.value() == 0:
        led_aleatoire.value(1)
        
        
TOUCH_CONFIG = 600
TOUCHE_ACTIVATION = 300
touch_music = TouchPad(Pin(15))
touch_OnOff = TouchPad(Pin(2))
touch_music.config(TOUCH_CONFIG), touch_OnOff.config(TOUCH_CONFIG)

led_aleatoire = Pin(21, Pin.OUT, 0)
buzzer = PWM(Pin(27, Pin.OUT))
buzzer.init(duty=0)
timer = Timer(0)

timer.init(period=3000, mode=Timer.PERIODIC, callback=handleInterrupt)

