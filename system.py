import json
import auth.enum.py
import gpio_service.py as gpios

from json_service import JSONService

#gpio imports
#will be removed later
from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from gpiozero.tones import Tone
from gpiozero import LED
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
    def changeAlarm():
        alarmState = not alarmArmed

    #
    # authType {"rfid", "pwd"}
    #
    def auth(authCode : str, authType : str) -> bool:
        jsonFile = JSONService.getJSON()

        if authCode == jsonFile[authType]:
            return True
        else:
            return False

    def changePWD(pwd: str):
        print('test')

    def changeRFID(rfid: str):
        print('test')

    def triggerAlarm():
        gpio_led_thread = threading.Thread(target=gpios.gpio_alarm_LEDs, name="led_thread")
        gpio_led_thread.start()
