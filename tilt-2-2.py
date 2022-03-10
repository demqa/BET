import RPi.GPIO as GPIO
from time import sleep

DAC = [26, 19, 13, 6, 5, 11, 9, 10]
NUM = [ 0,  0,  0, 0, 0,  0, 1,  0]

GPIO.setmode(GPIO.BCM)
GPIO.setup(DAC, GPIO.OUT)

DAC.reverse()

while True:
    n = int(input())

    if (n < 0) or (n > 255):
        break

    print(n)

    for LED in DAC:
        GPIO.output(LED, n & 1)
        n = (n >> 1)

    sleep(10)

    GPIO.output(DAC, 0)

GPIO.cleanup()