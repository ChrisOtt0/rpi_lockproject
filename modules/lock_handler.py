from .lock_types import LockTypes
from .ilock import ILock
from .servo_lock import ServoLock

class LockHandler:
    def __init__(self, type: LockTypes):
        if type == LockTypes.SERVO:
            self.lock = ServoLock()
        elif type == LockTypes.ELECTRIC:
            self.lock = ILock()

    def unlock(self, seconds: int):
        self.lock.unlock(seconds)
