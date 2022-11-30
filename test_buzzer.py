import machine
from machine import Pin, PWM
import time
from time import sleep

def play():
    tempo = 2
    tones = {
        'c': 262,
        'd': 294,
        'e': 330,
        'f': 349,
        'g': 392,
        'a': 440,
        'b': 494,
        'C': 523,
        ' ': 0,
        }

    pin= Pin(27, Pin.OUT)
    beeper = PWM(pin, duty=100)
    melody = 'cdefgab'
    rhythm = [4, 4, 4, 4, 4, 4, 4]

    for tone, length in zip(melody, rhythm):
        beeper.freq(tones[tone])
        sleep(tempo/length)
        
    beeper.deinit()