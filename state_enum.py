from enum import Enum


# Gives the State of the Alarm
class AlarmState(Enum):
    ARMED = 0
    RUNNING = 1
    DISABLED = 2
