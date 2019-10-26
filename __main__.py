import RPi.GPIO as GPIO
import threading
from settings import *


if __name__ == '__main__':

    import system
    import num_pad
    import rfid_read as rr
    import rfid_read_id

    print(rfid_read_id())

    #use RPi.GPIO Layout
    GPIO.setmode(GPIO.BOARD)

    #setup for Output Pins
    GPIO.setup(GPIO_SETTINGS["ALARM_CHANGER"], GPIO.OUT)
    GPIO.setup(GPIO_SETTINGS["ALARM_SOURCE"], GPIO.OUT)

    GPIO.output(GPIO_SETTINGS["ALARM_SOURCE"], GPIO.LOW)
    GPIO.output(GPIO_SETTINGS["ALARM_CHANGER"], GPIO.LOW)


    #setup for Input Pins
    GPIO.setup(GPIO_SETTINGS["ALARM_SIGNAL"]["1"], GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)

    #disables warnings
    GPIO.setwarnings(False);

    sec_serv = system.SecuritySystem()
    sec_serv.setup()

    #sec_serv.triggerAlarm()
    # checks if someone inputs something over the membrane pad
    num_pad = num_pad.NumPad();
    num_pad_checker = threading.Thread(target=num_pad.check)
    num_pad_checker.start()

    try:
        rr.runWhileRFID()
    except KeyboardInterrupt:
        GPIO.output(GPIO_SETTINGS["ALARM_SOURCE"], GPIO.LOW)
        GPIO.output(GPIO_SETTINGS["ALARM_CHANGER"], GPIO.LOW)
        GPIO.cleanup()
