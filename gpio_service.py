import time
import RPi.GPIO as GPIO
import state_enum as se
from settings import *
from pygame import mixer

#Activating Alarm LEDs
def gpioAlarmLEDs():
    from __main__ import sec_serv
    while sec_serv.alarmState == se.AlarmState.RUNNING:
        GPIO.output(GPIO_SETTINGS['ALARM_CHANGER'], GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(GPIO_SETTINGS['ALARM_CHANGER'], GPIO.LOW)
        time.sleep(0.5)

def handleAlarmSignal(thread):
    from __main__ import sec_serv
    #if GPIO.input(GPIO_SETTINGS["ALARM_SIGNAL"]["1"]) == GPIO.HIGH:
    sec_serv.triggerAlarm()

def runAlarmSound():
    from __main__ import sec_serv
    #GPIO.output(GPIO_SETTINGS['ALARM_SOURCE'], GPIO.HIGH)
    sec_serve.sound_obj.music.play()

def setup():
    from __main__ import sec_serv
    GPIO.setmode(GPIO.BOARD);

    #setup for Output Pins
    GPIO.setup(GPIO_SETTINGS["ALARM_CHANGER"], GPIO.OUT)

    #setup for Input Pins
    GPIO.setup(GPIO_SETTINGS["ALARM_SIGNAL"]["1"], GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)

    GPIO.add_event_detect(GPIO_SETTINGS["ALARM_SIGNAL"]["1"], GPIO.RISING, callback= handleAlarmSignal, bouncetime=300)
