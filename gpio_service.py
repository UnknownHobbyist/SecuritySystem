import time
import RPi.GPIO as GPIO
import __main__
import state.enum as se
import settings

def gpio_alarm_LEDs():
    while __main__.sec_serv.alarmState == se.AlarmState.RUNNING:
        GPIO.output(GPIO_SETIINGS["ALARM_CHANGER"], GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(GPIO_SETIINGS["ALARM_CHANGER"], GPIO.LOW)
        time.sleep(0.5)
