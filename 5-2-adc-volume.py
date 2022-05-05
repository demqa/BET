import RPi.GPIO as GPIO
import time

DAC    = [26, 19, 13,  6, 5, 11,  9, 10]
TROYKA =  17
COMP   =   4

def DecToBin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def Cleanup():
    GPIO.output(DAC, 0)
    GPIO.cleanup()

MAX_VOLTAGE = 3.3
N_BYTES     = 8
LEVELS      = 2**N_BYTES

def CalculateVoltage(number):
    print("Current Voltage is about {:.2f}".format(MAX_VOLTAGE * number / pow(2, N_BYTES)))


GPIO.setmode(GPIO.BCM)
GPIO.setup  (DAC, GPIO.OUT)

GPIO.setup  (COMP, GPIO.IN)

GPIO.setup  (TROYKA, GPIO.OUT, initial = GPIO.HIGH)

def NumToDac(value):
    signal = DecToBin(value)
    GPIO.output(DAC, signal)

def adc():
    prop = LEVELS // 2
    value = prop

    while prop > 0:
        NumToDac(value)
        time.sleep(0.005)
        CompValue = GPIO.input(COMP)

        prop = prop // 2
        if CompValue == 0:
            value = value - prop
        else:
            value = value + prop
        
    return value

try:
    while True:
        value = adc()
        voltage = value / LEVELS * MAX_VOLTAGE
        print("input voltage = {:2f}".format(voltage))
        time.sleep(0.5)

except KeyboardInterrupt:
    print("puk puk turning off forever")

else:
    print("exception")

finally:
    Cleanup()