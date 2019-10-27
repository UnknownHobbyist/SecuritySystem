from state_enum import *
import subprocess

import time
def rfid_named(id):
    print(id)

def rfid_checker(callback_function):

    import RPi.GPIO as GPI

    from __main__ import sec_serv

    while True:
        sp = subprocess.Popen(['python3.7', '/home/pi/MFRC522-python/Read.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = sp.communicate()
        std = stdout.split('\n')
        id = std[1]

        callback_function(id)

        time.sleep(2.5)
