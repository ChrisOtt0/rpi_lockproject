import RPi.GPIO as GPIO
import time

pin = 18
led = 17
lock = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(lock, GPIO.OUT)

GPIO.output(led, False);
GPIO.output(lock, False);

def switch_handler(channel):
    print(str(channel) + " pressed")
    GPIO.output(led, True)
    GPIO.output(lock, True)
    time.sleep(2)
    GPIO.output(lock, False)
    GPIO.output(led, False)

GPIO.add_event_detect(pin, GPIO.FALLING, callback=switch_handler)

try:
    while True:
        i = 0
except KeyboardInterrupt:
    GPIO.output(led, False);
    GPIO.output(lock, False);
    GPIO.cleanup()
