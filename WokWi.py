from machine import Pin
from neopixel import NeoPixel
from random import randint
from time import sleep

r = NeoPixel(Pin(15), 32)
w = [randint(0,255) for _ in range(32)]

for i in range(32):
    for j in range(31-i):
        if w[j] > w[j+1]:
            w[j],w[j+1] = w[j+1],w[j]
            
            for k in range(32):
                r[k] = (w[k],0,0)
            r.write()
            sleep(.1)
