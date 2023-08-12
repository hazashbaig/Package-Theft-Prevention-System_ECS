import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

servo_pin = 18

GPIO.setup(servo_pin, GPIO.OUT)

# Create a PWM instance
pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz (20 ms period)

# Start PWM with 0% duty cycle (servo at 0 degrees)
pwm.start(0)

def open_barrier():
    pwm.ChangeDutyCycle(7.5)  # 90 degrees (middle position)
    time.sleep(1)

def close_barrier():
    pwm.ChangeDutyCycle(2.5)  # 0 degrees (min position)
    time.sleep(1)

try:
    while True:
        open_barrier()  # Raise the barrier
        time.sleep(6)   # Keep the barrier raised for 6 seconds
        close_barrier() # Lower the barrier

except KeyboardInterrupt:
    # Clean up on Ctrl+C
    pwm.stop()
    GPIO.cleanup()