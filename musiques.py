import machine
from machine import Pin, PWM
import time
import random

pin = Pin(27, Pin.OUT)

# These are the notes with equivalent frequency
B0  = 31
C1  = 33
CS1 = 35
D1  = 37
DS1 = 39
E1  = 41
F1  = 44
FS1 = 46
G1  = 49
GS1 = 52
A1  = 55
AS1 = 58
B1  = 62
C2  = 65
CS2 = 69
D2  = 73
DS2 = 78
E2  = 82
F2  = 87
FS2 = 93
G2  = 98
GS2 = 104
A2  = 110
AS2 = 117
B2  = 123
C3  = 131
CS3 = 139
D3  = 147
DS3 = 156
E3  = 165
F3  = 175
FS3 = 185
G3  = 196
GS3 = 208
A3  = 220
AS3 = 233
B3  = 247
C4  = 262
CS4 = 277
D4  = 294
DS4 = 311
E4  = 330
F4  = 349
FS4 = 370
G4  = 392
GS4 = 415
A4  = 440
AS4 = 466
B4  = 494
C5  = 523
CS5 = 554
D5  = 587
DS5 = 622
E5  = 659
F5  = 698
FS5 = 740
G5  = 784
GS5 = 831
A5  = 880
AS5 = 932
B5  = 988
C6  = 1047
CS6 = 1109
D6  = 1175
DS6 = 1245
E6  = 1319
F6  = 1397
FS6 = 1480
G6  = 1568
GS6 = 1661
A6  = 1760
AS6 = 1865
B6  = 1976
C7  = 2093
CS7 = 2217
D7  = 2349
DS7 = 2489
E7  = 2637
F7  = 2794
FS7 = 2960
G7  = 3136
GS7 = 3322
A7  = 3520
AS7 = 3729
B7  = 3951
C8  = 4186
CS8 = 4435
D8  = 4699
DS8 = 4978
Z = 100000

def play(melodies, delays, duty):
    pwm = PWM(pin)
    pwm.duty_u16(32768)
    pwm.init(freq=5000, duty_ns=5000)

    for note in melodies:
        pwm.freq(note)
        pwm.duty(duty)
        time.sleep(delays)
    pwm.duty(0)
    pwm.deinit()

# This is the list of notes for mario theme
liste_music = {
    "mario" : [
        [E7, E7,  Z, E7,  Z, C7, E7,  Z,
        G7,  Z,  Z,  Z, G6,  Z,  Z,  Z,
        C7,  Z,  Z, G6,  Z,  Z, E6,  Z,
        Z, A6,  Z, B6,  Z,AS6, A6,  Z,
        G6, E7,  Z, G7, A7,  Z, F7, G7,
        Z, E7,  Z, C7, D7, B6,  Z,  Z,
        C7,  Z,  Z, G6,  Z,  Z, E6,  Z,
        Z, A6,  Z, B6,  Z,AS6, A6,  Z,
        G6, E7,  Z, G7, A7,  Z, F7, G7,
        Z, E7,  Z, C7, D7, B6,  Z,  Z,
        ], 0.15, 250],

# This is the list of notes for jingle, Jingle bells
    "jingle" : [
        [E7, E7, E7, Z,
        E7, E7, E7, Z,
        E7, G7, C7, D7, E7, Z,
        F7, F7, F7, F7, F7, E7, E7, E7, E7, D7, D7, E7, D7, Z, G7, Z,
        E7, E7, E7, Z,
        E7, E7, E7, Z,
        E7, G7, C7, D7, E7, Z,
        F7, F7, F7, F7, F7, E7, E7, E7, G7, G7, F7, D7, C7, Z 
        ], 0.25 , 512],

# This is the list of notes for Twinkle, Twinkle Little Star
    "twinkle" : [
        [C6, C6, G6, G6, A6, A6, G6, Z,
        F6, F6, E6, E6, D6, D6, C6, Z,
        G6, G6, F6, F6, E6, E6, D6, Z,
        G6, G6, F6, F6, E6, E6, D6, Z,
        C6, C6, G6, G6, A6, A6, G6, Z,
        F6, F6, E6, E6, D6, D6, C6, Z,
    ],0.6, 50],

# This is the list of notes for Jolly, Jolly Old St. Nicholas
    "jolly" : [
        [E6, Z, E6, Z, E6, Z, E6, Z, D6, Z, D6, Z, D6, D6, D6, Z,
        C6, Z, C6, Z, C6, Z, C6, Z, E6, E6, E6, Z, Z, Z, Z, Z,
        A5, Z, A5, Z, A5, Z, A5, Z, C5, Z, G5, Z, C5, C5, C5, Z,
        D6, C6, D6, E6, D6, D6, Z, Z, Z,
        E6, Z, E6, Z, E6, Z, E6, Z, D6, Z, D6, Z, D6, D6, D6, Z,
        C6, Z, C6, Z, C6, Z, C6, Z, E6, E6, E6, Z, Z, Z, Z, Z,
        A5, Z, A5, Z, A5, Z, A5, Z, C5, Z, G5, Z, C5, C5, C5, Z,
        D6, C6, D6, E6, C6, C6, C6, Z,
    ],0.12, 250],

# This is the list of notes for Wish, We wish you a merry Christmas
    "wish" : [
        [G5, Z, C6, Z, C6, D6, C6, B5, A5, Z, A5, Z, A5, Z,
        D6, Z, D6, E6, D6, C6, B5, Z, G5, Z, G5, Z,
        E6, Z, E6, F6, E6, D6, C6, Z, A5, Z, G5, Z,
        A5, A5, D6, D6, B5, B5, C6, C6, C6, Z,
        G5, Z, C6, Z, C6, D6, C6, B5, A5, Z, A5, Z, A5, Z,
        D6, Z, D6, E6, D6, C6, B5, Z, G5, Z, G5, Z,
        E6, Z, E6, F6, E6, D6, C6, Z, A5, Z, G5, Z, G5, Z,
        A5, A5, D6, D6, B5, B5, C6, C6, C6,
    ],0.2, 120],

# This is the list of notes for Vive, Vive le vent
    "vive" : [
        [E6, Z, E6, Z, E6, E6, E6, Z, E6, Z, E6, Z, E6, E6, E6, Z,
        E6, Z, G6, Z, C6, Z, D6, Z, E6, E6, E6, E6, Z, Z, Z, Z,
        F6, Z, F6, Z, F6, F6, F6, G6, E6, Z, E6, Z, E6, E6, E6,
        C6, D6, Z, D6, Z, D6, Z, E6, Z, D6, D6, Z, Z, G6, G6, G6, Z,
        E6, Z, E6, Z, E6, E6, E6, Z, E6, Z, E6, Z, E6, E6, E6, Z,
        E6, Z, G6, Z, C6, Z, D6, Z, E6, E6, E6, E6, Z, Z, Z, Z,
        F6, Z, F6, Z, F6, F6, F6, G6, E6, Z,  E6, Z, E6, E6, Z,
        E6, G6, Z, G6, Z, F6, Z, D6, Z, C6, C6, C6, Z,
    ],0.14, 250],

# This is the list of notes for Papa, Petit papa Noël
     "papa" : [
        [G5, G5, C6, Z, C6, Z, C6, Z, D6, Z, C6, C6, C6, C6, C6, Z,
        C6, D6, E6, Z, E6, Z, E6, Z, F6, Z, E6, E6, E6, E6, E6, Z,
        D6, D6, C6, C6, C6, Z, C6, C5, C6, B5, A5, G5, G5, G5, G5, Z,
        G5, C5, C6, C6, C6, C6, Z, C6, C5, B5, C5, D6, D6, D6, Z,
        G5, G5, C6, Z, C6, Z, C6, Z, D6, Z, C6, C6, C6, C6, C6, Z,
        C6, D6, E6, Z, E6, Z, E6, Z, F6, Z, E6, E6, E6, E6, E6, Z,
        D6, D6, C6, C6, C6, Z, C6, C5, C6, B5, A5, G5, G5, G5, G5, Z,
        G5, C5, C6, C6, C6, C6, Z, C6, C5, D6, D5, C6, C6, C6, C6, Z,
    ],0.20, 250],

# This is the list of notes for Sapin, Mon beau sapin
    "sapin" : [
        [G5, G5, C6, C5, C6, C6, C6, Z,
        D6, D6, E6, E5, E6, E6, E6, Z,
        E6, D6, E6, F5, F5, B5, B5, D6, D6, C6, C6, C6, Z,
        G5, G6, E6, A6, A6, A6, Z, G5, G6, F5, F5, F5, Z,
        G5, G6, D6, G6, G6, G6, Z, F5, F6, E6, E6, E6, Z,
        G5, G5, C6, C5, C6, C6, C6, Z,
        D6, D6, E6, E5, E6, E6, E6, Z,
        E6, D6, E6, F5, F5, B5, B5, D6, D6, D6, D6, C6, C6, C6, C6, C6, Z,
    ],0.30, 250],
    
# This is the list of notes for Douce, Douce nuit
    "douce" : [
        [G6, G6, G6, A6, G6, G6, E6, E6, E6, E6, E6, Z,
         G6, G6, G6, A6, G6, G6, E6, E6, E6, E6, E6, Z,
         D6, D6, D6, Z, D6, D6, B5, B5, B5, B5, Z,
         C6, C6, C6, Z, C6, C6, G5, G5, G5, G5, Z,
         A5, A5, A5, Z, A5, A5, C6, C6, C6, B5, A5, A5, G5, G5, G5, A5, G5, G5, E5, E5, E5, E5, Z, Z,
         A5, A5, A5, Z, A5, A5, C6, C6, C6, B5, A5, A5, G5, G5, G5, A5, G5, G5, E5, E5, E5, E5, Z, Z,
         D6, D6, D6, Z, D6, D6, F6, F6, F6, D6, B5, B5, C6, C6, C6, C6, C6, E6, E6, E6, E6, Z, Z,
         C6, C6, C6, G5, E5, E5, G5, G5, G5, F5, D5, D5, C5, C5, C5, C5, C5, C5, C5, C5, Z,
    ],0.28, 250],

}




