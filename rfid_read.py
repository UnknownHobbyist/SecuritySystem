import RPi.GPIO as GPIO
import __main__
import system

import sys
sys.path.append('/home/pi/MFRC522-python')

from mfrc522 import SimpleMFRC522

sec_serv = system.SecuritySystem()
reader = SimpleMFRC522()

print("Halten Sie ein Clip oder eine Karte an dem Sensor.")

while True:
    try:
        id, text = reader.read()
        if sec_serv.auth(str(id),"rfid")==True:
            print("access granted")
        else:
            print("access denied")

    finally:

        GPIO.cleanup()
