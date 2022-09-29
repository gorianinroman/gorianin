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

try:
    while True:
        for value in range(256):
            signal = num2dac(value)
            voltage = value/levels * maxV
            time.sleep(0.0001)
            compValue = GPIO.input(comp)
            if compValue == 0:
                print ("ADC value = {:^3} -> {}, input voltage = {:.2f}".format(value, signal, voltage))
                break

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
