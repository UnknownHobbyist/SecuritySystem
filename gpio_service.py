import time
import RPi.GPIO as GPIO
import state_enum as se
from settings import *
from __main__ import sec_serv

#Activating Alarm LEDs
def gpioAlarmLEDs():
    while sec_serv.alarmState == se.AlarmState.RUNNING:
        GPIO.output(GPIO_SETTINGS['ALARM_CHANGER'], GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(GPIO_SETTINGS['ALARM_CHANGER'], GPIO.LOW)
        time.sleep(0.5)

def handleAlarmSignal(thread):
    #if GPIO.input(GPIO_SETTINGS["ALARM_SIGNAL"]["1"]) == GPIO.HIGH:
    sec_serv.triggerAlarm()

def runAlarmSound():
    GPIO.output(GPIO_SETTINGS['ALARM_SOURCE'], GPIO.HIGH)

def setup():
    GPIO.setmode(GPIO.BOARD);

    #setup for Output Pins
    GPIO.setup(GPIO_SETTINGS["ALARM_CHANGER"], GPIO.OUT)

    #setup for Input Pins
    GPIO.setup(GPIO_SETTINGS["ALARM_SIGNAL"]["1"], GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)

    GPIO.add_event_detect(GPIO_SETTINGS["ALARM_SIGNAL"]["1"], GPIO.RISING, callback= handleAlarmSignal, bouncetime=300)
