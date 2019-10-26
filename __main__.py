import RPi.GPIO as GPIO
import threading
from settings import *

sec_serv = None

if __name__ == '__main__':
    import system
    import num_pad

    #use RPi.GPIO Layout
    GPIO.setmode(GPIO.BOARD)

    #setup for Output Pins
    GPIO.setup(GPIO_SETTINGS["ALARM_CHANGER"], GPIO.OUT)

    #setup for Input Pins
    GPIO.setup(GPIO_SETTINGS["ALARM_SIGNAL"]["1"], GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)

    #sec_serv = system.SystemService()


    # checks if someone inputs something over the membrane pad
    num_pad = num_pad.NumPad();
    num_pad_checker = threading.Thread(target=num_pad.check)
    num_pad_checker.start()
    num_pad_checker.join()
