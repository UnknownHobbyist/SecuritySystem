import RPi.GPIO as GPIO
import settings
import system
sec_serv = system.SystemService()
if __name__ == '__main__':
    #use RPi.GPIO Layout
    GPIO.setmode(GPIO.BOARD)

    #setup for Output Pins
    GPIO.setup(GPIO_SETIINGS["ALARM_CHANGER"], GPIO.OUT)

    #setup for Input Pins
    GPIO.setup(GPIO_SETIINGS["ALARM_SIGNAL"]["1"], GPIO.IN)
