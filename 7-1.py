import RPi.GPIO as gpio
import time
from matplotlib import pyplot as plt

gpio.setmode(gpio.BCM)

leds=[21, 20, 16, 12, 7, 8, 25, 24]
gpio.setup(leds, gpio.OUT)

dac=[26, 19, 13, 6, 5, 11, 9, 10]
gpio.setup(dac, gpio.OUT, initial=gpio.HIGH)

comp=4
troyka=17 
gpio.setup(troyka,gpio.OUT)
gpio.output(17, 0)
gpio.setup(comp, gpio.IN)

def adc():
    k=0
    for i in range(7, -1, -1):
        k+=2**i
        gpio.output(dac, perev(k))
        time.sleep(0.001)
        if gpio.input(comp)==0:
            k-=2**i
    return k

#перевод в двоичную
def perev(a):
    return [int (elem) for elem in bin(a)[2:].zfill(8)]

try:
    napr=0
    results=[]
    time_start = time.time()
    count=0

    #зарядка конденсатора, запись показаний в процессе
    print('начало зарядки конденсатора')
    while napr<155:
        napr=adc()
        print(napr, 'зарядка')
        results.append(napr)
        count+=1
        gpio.output(leds, perev(napr))

    gpio.output(17, 1)

    #разрядка конденсатора, запис показаний в процессе
    print('начало разрядки конденсатора')
    while napr>60:
        napr=adc()
        print(napr, 'разрядка')
        results.append(napr)
        count+=1
        gpio.output(leds, perev(napr))

    time_experiment=time.time()-time_start

    #запись данных в файлы
    print('запись данных в файл')
    with open('data.txt', 'w') as f:
        for i in results:
            f.write(str(i) + '\n')
    with open('settings.txt', 'w') as f:
        f.write(str(1/time_experiment/count) + '\n')
        f.write('0.01289')
    
    print('общая продолжительность эксперимента {}, период одного измерения {}, средняя частота дискретизации {}, шаг квантования АЦП {}'.format(time_experiment, time_experiment/count, 1/time_experiment/count, 0.013))

    #графики
    print('построение графиков')
    y=[i/256*3.3 for i in results]
    x=[i*time_experiment/count for i in range(len(results))]
    plt.plot(x, y)
    plt.xlabel('время')
    plt.ylabel('вольтаж')
    plt.show()

finally:
    gpio.output(leds, 0)
    gpio.output(dac, 0)
    gpio.cleanup()
