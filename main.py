from machine import Pin, PWM, Timer, TouchPad
from time import sleep_ms, sleep
import time, utime
import musiques
import test_buzzer

# 18h allumage des les clignotantes
# 22h extinction des leds clignotantes
# jouer des champs de Noel à heure précise
# ok allumage/extinction des leds clignontantes à la demande par appui sur bouton sensitif


def musique():
    test_buzzer.play()
    #musiques.play_musique()


#def button_push(p):
    #allumage_aleatoire = True
    #led_aleatoire.value(0)
    #print("boutton appuyé")
    #musique()
    #return allumage_aleatoire
    

def handleInterrupt(timer):
    #print("valeur boutton :", button.value())
    #led_aleatoire.value(1)
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
#button = Pin(33, Pin.IN, Pin.OPEN_DRAIN)
buzzer = PWM(Pin(27, Pin.OUT))
buzzer.init(duty=0)
timer = Timer(0)
#allumage_aleatoire = not button

#button.irq(trigger = Pin.IRQ_FALLING, handler=button_push)
timer.init(period=3000, mode=Timer.PERIODIC, callback=handleInterrupt)
