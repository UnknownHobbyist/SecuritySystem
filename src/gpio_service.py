from time import sleep
import RPi.GPIO as GPIO
import state_enum as se
from settings import *


# Activating Alarm LEDs
def gpioAlarmLEDs():
    from __main__ import sec_serv

    while sec_serv.alarmState == se.AlarmState.RUNNING:
        GPIO.output(GPIO_SETTINGS["ALARM_CHANGER"], GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(GPIO_SETTINGS["ALARM_CHANGER"], GPIO.LOW)
        time.sleep(0.5)


def handleAlarmSignal(thread):
    from __main__ import sec_serv
    sleep(5)
    sec_serv.triggerAlarm()


def handleResetSignal(thread):
    from __main__ import sec_serv
    sec_serv.changeAlarm(AlarmState.DISABLED)
    sec_serv.stopAlarm()


def setup():
    from __main__ import sec_serv

    GPIO.setmode(GPIO.BCM)

    # setup for Output Pins
    GPIO.setup(GPIO_SETTINGS["ALARM_CHANGER"], GPIO.OUT)

    #setup for Input Pins
    GPIO.setup(GPIO_SETTINGS["ALARM_SIGNAL"]["1"], GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)


    GPIO.setup(GPIO_SETTINGS["RESET"], GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)

    GPIO.add_event_detect(
        GPIO_SETTINGS["ALARM_SIGNAL"]["1"],
        GPIO.RISING,
        callback=handleAlarmSignal,
        bouncetime=300,
    )
    GPIO.add_event_detect(
        GPIO_SETTINGS["RESET"],
        GPIO.BOTH,
        callback=handleResetSignal,
        bouncetime=300
    )
