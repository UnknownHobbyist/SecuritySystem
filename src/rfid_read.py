from state_enum import *
import subprocess

import time
def rfid_checker():

    import RPi.GPIO as GPIO
    import sys

    sys.path.append("/home/pi/MFRC522-python")

    from __main__ import sec_serv
    from mfrc522 import SimpleMFRC522

    reader = SimpleMFRC522()

    while True:
        sp = subprocess.Popen(['python3.7', '/home/pi/MFRC522-python/Read.py'], stdout=subproces.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = sp.communicate()
        print(stdout)
        time.sleep(2.5)
