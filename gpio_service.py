import time
import RPi.GPIO as GPIO
import __main__
import state.enum as se
import settings

def gpio_alarm_LEDs():
    while __main__.sec_serv.alarmState == se.AlarmState.RUNNING:
        
