import RPi.GPIO as GPIO
import time
from matplotlib import pyplot as plt
dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxV = 3.3
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setwarnings(False)

def decimal2binary(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(bits)]

def adc():
    value = 0
    GPIO.output(dac, 0)
    for i in range (0,8,1):
        GPIO.output(dac[i], 1)
        time.sleep(0.05)
        compValue = GPIO.input(comp)
        if compValue == 0 :
            GPIO.output(dac[i], 0)
        else: 
            value = value + 2**(7-i)
    return value

try:
    
    start_time = time.time()
    measured_data = []
    while True:
        num = adc()
        Volts_C = num * 3.3/256 
        print(Volts_C)
        list.append(measured_data, num)
        #print ("ADC value = {:^3}".format(adc())) 
        if num > 256*0.97:
            GPIO.setup(troyka, GPIO.OUT, initial=GPIO.LOW)
            break   
    while True: 
        num = adc()  
        Volts_C = num * 3.3/256 
        print(Volts_C)
        list.append(measured_data, num) 
        if num < 256*0.02: 
            t_exp=time.time() - start_time
            x = [i * t_exp/len(measured_data) for i in range (len(measured_data))]
            plt.plot(x, measured_data)
            plt.show()
            measured_data_str = [str(item) for item in measured_data]    
            with open("data.txt", "w") as outfile:
                outfile.write("\n".join(measured_data_str))  
            with open("settings.txt","w") as outfile:
                outfile.write("Частота дискретизации : ")
                outfile.write(str(t_exp/len(measured_data)))
                outfile.write("\nШаг квантования : ")
                outfile.write("0.01289")
            break
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    GPIO.setup(troyka, GPIO.OUT, initial=GPIO.LOW)
    GPIO.cleanup(troyka)
