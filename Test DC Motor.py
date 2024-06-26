import time
import board
import pwmio
from adafruit_motor import motor

PWM_M1A = board.GP8
PWM_M1B = board.GP9
PWM_M2A = board.GP10
PWM_M2B = board.GP11
'''iqmal comel'''
# DC motor setup
M1A = pwmio.PWMOut(PWM_M1A, frequency=10000)
M1B = pwmio.PWMOut(PWM_M1B, frequency=10000)
M2A = pwmio.PWMOut(PWM_M2A, frequency=10000)
M2B = pwmio.PWMOut(PWM_M2B, frequency=10000)
motor1 = motor.DCMotor(M1A, M1B)
motor2 = motor.DCMotor(M2A, M2B)

# Throttle value must be between -1.0 and +1.0
print("\nForwards")
motor1.throttle = 1 #Power 0.0 - 1.0
motor2.throttle = 1
time.sleep(5)

print("\nStop")
motor1.throttle = 0
motor2.throttle = 0
time.sleep(1)
