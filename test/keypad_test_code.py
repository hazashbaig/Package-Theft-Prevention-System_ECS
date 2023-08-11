import RPi.GPIO as GPIO
import time

Password = '12345'
SafePass = '42069'

CurrPass = ""
flag = 0
auth_token = False
safe = False

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


class keypad:

    def getAuthToken():
        return auth_token

    def getCode():
        return Password
    
    def checkSafe():
        return safe

    def check(Code):
        global Password
        global auth_token
        global flag
        global safe
        
        auth_token = False
        safe = False
        
        if Password == Code:
            auth_token = True
       
        elif SafePass == Code:
            print("\nSafe PIN triggered !")
            print("Contacting the Police...\n")
            time.sleep(3) 
            safe = True
        
        else:
            print("Wrong PIN!")
            flag = 1

    def readLine(line, characters):
        global CurrPass
        GPIO.output(line, GPIO.HIGH)
        if(GPIO.input(C1) == 1):
            if characters[0] == '*':
                CurrPass = CurrPass[:-1]
                print(CurrPass)
            elif characters[0] == '#':
                keypad.check(CurrPass)
            else:
                CurrPass = CurrPass + characters[0]
                print(CurrPass)
        
        if(GPIO.input(C2) == 1):
            if characters[1] == '*':
                CurrPass = CurrPass[:-1]
                print(CurrPass)
            elif characters[1] == '#':
                keypad.check(CurrPass)
            else:
                CurrPass = CurrPass + characters[1]
                print(CurrPass)
        if(GPIO.input(C3) == 1):
            if characters[2] == '*':
                CurrPass = CurrPass[:-1]
                print(CurrPass)
            elif characters[2] == '#':
                keypad.check(CurrPass)
            else:
                CurrPass = CurrPass + characters[2]
                print(CurrPass)
    
        GPIO.output(line, GPIO.LOW)

    def getDeets():
        global flag
        flag = 0
        # Displaying input message
        print("Welcome, Enter Password:")
        try:
            while not auth_token and not safe and flag != 1:
                keypad.readLine(L1, ["1", "2", "3"])
                keypad.readLine(L2, ["4", "5", "6"])
                keypad.readLine(L3, ["7", "8", "9"])
                keypad.readLine(L4, ["*", "0", "#"])
                time.sleep(0.3)
        except KeyboardInterrupt:
            print("\nApplication stopped!")
            GPIO.cleanup()


if __name__ == "__main__":
    keypad.getDeets()
