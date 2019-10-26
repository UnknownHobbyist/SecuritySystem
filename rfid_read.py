import RPi.GPIO as GPIO
import __main__
import system
import time

from state_enum import *

import sys
sys.path.append('/home/pi/MFRC522-python')

from mfrc522 import SimpleMFRC522
sec_serv= system.SecuritySystem()

reader = SimpleMFRC522()

print("Halten Sie ein Clip oder eine Karte an dem Sensor.")

while True:
    try:
        id, text = reader.read()
        if sec_serv.auth(str(id),"rfid")==True:
            if sec_serv.alarmState != AlarmState.DISABLED:
                sec_serv.changeAlarm(Alarmstate.DISABLED)
            else:
                sec_serv.changeAlarm(AlarmState.ARMED)
            print("Security system "+str(sec_serv.alarmState))
            time.sleep(2)
        else:
            print("access denied")
            time.sleep(2)


    finally:

        GPIO.cleanup()
