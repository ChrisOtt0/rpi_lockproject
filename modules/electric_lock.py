from .ilock import ILock
import RPi.GPIO as GPIO
import time

class ElectricLock(ILock):
    def __init__(self):
        GPIO.setup(20, GPIO.OUT)

    def unlock(self, seconds: int):
        GPIO.output(20, 1)
        time.sleep(seconds)
        GPIO.output(20, 0)
