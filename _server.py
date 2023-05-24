from fastapi import FastAPI
from threading import Thread
from modules.models.unlock_req import UnlockReq
from modules.config_handler import ConfigHandler
from modules.lock_handler import LockHandler
from modules.lock_types import LockTypes
from modules.logger import Logger
from modules.http_handler import HttpHandler
from datetime import datetime

test_url = "http://192.168.1.245:8000/api/"
production_url = "http://51.75.69.121:3000/api/"

config = ConfigHandler(is_test=False)
logger = Logger(is_test=False)
lock = LockHandler(LockTypes.SERVO)
http = HttpHandler(test_url)

app = FastAPI()

@app.put("/unlock", status_code=200)
async def unlock(req: UnlockReq):
    dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    message = "Event at " + dt_string + ": \n"
    message += "Lock " + str(config.get_lock_id) + " unlocked via " + req.caller_type + "."
    logger.log_event(message)
    # http.log_event(message)
    thread = Thread(target=lock.unlock, args=(config.get_unlocked_time(),))
    thread.start()
    return { "status": "unlocked" }
