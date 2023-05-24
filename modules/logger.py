import os
from datetime import datetime

class Logger:
    def __init__(self, is_test: bool):
        self.path = "/home/pi/.config/lockproject/"
        if is_test:
            self.path += "tests/"
        self._logs_exists()

    def _logs_exists(self):
        if not os.path.exists(self.path):
            os.mkdir(self.path)

        if not os.path.exists(self.path + "err_logs.txt"):
            with open(self.path + "err_logs.txt", "w") as log:
                log.write("")

        if not os.path.exists(self.path + "event_logs.txt"):
            with open(self.path + "event_logs.txt", "w") as log:
                log.write("")

    def _write_to_log(self, path, message):
        with open(path, "a") as log:
            log.write(message + "\n")

    def _gen_error_log(self, e: str):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        message = "Error logged at: " + dt_string + "\n"
        message += e + "\n"
        return message

    def get_err_log_path(self) -> str:
        return self.path + "err_logs.txt"

    def log_error(self, e: str):
        message = self._gen_error_log(e)
        self._write_to_log(self.path + "err_logs.txt", message)

    def log_event(self, e):
        self._write_to_log(self.path + "event_logs.txt", e)
