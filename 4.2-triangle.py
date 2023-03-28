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
    print('enter period in seconds')
    t = float(input())
    a = 0
    k = 1
    n = 0
    while n<5:
        for i in range(8):
            GPIO.output(dac[i], int(dec2bin(a)[i]))
        time.sleep(t/256)
        if a==255:
            a = 254
            k = 0
        elif a==0:
            a = 1
            k = 1
            n += 1
        elif k == 1:
            a+=1
        else:
            a-=1
        
finally:
    for i in range(8):
        GPIO.output(dac[i], 0)
    GPIO.cleanup()