import RPi.GPIO as GPIO

DAC  = [26, 19, 13,  6, 5, 11,  9, 10]
LEDs = [21, 20, 16, 12, 7,  8, 25, 24]
AUX  = [22, 23, 27, 18, 15, 14,  3,  2]

GPIO.setmode(GPIO.BCM)

GPIO.setup(LEDs, GPIO.OUT)
GPIO.setup(DAC,  GPIO.OUT)
GPIO.setup(AUX,  GPIO.IN)

for i in range(len(AUX)):
    print(GPIO.input(AUX[i]), end = " ")
print()

GPIO.output(LEDs, 0)
GPIO.output(DAC,  0)

GPIO.cleanup()