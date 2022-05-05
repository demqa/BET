import RPi.GPIO as GPIO

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


GPIO.setmode(GPIO.BCM)
GPIO.setup(DAC, GPIO.OUT)

while True:
    try:
        inputStr = input("Give me a number 0-255, or q to exit: ")
        if inputStr == 'q':
            break

        number = int(inputStr)
        if (number < 0) or (number > 255):
            print("Give program nice input")
            continue

        binary = DecToBin(number)
        GPIO.output(DAC, binary)

    except ValueError:
        print("Give program a number")
            
#   finally:
#       Cleanup()


Cleanup()
