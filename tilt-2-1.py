import RPi.GPIO as GPIO
from time import sleep

LEDs = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDs, GPIO.OUT)

for _ in range(3):
    for LED in LEDs:
        GPIO.output(LED, 1)
        sleep(0.2)
        GPIO.output(LED, 0)

GPIO.output(LEDs, 0)

GPIO.cleanup()