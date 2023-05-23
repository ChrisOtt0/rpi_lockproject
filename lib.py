from modules.config_handler import ConfigHandler
from modules.lock_handler import LockHandler
from modules.lock_types import LockTypes
from modules.logger import Logger
# from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

# reader = SimpleMFRC522()
config = ConfigHandler(is_test=False)
logger = Logger(is_test=False)
lock = LockHandler(LockTypes.SERVO)

def switch_handler(channel):
    if channel == 18:
        lock.unlock(config.get_unlocked_time())

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(18, GPIO.FALLING, callback=switch_handler)

def main():
    while True:
        try:
            # id, text = reader.read()
            # print("ID: " + str(id))
            # print("Text: " + str(text))
            # lock.unlock(config.get_unlocked_time())
            # time.sleep(2)
            i = 1
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as e:
            print("An error occured. Please check the logs at: " + logger.get_err_log_path())
            logger.log_error(e)
            raise KeyboardInterrupt
