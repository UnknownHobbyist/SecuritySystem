import __main__
import RPi.GPIO as GPIO
from settings import *
from state_enum import *
import os


def supply_msg(msg: str):
    os.popen("espeak " + msg)


class NumPad:

    matrix = None
    row = None
    col = None
    code = ""

    def __init__(self):
        # use RPi.GPIO Layout
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        self.matrix = [
            [1, 2, 3, "A"],
            [4, 5, 6, "B"],
            [7, 8, 9, "C"],
            ["*", 0, "#", "D"],
        ]

        self.row = [
            GPIO_SETTINGS["KEYBOARD"]["1"],
            GPIO_SETTINGS["KEYBOARD"]["2"],
            GPIO_SETTINGS["KEYBOARD"]["3"],
            GPIO_SETTINGS["KEYBOARD"]["4"],
        ]
        self.col = [
            GPIO_SETTINGS["KEYBOARD"]["5"],
            GPIO_SETTINGS["KEYBOARD"]["6"],
            GPIO_SETTINGS["KEYBOARD"]["7"],
            GPIO_SETTINGS["KEYBOARD"]["8"],
        ]

        for j in range(4):
            GPIO.setup(self.col[j], GPIO.OUT)
            GPIO.output(self.col[j], 1)

        for i in range(4):
            GPIO.setup(self.row[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def check(self):
        print("num_pad_checker running")
        try:
            while True:
                for j in range(4):
                    GPIO.output(self.col[j], 0)
                    for i in range(4):
                        if GPIO.input(self.row[i]) == 0:
                            self.addChar(str(self.matrix[i][j]))

                            print(self.matrix[i][j])
                            while GPIO.input(self.row[i]) == 0:
                                pass

                    GPIO.output(self.col[j], 1)
        except KeyboardInterrupt:
            GPIO.cleanup()

    #
    # Uses a string to collect and handle the input from check
    #
    def addChar(self, char: str):
        from __main__ import sec_serv

        if char == 'A':
            if sec_serv.auth(self.code[1:], 'pwd'):
                self.code = 'A'
                print('Bitte geben sie nun ihr neues Passwort ein und bestätigen sie mit D!')
            else:
                print('Um ihr passwort zuändern müssen sie zunächst ihr aktuelles Passwort angeben!')
                self.code = ''
        elif char == 'B':
            self.code = ''
        elif char == 'C':
            # The device is set to armed State
            sleep(10)
            sec_serv.alarmState = AlarmState.ARMED
            pass
        elif char == 'D':
            if self.code[0] == 'A' and len(self.code) > 1:
                sec_serv.changePWD(self.code[1:])
                print('Sie haben ihren Code erfolgreich auf: ' + self.code + " geändert")
                self.code = ''
            else:
                if sec_serv.auth(self.code, "pwd"):
                    sec_serv.stopAlarm()
                    sec_serv.changeAlarm(AlarmState.DISABLED)
                    print('Willkommen zurück Master!')
                    self.code = ''
                else:
                    print('Das eingegebene Passwort ist falsch!')
                    self.code = ''
        elif char == '\#':
            pass
        elif char == '*':
            pass
        else:
            self.code += char
