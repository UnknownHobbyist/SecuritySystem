from state_enum import *
import subprocess

import time
def rfid_checker():

    import RPi.GPIO as GPI

    from __main__ import sec_serv

    while True:
        sp = subprocess.Popen(['python3.7', '/home/pi/MFRC522-python/Read.py'], stdout=subproces.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = sp.communicate()
        print(stdout)
        time.sleep(2.5)
