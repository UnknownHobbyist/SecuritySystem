import RPi.GPIO as GPIO
import time

from state_enum import *

import sys
sys.path.append('/home/pi/MFRC522-python')

def runWhileRFID():
    from __main__ import sec_serv
    from mfrc522 import SimpleMFRC522
    reader = SimpleMFRC522()

    print(1)

    while True:
        print(3)
        id, text = reader.read()
        if sec_serv.auth(str(id),"rfid")==True:
            if sec_serv.alarmState != AlarmState.DISABLED:
                sec_serv.changeAlarm(AlarmState.DISABLED)
            else:
                if sec_serv.alarmState == AlarmState.RUNNING:
                    sec_serv.stopAlarm()
                sec_serv.changeAlarm(AlarmState.ARMED)
            print("Security system "+str(sec_serv.alarmState))
        else:
            print("access denied")
        time.sleep(2)
