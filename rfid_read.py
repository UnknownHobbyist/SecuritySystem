import time

from state_enum import *

def runWhileRFID():
    import RPi.GPIO as GPIO

    import sys
    sys.path.append('/home/pi/MFRC522-python')

    from __main__ import sec_serv

    from mfrc522 import SimpleMFRC522
    reader = SimpleMFRC522()

    while True:
        try:
            print(2)
            id, text = reader.read()
            print(id)
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
        except:
            pass
            
        finally:
            pass
