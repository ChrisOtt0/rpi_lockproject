import configparser
import os

class ConfigHandler:
    def __init__(self):
        self._path = "/home/pi/.config/lockproject/"
        self._config_exists()
        self._config = self._load_config()

    def _config_exists(self):
        if not os.path.exists(self._path):
            os.mkdir(self._path)

        if not os.path.exists(self._path + "config.ini"):
            self._gen_default_conf()

    def _gen_default_conf(self):
        config = configparser.ConfigParser()
        config["SERVER"] = {
            "ServerIp": "51.75.69.121",
            "ServerPort": "3000"
        }

        config["DATA"] = {
            "Id": "123je1mn4567ma82",
            "Activated": "True",
        }

        with open(self._path + "config.ini", 'w') as configfile:
            config.write(configfile)

    def _load_config(self):
        config = configparser.ConfigParser()
        config.read(self._path + "config.ini")

        if not "SERVER" in config:
            raise RuntimeError("Config needs to contain a SERVER section.")

        if not "DATA" in config:
            raise RuntimeError("Config needs to contain a DATA section.")

        return config

    def get_server_ip(self):
        return self._config["SERVER"]["ServerIp"]

    def get_server_port(self):
        return self._config["SERVER"]["ServerPort"]

    def get_lock_id(self):
        return self._config["DATA"]["Id"]

    def is_lock_activated(self):
        activated = self._config["DATA"]["Activated"]
        if activated == "True":
            return True
        else:
            return False

    def set_lock_activated(self, state: bool):
        if state:
            self._config["DATA"]["Activated"] = "True"
        else:
            self._config["DATA"]["Activated"] = "False"

        with open(self._path + "config.ini", 'w') as configfile:
            self._config.write(configfile)
