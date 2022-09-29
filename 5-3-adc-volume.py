import RPi.GPIO as GPIO
import time
dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21,20,16,12,7,8,25,24]
bits = len(dac)
levels = 2**bits
maxV =3.3
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)
GPIO.setwarnings(False)

def decimal2binary(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(bits)]

def num2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac,signal)
    return signal

try:
    while True:
        value = 0
        GPIO.output(dac, 0)
        for i in range (0,8,1):
            GPIO.output(dac[i], 1)
            time.sleep(0.01)
            compValue = GPIO.input(comp)
            if compValue == 0 :
                GPIO.output(dac[i], 0)
            else: 
                value = value + 2**(7-i)
        if value == 0:
            a = 0
        else :
            a = value // 32 + 1
        for i in range(0,a,1):
            GPIO.output(leds[7-i],1)
        b = 8 - a
        for i in range(b):
            GPIO.output(leds[i], 0)



        

        print ("ADC value = {:^3}".format(value))
        
finally:
    GPIO.output(leds, GPIO.LOW)
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
