import RPi.GPIO as GPIO
import settings

sec_serv = None

if __name__ == '__main__':
    import system

    sec_serv = system.SystemService()

    #use RPi.GPIO Layout
    GPIO.setmode(GPIO.BOARD)

    #setup for Output Pins
    GPIO.setup(GPIO_SETIINGS["ALARM_CHANGER"], GPIO.OUT)

    #setup for Input Pins
    GPIO.setup(GPIO_SETIINGS["ALARM_SIGNAL"]["1"], GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)


return 0
