import RPi.GPIO as GPIO
import traceback
from modules.config_handler import ConfigHandler
from modules.lock_handler import LockHandler
from modules.lock_types import LockTypes
from modules.logger import Logger
from modules.http_handler import HttpHandler
from modules.wsdelegater import WsDelegater

inside_switch = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(inside_switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

test_url = "://192.168.1.22:8000"
dev_url = "://51.75.69.121:3000"

config = ConfigHandler(is_test=False)
logger = Logger(is_test=False)
lock = LockHandler(LockTypes.ELECTRIC)
http = HttpHandler(dev_url)

websocket_header = [
    'lockid: ' + config.get_lock_id()
]

wsdelegater = WsDelegater(
    config=config,
    logger=logger,
    lock=lock,
    http=http,
    ws_url=dev_url,
    ws_headers=websocket_header
)

GPIO.add_event_detect(inside_switch, GPIO.FALLING, callback=wsdelegater.switch_handler, bouncetime=1200)

try:
    wsdelegater.run()
except KeyboardInterrupt:
    pass
except Exception:
    print("An error occured.")
    print("Please check the logs at: " + logger.get_err_log_path())
    logger.log_error(traceback.format_exc())
finally:
    GPIO.cleanup()
