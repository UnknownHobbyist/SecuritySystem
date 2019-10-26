import __main__
import RPi.GPIO as GPIO

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

        self.row = [35, 37, 16, 29]
        self.col = [32, 36, 38, 40]

        for j in range(4):
            GPIO.setup(self.col[j], GPIO.OUT)
            GPIO.output(self.col[j], 1)

        for i in range(4):
            GPIO.setup(self.row[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

    def check(self):

        print('running')

        try:
            while(True):
                for j in range(4):
                    GPIO.output(self.col[j], 0)

                    for i in range(4):
                        if GPIO.input(self.row[i]) == 0:
                            print(self.matrix[i][j])
                            #do stuff
                            while(GPIO.input(self.row[i]) == 0):
                                pass

                    GPIO.output(self.col[j], 1)


        except KeyboardInterrupt:
            GPIO.cleanup()
