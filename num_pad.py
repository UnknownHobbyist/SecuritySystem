import __main__
import RPi.GPIO as GPIO
from settings import *

class NumPad:

    matrix = None
    row = None
    col = None

    def __init__(self):
        #use RPi.GPIO Layout
        GPIO.setmode(GPIO.BOARD)

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

        try:
            while(True):
                for j in range(4):
                    GPIO.output(self.col[j], 0)

                    for i in range(4):
                        if GPIO.input(self.row[i]) == 0:



                            while(GPIO.input(self.row[i]) == 0):
                                pass

                    GPIO.output(self.col[j], 1)


        except KeyboardInterrupt:
            GPIO.cleanup()
