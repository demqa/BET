import RPi.GPIO as GPIO
from time import sleep

DAC  = [26, 19, 13,  6, 5, 11,  9, 10]

def DecToBin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def Cleanup():
    GPIO.output(DAC, 0)
    GPIO.cleanup()

MAX_VOLTAGE = 3.3
N_BYTES     = 8

def CalculateVoltage(number):
    print("Current Voltage is about {:.2f}".format(MAX_VOLTAGE * number / pow(2, N_BYTES)))

PERIOD = 10

def TriangleSignal():
    number = 0
    while (number < pow(2, N_BYTES)):
        binary = DecToBin(number)
        GPIO.output(DAC, binary)
        number += 1
        sleep(PERIOD / (2 * pow(2, N_BYTES)))
    
    number = pow(2, N_BYTES) - 1
    while (number >= 0):
        binary = DecToBin(number)
        GPIO.output(DAC, binary)
        number -= 1
        sleep(PERIOD / (2 * pow(2, N_BYTES)))


GPIO.setmode(GPIO.BCM)
GPIO.setup(DAC, GPIO.OUT)

try:
    inputStr = input("Give a period of Triangle Signal in seconds, or q: ")
    if (inputStr == 'q'):
        print("exit")
        exit()

    PERIOD = int(inputStr)
    if (PERIOD <= 1):
        print("It hard to accept, but i really cannot use this value to make it period")

    while True:
        TriangleSignal()

except ValueError:
    print("It hard to accept, but i really cannot use this value to make it period")

finally:
    Cleanup()