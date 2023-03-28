import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

def to_bin(n):
    if n>=2**8 or n<0:
        ValueError("given number is too big")
    else:
        r = bin(n)[2:]
        while len(r) != 8:
            r = '0' + r
        return(r)

def voltage(n):
    return 3.3 * n / 255

try:
    while True:
        print('введите число')
        a = input()
        if a == 'q':
            break
        try:
            a = int(a)
            if a>255 or a<0:
                print('number is out of range')
            for i in range(8):
                GPIO.output(dac[i], int(to_bin(a)[i]))
            print(round(voltage(a), 3), 'V')
        except:
            print('symbols are incorrect')
finally:
    for i in range(8):
        GPIO.output(dac[i], 0)
    GPIO.cleanup()