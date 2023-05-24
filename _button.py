import RPi.GPIO as GPIO
from requests.models import HTTPError
from modules.http_handler import HttpHandler

http = HttpHandler("http://127.0.0.1:8080/")

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def switch_handler(channel):
    if channel == 18:
        if not http.unlock():
            raise HTTPError

GPIO.add_event_detect(18, GPIO.FALLING, callback=switch_handler)

while True:
    i = 0
