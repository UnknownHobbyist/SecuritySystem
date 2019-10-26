import RPi.GPIO as GPIO
import __main__
import system
import time
from __main__ import sec_serv

import sys
sys.path.append('/home/pi/MFRC522-python')

from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

print("Halten Sie ein Clip oder eine Karte an dem Sensor.")

while True:
    try:
        id, text = reader.read()
        if sec_serv.auth(str(id),"rfid")==True:
            if sec_serv.AlarmState != AlarmState.DISABLED:
                sec_serv.changeAlarm(Alarmstate.DISABLED)
            else:
                sec_serv.changeAlarm(AlarmState.ARMED)
            print("Security system "+str(sec_serv.AlarmState))
            time.sleep(2)
        else:
            print("access denied")
            time.sleep(2)


    finally:

        GPIO.cleanup()
