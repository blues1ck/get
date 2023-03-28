import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [22, 23, 27, 18, 15, 14, 3, 2]

for i in leds:
    GPIO.setup(i, GPIO.OUT)

for i in aux:
    GPIO.setup(i, GPIO.IN)

while True:
    for i in range(8):
        if GPIO.input(aux[i])==1:
            GPIO.output(leds[i], 0)
        else:
            GPIO.output(leds[i], 1)


