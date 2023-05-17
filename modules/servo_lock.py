from .ilock import ILock
import RPi.GPIO as GPIO
import time

class ServoLock(ILock):
    def __init__(self):
        self.pin = 21
        self.closed_duty_cycle = 7.5
        self.open_duty_cycle = 3
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm_servo = GPIO.PWM(self.pin, 50)
        self.pwm_servo.start(self.closed_duty_cycle)

    def unlock(self, seconds: int):
        time.sleep(0.5)
        self.pwm_servo.ChangeDutyCycle(self.open_duty_cycle)
        time.sleep(seconds)
        self.pwm_servo.ChangeDutyCycle(self.closed_duty_cycle)
        time.sleep(0.5)
