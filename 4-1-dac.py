import RPi.GPIO as GPIO

def binary(a):
    return [int(i) for i in bin(a)[2::].zfill(8)]

GPIO.setmode(GPIO.BCM)
dac = [26,19,13,6,5,11,9,10]
[GPIO.setup(i, GPIO.OUT) for i in dac]

try:
    while True :
        num = input()
        if num == 'q' :
            break
        if num.isdigit() and 0 <= int(num) <= 255:
            a = binary(int(num))
            [GPIO.output(dac[i], a[i]) for i in range(8)]
            volts = int(num) / 256 * 3.3
            print (volts, " В")
        else : 
            print("Введите число от 0 до 255")
finally:
    [GPIO.output(i, 0) for i in dac]
    GPIO.cleanup()