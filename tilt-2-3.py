import RPi.GPIO as GPIO
from time import sleep

LEDs = [21, 20, 16, 12,  7,  8, 25, 24]
AUX  = [22, 23, 27, 18, 15, 14,  3,  2]

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDs, GPIO.OUT)
GPIO.setup(AUX,  GPIO.IN)  

while True:
    for index in range(len(AUX)):
        GPIO.output(LEDs[index], GPIO.input(AUX[index]))

    sleep(0.2)

GPIO.output(LEDs, 0)

GPIO.cleanup()