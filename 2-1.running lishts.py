import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)

# leds = [21, 20, 16, 12, 7, 8, 25, 24]
leds = [24, 25, 8, 7, 12, 16, 20, 21]
for i in leds:
    GPIO.setup(i, GPIO.OUT)

for i in leds:
    GPIO.output(i, 0)

c = 0
while c<3:
    c+=1
    for i in leds:
        GPIO.output(i, 1)
        time.sleep(0.2)
        GPIO.output(i, 0)

for i in leds:
    GPIO.output(i, 0)

GPIO.cleanup()