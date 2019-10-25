import json
import auth.enum.py
from json_service import JSONService


class SecuritySystem:
    # if the alarm is armed or not
    alarmState =

    #
    # Changes the state of the alarm
    #
    def changeAlarm():
        alarmArmed = !alarmArmed

    #
    # authType {"rfid", "pwd"}
    #
    def auth(authCode : str, authType : str) -> bool:
        jsonFile = JSONService.getJSON()

        if authCode == jsonFile[authType]:
            return True
        else:
            return False
