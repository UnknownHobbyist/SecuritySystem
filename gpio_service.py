import time
import RPi.GPIO as GPIO
import __main__
import state_enum as se
import settings

#Activating Alarm LEDs
def gpio_Alarm_LEDs():
    while __main__.sec_serv.alarmState == se.AlarmState.RUNNING:
        GPIO.output(GPIO_SETIINGS["ALARM_CHANGER"], GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(GPIO_SETIINGS["ALARM_CHANGER"], GPIO.LOW)
        time.sleep(0.5)

def handle_Alarm_Signal():
    time.sleep(1.5)
    if GPIO.input(GPIO_SETIINGS["ALARM_SIGNAL"]["1"]) == GPIO.HIGH:
            __main__.sec_serv.triggerAlarm()

GPIO.add_event_detect(GPIO_SETIINGS["ALARM_SIGNAL"]["1"], GPIO.RISING, callback= Handle_Alarm_Signal, bouncetime=300)
