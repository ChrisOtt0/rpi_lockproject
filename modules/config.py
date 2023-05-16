import unittest
import configparser
import os

class ConfigHandler:
    def __init__(self, path: str, is_test: bool):
        self._path = path

        if not is_test:
            self._config_exists()
            self._config = self._load_config()

    def _config_exists(self):
        if not os.path.exists(self._path):
            os.mkdir(self._path)

        if not os.path.exists(self._path + "config.ini"):
            config = self._gen_default_conf()
            self._write_config(config)

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
        return config

    def _write_config(self, config: configparser.ConfigParser):
        with open(self._path + "config.ini", "w") as configfile:
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

        self._write_config(self._config)


#### UNIT TESTS ####
class ConfTestMethods(unittest.TestCase):
    def test_gen_default_conf(self):
        # Arrange
        expected = configparser.ConfigParser()
        expected["SERVER"] = {
            "ServerIp": "51.75.69.121",
            "ServerPort": "3000"
        }
        expected["DATA"] = {
            "Id": "123je1mn4567ma82",
            "Activated": "True",
        }

        handler = ConfigHandler("", True)

        # Act
        result = handler._gen_default_conf()

        # Assert
        self.assertEqual(expected, result)

    
    def test_get_server_ip(self):
        # Arrange
        handler = ConfigHandler("", True)
        config = handler._gen_default_conf()
        expected = "51.75.69.121"

        # Act
        result = config["SERVER"]["ServerIp"]

        # Assert
        self.assertEqual(expected, result)
        

    def test_get_server_port(self):
        # Arrange
        handler = ConfigHandler("", True)
        config = handler._gen_default_conf()
        expected = "3000"

        # Act
        result = config["SERVER"]["ServerPort"]

        # Assert
        self.assertEqual(expected, result)


    def test_get_lock_id(self):
        # Arrange
        handler = ConfigHandler("", True)
        config = handler._gen_default_conf()
        expected = "123je1mn4567ma82"

        # Act
        result = config["DATA"]["Id"]

        # Assert
        self.assertEqual(expected, result)


    def test_is_lock_activated(self):
        # Arrange
        handler = ConfigHandler("", True)
        config = handler._gen_default_conf()
        expected = "True"

        # Act
        result = config["DATA"]["Activated"]

        # Assert
        self.assertEqual(expected, result)
