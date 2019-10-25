from json_service import JSONService

class SecuritySystem:
    # if the alarm is armed or not
    alarmArmed = False

    def changeAlarm():
        alarmArmed = !alarmArmed

    def auth(authentificationCode : str) -> bool:
        jsonFile = JSONService.getJSON()

        if jsonFile.
