import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
for i in range(100):

    GPIO.output(22, 1)
    time.sleep(1)
    GPIO.output(22, 0)
    time.sleep(1)
