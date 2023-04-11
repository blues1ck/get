import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)
dac = []
dac=[26, 19, 13, 6, 5, 11, 9, 10]
comp=4
troyka=17
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka,gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

def ToBin(a):
    return [int (elem) for elem in bin(a)[2:].zfill(8)]

def adc():
    for i in range(256):
        out=ToBin(i)
        gpio.output(dac, out)
        sleep(0.05)
        inp=gpio.input(comp)
        
        if inp==0:
            return i
    return 0

try:
    while True:
        i = adc()
        print(i, '{:.2f}v'.format(3.3*i/256))


finally:
    gpio.output(dac, 0)
    gpio.cleanup()