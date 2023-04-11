import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)
dac = []
dac=[26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp=4
troyka=17
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka,gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)
gpio.setup(leds, gpio.OUT)

def ToBin(a):
    return [int (elem) for elem in bin(a)[2:].zfill(8)]

def adc():
    k=0
    for i in range(7, -1, -1):
        k+=2**i
        gpio.output(dac, ToBin(k))
        sleep(0.01)
        if gpio.input(comp)==0:
            k-=2**i
    _leds(k)
    return k

def _leds(n):
    s = bin(n)[2:]
    if n<=255 and n>=0:
        for i in range(len(s)):
            gpio.output(leds[i], int(s[i]))


try:
    while True:
        i = adc()
        print(i, '{:.2f}v'.format(3.3*i/256))


finally:
    gpio.output(dac, 0)
    gpio.cleanup()