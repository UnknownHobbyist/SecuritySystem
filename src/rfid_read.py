import subprocess

import time
def rfid_named(id):
    from __main__ import sec_serv
    from state_enum import AlarmState


    print(id)

    if sec_serv.auth(id,"rfid")==True:
        if sec_serv.alarmState != AlarmState.DISABLED:
            sec_serv.changeAlarm(AlarmState.DISABLED)
            sec_serv.voice_audi0("Security System disabled")

            if sec_serv.alarmState == AlarmState.RUNNING:
                sec_serv.voice_audi0("Alarm disabled")

        else:
            time.sleep(10)
            sec_serv.changeAlarm(AlarmState.ARMED)
            sec_serv.voice_audio("Security System enabled")
            time.sleep(10)

def rfid_checker(callback_function):

    import RPi.GPIO as GPI

    from __main__ import sec_serv

    while True:
        sp = subprocess.Popen(['python3.7', '/home/pi/MFRC522-python/Read.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = sp.communicate()
        std = stdout.decode('utf-8').split('\n')
        id = std[1]
        print(id)

        callback_function(id)

        time.sleep(2.5)
