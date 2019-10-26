import RPi.GPIO as GPIO
import time

from state_enum import *

import sys
sys.path.append('/home/pi/MFRC522-python')

from mfrc522 import SimpleMFRC522

def runWhileRFID():
    from __main__ import sec_serv
    reader = SimpleMFRC522()

    print(1)

    while True:
        try:
            id, text = reader.read()
            if sec_serv.auth(str(id),"rfid")==True:
                if sec_serv.alarmState != AlarmState.DISABLED:
                    sec_serv.changeAlarm(AlarmState.DISABLED)
                else:
                    if sec_serv.alarmState == AlarmState.RUNNING:
                        sec_serv.stopAlarm()
                    sec_serv.changeAlarm(AlarmState.ARMED)
                print("Security system "+str(sec_serv.alarmState))
                time.sleep(2)
            else:
                print("access denied")
                time.sleep(2)


        finally:

            GPIO.cleanup()
