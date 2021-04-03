import RPi.GPIO as GPIO
from time import sleep
from termcolor import cprint

ledPin = 11
delaytime = 0.5


def gpio_setup():
    cprint("GPIO setup", "green")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)


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
