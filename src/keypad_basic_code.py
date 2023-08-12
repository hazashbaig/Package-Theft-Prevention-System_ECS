import RPi.GPIO as GPIO
import time

# Pin setup for keypad
L1 = 5
L2 = 6
L3 = 13
L4 = 19

C1 = 12
C2 = 16
C3 = 20

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def readLine(line, characters):
    GPIO.output(line, GPIO.HIGH)
    if GPIO.input(C1) == 1:
        return characters[0]
    if GPIO.input(C2) == 1:
        return characters[1]
    if GPIO.input(C3) == 1:
        return characters[2]
    GPIO.output(line, GPIO.LOW)

def read_key_pressed():
    try:
        while True:
            readLine(L1, ["1", "2", "3"])
            readLine(L2, ["4", "5", "6"])
            readLine(L3, ["7", "8", "9"])
            readLine(L4, ["*", "0", "#"])
            time.sleep(0.3)
    except KeyboardInterrupt:
        print("\nApplication stopped!")
        GPIO.cleanup()
