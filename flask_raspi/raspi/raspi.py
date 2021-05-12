import time
import RPi.GPIO as GPIO
from time import sleep
from termcolor import cprint

ledPin = 11
redPin = 8
greenPin = 10
bluePin = 12
delaytime = 0.5
LEDPin = [ledPin, redPin, greenPin, bluePin]
red, green, blue = 0, 0, 0


def gpio_setup():
    global red, green, blue
    cprint("GPIO setup", "green")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LEDPin, GPIO.OUT, initial=GPIO.LOW)
    red = GPIO.PWM(redPin, 50)  # 50Hz
    green = GPIO.PWM(greenPin, 50)  # 50Hz
    blue = GPIO.PWM(bluePin, 50)  # 50Hz
    for i in range(2):
        GPIO.output(LEDPin, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(LEDPin, GPIO.LOW)
        sleep(0.1)


def gpio_destroy():
    cprint("GPIO destroy", "green")
    GPIO.cleanup()


def Blink():
    GPIO.output(ledPin, GPIO.HIGH)
    sleep(delaytime)
    GPIO.output(ledPin, GPIO.LOW)
    sleep(delaytime)


def High():
    GPIO.output(ledPin, GPIO.HIGH)


def LOW():
    GPIO.output(ledPin, GPIO.LOW)


def RGB():
    global red, green, blue
    red.start(0)
    green.start(100)
    blue.start(0)
    delaytime2 = 0.03

    for loop in range(2):
        for i in range(0, 100, 10):
            red.ChangeDutyCycle(0)
            green.ChangeDutyCycle(100-i)
            blue.ChangeDutyCycle(i)
            time.sleep(delaytime2)

        for i in range(0, 100, 10):
            red.ChangeDutyCycle(i)
            green.ChangeDutyCycle(0)
            blue.ChangeDutyCycle(100-i)
            time.sleep(delaytime2)

        for i in range(0, 100, 10):
            red.ChangeDutyCycle(100-i)
            green.ChangeDutyCycle(i)
            blue.ChangeDutyCycle(0)
            time.sleep(delaytime2)

    red.stop()
    green.stop()
    blue.stop()
