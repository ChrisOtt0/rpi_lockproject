import websocket
import jsonpickle
from datetime import datetime
from .config_handler import ConfigHandler
from .lock_handler import LockHandler
from .logger import Logger
from .http_handler import HttpHandler
from .models.wsrequest import WsRequest

class WsDelegater():
    def __init__(self, 
            config: ConfigHandler, 
            logger: Logger, 
            lock: LockHandler, 
            http: HttpHandler,
            ws_url: str,
            ws_headers: list):
        self._config = config
        self._logger = logger
        self._lock = lock
        self._http = http
        self._wsapp = websocket.WebSocketApp(
            url="ws" + ws_url,
            header=ws_headers,
            on_message=self._ws_delegater
        )

    def _ws_delegater(self, wsapp, message):
        wsrequest: WsRequest = jsonpickle.decode(message)
        if wsrequest["action"] == "unlock":
            self._unlock_door(wsrequest["args"]["caller"])

    def _unlock_door(self, caller: str):
        event = "Event at: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n"
        event += "Door opened by " + caller + ".\n"
        self._logger.log_event(event)
        self._http.log_event(event)
        self._lock.unlock(self._config.get_unlocked_time())
        

    def switch_handler(self, channel):
        if channel == 21:
            self._unlock_door("inside switch.")

    def run(self):
        self._wsapp.run_forever()
