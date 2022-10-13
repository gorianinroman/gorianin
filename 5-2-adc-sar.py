import RPi.GPIO as GPIO
import time
dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxV =3.3
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setwarnings(False)

def decimal2binary(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(bits)]

def num2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac,signal)
    return signal
def adc():
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
        volt_comp = 3.3 * value / 256
        

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
        
        print ("ADC value = {:^3}".format(value))
        
        # print ("ADC value = {:^3}".format(value))
       
        
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
