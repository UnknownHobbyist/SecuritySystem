import time
import RPi.GPIO as GPIO
import __main__
import state_enum as se
from settings import *

#Activating Alarm LEDs
def gpioAlarmLEDs():
    while __main__.sec_serv.alarmState == se.AlarmState.RUNNING:
        GPIO.output(GPIO_SETTINGS["ALARM_CHANGER"], GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(GPIO_SETTINGS["ALARM_CHANGER"], GPIO.LOW)
        time.sleep(0.5)

def handleAlarmSignal():
    time.sleep(1.5)
    if GPIO.input(GPIO_SETTINGS["ALARM_SIGNAL"]["1"]) == GPIO.HIGH:
            __main__.sec_serv.triggerAlarm()

GPIO.setmode(GPIO.BOARD);

#setup for Output Pins
GPIO.setup(GPIO_SETTINGS["ALARM_CHANGER"], GPIO.OUT)

#setup for Input Pins
GPIO.setup(GPIO_SETTINGS["ALARM_SIGNAL"]["1"], GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(GPIO_SETTINGS["ALARM_SIGNAL"]["1"], GPIO.RISING, callback= handleAlarmSignal, bouncetime=300)
