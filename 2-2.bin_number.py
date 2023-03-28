import RPi.GPIO as GPIO
import time 
import random 

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
num = [random.randint(0, 1) for i in dac]
num = [0,0,0,0,0,0,0,0]

for i in dac:
    GPIO.setup(i, GPIO.OUT)

for i in range(len(dac)):
    GPIO.output(dac[i], num[i])
time.sleep(1)

GPIO.cleanup()

import matplotlib.pyplot as plt
plt.plot([255, 127, 64, 32, 5, 0],[3.26, 1.63, 0.826, 0.5, 0.48,0.48], color="orange")
plt.scatter([255, 127, 64, 32, 5, 0],[3.26, 1.63, 0.826, 0.5, 0.48,0.48], color = 'blue')
plt.show()