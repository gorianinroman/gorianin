import RPi.GPIO as GPIO
import time

def binary(a):
    return [int(i) for i in bin(a)[2::].zfill(8)]

GPIO.setmode(GPIO.BCM)
dac = [26,19,13,6,5,11,9,10]
[GPIO.setup(i, GPIO.OUT) for i in dac]
num = 0
try:
    while True:
        num = 0
        for num in range (255):
            a = binary(int(num))
            [GPIO.output(dac[i], a[i]) for i in range(8)]
            time.sleep(1.5/256)
        num = 255
        for num in range (255, 0, -1):
            a = binary(int(num))
            [GPIO.output(dac[i], a[i]) for i in range(8)]
            time.sleep(1.5/256)

        
finally:
    [GPIO.output(i, 0) for i in dac]
    GPIO.cleanup()            
