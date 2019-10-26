import __main__

class NumPad:

    matrix = None
    row = None
    col = None

    def __init__(self):

        self.matrix = [ [1, 2, 3, 'A'],
                        [4, 5, 6, 'B'],
                        [7, 8, 9, 'C'],
                        ['*', 0, '#', 'D'] ]

    row = [7, 11, 13, 15]
    col = [12, 16, 18, 22]

    for j in range(4):
        GPIO.setup(col[j], GPIO.OUT)
        GPIO.output(col[j], 1)

    for i in range(4):
        GPIO.setup(row[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

def check():

    try:
        while(True):
            print('stuff')
            #do stuff

            for j in range(4):
                GPIO.output(col[j], 0)

                for i in range(4):
                    if GPIO.input(row[i]) == 0
                        print matrix[i][j]
                        #do stuff
                        while(GPIO.input(row[i]) == 0)
                            pass

                GPIO.output(col[j], 1)


    except KeyboardInterrupt:
        GPIO.cleanup()
