import time
import RPi.GPIO as GPIO
import __main__
import state_enum as se
import settings

#Activating Alarm LEDs
def gpioAlarmLEDs():
    while __main__.sec_serv.alarmState == se.AlarmState.RUNNING:
        GPIO.output(GPIO_SETIINGS["ALARM_CHANGER"], GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(GPIO_SETIINGS["ALARM_CHANGER"], GPIO.LOW)
        time.sleep(0.5)

def handleAlarmSignal():
    time.sleep(1.5)
    if GPIO.input(GPIO_SETIINGS["ALARM_SIGNAL"]["1"]) == GPIO.HIGH:
            __main__.sec_serv.triggerAlarm()

#GPIO.setmode(GPIO.BCM);
#GPIO.add_event_detect(settings.GPIO_SETTINGS["ALARM_SIGNAL"]["1"], GPIO.RISING, callback= handleAlarmSignal, bouncetime=300)
