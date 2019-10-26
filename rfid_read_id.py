def rfid_read_id():

    import RPi.GPIO as GPIO

    import sys
    sys.path.append('/home/pi/MFRC522-python')

    from mfrc522 import SimpleMFRC522

    reader = SimpleMFRC522()

    id, text = reader.read()

    return id
