from enum import Enum

class AuthID(Enum):
    RFID = 0
    PWD  = 1

class AlarmState(Enum):
    ARMED = 0
    RUNNING  = 1
    DEACTIVE = 2
