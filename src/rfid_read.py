from state_enum import *

def rfid_checker():

    import RPi.GPIO as GPIO
    import sys

    sys.path.append("/home/pi/MFRC522-python")

    from __main__ import sec_serv
    from mfrc522 import SimpleMFRC522

    reader = SimpleMFRC522()

    while True:
        try:
            print(1)
            id, text = reader.read()
            print(2)
            print(id + " something")

            if sec_serv.auth(str(id),"rfid"):
                if sec_serv.alarmState != AlarmState.DISABLED:
                    if sec_serv.alarmState == AlarmState.RUNNING:
                        sec_serv.stopAlarm()
                    sec_serv.changeAlarm(AlarmState.DISABLED)
                else:
                    sec_serv.changeAlarm(AlarmState.ARMED)
                #print("Security system " + str(sec_serv.alarmState))
            else:
                print("Access has been denied")
        except:
            GPIO.output(GPIO_SETTINGS["ALARM_CHANGER"], GPIO.LOW)
            GPIO.cleanup()
        finally:
            pass
