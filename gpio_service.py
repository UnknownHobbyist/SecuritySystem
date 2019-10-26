import time
import RPi.GPIO as GPIO
import __main__
import state.enum as se
import settings

#Activating Alarm LEDs
def Gpio_Alarm_LEDs():
    while __main__.sec_serv.alarmState == se.AlarmState.RUNNING:
        GPIO.output(GPIO_SETIINGS["ALARM_CHANGER"], GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(GPIO_SETIINGS["ALARM_CHANGER"], GPIO.LOW)
        time.sleep(0.5)

def Handle_Alarm_Signal():
    while True:
        if GPIO.input(GPIO_SETIINGS["ALARM_SIGNAL"]["1"]) == GPIO.HIGH:
            __main__.sec_serv.triggerAlarm()
