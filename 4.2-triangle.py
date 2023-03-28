import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

import time

def dec2bin(n):
    if n>=2**8 or n<0:
        ValueError("given number is too big")
    else:
        r = bin(n)[2:]
        while len(r) != 8:
            r = '0' + r
        return(r)

try:
    print('enter period')
    t = float(input())
    a = 0
    while True:
        if a == 256:
            a = 0
        for i in range(8):
                GPIO.output(dac[i], int(dec2bin(a)[i]))
        time.sleep(t)
        a += 1
finally:
    for i in range(8):
        GPIO.output(dac[i], 0)
    GPIO.cleanup()