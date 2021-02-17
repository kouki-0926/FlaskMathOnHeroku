import RPi.GPIO as GPIO
from time import sleep

ledPin = 11
delaytime = 0.01


def Blink():
    GPIO.output(ledPin, GPIO.HIGH)
    sleep(delaytime)
    GPIO.output(ledPin, GPIO.LOW)
    sleep(delaytime)


def setup():
    print("setup")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)


def destroy():
    print("destroy")
    GPIO.cleanup()
