import RPi.GPIO as GPIO
from time import sleep

ledPin = 11
delaytime = 0.01


def gpio_setup():
    print("GPIO setup")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)


def gpio_destroy():
    print("GPIO destroy")
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
