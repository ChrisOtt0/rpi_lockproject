from modules.config import ConfigHandler

config_path = "/home/pi/.config/lockproject/"
config = ConfigHandler(path=config_path, is_test=False)

def main():
    print("Config works")
