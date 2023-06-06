from .lock_types import LockTypes
from .ilock import ILock
from .servo_lock import ServoLock
from .electric_lock import ElectricLock

class LockHandler:
    def __init__(self, type: LockTypes):
        if type == LockTypes.SERVO:
            self.lock = ServoLock()
        elif type == LockTypes.ELECTRIC:
            self.lock = ElectricLock()

    def unlock(self, seconds: int):
        self.lock.unlock(seconds)
