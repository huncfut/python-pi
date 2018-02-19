import RPi.GPIO as GPIO
import time
import json
import threading
from pprint import pprint

import threading

comPins = [17, 18, 19, 20, 21, 22, 23, 24]
GPIO.setmode(GPIO.BCM)
for pin in comPins:
    GPIO.setup(pin, GPIO.OUT)

def turnOn(compNum):
    GPIO.output(compNum, 1)
    time.sleep(0.5)
    GPIO.output(compNum, 0)

def turnOff(numOfComp):
    GPIO.output(numOfComp, 1)
    time.sleep(0.5)
    GPIO.output(numOfComp, 0)

def turnHardOff(numOfComp):
    GPIO.output(numOfComp, 1)
    time.sleep(5)
    GPIO.output(numOfComp, 0)


def setup():
    threading.Timer(10.0, setup).start()

    instructionJson = json.load(open('kupa.json'))

    for compNum in instructionJson["turnOn"]:
        turnOn(comPins[compNum-1])
    for compNum in instructionJson["turnOff"]:
        turnOff(comPins[compNum-1])
    for compNum in instructionJson["turnHardOff"]:
        turnHardOff(comPins[compNum-1])


setup()
