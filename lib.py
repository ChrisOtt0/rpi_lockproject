from modules.config_handler import ConfigHandler
from modules.lock_handler import LockHandler
from modules.lock_types import LockTypes

config = ConfigHandler(is_test=False)
lock = LockHandler(LockTypes.SERVO)

def main():
    lock.unlock(config.get_unlocked_time())
