import RPi.GPIO as GPIO
import settings
import system
sec_serv = system.SystemService()
if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(GPIO_SETIINGS["ALARM_CHANGER"])
