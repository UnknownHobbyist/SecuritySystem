import __main__
import RPi.GPIO as GPIO
from settings import *
from state_enum import *

class NumPad:

    matrix = None
    row = None
    col = None
    code = None

    def __init__(self):
        #use RPi.GPIO Layout
        GPIO.setmode(GPIO.BCM)

        self.matrix = [ [1, 2, 3, 'A'],
                        [4, 5, 6, 'B'],
                        [7, 8, 9, 'C'],
                        ['*', 0, '#', 'D'] ]

        self.row = [GPIO_SETTINGS['KEYBOARD']['1'], GPIO_SETTINGS['KEYBOARD']['2'], GPIO_SETTINGS['KEYBOARD']['3'], GPIO_SETTINGS['KEYBOARD']['4']]
        self.col = [GPIO_SETTINGS['KEYBOARD']['5'], GPIO_SETTINGS['KEYBOARD']['6'], GPIO_SETTINGS['KEYBOARD']['7'], GPIO_SETTINGS['KEYBOARD']['8']]

        for j in range(4):
            GPIO.setup(self.col[j], GPIO.OUT)
            GPIO.output(self.col[j], 1)

        for i in range(4):
            GPIO.setup(self.row[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

    def check(self):
        print("num_pad_checker running")
        try:
            while(True):
                for j in range(4):
                    GPIO.output(self.col[j], 0)
                    for i in range(4):
                        if GPIO.input(self.row[i]) == 0:
                            while(GPIO.input(self.row[i]) == 0):
                                if matrix[i][j] == 'D':
                                    self.run_code()
                                elif matrix[i][j] == 'A':
                                    self.run_code()
                                elif matrix[i][j] == 'B':
                                    self.code = ''
                                else:
                                    self.code += str(self.matrix[i][j])

                                print(matrix[i][j])

                    GPIO.output(self.col[j], 1)
        except KeyboardInterrupt:
            GPIO.cleanup()

    def run_code(self):
        from main import sec_serv
        if self.code[0] == 'A':
            if sec_serv.alarmState == AlarmState.DISABLED and len(self.code) == 1:
                print('neues passwort bitte')
            else:
                print('das neue passwort ist: ' + self.code[1:])
        elif self.code[0] == 'B':

            pass
        elif self.code[0] == 'C':

            pass
        else:
            if sec_serv.alarmState == not AlarmState.DISABLED and self.code == sec_serv.password:
                sec_serv.alarmState = AlarmState.DISABLED
