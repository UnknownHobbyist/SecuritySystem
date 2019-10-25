import json
import auth.enum.py

from json_service import JSONService

#gpio imports
#will be removed later
from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from gpiozero.tones import Tone
from gpiozero import LED
from time import sleep

class SecuritySystem:
    # if the alarm is armed or not
    alarmState = AlarmState.DISABLED

    #initializing sound for triggerAlarm
    button_sounds = {
        Button(2): Sound("samples/drum_tom_mid_hard.wav"),
        Button(3): Sound("samples/drum_cymbal_open.wav"),
    }


    #
    # Changes the state of the alarm
    #
    def changeAlarm():
        alarmState = !alarmArmed

    #
    # authType {"rfid", "pwd"}
    #
    def auth(authCode : str, authType : str) -> bool:
        jsonFile = JSONService.getJSON()

        if authCode == jsonFile[authType]:
            return True
        else:
            return False

    def triggerAlarm():

        #
        # Multi-Threading for sound and light
        # testing
        #

        #light
        led = LED(17)
        led.on()
        sleep(1)
        led.off();

        #sound
        soundBox = TonalBuzzer(17)
        soundBox.play(Tone(60))
        sleep(1)
        soundBox.stop()
