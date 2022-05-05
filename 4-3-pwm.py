import RPi.GPIO as GPIO

def Cleanup():
    GPIO.output(CHANNEL, 0)
    GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

CHANNEL = 2
GPIO.setup(CHANNEL, GPIO.OUT)

pwm = GPIO.PWM(CHANNEL, 1000)     # frequency is 1000Hz
pwm.start(0)                      # duty cycle is 0

try:
    while True:
        inputStr = input("Give a duty cycle or q to quit: ")
        if (inputStr == 'q'):
            break
            
        number = float(inputStr)
        if (number < 0) or (number > 100):
            print("error")

        pwm.ChangeDutyCycle(number)

except ValueError:
    print("error")

finally:
    pwm.stop()
    Cleanup()