import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.IN)

GPIO.setup(22, GPIO.OUT)

if GPIO.input(14) == 1:
    GPIO.output(22, 1)
else:
    GPIO.output(22, 0)
print(GPIO.input(14))