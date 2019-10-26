import __main__
import json
import gpio_service as gpios
import rfid_read as rr
import threading
import vlc

from json_service import JsonService
from time import sleep
from state_enum import *

class SecuritySystem:

    num_pad = None
    num_pad_checker = None
    sound_obj = None
    gpio_led_thread = None

    def __init__(self):

        # if the alarm is armed or not
        self.alarmState = AlarmState.DISABLED

        self.sound_obj = vlc.MediaPlayer("file://home/pi/SecuritySystem/sounds/alarm.mp3")

    #
    # Changes the state of the alarm
    #
    def changeAlarm(self, state: AlarmState):
        self.alarmState = state;

    #
    # authType {"rfid", "pwd"}
    #
    def auth(self, authCode: str, authType: str)->bool:
        jsonFile = JsonService.getJson()

        if authCode == jsonFile[authType]:
            return True
        else:
            return False

    def changePWD(self, pwd: str):
        print('test')

    def changeRFID(self, rfid: str):
        print('test')

    def triggerAlarm(self):
        if self.alarmState == AlarmState.RUNNING:
            return

        self.alarmState = AlarmState.RUNNING
        self.gpio_led_thread = threading.Thread(target=gpios.gpioAlarmLEDs)
        self.gpio_led_thread.start()

        #hierfür müsste möglicherweise ein neuer thread gestartet werden
        self.sound_obj.play()

    def freePorts(self):
        gpio.cleanup()

    def setup(self):
        rr_fred = threading.Thread(target=rr.runWhileRFID)
        rr_fred.start()
        # Give us 100 points PLEASE!
        gpios.setup()

    def stopAlarm(self):
        if alarmState != AlarmState.RUNNING:
            self.gpio_led_thread.kill()
            self.sound_obj.stop();
