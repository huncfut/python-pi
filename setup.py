# import RPi.GPIO as GPIO
# import time
import json
from pprint import pprint
import threading

# GPIO.setmode(GPIO.BCM)
def turnOn(compNum):
    print(compNum)
    return 0

def runTurnOn(turnOnList):
    for element in turnOnList:
        turnOn(comPins[element-1])

comPins = [17, 18, 19, 20, 21, 22, 23, 24]


def setup():
    threading.Timer(10.0, setup).start()
    instructionJson = json.load(open('kupa.json'))
    runTurnOn(instructionJson["turnOn"])

setup()




# def turnOn(numOfComp):
#     GPIO.output(numOfComp, GPIO.HIGH)
#     time.sleep(0.5)
#     GPIO.output(numOfComp, GPIO.LOW)
#
# def turnOff(numOfComp):
#     GPIO.output(numOfComp, GPIO.HIGH)
#     time.sleep(0.5)
#     GPIO.output(numOfComp, GPIO.LOW)
#
# def turnHardOff(arg):
#     GPIO.output(numOfComp, GPIO.HIGH)
#     time.sleep(5)
#     GPIO.output(numOfComp, GPIO.LOW)
#
# while True:
#     compNum = int(input("Computer #"))
#     funcNum = int(input("Function:\n1 => turn on\n2 => turn off\n3 => hard reset\n"))
