import RPi.GPIO as GPIO
import threading
from settings import *
import time, threading

import flask

global man_come

app = flask.Flask(__name__)

man_come = False
def set_man_come_off():
    time.sleep(7)

def man_come_to_home():
    man_come = True
    t = threading.Thread(target=set_man_come_off)
    t.start()
def start_flask():
    h = FLASK_NAME.split(':')
    app.run(host=h[0], port=h[1], debug=FLASK_DEBUG)
@app.route("/smarthome/webhook")
def smarthome_webhook():
    if man_come:
        man_come = False
        return "TRUE"
    else:
        return "FALSE"


if __name__ == "__main__":

    import system
    import num_pad
    import rfid_read as rr

    # use RPi.GPIO Layout
    GPIO.setmode(GPIO.BCM)

    # setup for Output Pins
    GPIO.setup(GPIO_SETTINGS["ALARM_CHANGER"], GPIO.OUT)
    GPIO.output(GPIO_SETTINGS["ALARM_CHANGER"], GPIO.LOW)


    #setup for Input Pins
    GPIO.setup(GPIO_SETTINGS["ALARM_SIGNAL"]["1"], GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(GPIO_SETTINGS["RESET"], GPIO.IN,  pull_up_down=GPIO.PUD_UP)

    #disables gpio warnings
    GPIO.setwarnings(False);

    sec_serv = system.SecuritySystem()
    sec_serv.setup()

    #sec_serv.triggerAlarm()
    #testing -remove

    # checks the input from the membrane pad
    num_pad = num_pad.NumPad();
    num_pad_checker = threading.Thread(target=num_pad.check)
    num_pad_checker.start()
    # start smarthome webserver
    t_f = threading.Thread(target=smarthome_webhook)
    t_f.start()
    try:
        rr.rfid_checker(rr.rfid_named)
    except KeyboardInterrupt:
        GPIO.output(GPIO_SETTINGS["ALARM_CHANGER"], GPIO.LOW)
        GPIO.cleanup()
