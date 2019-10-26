from enum import Enum

#
# unused
#
class AuthID(Enum):
    RFID = 0
    PWD  = 1

#
# Gives the State of the Alarm
#
class AlarmState(Enum):
    ARMED = 0
    RUNNING  = 1
    DISABLED = 2
