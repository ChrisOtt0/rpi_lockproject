import unittest
import configparser
import os
import shutil

class ConfigHandler:
    def __init__(self, is_test: bool):
        if not is_test:
            self._path = "/home/pi/.config/lockproject/"
            self._config_exists()
            self._config = self._load_config()
        else:
            self._path = "/home/pi/.config/lockproject/tests/"
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
            "Paired": "False"
        }
        config["SETTINGS"] = {
            "UnlockedTime": "4"
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

    def get_unlocked_time(self):
        return int(self._config["SETTINGS"]["UnlockedTime"])

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

    def is_lock_paired(self):
        paired = self._config["DATA"]["Paired"]
        if paired == "True":
            return True
        else:
            return False

    def set_lock_paired(self, state: bool):
        if state:
            self._config["DATA"]["Paired"] = "True"
        else:
            self._config["DATA"]["Paired"] = "False"

        self._write_config(self._config)


#### UNIT TESTS ####
class ConfTestMethods(unittest.TestCase):
    def _rm_conf(self):
        path = "/home/pi/.config/lockproject/tests/"
        shutil.rmtree(path)
        
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
            "Paired": "False"
        }
        expected["SETTINGS"] = {
            "UnlockedTime": "6"
        }

        handler = ConfigHandler(True)

        # Act
        result = handler._gen_default_conf()

        # Assert
        self.assertEqual(expected, result)
        self._rm_conf()

    def test_set_lock_activated(self):
        # Arrange
        expected = configparser.ConfigParser()
        expected["SERVER"] = {
            "ServerIp": "51.75.69.121",
            "ServerPort": "3000"
        }
        expected["DATA"] = {
            "Id": "123je1mn4567ma82",
            "Activated": "False",
            "Paired": "False"
        }
        expected["SETTINGS"] = {
            "UnlockedTime": "6"
        }

        handler = ConfigHandler(True)

        # Act
        handler.set_lock_activated(False)
        result = handler._load_config()

        # Assert
        self.assertEqual(expected, result)
        self._rm_conf()

    def test_set_lock_paired(self):
        # Arrange
        expected = configparser.ConfigParser()
        expected["SERVER"] = {
            "ServerIp": "51.75.69.121",
            "ServerPort": "3000"
        }
        expected["DATA"] = {
            "Id": "123je1mn4567ma82",
            "Activated": "True",
            "Paired": "True"
        }
        expected["SETTINGS"] = {
            "UnlockedTime": "6"
        }

        handler = ConfigHandler(True)
        
        # Act
        handler.set_lock_paired(True)
        result = handler._load_config()
        
        # Assert
        self.assertEqual(expected, result)
        self._rm_conf()
    
    def test_get_server_ip(self):
        # Arrange
        handler = ConfigHandler(True)
        expected = "51.75.69.121"

        # Act
        result = handler.get_server_ip()

        # Assert
        self.assertEqual(expected, result)
        self._rm_conf()
        

    def test_get_server_port(self):
        # Arrange
        handler = ConfigHandler(True)
        expected = "3000"

        # Act
        result = handler.get_server_port()

        # Assert
        self.assertEqual(expected, result)
        self._rm_conf()


    def test_get_lock_id(self):
        # Arrange
        handler = ConfigHandler(True)
        expected = "123je1mn4567ma82"

        # Act
        result = handler.get_lock_id()

        # Assert
        self.assertEqual(expected, result)
        self._rm_conf()

    
    def test_get_unlocked_time(self):
        # Arrange
        handler = ConfigHandler(True)
        expected = 6

        # Act
        result = handler.get_unlocked_time()

        # Assert
        self.assertEqual(expected, result)
        self._rm_conf()


    def test_is_lock_activated(self):
        # Arrange
        handler = ConfigHandler(True)
        expected = True

        # Act
        result = handler.is_lock_activated()

        # Assert
        self.assertEqual(expected, result)
        self._rm_conf()

    def test_is_lock_paired(self):
        # Arrange
        handler = ConfigHandler(True)
        expected = False

        # Act
        result = handler.is_lock_paired()

        # Assert
        self.assertEqual(expected, result)
        self._rm_conf()
