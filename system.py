import __main__
import json
import state_enum
import gpio_service as gpios

from json_service import JsonService
from time import sleep

class SecuritySystem:

    def __init__(self):

        # if the alarm is armed or not
        self.alarmState = AlarmState.DISABLED

        #initializing sound for triggerAlarm
        self.button_sounds = {
            Button(2): Sound("samples/drum_tom_mid_hard.wav"),
            Button(3): Sound("samples/drum_cymbal_open.wav"),
        }


    #
    # Changes the state of the alarm
    #
    def changeAlarm(self, state: AlarmState):
        self.alarmState = state;

    #
    # authType {"rfid", "pwd"}
    #
    def auth(self, authCode: str, authType: str)->bool:
        jsonFile = JSONService.getJSON()

        if authCode == jsonFile[authType]:
            return True
        else:
            return False

    def changePWD(self, pwd: str):
        print('test')

    def changeRFID(self, rfid: str):
        print('test')

    def triggerAlarm(self):
        gpio_led_thread = threading.Thread(target=gpios.gpio_alarm_LEDs)
        gpio_led_thread.start()
